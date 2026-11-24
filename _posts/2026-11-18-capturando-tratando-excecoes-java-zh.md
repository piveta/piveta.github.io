---
layout: post
title: "在 Java 中捕获并处理异常"
date: 2026-11-24
lang: zh
translation_id: capturando-tratando-excecoes-java
permalink: /zh/catching-and-handling-exceptions-in-java/
share_text: >-
  Java 使用 try 块和 catch 子句处理异常。JDBC 示例展示 SQLException、多重捕获和按异常类型分别处理。
---

发生异常时（无论是错误还是偏离预期流程的情况），发生异常的方法会创建一个异常类的对象，并连同相关信息传递给运行系统，即 JVM。

随后 JVM 在调用栈中寻找与该异常对象兼容的处理器。它首先检查异常发生的方法；如果该方法有合适的处理器，就在本地处理。否则 JVM 检查调用该方法的方法。搜索会沿调用栈继续，直到找到处理器或到达最初的调用者。如果没有方法处理异常，JVM 将终止程序，并输出错误消息及导致异常的堆栈跟踪。

可能抛出受检异常的 Java 代码必须满足**捕获或声明**的要求：

- 将可能抛出异常的语句放入有适当处理器（`catch` 子句）的受保护块（`try` 块）中；或者
- 包含这些语句的方法使用 `throws` 声明可能抛出该异常。该方法本身不处理异常；调用者必须处理它，或继续声明可能传播它。

Java 为异常处理提供了由三部分组成的 **`try` 语句**：

- `try` 块包含可能抛出异常的语句，也可以包含其他语句。还可以在 `try` 关键字后面用括号指定资源的声明或初始化，这称为 try-with-resources。
- 零个（注：只有在 try-with-resources 语句中声明或初始化资源时，`try` 块才能单独出现；否则至少需要一个 `catch` 子句或 `finally` 块）或多个 `catch` 子句包含异常处理代码块。开发者指定在执行 `try` 块期间抛出各类待处理异常时应采取的操作。
- 零个或一个 `finally` 块包含清理代码，通常用于关闭文件或释放资源。无论 `try` 块是否成功完成，这些语句都会执行。

以下是 `try` 语句的部分语法（注：<https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>）：

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

因此，`try` 语句（第 1 行）可以由以下部分组成：

- `try` 块，后接 `catch` 子句（第 2 行）；
- `try` 块、可选的 `catch` 子句和 `finally` 块（第 3 行）；或
- try-with-resources 语句（第 4 行）。

`catch` 子句（第 5 行）由保留字 `catch`、括号内的形式参数以及代码块（第 6 行）构成。可以连续使用多个 `catch` 子句，如 `CatchClause {CatchClause}` 所示。`finally` 块由保留字 `finally` 和代码块构成（第 13 行）。

本文重点介绍 `try` 块与 `catch` 子句：前者保护可能抛出异常的语句，后者定义如何捕获并处理异常。

## `try` 块

**`try` 块**包围可能抛出异常的代码，包括受检异常，以及我们希望显式处理的非受检异常。保留字 `try` 后面是用花括号包围的代码块。如果发生的异常能被该语句的某个 `catch` 子句捕获，控制流就会转到那个子句。

以下示例用 `try` 语句包围多个数据库访问操作（第 3 至 21 行）。它包含一个 `try` 块（第 3 至 18 行）以及处理 `SQLException` 的 `catch` 子句（第 18 至 21 行）：

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

还需要以下导入。这里先列出它们；后续示例假定已导入相关类型（IDE 通常会协助添加导入）：

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

要确定示例中哪些语句实际上可能抛出异常，可以使用 IDE、查阅所调用方法的文档，或查看缺少合适 `catch` 子句时的编译错误。

在本例中，以下方法可能抛出 `SQLException`：

- `DriverManager.getConnection(...)` —— 第 4 行；
- `Connection.createStatement()` —— 第 9 行；
- `Statement.executeQuery(...)` —— 第 10 行；
- `ResultSet.next()` —— 第 12 行；
- `ResultSet.getInt(...)` —— 第 13 行；
- `ResultSet.getString(...)` —— 第 14 行；
- `ResultSet.close()` —— 第 15 行；
- `Statement.close()` —— 第 16 行；
- `Connection.close()` —— 第 17 行。

换言之，示例中几乎所有数据库操作——打开连接、创建语句、执行查询、遍历结果和关闭资源——都可能抛出 `SQLException`。

IDE 还能指出哪些调用需要保护。之所以能知道某个方法可能抛出异常，是因为存在“捕获或声明”的要求。

如果一个方法不知道如何处理受检异常，或不适合在自身内部处理，就会在签名中添加 `throws` 子句。例如，`DriverManager` 中 `getConnection` 的签名如下：

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

因此，调用 `getConnection` 的代码必须将调用放在 `try` 语句中，或在自身方法的签名中添加 `throws` 子句。

## `catch` 子句

**`catch` 子句**处理来自 `try` 块的异常。对每一种可能抛出的受检异常，都可以提供单独的 `catch` 子句。在以下示例中，`catch` 子句显示异常的细节（第 5 至 10 行）：消息（第 7 行）、SQL 状态（第 8 行）和数据库特有的错误代码（第 9 行）：

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

例如，如果在 `try` 中的 SQL 语句里把表名 `student` 错写为 `studnet`，PostgreSQL 会抛出包含类似以下信息的 `SQLException`：

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

使用竖线（`|`），一个 `catch` 子句还可以处理多个异常类型。假设开发者希望通过 `Class.forName` 显式加载 JDBC 驱动（第 4 行），并以同样方式处理两种可能的异常。竖线表示该 `catch` 子句同时捕获 `SQLException` 和 `ClassNotFoundException`（第 7 行）：

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

如果找不到驱动，程序会显示大致如下的内容（注：完整程序还会包含 `import` 行，因此 `DBExample.java` 中实际的行号会稍大一些）：

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

另一种方法是为每种异常类型提供单独的 `catch` 子句，以便分别处理。在下一个示例中，处理 `SQLException` 的子句从第 7 行开始，处理 `ClassNotFoundException` 的子句从第 12 行开始：

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

这里有两个不同的异常处理块，每种类型各一个。如果多个类型具有共同的父类（或其中一种类型是其他类型的父类），也可以在一个块中处理。

---

*本文改编自 Eduardo Kessler Piveta 的著作 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
