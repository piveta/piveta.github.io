---
layout: post
title: "Connecter Java à PostgreSQL avec JDBC"
date: 2026-11-24
lang: fr
translation_id: conectando-postgresql-jdbc-java
permalink: /fr/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager ouvre la connexion à academic avant les opérations SQL.
---

JDBC relie un programme Java à une base relationnelle. `DriverManager.getConnection` reçoit l’URL PostgreSQL, l’utilisateur et le mot de passe, puis renvoie un objet `Connection`. La base `academic` et la table `student(enrollment_number, name)` doivent exister ; le pilote JDBC PostgreSQL est également nécessaire.

Voici le programme complet en anglais. Il insère, affiche, modifie et supprime des étudiants. Les deux identifiants de connexion sont fixés à `postgres` dans l’exemple ; l’installation locale doit les accepter.

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

Dans l’URL, `localhost` est le serveur, `5432` le port et `academic` la base. `main` déclare `throws SQLException` et propage donc les erreurs JDBC. À la fin d’une exécution normale, le programme ferme explicitement ses ressources avec `close()`.

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
