---
layout: post
title: "Infoga studenter med PreparedStatement"
date: 2026-11-19
lang: sv
translation_id: inserindo-alunos-preparedstatement-java
permalink: /sv/inserting-students-with-preparedstatement-in-java/
share_text: >-
  Tre direkta infogningar återanvänder en parameteriserad sats utan arrayer eller loopar.
---

Ett `PreparedStatement` innehåller SQL med platshållarna `?`. `setInt` och `setString` anger värdena utan att sammanfoga dem med SQL-texten, vilket minskar risken för SQL-injektion. I kodutdraget är `c` anslutningen till `academic`; `student` har kolumnerna `enrollment_number` och `name`.

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

Position 1 är studentnumret och position 2 namnet. Samma sats körs för Maria, Pedro och João. Motsvarande SQL-satser är:

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

Ett dubbelt studentnummer bryter mot primärnyckeln och orsakar `SQLException`. Det fullständiga programmets `main` vidarebefordrar undantaget och stänger resurserna i slutet.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
