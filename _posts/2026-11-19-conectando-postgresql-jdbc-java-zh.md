---
layout: post
title: "使用 JDBC 将 Java 连接到 PostgreSQL"
date: 2026-11-24
lang: zh
translation_id: conectando-postgresql-jdbc-java
permalink: /zh/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager 打开到 academic 的连接并执行 SQL 操作。
---

JDBC 让 Java 程序访问关系数据库。`DriverManager.getConnection` 接收 PostgreSQL URL、用户名和密码，并返回 `Connection`。运行前要创建 `academic` 和 `student(enrollment_number, name)`，并为项目添加 PostgreSQL JDBC 驱动。

以下是完整的英文程序，依次插入、列出、修改和删除学生。用户名和密码在示例中都固定为 `postgres`；本地安装需要接受这组凭据。

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

URL 中，`localhost` 是服务器，`5432` 是端口，`academic` 是数据库名。`main` 声明 `throws SQLException`，因此会继续抛出 JDBC 错误。正常完成时，程序显式调用 `close()` 关闭资源。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
