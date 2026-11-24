---
layout: post
title: "Ausnahmen in Java abfangen und behandeln"
date: 2026-11-24
lang: de
translation_id: capturando-tratando-excecoes-java
permalink: /de/catching-and-handling-exceptions-in-java/
share_text: >-
  try-Blöcke und catch-Klauseln behandeln Ausnahmen in Java. JDBC-Beispiele zeigen SQLException, Multi-Catch und getrennte Behandlung nach Ausnahmetyp.
---

Wenn eine Ausnahme auftritt — sei es ein Fehler oder eine Situation außerhalb des erwarteten Ablaufs —, erzeugt die Methode, in der sie auftritt, ein Objekt einer Ausnahmeklasse und übergibt es zusammen mit den relevanten Informationen an das Laufzeitsystem, in diesem Fall die JVM.

Die JVM durchsucht anschließend den Aufrufstapel nach einem zum Ausnahmeobjekt passenden Ausnahmebehandler. Sie beginnt bei der Methode, in der die Ausnahme aufgetreten ist. Hat diese einen geeigneten Behandler, wird die Ausnahme dort behandelt. Andernfalls prüft die JVM die aufrufende Methode. Die Suche setzt sich im Aufrufstapel fort, bis ein Behandler gefunden oder der ursprüngliche Aufrufer erreicht wird. Behandelt keine Methode die Ausnahme, beendet die JVM das Programm und gibt eine Fehlermeldung sowie den Stacktrace aus, der zur Ausnahme geführt hat.

Java-Code, der geprüfte Ausnahmen auslösen kann, unterliegt der Anforderung **abfangen oder deklarieren**:

- Die Anweisungen, die eine Ausnahme auslösen können, müssen von einem geschützten Block (einem `try`-Block) mit einem passenden Behandler (einer `catch`-Klausel) umgeben sein; oder
- Die Methode, die diese Anweisungen enthält, muss mit `throws` deklarieren, dass sie die Ausnahme auslösen kann. Sie behandelt die Ausnahme dann nicht selbst: Ihr Aufrufer muss sie behandeln oder seinerseits deklarieren, dass er sie weitergibt.

Zur Ausnahmebehandlung stellt Java die **`try`-Anweisung** mit drei Teilen bereit:

- Ein `try`-Block enthält die Anweisungen, die eine Ausnahme auslösen können, und kann auch andere Anweisungen enthalten. Optional können unmittelbar nach `try` Ressourcendeklarationen oder -initialisierungen in Klammern stehen; dies wird `try` mit Ressourcen genannt.
- Null (Hinweis: Ein `try`-Block darf nur dann allein stehen, wenn in einer `try`-Anweisung mit Ressourcen Ressourcen deklariert oder initialisiert werden. Andernfalls ist mindestens eine `catch`-Klausel oder ein `finally`-Block erforderlich) oder mehrere `catch`-Klauseln enthalten Blöcke zur Ausnahmebehandlung. Der Entwickler legt fest, was mit jeder zu behandelnden Ausnahme geschehen soll, falls sie bei der Ausführung des `try`-Blocks ausgelöst wird.
- Null oder ein `finally`-Block enthält Aufräumcode, normalerweise zum Schließen von Dateien oder Freigeben von Ressourcen. Seine Anweisungen laufen unabhängig davon, ob der `try`-Block erfolgreich abgeschlossen wird.

Ein Teil der Syntax einer `try`-Anweisung (Hinweis: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>) ist hier dargestellt:

```text
TryStatement:  
    try Block Catches 
    try Block [Catches] Finally 
    TryWithResourcesStatement 
Catches: 
    CatchClause {CatchClause}
CatchClause:
    catch ( CatchFormalParameter ) Block 
CatchFormalParameter:
    {VariableModifier} CatchType VariableDeclaratorId
CatchType:
    UnannClassType {| ClassType}
Finally: 
    finally Block    
```

Eine `try`-Anweisung (Zeile 1) besteht demnach aus:

- Einem `try`-Block mit anschließenden `catch`-Klauseln (Zeile 2);
- Einem `try`-Block, optionalen `catch`-Klauseln und einem `finally`-Block (Zeile 3); oder
- Einer `try`-Anweisung mit Ressourcen (Zeile 4).

Eine `catch`-Klausel (Zeile 5) besteht aus dem reservierten Wort `catch`, formalen Parametern in Klammern und einem Codeblock (Zeile 6). Mehrere `catch`-Klauseln können aufeinanderfolgen, wie `CatchClause {CatchClause}` zeigt. Ein `finally`-Block besteht aus dem reservierten Wort `finally` und einem Codeblock (Zeile 13).

Dieser Artikel konzentriert sich auf den `try`-Block und die `catch`-Klauseln: Der erste schützt Anweisungen, die Ausnahmen auslösen können; die Klauseln legen fest, wie sie abgefangen und behandelt werden.

## Der `try`-Block

Ein **`try`-Block** umschließt Code, der Ausnahmen auslösen kann — geprüfte Ausnahmen ebenso wie ungeprüfte, die wir ausdrücklich behandeln möchten. Auf das reservierte Wort `try` folgt ein Block in geschweiften Klammern. Tritt eine Ausnahme auf, die von einer der `catch`-Klauseln der Anweisung abgefangen werden kann, geht die Kontrolle an diese Klausel über.

Das folgende Beispiel zeigt eine `try`-Anweisung um mehrere Datenbankzugriffe (Zeilen 3 bis 21). Sie enthält einen `try`-Block (Zeilen 3 bis 18) und eine `catch`-Klausel für `SQLException` (Zeilen 18 bis 21):

```java
public class DBExample {
    public static void main(String[] args) {
        try {   
            var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academic",
            "postgres", "postgres");
           
            IO.println("Listing students...");
            var s = c.createStatement();      
            var rs = s.executeQuery( 
                "select * from student order by enrollment_number");
            while (rs.next()) 
                IO.println(rs.getInt("enrollment_number") + " - " +
                           rs.getString("name"));
            rs.close(); 
            s.close();   
            c.close();   
        } catch (SQLException e){   
            // TODO Handle SQL exceptions
            e.printStackTrace();
        } 
    }
}
```

Die folgenden Imports werden ebenfalls benötigt. Sie werden hier gezeigt; in den weiteren Beispielen gelten die benötigten Typen als importiert (IDEs unterstützen normalerweise beim Hinzufügen der Imports):

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

Um festzustellen, welche Anweisungen des Beispiels tatsächlich Ausnahmen auslösen können, können wir eine IDE verwenden, die Dokumentation der aufgerufenen Methoden lesen oder Compilerfehler untersuchen, die ohne geeignete `catch`-Klausel auftreten würden.

In diesem Beispiel können folgende Methoden eine `SQLException` auslösen:

- `DriverManager.getConnection(...)` — Zeile 4;
- `Connection.createStatement()` — Zeile 9;
- `Statement.executeQuery(...)` — Zeile 10;
- `ResultSet.next()` — Zeile 12;
- `ResultSet.getInt(...)` — Zeile 13;
- `ResultSet.getString(...)` — Zeile 14;
- `ResultSet.close()` — Zeile 15;
- `Statement.close()` — Zeile 16;
- `Connection.close()` — Zeile 17.

Mit anderen Worten: Fast jeder Datenbankvorgang hier — Verbindung öffnen, Statement erstellen, Abfrage ausführen, Ergebnis durchlaufen und Ressourcen schließen — kann eine `SQLException` auslösen.

Eine IDE kann auch anzeigen, welche Aufrufe geschützt werden müssen. Sie weiß aufgrund der Anforderung „abfangen oder deklarieren“, dass eine Methode eine Ausnahme auslösen kann.

Wenn eine Methode eine geprüfte Ausnahme nicht sinnvoll selbst behandeln kann, ergänzt sie ihre Signatur um eine `throws`-Klausel. Die Signatur der Methode `getConnection` von `DriverManager` lautet beispielsweise:

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

Code, der `getConnection` aufruft, muss den Aufruf daher in eine `try`-Anweisung einschließen oder die eigene Methodensignatur um eine `throws`-Klausel ergänzen.

## `catch`-Klauseln

**`catch`-Klauseln** behandeln Ausnahmen aus einem `try`-Block. Für jede geprüfte Ausnahme, die ausgelöst werden kann, lässt sich eine eigene Klausel angeben. Im folgenden Beispiel zeigt eine `catch`-Klausel Einzelheiten der Ausnahme (Zeilen 5 bis 10): ihre Nachricht (Zeile 7), den SQL-Status (Zeile 8) und den datenbankspezifischen Fehlercode (Zeile 9):

```java
public class DBExample {
    public static void main(String[] args) {
        try { 
            // try code identical to the previous listing
        } catch (SQLException e){   
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage()); 
            IO.println("SQLState: " + e.getSQLState()); 
            IO.println("Error: " + e.getErrorCode());
        } 
    }
}
```

Wenn wir beispielsweise in der SQL-Anweisung innerhalb von `try` statt `student` den Tabellennamen `studnet` eingeben, wird eine `SQLException` mit etwa folgenden Informationen ausgelöst (in PostgreSQL):

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

Eine `catch`-Klausel kann mit einem senkrechten Strich (`|`) auch mehrere Ausnahmetypen behandeln. Angenommen, der Entwickler möchte den JDBC-Treiber mit `Class.forName` ausdrücklich laden (Zeile 4) und beide möglichen Ausnahmetypen gleich behandeln. Der senkrechte Strich legt fest, dass die `catch`-Klausel sowohl `SQLException` als auch `ClassNotFoundException` abfängt (Zeile 7):

```java
public class DBExample {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver"); 
            // Database access code
            // omitted
        } catch (SQLException | ClassNotFoundException e){ 
            IO.println("Error! Contact support.");
            IO.println("Message: " + e.getMessage());
            IO.println("Stack Trace: ");
            e.printStackTrace();
        }
    }
}
```

Falls der Treiber nicht gefunden wird, gibt das Programm ungefähr Folgendes aus (Hinweis: Im vollständigen Programm wäre die Zeilennummer in `DBExample.java` etwas höher, weil es zusätzlich `import`-Zeilen enthielte):

```text
Error! Contact support.
Message: org.postgresql.Driver
Stack Trace: 
java.lang.ClassNotFoundException: org.postgresql.Driver
	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:580)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:490)
	at java.base/java.lang.Class.forName0(Native Method)
	at java.base/java.lang.Class.forName(Class.java:467)
	at java.base/java.lang.Class.forName(Class.java:458)
	at DBExample.main(DBExample.java:4)
```

Eine weitere Möglichkeit ist je eine `catch`-Klausel pro Ausnahmetyp, sodass die Behandlung angepasst werden kann. Im nächsten Beispiel beginnt die Klausel für `SQLException` in Zeile 7 und die für `ClassNotFoundException` in Zeile 12:

```java
public class DBExample {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver");
            // Database access code
            // omitted
        } catch (SQLException e){ 
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage());
            IO.println("SQLState: " + e.getSQLState());
            IO.println("Error: " + e.getErrorCode());  
        } catch (ClassNotFoundException e){ 
            IO.println("Error loading the JDBC driver!"); 
            IO.println("Contact support.");
            IO.println("Message: " + e.getMessage());
            IO.println("Stack Trace: ");
            e.printStackTrace();
        }
    }
}
```

Hier gibt es zwei verschiedene Blöcke zur Ausnahmebehandlung, einen für jeden Typ. Mehrere Typen lassen sich auch in einem einzigen Block behandeln, wenn sie eine gemeinsame Oberklasse besitzen (oder einer der Typen eine Oberklasse der anderen ist).

---

*Dieser Artikel basiert auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
