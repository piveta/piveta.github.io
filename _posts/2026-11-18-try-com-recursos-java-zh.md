---
layout: post
title: "Java 中的 try-with-resources"
date: 2026-11-18
lang: zh
translation_id: try-com-recursos-java
permalink: /zh/try-with-resources-in-java/
share_text: >-
  try-with-resources 会自动关闭 AutoCloseable 对象。JDBC 示例展示了如何在一个 try 语句中管理连接、语句和结果集。
---

为了改进资源管理，从 Java 7 起，可以在 `try` 语句中指定语句结束时要关闭的资源。语言规范规定，`try` 语句可以指定一个或多个实现 `AutoCloseable` 接口的资源。根据文档，标准库中有一百多个类实现了这个接口。其定义如下：

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

try-with-resources 的语法如下：

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

资源写在括号内，通常是局部变量声明，或对已确定赋值且实际上为 final 的变量的访问（即该变量未被重新赋值；不要求使用 `final` 修饰符）。在 JDBC 查询中，需要关闭连接、语句和结果集。以下示例将 `c`（第 5 行）、`s`（第 8 行）和 `rs`（第 9 行）的声明及初始化放在 `try` 语句的资源说明部分：

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

这样就不需要 `finally` 块：Java 运行时会自动关闭所有指定的资源。这种方法使代码更简洁，降低忘记关闭资源的可能性，因此是管理资源时推荐的做法。

---

*本文改编自 Eduardo Kessler Piveta 的著作 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
