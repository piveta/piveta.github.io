---
layout: post
title: "try mit Ressourcen in Java"
date: 2026-11-18
lang: de
translation_id: try-com-recursos-java
permalink: /de/try-with-resources-in-java/
share_text: >-
  try mit Ressourcen schließt AutoCloseable-Objekte automatisch. Das Beispiel verwaltet eine JDBC-Verbindung, ein Statement und ein ResultSet in einer try-Anweisung.
---

Um die Verwaltung von Ressourcen zu verbessern, können seit Java 7 die Ressourcen, die am Ende einer `try`-Anweisung geschlossen werden sollen, innerhalb dieser Anweisung angegeben werden. Laut Sprachspezifikation darf eine `try`-Anweisung eine oder mehrere Ressourcen enthalten, die das Interface `AutoCloseable` implementieren. Der Dokumentation zufolge wird dieses Interface von mehr als hundert Klassen der Standardbibliothek implementiert. Seine Definition lautet:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

Die Syntax von `try` mit Ressourcen lautet:

```text
TryWithResourcesStatement:
    try ResourceSpecification Block [Catches] [Finally]
ResourceSpecification:
    ( ResourceList [;] )
ResourceList:
    Resource {; Resource}
Resource:
    LocalVariableDeclaration
    VariableAccess
VariableAccess:
    ExpressionName
    FieldAccess
```

Ressourcen werden in Klammern angegeben, normalerweise durch die Deklaration einer lokalen Variablen oder durch den Zugriff auf eine bereits definitiv zugewiesene und effektiv finale Variable (sie wurde also nicht erneut zugewiesen; der Modifikator `final` ist nicht erforderlich). Bei einer JDBC-Abfrage müssen Verbindung, Statement und ResultSet geschlossen werden. Im folgenden Beispiel stehen die Deklarationen und Initialisierungen von `c` (Zeile 5), `s` (Zeile 8) und `rs` (Zeile 9) in der Ressourcenspezifikation der `try`-Anweisung:

```java
import java.sql.*;

public class DBExample {
    public static void main(String[] args) {
        try (var c = DriverManager.getConnection(
              "jdbc:postgresql://localhost:5432/academic",
              "postgres", "postgres");
             var s = c.createStatement();
             var rs = s.executeQuery(
              "select * from student order by enrollment_number");){
            IO.println("Listing students...");
            while (rs.next())
                IO.println(rs.getInt("enrollment_number") + " - " +
                           rs.getString("name"));
        } catch (SQLException e){
            // TODO Handle SQL exceptions
        }
    }
}
```

Ein `finally`-Block ist damit nicht nötig: Die Java-Laufzeitumgebung schließt alle angegebenen Ressourcen automatisch. Das vereinfacht den Code und verringert das Risiko, eine Ressource offen zu lassen. Für Code, der Ressourcen verwaltet, ist dies der empfohlene Ansatz.

---

*Dieser Artikel basiert auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
