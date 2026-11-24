---
layout: post
title: "Capturando e tratando exceções em Java"
date: 2026-11-24
lang: pt-BR
translation_id: capturando-tratando-excecoes-java
permalink: /capturando-tratando-excecoes-java/
share_text: >-
  O artigo explica a sentença try e as cláusulas catch em Java, com exemplos de SQLException, captura múltipla e tratamento separado por tipo.
---

Quando uma exceção ocorre (seja ela um erro ou uma situação que foge ao fluxo comum esperado), o método no qual ela ocorreu cria um objeto de uma das classes de exceção e o envia para o ambiente de execução (*runtime system* - no caso, a JVM), contendo as informações relevantes acerca da exceção.

A partir disso, a JVM procura, na pilha de chamadas, por um tratador de exceção compatível com o objeto de exceção gerado. Esta busca inicia-se pelo método onde ocorreu a exceção. Caso exista um tratador de exceção no método, ele é tratado localmente. Caso contrário, a JVM procura no chamador do método. Caso exista um tratador, a exceção é tratada. Caso contrário, a JVM busca recursivamente na pilha de chamadas, do método atual até o chamador inicial, até encontrar um tratador ou encerrar o programa. Caso a exceção não seja tratada por nenhum método, a JVM encerra o programa, imprime no console a mensagem de erro e o rastreamento da pilha de execução que levou à exceção.

Trechos de código que podem lançar exceções verificadas em Java estão sujeitos ao requisito chamado **capturar ou especificar**. Assim:

- ou as sentenças que podem lançar a exceção devem ser envoltas em um bloco protegido (bloco `try`), fornecendo um tratador apropriado (cláusula `catch`) ou
- o método que contém as sentenças deve especificar que pode lançar uma exceção (usando `throws`). Neste caso, a exceção não é tratada pelo método, mas sim pelo seu chamador (caso o chamador trate também - caindo no mesmo caso *capturar ou especificar*).

Para auxiliar no tratamento de exceções, Java fornece uma construção, chamada de **sentença `try`**, composta por três partes:

- Um bloco `try`: contém as sentenças que podem lançar uma exceção, podendo incluir também outras sentenças (mesmo que estas não lancem exceções). Opcionalmente, podem existir sentenças de abertura/criação de recursos junto ao bloco `try`, logo após a palavra chave (tais sentenças são colocadas entre parênteses - o chamado `try` com recursos).
- Zero (Nota: Podemos ter apenas um bloco `try` sozinho, desde que existam recursos sendo abertos/criados em um `try` com recursos. Caso contrário, é obrigatório existir ao menos uma cláusula `catch` ou um bloco `finally` junto ao bloco `try`.) ou mais cláusulas `catch`: contém os blocos de tratamento de exceções. Aqui o desenvolvedor diz o que deve ser feito para cada uma das exceções que serão tratadas caso seja lançada alguma exceção durante a execução de um bloco `try`.
- Zero ou um bloco `finally`: contém código de limpeza. Tipicamente fechamento de arquivos, liberação de recursos, etc. É composto por sentenças que devem ser executadas independentemente de o código do bloco `try` ser bem sucedido ou não.

A sintaxe de uma sentença `try` (Nota: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>) é parcialmente mostrada a seguir:

```text
TryStatement:  
    try Block Catches 
    try Block [Catches] Finally 
    TryWithResourcesStatement 
Catches: 
    CatchClause {CatchClause}
CatchClause:
    catch ( CatchFormalParameter ) Block 
CatchFormalParameter:
    {VariableModifier} CatchType VariableDeclaratorId
CatchType:
    UnannClassType {| ClassType}
Finally: 
    finally Block    
```

Então, uma sentença `try` (linha 1) é composta por:

- Um bloco `try` seguido de cláusulas `catch` (linha 2).
- Um bloco `try` seguido de cláusulas `catch` opcionais, seguidas por um bloco `finally` (linha 3) ou
- Um `try` com recursos (linha 4)

Uma cláusula `catch` (linha 5) é composta pela palavra reservada `catch`, seguida por parâmetros formais (entre parênteses), seguida por um bloco de código (linha 6). Podemos ter várias cláusulas `catch` seguidas (denotado por `CatchClause {CatchClause}`). Um bloco `finally` é composto pela palavra reservada `finally` seguida de um bloco de código (linha 13).

Neste artigo, o foco está no bloco `try` e nas cláusulas `catch`: o primeiro protege as sentenças que podem lançar exceções, e as segundas definem como capturá-las e tratá-las.

## Bloco `try`

Um **bloco `try`** é usado para envolver os trechos de código que podem lançar exceções (sejam elas verificadas ou não verificadas que gostaríamos de tratar explicitamente). Isto é feito através da palavra reservada `try` seguida por um bloco (envolto entre chaves). Caso ocorra uma exceção que possa ser capturada por uma das cláusulas `catch` da sentença `try`, o controle é repassado para essa cláusula `catch`.

A seguir, temos um exemplo de uma sentença `try` envolvendo diversas sentenças relacionadas ao acesso a um banco de dados (linhas 3 a 21). Tal sentença possui um bloco `try` (linhas 3 a 18) e uma  cláusula `catch` (para exceções do tipo `SQLException` - linhas 18 a 21).

```java
public class DBExemplo {
    public static void main(String[] args) {
        try {   
            var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academico",
            "postgres", "postgres");
           
            IO.println("Listando os alunos...");
            var s = c.createStatement();      
            var rs = s.executeQuery( 
                "select * from aluno order by matricula");
            while (rs.next()) 
                IO.println(rs.getInt("matricula") + " - " +
                           rs.getString("nome"));
            rs.close(); 
            s.close();   
            c.close();   
        } catch (SQLException e){   
            // TODO Tratar exceções de SQL
            e.printStackTrace();
        } 
    }
}
```

Note que seriam necessárias as seguintes importações (iremos mostrá-las aqui - para os exemplos subsequentes assume-se que tais importações estejam informadas no código (as IDEs normalmente auxiliam a importar os tipos corretamente)):

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

Para saber quais sentenças do exemplo de fato podem lançar exceções, precisaremos da ajuda de uma IDE, da documentação dos métodos chamados ou do compilador (através dos erros que ocorreriam caso não especificássemos uma cláusula `catch`).

No código do exemplo, os métodos que podem lançar `SQLException` são:

- `DriverManager.getConnection(...)` - linha 4;
- `Connection.createStatement()` - linha 9;
- `Statement.executeQuery(...)` - linha 10;
- `ResultSet.next()` - linha 12;
- `ResultSet.getInt(...)` - linha 13;
- `ResultSet.getString(...)` - linha 14;
- `ResultSet.close()` - linha 15;
- `Statement.close()` - linha 16;
- `Connection.close()` - linha 17;

Ou seja, praticamente todas as operações de banco de dados (abrir conexão, criar sentença, executar consulta, iterar resultado e fechar recursos) podem lançar `SQLException`.

Para sabermos quando é necessário tratar uma determinada exceção em uma chamada a um método, podemos recorrer a uma IDE, que mostra os trechos de código que necessitam ser protegidos. As IDEs sabem que um determinado método pode lançar uma exceção por causa do requisito *capturar ou especificar*.

Uma vez que um método não saiba como (ou não é conveniente) tratar uma exceção verificada, ele adiciona uma cláusula `throws` em sua assinatura. Por exemplo, a assinatura do método `getConnection` da interface `DriverManager` é a seguinte:

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

Isso significa que quaisquer trechos de código que chamem o método `getConnection` necessitam envolver tais chamadas em uma sentença `try` ou então eles mesmos precisam adicionar uma cláusula `throws` em sua assinatura.

## Cláusulas `catch`

Nas **cláusulas `catch`**, podemos tratar as exceções protegidas no bloco `try`. Para cada exceção verificada passível de ser lançada, podemos criar uma cláusula `catch` específica. No exemplo a seguir, temos uma cláusula `catch` que mostra os detalhes da exceção (linhas 5 a 10), tais como a mensagem de erro (linha 7), o estado do SQL (linha 8) e o código específico do erro (linha 9):

```java
public class DBExemplo {
    public static void main(String[] args) {
        try { 
            // Código do try idêntico à listagem anterior
        } catch (SQLException e){   
            IO.println("SQLException capturada!");
            IO.println("Mensagem: " + e.getMessage()); 
            IO.println("SQLState: " + e.getSQLState()); 
            IO.println("Erro: " + e.getErrorCode());
        } 
    }
}
```

Se, por exemplo, digitássemos o nome da tabela como `aluo` (ao invés de `aluno`) no comando SQL de inserção dentro do `try`, seria lançada uma exceção do tipo `SQLException`, com as seguintes informações (no PostgreSQL):

```java
Mensagem: ERRO: relação "aluo" não existe
  Posição: 15
SQLState: 42P01
Erro: 0
```

É possível também criar cláusulas `catch` que tratam de mais de um tipo de exceção. Para isto, usamos uma barra vertical (|). Por exemplo, suponha que o desenvolvedor quisesse carregar manualmente o driver JDBC para a memória usando o método `forName` da classe `Class` (linha 4) e quisesse tratar ambas as exceções da mesma maneira. Poderíamos usar a barra vertical para especificar que a cláusula `catch` captura exceções de ambas as classes (linha 7) - `SQLException` e `ClassNotFoundException`.

```java
public class DBExemplo {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver"); 
            // Código de manipulação do banco de dados
            // omitido
        } catch (SQLException | ClassNotFoundException e){ 
            IO.println("Erro! Contate o suporte.");
            IO.println("Mensagem: " + e.getMessage());
            IO.println("Stack Trace: ");
            e.printStackTrace();
        }
    }
}
```

Se, por exemplo, o driver não fosse encontrado, o programa mostraria (Nota: Na verdade, o valor do número da linha no arquivo `DBExemplo.java` seria levemente diferente (maior), pois o programa completo ainda teria as linhas de importação (`import`).) algo como:

```text
Erro! Contate o suporte.
Mensagem: org.postgresql.Driver
Stack Trace: 
java.lang.ClassNotFoundException: org.postgresql.Driver
	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:580)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:490)
	at java.base/java.lang.Class.forName0(Native Method)
	at java.base/java.lang.Class.forName(Class.java:467)
	at java.base/java.lang.Class.forName(Class.java:458)
	at DBExemplo.main(DBExemplo.java:4)
```

Outra alternativa seria a criação de uma cláusula `catch` para cada tipo de exceção (personalizando o tratamento de exceções para cada tipo). No exemplo a seguir, temos a cláusula `catch` para `SQLException` iniciando na linha 7 e outra para `ClassNotFoundException` iniciando na linha 12:

```java
public class DBExemplo {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver");
            // Código de manipulação do banco de dados
            // omitido
        } catch (SQLException e){ 
            IO.println("SQLException capturada!");
            IO.println("Mensagem: " + e.getMessage());
            IO.println("SQLState: " + e.getSQLState());
            IO.println("Erro: " + e.getErrorCode());  
        } catch (ClassNotFoundException e){ 
            IO.println("Erro ao carregar o Driver JDBC!"); 
            IO.println("Contate o suporte.");
            IO.println("Mensagem: " + e.getMessage());
            IO.println("Stack Trace: ");
            e.printStackTrace();
        }
    }
}
```

Nesse caso, temos dois trechos de código distintos de tratamento de exceções: um para cada tipo de exceção. Note que é possível também tratar mais de um tipo de exceção em um único bloco caso elas tenham uma superclasse em comum (ou uma delas seja superclasse das demais).

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
