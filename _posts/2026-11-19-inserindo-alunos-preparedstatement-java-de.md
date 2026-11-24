---
layout: post
title: "Studierende mit PreparedStatement einfügen"
date: 2026-11-19
lang: de
translation_id: inserindo-alunos-preparedstatement-java
permalink: /de/inserting-students-with-preparedstatement-in-java/
share_text: >-
  Drei direkte Einfügungen verwenden dieselbe parametrisierte Anweisung ohne Arrays oder Schleifen.
---

Ein `PreparedStatement` enthält SQL mit Platzhaltern `?`. `setInt` und `setString` setzen die Werte ein, ohne sie mit dem SQL-Text zu verketten; dadurch sinkt das Risiko einer SQL-Injektion. Im Ausschnitt ist `c` die offene Verbindung zur Datenbank `academic`; die Tabelle `student` hat `enrollment_number` und `name`.

```java
IO.println("Inserting students...");
var p = c.prepareStatement("insert into student " +
        "(enrollment_number, name) values (?, ?)");
p.setInt(1, 1); 
p.setString(2, "Maria");
p.execute(); // Inserts 1 - Maria
p.setInt(1, 2);
p.setString(2, "Pedro");
p.execute(); // Inserts 2 - Pedro
p.setInt(1, 3);
p.setString(2, "João");
p.execute(); // Inserts 3 - João
```

Position 1 ist die Matrikelnummer, Position 2 der Name. Dieselbe Anweisung wird für Maria, Pedro und João dreimal ausgeführt. Das entspricht folgenden SQL-Anweisungen:

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

Eine doppelte Matrikelnummer verletzt den Primärschlüssel und führt zu einer `SQLException`. Das vollständige Programm gibt sie über `main` weiter und schließt seine Ressourcen am Ende.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
