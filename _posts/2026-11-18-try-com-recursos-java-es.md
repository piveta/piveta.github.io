---
layout: post
title: "try con recursos en Java"
date: 2026-11-18
lang: es
translation_id: try-com-recursos-java
permalink: /es/try-with-resources-in-java/
share_text: >-
  La sentencia try con recursos cierra automáticamente los objetos AutoCloseable. El ejemplo gestiona una conexión JDBC, una sentencia y un conjunto de resultados.
---

Para mejorar la gestión de recursos, Java permite desde la versión 7 especificar en una sentencia `try` los recursos que pueden cerrarse al terminarla. La especificación del lenguaje indica que una sentencia `try` puede incluir uno o más recursos que implementen la interfaz `AutoCloseable`. Según su documentación, más de cien clases de la biblioteca estándar implementan esta interfaz. Su definición es la siguiente:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

La sintaxis de `try` con recursos es la siguiente:

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

Los recursos se especifican entre paréntesis, normalmente mediante la declaración de una variable local o el acceso a una variable que ya haya sido asignada definitivamente y sea efectivamente final (es decir, que no se haya reasignado; no se requiere el modificador `final`). En una consulta JDBC deben cerrarse la conexión, la sentencia y el conjunto de resultados. El siguiente ejemplo coloca las declaraciones e inicializaciones de `c` (línea 5), `s` (línea 8) y `rs` (línea 9) en la especificación de recursos de la sentencia `try` con recursos:

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

Así no se necesita un bloque `finally`: el entorno de ejecución de Java cierra automáticamente todos los recursos especificados. Este enfoque simplifica el código y reduce la probabilidad de dejar algún recurso abierto. Es el enfoque recomendado para el código que gestiona recursos.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
