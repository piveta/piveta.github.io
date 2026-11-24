---
layout: post
title: "Conectando ao PostgreSQL com JDBC em Java"
date: 2026-11-24
lang: pt-BR
translation_id: conectando-postgresql-jdbc-java
permalink: /conectando-postgresql-jdbc-java/
share_text: >-
  O programa DBExemplo do livro usa DriverManager e Connection para acessar o banco academico com JDBC.
---

JDBC (*Java Database Connectivity*) permite que um programa Java se conecte a um banco relacional e execute SQL. No exemplo do livro, `DriverManager.getConnection` recebe a URL do PostgreSQL, o usuário e a senha e devolve um objeto `Connection`. O banco `academico` deve existir no servidor local, na porta `5432`, com a tabela `aluno(matricula, nome)`. O projeto também precisa do driver JDBC do PostgreSQL.

O código completo do exemplo do livro é o seguinte. Ele insere, lista, altera e exclui alunos. As credenciais `postgres` e `postgres` são **valores fixos do exemplo didático**; a instalação local precisa estar configurada com eles para que a conexão funcione.

```java
public class DBExemplo {
    public static void main(String[] args) 
        throws SQLException {
        var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academico", 
            "postgres", "postgres");
     
        IO.println("Inserindo alunos...");
        var p = c.prepareStatement("insert into aluno " + 
                "(matricula, nome) values (?, ?)");
        p.setInt(1, 1);
        p.setString(2, "Maria");
        p.execute();
        p.setInt(1, 2);
        p.setString(2, "Pedro");
        p.execute();
        p.setInt(1, 3);
        p.setString(2, "João");
        p.execute();

        IO.println("Listando os alunos...");
        var s = c.createStatement();      
        var rs = s.executeQuery(
          "select * from aluno order by matricula");
        while (rs.next()) 
            IO.println(rs.getInt("matricula") + " - " + 
                rs.getString("nome"));

        IO.println("Alterando um aluno...");
        p = c.prepareStatement(
          "update aluno set nome = ? where matricula = ?");
        p.setInt(2, 1);
        p.setString(1, "Maria da Silva");
        p.execute();

        IO.println("Listando os alunos...");
        rs = s.executeQuery(
          "select * from aluno order by matricula");
        while (rs.next()) 
            IO.println(rs.getInt("matricula") + " - " +
                rs.getString("nome"));

        IO.println("Apagando todos os alunos...");
        s.executeUpdate("delete from aluno");
        rs.close();
        s.close();
        p.close();
        c.close();
    }
}
```

Na URL, `jdbc` é o protocolo da API, `postgresql` identifica o banco, `localhost` é a máquina do servidor, `5432` é a porta e `academico` é a base de dados. O método `getConnection` seleciona o driver adequado e cria a conexão usada pelas operações seguintes.

O programa declara `throws SQLException` em `main`: se uma operação JDBC falhar, a exceção é propagada, em vez de ser tratada nesse método. Ao final do fluxo normal, o exemplo fecha `ResultSet`, `Statement`, `PreparedStatement` e `Connection` com chamadas explícitas a `close()`, como mostrado no código original.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
