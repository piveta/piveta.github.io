---
layout: post
title: "Java mit PostgreSQL über JDBC verbinden"
date: 2026-11-24
lang: de
translation_id: conectando-postgresql-jdbc-java
permalink: /de/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager öffnet die Verbindung zu academic; das Programm führt SQL-Operationen aus.
---

JDBC verbindet ein Java-Programm mit einer relationalen Datenbank. `DriverManager.getConnection` erhält die PostgreSQL-URL sowie Benutzer und Passwort und liefert ein `Connection`-Objekt. Die Datenbank `academic` mit `student(enrollment_number, name)` muss vorhanden sein; außerdem benötigt das Projekt den PostgreSQL-JDBC-Treiber.

Das vollständige englische Programm fügt Studierende ein, listet sie auf, ändert und löscht sie. Benutzername und Passwort sind im Beispiel fest auf `postgres` gesetzt; die lokale Installation muss diese Zugangsdaten akzeptieren.

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

In der URL bezeichnet `localhost` den Server, `5432` den Port und `academic` die Datenbank. `main` deklariert `throws SQLException` und gibt Datenbankfehler damit an den Aufrufer weiter. Nach einem normalen Ablauf schließt das Programm die JDBC-Ressourcen ausdrücklich mit `close()`.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
