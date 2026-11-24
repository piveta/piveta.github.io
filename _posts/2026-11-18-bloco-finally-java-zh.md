---
layout: post
title: "Java 中的 finally 块"
date: 2026-11-18
lang: zh
translation_id: bloco-finally-java
permalink: /zh/finally-block-in-java/
share_text: >-
  finally 块会在 try 和 catch 之后执行，即使操作失败也一样。JDBC 示例说明手动关闭 ResultSet、Statement 和 Connection 时的难点。
---

`try` 语句可以带有一个称为 **`finally` 块**的收尾块。无论 `try` 块中的代码是否成功完成，它都会执行。以下示例中的 `finally` 块（从第 25 行开始）关闭 `try` 块中打开的资源：`ResultSet`、`Statement` 和连接（`Connection`）：

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

不过，`ResultSet`、`Statement` 和 `Connection` 的 `close` 方法本身也可能抛出 `SQLException`。因此，上面的示例无法通过编译。我们必须处理这个异常，或声明不处理。可以为每次调用使用嵌套的 `try` 语句（如果它们需要不同的处理），也可以用一个语句处理这三次调用：

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

如果 `rs`、`s` 或 `c` 为 `null`，这段代码仍可能分别在第 15、22、28 行抛出非受检的 `NullPointerException`。通常不应只是捕获非受检异常，而应修正问题的根源。

因此，可以在调用 `close` 前检查变量是否为 `null`。下面的示例在第 4、12、20 行进行了检查：

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

即便如此，如果最初的 `try` 块抛出 `SQLException`，而某个 `close` 方法随后失败并抛出新的 `SQLException`，我们仍可能丢失原始异常的信息。可以保留原始异常，并借助 `Throwable` 的 `addSuppressed` 和 `getSuppressed` 等方法，将 `close` 产生的异常作为被抑制的异常附加进去。但代码会更加复杂。

为减少这种冗长写法和资源管理中的困难，Java 增加了一种 `try` 语句变体，可以指定语句结束时要关闭的资源，而不论语句是否正常完成。这就是 **try-with-resources**（注：<https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>）。

---

*本文改编自 Eduardo Kessler Piveta 的著作 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
