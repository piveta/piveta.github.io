---
layout: post
title: "Collegare Java a PostgreSQL con JDBC"
date: 2026-11-24
lang: it
translation_id: conectando-postgresql-jdbc-java
permalink: /it/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager apre la connessione ad academic per eseguire le operazioni SQL.
---

JDBC permette a Java di collegarsi a un database relazionale. `DriverManager.getConnection` riceve URL PostgreSQL, utente e password e restituisce un oggetto `Connection`. Devono esistere il database `academic` e la tabella `student(enrollment_number, name)`; il progetto richiede anche il driver JDBC PostgreSQL.

Il programma completo in inglese inserisce, elenca, modifica ed elimina studenti. Utente e password sono fissati a `postgres`; l’installazione locale deve accettare queste credenziali.

```java
public class DBExample {
    public static void main(String[] args) 
        throws SQLException {
        var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academic", 
            "postgres", "postgres");
     
        IO.println("Inserting students...");
        var p = c.prepareStatement("insert into student " + 
                "(enrollment_number, name) values (?, ?)");
        p.setInt(1, 1);
        p.setString(2, "Maria");
        p.execute();
        p.setInt(1, 2);
        p.setString(2, "Pedro");
        p.execute();
        p.setInt(1, 3);
        p.setString(2, "João");
        p.execute();

        IO.println("Listing students...");
        var s = c.createStatement();      
        var rs = s.executeQuery(
          "select * from student order by enrollment_number");
        while (rs.next()) 
            IO.println(rs.getInt("enrollment_number") + " - " + 
                rs.getString("name"));

        IO.println("Updating a student...");
        p = c.prepareStatement(
          "update student set name = ? where enrollment_number = ?");
        p.setInt(2, 1);
        p.setString(1, "Maria da Silva");
        p.execute();

        IO.println("Listing students...");
        rs = s.executeQuery(
          "select * from student order by enrollment_number");
        while (rs.next()) 
            IO.println(rs.getInt("enrollment_number") + " - " +
                rs.getString("name"));

        IO.println("Deleting all students...");
        s.executeUpdate("delete from student");
        rs.close();
        s.close();
        p.close();
        c.close();
    }
}
```

Nell’URL, `localhost` indica il server, `5432` la porta e `academic` il database. `main` dichiara `throws SQLException`, quindi propaga gli errori JDBC. Al termine normale, il programma chiude esplicitamente le risorse con `close()`.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
