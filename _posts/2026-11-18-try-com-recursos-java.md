---
layout: post
title: "try com recursos em Java"
date: 2026-11-18
lang: pt-BR
translation_id: try-com-recursos-java
permalink: /try-com-recursos-java/
share_text: >-
  O artigo apresenta try com recursos e o fechamento automático de objetos AutoCloseable, usando conexão, sentença e resultado JDBC como exemplo.
---

Como forma de melhorar o gerenciamento de recursos, a linguagem Java permite, desde a versão 7, que sejam informados na sentença `try` os recursos passíveis de serem fechados ao término de sua execução. A especificação da linguagem diz que uma sentença `try` pode informar um ou mais recursos que implementem a interface `AutoCloseable`. Tal interface, de acordo com sua documentação, é implementada por mais de cem classes da biblioteca padrão da linguagem. A seguir, temos sua definição:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

A sintaxe para o `try` com recursos é a seguinte:

```text
TryWithResourcesStatement:
    try ResourceSpecification Block [Catches] [Finally]
ResourceSpecification:
    ( ResourceList [;] )
ResourceList:
    Resource {; Resource}
Resource:
    LocalVariableDeclaration
    VariableAccess
VariableAccess:
    ExpressionName
    FieldAccess
```

Especificamos os recursos entre parênteses, tipicamente uma declaração de variável local ou um acesso a uma variável já definitivamente atribuída e efetivamente final (que não tenha sido reatribuída — não é obrigatório que ela tenha o modificador `final`). Em uma consulta JDBC, a conexão, a sentença e o conjunto de resultados precisam ser fechados. O exemplo a seguir coloca a declaração e inicialização das variáveis `c` (linha 5), `s` (linha 8) e `rs` (linha 9) na especificação de recursos do `try` com recursos:

```java
import java.sql.*;

public class DBExemplo {
    public static void main(String[] args) {
        try (var c = DriverManager.getConnection(
              "jdbc:postgresql://localhost:5432/academico",
              "postgres", "postgres");
             var s = c.createStatement();
             var rs = s.executeQuery(
              "select * from aluno order by matricula");){
            IO.println("Listando os alunos...");
            while (rs.next())
                IO.println(rs.getInt("matricula") + " - " +
                           rs.getString("nome"));
        } catch (SQLException e){
            // TODO Tratar exceções de SQL
        }
    }
}
```

Desta forma, não precisamos do bloco `finally`, pois todos os recursos informados serão fechados automaticamente pelo ambiente de execução da linguagem. Tal abordagem simplifica bastante o código e reduz a probabilidade de esquecermos de fechar algum recurso, sendo a abordagem recomendada atualmente (considerando trechos de código que manipulam recursos).

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
