---
layout: post
title: "PreparedStatementで学生を追加する"
date: 2026-11-24
lang: ja
translation_id: inserindo-alunos-preparedstatement-java
permalink: /ja/inserting-students-with-preparedstatement-in-java/
share_text: >-
  配列やループを使わず、同じパラメーター付きSQLを3回実行します。
---

`PreparedStatement` は `?` を使って値を後から設定するSQL文です。`setInt` と `setString` で値を渡すため、値をSQL文字列に連結せずに済み、SQLインジェクションの危険を減らせます。ここで `c` は `academic` への接続で、`student` の列は `enrollment_number` と `name` です。

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

位置1が学籍番号、位置2が名前です。同じ文をMaria、Pedro、Joãoに対して実行します。対応するSQLは次のとおりです。

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

学籍番号が重複すると主キー制約に違反し、`SQLException` が発生します。完全なプログラムでは `main` が例外を伝播し、最後にリソースを閉じます。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
