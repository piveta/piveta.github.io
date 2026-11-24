---
layout: post
title: "Łączenie Javy z PostgreSQL przez JDBC"
date: 2026-11-24
lang: pl
translation_id: conectando-postgresql-jdbc-java
permalink: /pl/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager otwiera połączenie z academic przed wykonaniem operacji SQL.
---

JDBC umożliwia programowi Java dostęp do relacyjnej bazy danych. `DriverManager.getConnection` otrzymuje URL PostgreSQL, użytkownika i hasło, po czym zwraca `Connection`. Baza `academic` i tabela `student(enrollment_number, name)` muszą istnieć, a projekt musi zawierać sterownik JDBC PostgreSQL.

Poniższy pełny program po angielsku wstawia, wyświetla, zmienia i usuwa studentów. Zarówno użytkownik, jak i hasło mają w przykładzie stałą wartość `postgres`; lokalna instalacja musi je akceptować.

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

W adresie `localhost` oznacza serwer, `5432` port, a `academic` nazwę bazy. `main` deklaruje `throws SQLException`, więc przekazuje błędy JDBC dalej. Po normalnym wykonaniu program jawnie zamyka zasoby przez `close()`.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
