---
layout: post
title: "Inserire studenti con PreparedStatement"
date: 2026-11-24
lang: it
translation_id: inserindo-alunos-preparedstatement-java
permalink: /it/inserting-students-with-preparedstatement-in-java/
share_text: >-
  Tre inserimenti diretti riutilizzano una query parametrizzata senza array né cicli.
---

Un `PreparedStatement` contiene SQL con segnaposto `?`. `setInt` e `setString` forniscono i valori senza concatenarli al testo SQL, riducendo il rischio di SQL injection. Nel frammento, `c` è la connessione a `academic` e `student` contiene `enrollment_number` e `name`.

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

La posizione 1 è il numero di iscrizione e la 2 è il nome. La stessa istruzione viene eseguita per Maria, Pedro e João. Le istruzioni SQL equivalenti sono:

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

Un numero duplicato viola la chiave primaria e causa una `SQLException`. Il `main` del programma completo propaga l’eccezione e chiude le risorse alla fine.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
