---
layout: post
title: "Insertar estudiantes con PreparedStatement"
date: 2026-11-19
lang: es
translation_id: inserindo-alunos-preparedstatement-java
permalink: /es/inserting-students-with-preparedstatement-in-java/
share_text: >-
  Tres inserciones directas reutilizan una sentencia parametrizada, sin arreglos ni bucles.
---

Un `PreparedStatement` representa una sentencia SQL con parámetros `?`. Los métodos `setInt` y `setString` asignan los valores sin concatenarlos con la SQL. Esto ayuda a evitar la inyección de SQL. En el fragmento, `c` es una conexión abierta a la base `academic`, y la tabla `student` tiene las columnas `enrollment_number` y `name`.

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

La posición 1 corresponde al número de matrícula y la posición 2 al nombre. La misma sentencia se ejecuta tres veces para Maria, Pedro y João. Las sentencias SQL equivalentes son:

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

Una matrícula duplicada infringe la clave primaria y provoca una `SQLException`. El método `main` del programa completo propaga esa excepción y cierra sus recursos al final.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
