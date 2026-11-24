---
layout: post
title: "Ansluta Java till PostgreSQL med JDBC"
date: 2026-11-24
lang: sv
translation_id: conectando-postgresql-jdbc-java
permalink: /sv/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager öppnar anslutningen till academic innan SQL-operationerna körs.
---

JDBC låter ett Java-program använda en relationsdatabas. `DriverManager.getConnection` får PostgreSQL-URL, användarnamn och lösenord och returnerar ett `Connection`-objekt. Databasen `academic` och tabellen `student(enrollment_number, name)` måste finnas; projektet behöver också PostgreSQLs JDBC-drivrutin.

Följande fullständiga engelska program infogar, listar, ändrar och tar bort studenter. Både användarnamn och lösenord är fasta värden, `postgres`; den lokala installationen måste godta dem.

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

I URL:en är `localhost` servern, `5432` porten och `academic` databasens namn. `main` deklarerar `throws SQLException` och vidarebefordrar JDBC-fel. Efter normal körning stänger programmet resurserna uttryckligen med `close()`.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
