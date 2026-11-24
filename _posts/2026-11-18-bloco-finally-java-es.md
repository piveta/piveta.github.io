---
layout: post
title: "El bloque finally en Java"
date: 2026-11-24
lang: es
translation_id: bloco-finally-java
permalink: /es/finally-block-in-java/
share_text: >-
  El bloque finally se ejecuta tras try y catch aunque falle la operación. Los ejemplos JDBC muestran los cuidados necesarios al cerrar ResultSet, Statement y Connection manualmente.
---

Una sentencia `try` puede tener asociado un bloque de finalización, llamado **bloque `finally`**, que se ejecuta independientemente de si el código del bloque `try` terminó correctamente. En el siguiente ejemplo, la sentencia `try` tiene un bloque `finally` (que comienza en la línea 25) que cierra los recursos abiertos en el bloque `try`: el `ResultSet`, el `Statement` y la conexión (`Connection`):

```java
import java.sql.*; 

public class DBExample {
    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        ResultSet rs = null;
        try {
            c = DriverManager.getConnection(
               "jdbc:postgresql://localhost:5432/academic",
               "postgres", "postgres");

            IO.println("Listing students...");
            s = c.createStatement();
            rs = s.executeQuery(
               "select * from student order by enrollment_number");
            while (rs.next())
                IO.println(rs.getInt("enrollment_number") + " - " +
                           rs.getString("name"));
        } catch (SQLException e) {
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage()); 
            IO.println("SQLState: " + e.getSQLState()); 
            IO.println("Error: " + e.getErrorCode()); 
        } finally { 
            rs.close(); // Closes the ResultSet
            s.close();  // Closes the Statement
            c.close();  // Closes the Connection
        }
    }
}
```

Sin embargo, el método `close` de `ResultSet`, `Statement` y `Connection` también puede lanzar una `SQLException`. Por eso, el ejemplo anterior no compilaría. Debemos tratar la excepción o declarar que no la trataremos. Podemos utilizar una sentencia `try` anidada para cada llamada (si cada una requiere un tratamiento diferente), o una única sentencia para las tres llamadas:

```java
import java.sql.*; 

public class DBExample {
    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        ResultSet rs = null;
        try {
            // Remaining code omitted
        } catch (SQLException e){
            // TODO Handle SQL exceptions
        } 
        finally {
            try {
                rs.close(); 
            } catch (SQLException e) {
                // Ignore or log the exception
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
            try {
                s.close(); 
            } catch (SQLException e) {
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
            try {
                c.close(); 
            } catch (SQLException e) {
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
        }
    }
}
```

Este código aún podría lanzar una `NullPointerException` no verificada si `rs`, `s` o `c` fueran `null` (en las líneas 15, 22 y 28, respectivamente). Normalmente, las excepciones no verificadas no se capturan para tratarlas: se corrige la causa del problema.

Podemos comprobar si cada variable es `null` antes de llamar a `close`. El siguiente ejemplo lo hace en las líneas 4, 12 y 20:

```java
    // Code omitted - same as the previous listing...
    finally {
        try {
            if (rs != null) 
                rs.close(); // Closes the ResultSet
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
        try {
            if (s != null) 
                s.close();  // Closes the Statement
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
        try {
            if (c != null) 
                c.close();  // Closes the Connection
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
    }
```

Incluso después de todo esto, si una sentencia del bloque `try` inicial lanzara una `SQLException` y fallara uno de los métodos `close` (lanzando otra `SQLException`), podríamos perder la información de la excepción original. Podríamos conservarla y añadir las excepciones producidas por `close` como excepciones suprimidas, mediante métodos de `Throwable` como `addSuppressed` y `getSuppressed`. Pero eso complicaría aún más el código.

Para reducir esta verbosidad y las dificultades del tratamiento de recursos, Java incorporó una variante de la sentencia `try` que especifica los recursos que deben cerrarse cuando termina la sentencia, tanto si finaliza normalmente como si no. Se denomina **`try` con recursos** (Nota: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
