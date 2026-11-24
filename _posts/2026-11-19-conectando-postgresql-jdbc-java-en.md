---
layout: post
title: "Connecting to PostgreSQL with JDBC in Java"
date: 2026-11-24
lang: en
translation_id: conectando-postgresql-jdbc-java
permalink: /en/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  An English adaptation of the book's program uses DriverManager and Connection to access the academic database through JDBC.
---

JDBC (*Java Database Connectivity*) lets a Java program connect to a relational database and execute SQL. In this English adaptation of the book's example, `DriverManager.getConnection` receives the PostgreSQL URL, username, and password and returns a `Connection` object. The `academic` database must exist on the local server at port `5432`, with the `student(enrollment_number, name)` table. The project also needs the PostgreSQL JDBC driver.

The English version of the book's complete program follows. Its identifiers, SQL names, and messages are translated; its JDBC operations and control flow are preserved. It inserts, lists, updates, and deletes students. The `postgres` username and `postgres` password are **fixed values in this teaching example**; the local installation must be configured with them for the connection to work.

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

In the URL, `jdbc` identifies the API protocol, `postgresql` identifies the database, `localhost` is the server machine, `5432` is the port, and `academic` is the database name. `getConnection` selects the appropriate driver and creates the connection used by the following operations.

The program declares `throws SQLException` in `main`: if a JDBC operation fails, the exception is propagated rather than handled in this method. At the end of the normal flow, the example explicitly closes the `ResultSet`, `Statement`, `PreparedStatement`, and `Connection` with `close()` calls, as in the original listing.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
