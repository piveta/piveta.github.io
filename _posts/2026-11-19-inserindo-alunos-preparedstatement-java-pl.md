---
layout: post
title: "Wstawianie studentów przez PreparedStatement"
date: 2026-11-19
lang: pl
translation_id: inserindo-alunos-preparedstatement-java
permalink: /pl/inserting-students-with-preparedstatement-in-java/
share_text: >-
  Trzy bezpośrednie wstawienia używają jednej instrukcji parametryzowanej, bez tablic i pętli.
---

`PreparedStatement` przechowuje SQL z parametrami `?`. Metody `setInt` i `setString` podają wartości bez łączenia ich z tekstem zapytania, co ogranicza ryzyko SQL injection. W tym fragmencie `c` jest połączeniem z `academic`, a `student` ma kolumny `enrollment_number` i `name`.

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

Pozycja 1 oznacza numer studenta, a pozycja 2 jego nazwę. Tę samą instrukcję wykonuje się dla Marii, Pedra i João. Odpowiadają jej polecenia SQL:

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

Powtórzenie numeru narusza klucz główny i powoduje `SQLException`. W pełnym programie `main` przekazuje wyjątek dalej, a zasoby są zamykane na końcu.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
