---
layout: post
title: "Inserting Students with PreparedStatement in Java"
date: 2026-11-19
lang: en
translation_id: inserindo-alunos-preparedstatement-java
permalink: /en/inserting-students-with-preparedstatement-in-java/
share_text: >-
  The book's JDBC example inserts Maria, Pedro, and João by reusing a PreparedStatement with two parameters.
---

In the book's example, `PreparedStatement` represents a parameterized SQL statement. Question marks (`?`) stand for variable values, which are supplied with methods such as `setInt` and `setString`. This avoids concatenating data into the SQL statement and reduces the risk of SQL injection.

The translated excerpt below belongs to the `main` method of `DBExample`. The variable `c` is the connection opened with `DriverManager.getConnection` to the PostgreSQL database `academic`. The `student` table has `enrollment_number` (integer, primary key) and `name` (text) columns. As in the book, the code inserts three students directly, without arrays or loops:

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

Position **1** is the enrollment number, and position **2** is the name. The `PreparedStatement` is reused: after each pair of values, `execute()` runs the insertion. The three operations correspond to the English equivalents of the SQL statements shown in the book:

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

Because `enrollment_number` is the primary key, the database rejects an insertion with a repeated value. In this example, `main` declares `throws SQLException`, so the failure is propagated. The connection, statement, and other resources are closed explicitly at the end of the book's complete program.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
