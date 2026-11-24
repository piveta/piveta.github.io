---
layout: post
title: "Conectar Java a PostgreSQL con JDBC"
date: 2026-11-24
lang: es
translation_id: conectando-postgresql-jdbc-java
permalink: /es/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager abre una conexión con la base academic y el programa ejecuta operaciones SQL.
---

JDBC permite conectar un programa Java a una base de datos relacional. En este ejemplo, `DriverManager.getConnection` recibe la URL de PostgreSQL, el usuario y la contraseña, y devuelve una `Connection`. La base `academic` y la tabla `student(enrollment_number, name)` deben existir; también se necesita el controlador JDBC de PostgreSQL.

El siguiente es el programa completo en inglés. Inserta, enumera, modifica y elimina estudiantes. `postgres` es tanto el usuario como la contraseña fija del ejemplo; la instalación local debe aceptar esas credenciales.

```java
public class DBExample {
    public static void main(String[] args) 
        throws SQLException {
        var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academic", 
            "postgres", "postgres");
     
        IO.println("Inserting students...");
        var p = c.prepareStatement("insert into student " + 
                "(enrollment_number, name) values (?, ?)");
        p.setInt(1, 1);
        p.setString(2, "Maria");
        p.execute();
        p.setInt(1, 2);
        p.setString(2, "Pedro");
        p.execute();
        p.setInt(1, 3);
        p.setString(2, "João");
        p.execute();

        IO.println("Listing students...");
        var s = c.createStatement();      
        var rs = s.executeQuery(
          "select * from student order by enrollment_number");
        while (rs.next()) 
            IO.println(rs.getInt("enrollment_number") + " - " + 
                rs.getString("name"));

        IO.println("Updating a student...");
        p = c.prepareStatement(
          "update student set name = ? where enrollment_number = ?");
        p.setInt(2, 1);
        p.setString(1, "Maria da Silva");
        p.execute();

        IO.println("Listing students...");
        rs = s.executeQuery(
          "select * from student order by enrollment_number");
        while (rs.next()) 
            IO.println(rs.getInt("enrollment_number") + " - " +
                rs.getString("name"));

        IO.println("Deleting all students...");
        s.executeUpdate("delete from student");
        rs.close();
        s.close();
        p.close();
        c.close();
    }
}
```

En la URL, `localhost` indica el servidor, `5432` la puerta y `academic` la base. El método `main` declara `throws SQLException`: si una operación falla, propaga la excepción. Al terminar normalmente, el código llama explícitamente a `close()` para cerrar los recursos JDBC.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
