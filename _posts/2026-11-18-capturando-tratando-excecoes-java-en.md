---
layout: post
title: "Catching and Handling Exceptions in Java"
date: 2026-11-24
lang: en
translation_id: capturando-tratando-excecoes-java
permalink: /en/catching-and-handling-exceptions-in-java/
share_text: >-
  Java's try block and catch clauses handle exceptions. JDBC examples illustrate SQLException, multi-catch, and separate handling for different exception types.
---

When an exception occurs (whether an error or a situation outside the expected flow), the method in which it occurs creates an object of an exception class and sends it to the runtime system (the JVM), together with relevant information about the exception.

The JVM then searches the call stack for an exception handler compatible with the exception object. It begins with the method where the exception occurred. If that method has a suitable handler, the exception is handled locally. Otherwise, the JVM checks the method's caller. This search continues through the call stack until a handler is found or the initial caller is reached. If no method handles the exception, the JVM terminates the program and prints an error message and the stack trace that led to the exception.

Java code that may throw checked exceptions is subject to the **catch-or-specify** requirement. Thus:

- The statements that may throw an exception must be enclosed in a protected block (a `try` block) with an appropriate handler (a `catch` clause); or
- The method containing those statements must declare that it may throw the exception, using `throws`. The method does not handle the exception; its caller must handle it or, in turn, specify that it may throw it.

To support exception handling, Java provides the **`try` statement**, which has three parts:

- A `try` block contains the statements that may throw an exception and may also contain other statements. Optionally, resource declarations or initializations can appear immediately after the `try` keyword, in parentheses; this is called try-with-resources.
- Zero (Note: A `try` block can stand alone only when resources are declared or initialized in a try-with-resources statement. Otherwise, at least one `catch` clause or a `finally` block is required.) or more `catch` clauses contain exception-handling blocks. The developer specifies what should happen for each exception that will be handled if one is thrown during execution of the `try` block.
- Zero or one `finally` block contains cleanup code, typically to close files or release resources. Its statements run regardless of whether the `try` block completes successfully.

Part of the syntax of a `try` statement (Note: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>) is shown below:

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

Accordingly, a `try` statement (line 1) consists of:

- A `try` block followed by `catch` clauses (line 2);
- A `try` block followed by optional `catch` clauses and a `finally` block (line 3); or
- A try-with-resources statement (line 4).

A `catch` clause (line 5) consists of the reserved word `catch`, followed by formal parameters in parentheses and then a code block (line 6). Several `catch` clauses may follow one another, as indicated by `CatchClause {CatchClause}`. A `finally` block consists of the reserved word `finally` followed by a code block (line 13).

This article focuses on the `try` block and `catch` clauses: the former protects statements that may throw exceptions, while the latter define how to catch and handle them.

## The `try` block

A **`try` block** encloses code that may throw exceptions, whether checked exceptions or unchecked ones we explicitly want to handle. The reserved word `try` is followed by a block enclosed in braces. If an exception occurs that can be caught by one of the statement's `catch` clauses, control passes to that clause.

The following example shows a `try` statement around several statements that access a database (lines 3 to 21). It has a `try` block (lines 3 to 18) and a `catch` clause for `SQLException` (lines 18 to 21):

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

The following imports are also needed. They are shown here; subsequent examples assume the relevant types have been imported (IDEs normally help with these imports):

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

To identify which statements in the example may actually throw exceptions, we can use an IDE, consult the documentation of the methods called, or examine compiler errors that would occur without an appropriate `catch` clause.

In this example, the methods that may throw `SQLException` are:

- `DriverManager.getConnection(...)` — line 4;
- `Connection.createStatement()` — line 9;
- `Statement.executeQuery(...)` — line 10;
- `ResultSet.next()` — line 12;
- `ResultSet.getInt(...)` — line 13;
- `ResultSet.getString(...)` — line 14;
- `ResultSet.close()` — line 15;
- `Statement.close()` — line 16;
- `Connection.close()` — line 17.

In other words, nearly every database operation here—opening the connection, creating the statement, executing the query, iterating over the result, and closing resources—may throw `SQLException`.

An IDE can also show which calls require protection. It knows that a method may throw an exception because of the catch-or-specify requirement.

If a method does not know how to handle a checked exception, or if handling it there is inappropriate, it adds a `throws` clause to its signature. For example, the signature of the `getConnection` method in `DriverManager` is:

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

This means that code calling `getConnection` must either enclose the call in a `try` statement or add a `throws` clause to its own method signature.

## `catch` clauses

**`catch` clauses** handle exceptions arising in a `try` block. We can provide a separate `catch` clause for each checked exception that may be thrown. In the following example, a `catch` clause displays details of the exception (lines 5 to 10): its message (line 7), SQL state (line 8), and database-specific error code (line 9):

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

If, for example, we typed `studnet` instead of `student` as the table name in the SQL statement inside `try`, a `SQLException` would be thrown with information such as the following (in PostgreSQL):

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

A `catch` clause can also handle more than one exception type by using a vertical bar (`|`). Suppose, for example, that the developer wanted to load the JDBC driver explicitly with `Class.forName` (line 4) and handle both possible exception types in the same way. The vertical bar specifies that the `catch` clause catches both `SQLException` and `ClassNotFoundException` (line 7):

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

If the driver could not be found, the program would display something like the following (Note: The line number in `DBExample.java` would actually be slightly higher in the complete program because it would also contain `import` lines):

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

Another option is to provide one `catch` clause for each exception type, tailoring the handling to each. In the next example, the `catch` clause for `SQLException` starts on line 7 and the one for `ClassNotFoundException` starts on line 12:

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

Here, we have two distinct exception-handling blocks, one for each exception type. It is also possible to handle more than one exception type in a single block if they have a common superclass (or if one type is a superclass of the others).

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
