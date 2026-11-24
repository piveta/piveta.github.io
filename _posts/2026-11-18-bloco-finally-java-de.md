---
layout: post
title: "Der finally-Block in Java"
date: 2026-11-18
lang: de
translation_id: bloco-finally-java
permalink: /de/finally-block-in-java/
share_text: >-
  Ein finally-Block wird nach try und catch auch bei Fehlern ausgeführt. JDBC-Beispiele zeigen die Schwierigkeiten beim manuellen Schließen von ResultSet, Statement und Connection.
---

Eine `try`-Anweisung kann einen zugehörigen Abschlussblock besitzen, den **`finally`-Block**. Er wird unabhängig davon ausgeführt, ob der Code im `try`-Block erfolgreich abgeschlossen wurde. Im folgenden Beispiel enthält die `try`-Anweisung einen `finally`-Block (ab Zeile 25), der die im `try`-Block geöffneten Ressourcen schließt: `ResultSet`, `Statement` und die Verbindung (`Connection`):

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

Allerdings kann die Methode `close` von `ResultSet`, `Statement` und `Connection` selbst eine `SQLException` auslösen. Deshalb würde das vorherige Beispiel nicht kompilieren. Wir müssen die Ausnahme behandeln oder deklarieren, dass wir sie nicht behandeln. Dazu können wir für jeden Aufruf eine geschachtelte `try`-Anweisung verwenden (wenn jeder Aufruf eine andere Behandlung erfordert) oder eine Anweisung für alle drei Aufrufe:

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

Dieser Code könnte weiterhin eine ungeprüfte `NullPointerException` auslösen, wenn `rs`, `s` oder `c` den Wert `null` hätten (in den Zeilen 15, 22 beziehungsweise 28). Normalerweise fängt man ungeprüfte Ausnahmen nicht einfach ab, sondern behebt die Ursache des Problems.

Wir können vor dem Aufruf von `close` prüfen, ob die jeweilige Variable `null` ist. Im folgenden Beispiel geschieht das in den Zeilen 4, 12 und 20:

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

Selbst danach könnten Informationen über die ursprüngliche Ausnahme verloren gehen: wenn eine Anweisung im ersten `try`-Block eine `SQLException` auslöst und eine der `close`-Methoden fehlschlägt und eine weitere `SQLException` auslöst. Wir könnten die ursprüngliche Ausnahme behalten und die Ausnahmen aus `close` als unterdrückte Ausnahmen hinzufügen, etwa mit `addSuppressed` und `getSuppressed` aus `Throwable`. Das würde den Code aber noch komplizierter machen.

Um diese Ausführlichkeit und die Schwierigkeiten bei der Ressourcenbehandlung zu verringern, wurde eine Variante der `try`-Anweisung eingeführt. Darin werden Ressourcen angegeben, die am Ende der Anweisung geschlossen werden, unabhängig davon, ob sie normal endet. Diese Variante heißt **`try` mit Ressourcen** (Hinweis: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*Dieser Artikel basiert auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
