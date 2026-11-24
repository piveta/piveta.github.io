---
layout: post
title: "Le bloc finally en Java"
date: 2026-11-24
lang: fr
translation_id: bloco-finally-java
permalink: /fr/finally-block-in-java/
share_text: >-
  Un bloc finally s’exécute après try et catch, même en cas d’échec. Des exemples JDBC montrent les difficultés de fermeture manuelle de ResultSet, Statement et Connection.
---

Une instruction `try` peut être associée à un bloc de finalisation, appelé **bloc `finally`**, exécuté que le code du bloc `try` se termine correctement ou non. Dans l’exemple suivant, l’instruction `try` possède un bloc `finally` (à partir de la ligne 25) qui ferme les ressources ouvertes dans le bloc `try` : le `ResultSet`, le `Statement` et la connexion (`Connection`) :

```java
import java.sql.*; 

public class DBExample {
    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        ResultSet rs = null;
        try {
            c = DriverManager.getConnection(
               "jdbc:postgresql://localhost:5432/academic",
               "postgres", "postgres");

            IO.println("Listing students...");
            s = c.createStatement();
            rs = s.executeQuery(
               "select * from student order by enrollment_number");
            while (rs.next())
                IO.println(rs.getInt("enrollment_number") + " - " +
                           rs.getString("name"));
        } catch (SQLException e) {
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage()); 
            IO.println("SQLState: " + e.getSQLState()); 
            IO.println("Error: " + e.getErrorCode()); 
        } finally { 
            rs.close(); // Closes the ResultSet
            s.close();  // Closes the Statement
            c.close();  // Closes the Connection
        }
    }
}
```

Cependant, la méthode `close` de `ResultSet`, `Statement` et `Connection` peut elle-même lever une `SQLException`. L’exemple précédent ne compilerait donc pas. Nous devons traiter cette exception ou déclarer que nous ne la traiterons pas. Nous pouvons utiliser une instruction `try` imbriquée pour chaque appel (si chacun demande un traitement différent), ou une seule instruction pour les trois appels :

```java
import java.sql.*; 

public class DBExample {
    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        ResultSet rs = null;
        try {
            // Remaining code omitted
        } catch (SQLException e){
            // TODO Handle SQL exceptions
        } 
        finally {
            try {
                rs.close(); 
            } catch (SQLException e) {
                // Ignore or log the exception
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
            try {
                s.close(); 
            } catch (SQLException e) {
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
            try {
                c.close(); 
            } catch (SQLException e) {
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
        }
    }
}
```

Ce code pourrait encore lever une `NullPointerException` non vérifiée si `rs`, `s` ou `c` valaient `null` (aux lignes 15, 22 et 28, respectivement). En général, on ne se contente pas d’intercepter les exceptions non vérifiées : on corrige la cause du problème.

Nous pouvons vérifier si chaque variable vaut `null` avant d’appeler `close`. C’est ce que fait l’exemple suivant aux lignes 4, 12 et 20 :

```java
    // Code omitted - same as the previous listing...
    finally {
        try {
            if (rs != null) 
                rs.close(); // Closes the ResultSet
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
        try {
            if (s != null) 
                s.close();  // Closes the Statement
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
        try {
            if (c != null) 
                c.close();  // Closes the Connection
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
    }
```

Même après cela, nous pourrions perdre les informations sur l’exception initiale si une instruction du premier bloc `try` levait une `SQLException` et si l’une des méthodes `close` échouait en levant une nouvelle `SQLException`. Nous pourrions conserver l’exception initiale et ajouter celles de `close` comme exceptions supprimées, à l’aide de méthodes de `Throwable` telles que `addSuppressed` et `getSuppressed`. Le code en deviendrait toutefois plus complexe.

Pour réduire cette verbosité et ces difficultés, Java a ajouté une variante de l’instruction `try` dans laquelle on indique les ressources à fermer à la fin de l’instruction, qu’elle se termine normalement ou non. Il s’agit de **`try` avec ressources** (Remarque : <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
