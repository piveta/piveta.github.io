---
layout: post
title: "O bloco finally em Java"
date: 2026-11-18
lang: pt-BR
translation_id: bloco-finally-java
permalink: /bloco-finally-java/
share_text: >-
  O bloco finally executa a finalização após try e catch; os exemplos mostram o fechamento de ResultSet, Statement e Connection e seus cuidados.
---

Uma sentença `try` pode ter um bloco de finalização associado, chamado **bloco `finally`**, que é executado independentemente de o trecho de código do bloco `try` ter sido concluído com sucesso ou não. No exemplo a seguir, a sentença `try` possui um bloco `finally` associado (iniciando na linha 25) que fecha os recursos abertos dentro do bloco `try`. São fechados o `ResultSet`, o `Statement` e a conexão (`Connection`):

```java
import java.sql.*; 

public class DBExemplo {
    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        ResultSet rs = null;
        try {
            c = DriverManager.getConnection(
               "jdbc:postgresql://localhost:5432/academico",
               "postgres", "postgres");

            IO.println("Listando os alunos...");
            s = c.createStatement();
            rs = s.executeQuery(
               "select * from aluno order by matricula");
            while (rs.next())
                IO.println(rs.getInt("matricula") + " - " +
                           rs.getString("nome"));
        } catch (SQLException e) {
            IO.println("SQLException capturada!");
            IO.println("Mensagem: " + e.getMessage()); 
            IO.println("SQLState: " + e.getSQLState()); 
            IO.println("Erro: " + e.getErrorCode()); 
        } finally { 
            rs.close(); // Fecha o ResultSet
            s.close();  // Fecha o Statement
            c.close();  // Fecha a Connection
        }
    }
}
```

Note, no entanto, que o método `close` (de `ResultSet`, `Statement` e `Connection`) também pode lançar uma `SQLException`. Então, o exemplo anterior não compilaria. Logo, precisamos ou tratar esta exceção ou especificar que não a trataremos. Podemos fazer isso com uma sentença `try` aninhada para cada chamada (caso exista um tratamento diferente para cada sentença) ou usar uma única sentença para as três chamadas:

```java
import java.sql.*; 

public class DBExemplo {
    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        ResultSet rs = null;
        try {
            // Código restante omitido
        } catch (SQLException e){
            // TODO Tratar exceções de SQL
        } 
        finally {
            try {
                rs.close(); 
            } catch (SQLException e) {
                // Ignora ou faz um log da exceção
                System.err.println("Erro ao fechar: "
                        + e.getMessage());
            }
            try {
                s.close(); 
            } catch (SQLException e) {
                System.err.println("Erro ao fechar: "
                        + e.getMessage());
            }
            try {
                c.close(); 
            } catch (SQLException e) {
                System.err.println("Erro ao fechar: "
                        + e.getMessage());
            }
        }
    }
}
```

Esse código ainda poderia lançar uma exceção não verificada do tipo `NullPointerException` caso `rs` ou `s` ou `c` fossem `null` (linhas 15, 22 e 28, respectivamente). Normalmente, exceções não verificadas não são capturadas e tratadas, mas sim a origem do problema é corrigida.

Podemos então verificar se as variáveis têm `null` como valor antes de chamar o método `close`. Isto é feito no exemplo a seguir, nas linhas 4, 12 e 20:

```java
    // Codigo omitido - idem listagem anterior...
    finally {
        try {
            if (rs != null) 
                rs.close(); // Fecha o ResultSet
        } catch(SQLException e){
            // Ignora ou faz um log da exceção
            System.err.println("Erro ao fechar: " 
               + e.getMessage());
        }
        try {
            if (s != null) 
                s.close();  // Fecha o Statement
        } catch(SQLException e){
            // Ignora ou faz um log da exceção
            System.err.println("Erro ao fechar: " 
               + e.getMessage());
        }
        try {
            if (c != null) 
                c.close();  // Fecha a Connection
        } catch(SQLException e){
            // Ignora ou faz um log da exceção
            System.err.println("Erro ao fechar: " 
               + e.getMessage());
        }
    }
```

Mesmo fazendo tudo isso, caso as sentenças do bloco `try` inicial lançassem uma `SQLException` e um dos métodos `close` falhasse (e fosse lançada uma nova `SQLException`), poderíamos perder as informações da exceção original. É possível guardar a exceção original e adicionar as exceções de `close` como suprimidas (usando os métodos `addSuppressed` e `getSuppressed` de `Throwable`, por exemplo). No entanto, isso complicaria ainda mais o código.

Portanto, para mitigar toda essa verbosidade e essa série de problemas e empecilhos no tratamento de recursos, foi adicionada uma variante da sentença `try` que permite especificar os recursos a serem fechados ao término da sentença (independente de sua completa execução ou não). Tal sentença é chamada de **`try` com recursos** (Nota: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
