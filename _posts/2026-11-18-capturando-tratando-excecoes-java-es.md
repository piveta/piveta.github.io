---
layout: post
title: "Captura y tratamiento de excepciones en Java"
date: 2026-11-24
lang: es
translation_id: capturando-tratando-excecoes-java
permalink: /es/catching-and-handling-exceptions-in-java/
share_text: >-
  Los bloques try y las cláusulas catch permiten tratar excepciones en Java. Ejemplos JDBC ilustran SQLException, la captura múltiple y el tratamiento separado por tipo.
---

Cuando ocurre una excepción (sea un error o una situación fuera del flujo esperado), el método en el que ocurre crea un objeto de una clase de excepción y lo envía al sistema de ejecución (la JVM), junto con la información pertinente sobre la excepción.

La JVM busca entonces en la pila de llamadas un manejador compatible con el objeto de excepción. Comienza por el método en el que ocurrió. Si ese método dispone de un manejador adecuado, la excepción se trata localmente. De lo contrario, la JVM examina el método que lo llamó. La búsqueda continúa por la pila hasta encontrar un manejador o llegar a la llamada inicial. Si ningún método trata la excepción, la JVM termina el programa e imprime un mensaje de error y el rastreo de la pila que condujo a ella.

El código Java que puede lanzar excepciones verificadas está sujeto al requisito de **capturar o especificar**. Por tanto:

- Las sentencias que pueden lanzar una excepción deben incluirse en un bloque protegido (un bloque `try`) con un manejador adecuado (una cláusula `catch`); o
- El método que contiene esas sentencias debe declarar con `throws` que puede lanzar la excepción. Ese método no la trata: el método que lo llama debe tratarla o, a su vez, declarar que puede lanzarla.

Para facilitar el tratamiento de excepciones, Java proporciona la **sentencia `try`**, que tiene tres partes:

- Un bloque `try` contiene las sentencias que pueden lanzar una excepción y también puede contener otras sentencias. Opcionalmente, pueden aparecer declaraciones o inicializaciones de recursos inmediatamente después de la palabra `try`, entre paréntesis; esto se denomina `try` con recursos.
- Cero (Nota: Un bloque `try` puede aparecer solo únicamente cuando se declaran o inicializan recursos en una sentencia `try` con recursos. En caso contrario, se necesita al menos una cláusula `catch` o un bloque `finally`) o más cláusulas `catch` contienen los bloques de tratamiento. El desarrollador indica qué debe ocurrir con cada excepción que se tratará si se lanza durante la ejecución del bloque `try`.
- Cero o un bloque `finally` contiene código de limpieza, normalmente para cerrar archivos o liberar recursos. Sus sentencias se ejecutan independientemente de si el bloque `try` termina correctamente.

A continuación se muestra parte de la sintaxis de una sentencia `try` (Nota: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>):

```text
TryStatement:  
    try Block Catches 
    try Block [Catches] Finally 
    TryWithResourcesStatement 
Catches: 
    CatchClause {CatchClause}
CatchClause:
    catch ( CatchFormalParameter ) Block 
CatchFormalParameter:
    {VariableModifier} CatchType VariableDeclaratorId
CatchType:
    UnannClassType {| ClassType}
Finally: 
    finally Block    
```

Por tanto, una sentencia `try` (línea 1) consta de:

- Un bloque `try` seguido de cláusulas `catch` (línea 2);
- Un bloque `try` seguido de cláusulas `catch` opcionales y un bloque `finally` (línea 3); o
- Una sentencia `try` con recursos (línea 4).

Una cláusula `catch` (línea 5) consta de la palabra reservada `catch`, seguida de parámetros formales entre paréntesis y de un bloque de código (línea 6). Pueden aparecer varias cláusulas `catch` consecutivas, como indica `CatchClause {CatchClause}`. Un bloque `finally` consta de la palabra reservada `finally` seguida de un bloque de código (línea 13).

Este artículo se centra en el bloque `try` y las cláusulas `catch`: el primero protege las sentencias que pueden lanzar excepciones y las segundas definen cómo capturarlas y tratarlas.

## El bloque `try`

Un **bloque `try`** engloba código que puede lanzar excepciones, ya sean verificadas o no verificadas que queramos tratar explícitamente. La palabra reservada `try` va seguida de un bloque entre llaves. Si se produce una excepción que puede capturar alguna de las cláusulas `catch` de la sentencia, el control pasa a esa cláusula.

El siguiente ejemplo muestra una sentencia `try` que engloba varias operaciones de acceso a una base de datos (líneas 3 a 21). Tiene un bloque `try` (líneas 3 a 18) y una cláusula `catch` para `SQLException` (líneas 18 a 21):

```java
public class DBExample {
    public static void main(String[] args) {
        try {   
            var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academic",
            "postgres", "postgres");
           
            IO.println("Listing students...");
            var s = c.createStatement();      
            var rs = s.executeQuery( 
                "select * from student order by enrollment_number");
            while (rs.next()) 
                IO.println(rs.getInt("enrollment_number") + " - " +
                           rs.getString("name"));
            rs.close(); 
            s.close();   
            c.close();   
        } catch (SQLException e){   
            // TODO Handle SQL exceptions
            e.printStackTrace();
        } 
    }
}
```

También se necesitan las siguientes importaciones. Se muestran aquí; en los ejemplos posteriores se supone que los tipos pertinentes ya están importados (las IDE suelen ayudar a añadir estas importaciones):

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

Para identificar qué sentencias del ejemplo pueden lanzar realmente excepciones, podemos utilizar una IDE, consultar la documentación de los métodos llamados o examinar los errores del compilador que surgirían sin una cláusula `catch` adecuada.

En este ejemplo, los métodos que pueden lanzar una `SQLException` son:

- `DriverManager.getConnection(...)` — línea 4;
- `Connection.createStatement()` — línea 9;
- `Statement.executeQuery(...)` — línea 10;
- `ResultSet.next()` — línea 12;
- `ResultSet.getInt(...)` — línea 13;
- `ResultSet.getString(...)` — línea 14;
- `ResultSet.close()` — línea 15;
- `Statement.close()` — línea 16;
- `Connection.close()` — línea 17.

En otras palabras, casi todas las operaciones de base de datos de este ejemplo —abrir la conexión, crear la sentencia, ejecutar la consulta, recorrer el resultado y cerrar los recursos— pueden lanzar una `SQLException`.

Una IDE también puede indicar qué llamadas requieren protección. Sabe que un método puede lanzar una excepción gracias al requisito de capturar o especificar.

Si un método no sabe cómo tratar una excepción verificada, o no conviene tratarla allí, añade una cláusula `throws` a su firma. Por ejemplo, la firma del método `getConnection` de `DriverManager` es:

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

Esto significa que el código que llama a `getConnection` debe incluir la llamada en una sentencia `try` o añadir una cláusula `throws` a la firma de su propio método.

## Cláusulas `catch`

Las **cláusulas `catch`** tratan las excepciones que se producen en un bloque `try`. Podemos proporcionar una cláusula distinta para cada excepción verificada que pueda lanzarse. En el siguiente ejemplo, una cláusula `catch` muestra los datos de la excepción (líneas 5 a 10): su mensaje (línea 7), el estado SQL (línea 8) y el código de error específico de la base de datos (línea 9):

```java
public class DBExample {
    public static void main(String[] args) {
        try { 
            // try code identical to the previous listing
        } catch (SQLException e){   
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage()); 
            IO.println("SQLState: " + e.getSQLState()); 
            IO.println("Error: " + e.getErrorCode());
        } 
    }
}
```

Si, por ejemplo, escribiéramos `studnet` en lugar de `student` como nombre de la tabla en la sentencia SQL dentro de `try`, se lanzaría una `SQLException` con información como la siguiente (en PostgreSQL):

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

Una cláusula `catch` también puede tratar más de un tipo de excepción mediante una barra vertical (`|`). Supongamos que el desarrollador quisiera cargar explícitamente el driver JDBC con `Class.forName` (línea 4) y tratar los dos tipos de excepción posibles de la misma forma. La barra vertical indica que la cláusula `catch` captura tanto `SQLException` como `ClassNotFoundException` (línea 7):

```java
public class DBExample {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver"); 
            // Database access code
            // omitted
        } catch (SQLException | ClassNotFoundException e){ 
            IO.println("Error! Contact support.");
            IO.println("Message: " + e.getMessage());
            IO.println("Stack Trace: ");
            e.printStackTrace();
        }
    }
}
```

Si no se encontrara el driver, el programa mostraría algo como lo siguiente (Nota: El número de línea de `DBExample.java` sería en realidad algo mayor en el programa completo, porque este también contendría líneas `import`):

```text
Error! Contact support.
Message: org.postgresql.Driver
Stack Trace: 
java.lang.ClassNotFoundException: org.postgresql.Driver
	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:580)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:490)
	at java.base/java.lang.Class.forName0(Native Method)
	at java.base/java.lang.Class.forName(Class.java:467)
	at java.base/java.lang.Class.forName(Class.java:458)
	at DBExample.main(DBExample.java:4)
```

Otra posibilidad consiste en incluir una cláusula `catch` para cada tipo de excepción y adaptar el tratamiento a cada uno. En el siguiente ejemplo, la cláusula para `SQLException` comienza en la línea 7 y la de `ClassNotFoundException` en la línea 12:

```java
public class DBExample {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver");
            // Database access code
            // omitted
        } catch (SQLException e){ 
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage());
            IO.println("SQLState: " + e.getSQLState());
            IO.println("Error: " + e.getErrorCode());  
        } catch (ClassNotFoundException e){ 
            IO.println("Error loading the JDBC driver!"); 
            IO.println("Contact support.");
            IO.println("Message: " + e.getMessage());
            IO.println("Stack Trace: ");
            e.printStackTrace();
        }
    }
}
```

Aquí tenemos dos bloques de tratamiento distintos, uno por cada tipo de excepción. También es posible tratar varios tipos en un solo bloque si comparten una superclase (o si uno de ellos es superclase de los demás).

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
