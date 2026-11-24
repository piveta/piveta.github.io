---
layout: post
title: "JDBCでJavaからPostgreSQLに接続する"
date: 2026-11-24
lang: ja
translation_id: conectando-postgresql-jdbc-java
permalink: /ja/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManagerでacademicに接続し、SQL操作を実行するプログラムを示します。
---

JDBCはJavaプログラムからリレーショナルデータベースを利用するためのAPIです。`DriverManager.getConnection` はPostgreSQLのURL、ユーザー名、パスワードを受け取り、`Connection` を返します。`academic` と `student(enrollment_number, name)` を作成し、PostgreSQLのJDBCドライバーをプロジェクトに追加しておきます。

次は英語版の完全なプログラムです。学生の追加、一覧表示、変更、削除を行います。接続情報は例に合わせて `postgres` と `postgres` に固定されています。

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

URLの `localhost` はサーバー、`5432` はポート、`academic` はデータベース名です。`main` の `throws SQLException` により、JDBCエラーは呼び出し側へ伝えられます。正常終了時には `close()` を明示的に呼び、リソースを閉じます。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
