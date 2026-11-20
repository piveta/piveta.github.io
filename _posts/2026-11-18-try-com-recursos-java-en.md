---
layout: post
title: "Try-with-resources in Java"
date: 2026-11-18
lang: en
translation_id: try-com-recursos-java
permalink: /en/try-with-resources-in-java/
share_text: >-
  Try-with-resources closes AutoCloseable objects automatically. This article shows how a JDBC connection, statement, and result set can be managed in one try statement.
---

To improve resource management, Java has allowed, since version 7, resources that can be closed at the end of a `try` statement to be specified within that statement. The language specification says that a `try` statement may specify one or more resources that implement the `AutoCloseable` interface. According to its documentation, this interface is implemented by more than a hundred classes in the standard library. Its definition follows:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

The syntax of try-with-resources is as follows:

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

We specify resources in parentheses, typically through a local variable declaration or access to a variable that has already been definitely assigned and is effectively final (that is, it has not been reassigned; the `final` modifier is not required). In a JDBC query, the connection, statement, and result set must be closed. The following example places the declarations and initializations of `c` (line 5), `s` (line 8), and `rs` (line 9) in the resource specification of the try-with-resources statement:

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

This way, we do not need a `finally` block: all specified resources are closed automatically by the Java runtime. This approach simplifies the code and makes it less likely that a resource will be left open. It is the recommended approach for code that manages resources.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
