---
layout: post
title: "The finally Block in Java"
date: 2026-11-18
lang: en
translation_id: bloco-finally-java
permalink: /en/finally-block-in-java/
share_text: >-
  A finally block runs after try and catch even when execution fails. JDBC examples show the complications of closing ResultSet, Statement, and Connection manually.
---

A `try` statement may have an associated finalization block, called a **`finally` block**, which runs regardless of whether the code in the `try` block completed successfully. In the following example, the `try` statement has a `finally` block (starting on line 25) that closes the resources opened in the `try` block: the `ResultSet`, the `Statement`, and the connection (`Connection`):

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

Note, however, that the `close` method of `ResultSet`, `Statement`, and `Connection` can itself throw a `SQLException`. Therefore, the preceding example would not compile. We must either handle the exception or declare that we will not handle it. We can use a nested `try` statement for each call (if each call requires different handling), or use one statement for all three calls:

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

This code could still throw an unchecked `NullPointerException` if `rs`, `s`, or `c` were `null` (on lines 15, 22, and 28, respectively). Normally, unchecked exceptions are not caught and handled; instead, the cause of the problem is corrected.

We can check whether each variable is `null` before calling `close`. This is done in the following example, on lines 4, 12, and 20:

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

Even after doing all this, if a statement in the initial `try` block threw a `SQLException` and one of the `close` methods failed (throwing a new `SQLException`), we could lose information about the original exception. We could retain the original exception and add the `close` exceptions as suppressed exceptions, using methods such as `addSuppressed` and `getSuppressed` of `Throwable`. That would make the code even more complicated.

To reduce this verbosity and these difficulties in resource handling, Java added a variant of the `try` statement that specifies resources to close when the statement ends, whether or not it completes normally. This is called **try-with-resources** (Note: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
