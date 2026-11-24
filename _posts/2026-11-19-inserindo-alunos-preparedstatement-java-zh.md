---
layout: post
title: "使用 PreparedStatement 插入学生"
date: 2026-11-24
lang: zh
translation_id: inserindo-alunos-preparedstatement-java
permalink: /zh/inserting-students-with-preparedstatement-in-java/
share_text: >-
  不使用数组或循环，直接执行三次参数化插入。
---

`PreparedStatement` 使用 `?` 作为 SQL 参数占位符。`setInt` 和 `setString` 分别设置值，不必将数据拼接进 SQL 字符串，因此有助于防止 SQL 注入。片段中的 `c` 是到 `academic` 的连接；`student` 包含 `enrollment_number` 和 `name` 两列。

```java
IO.println("Inserting students...");
var p = c.prepareStatement("insert into student " +
        "(enrollment_number, name) values (?, ?)");
p.setInt(1, 1); 
p.setString(2, "Maria");
p.execute(); // Inserts 1 - Maria
p.setInt(1, 2);
p.setString(2, "Pedro");
p.execute(); // Inserts 2 - Pedro
p.setInt(1, 3);
p.setString(2, "João");
p.execute(); // Inserts 3 - João
```

位置1是学号，位置2是姓名。同一语句分别为 Maria、Pedro 和 João 执行。等价的 SQL 语句如下：

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

重复学号违反主键约束并引发 `SQLException`。完整程序的 `main` 会继续抛出该异常，最后关闭资源。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
