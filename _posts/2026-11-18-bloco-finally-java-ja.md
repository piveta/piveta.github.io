---
layout: post
title: "Javaのfinallyブロック"
date: 2026-11-18
lang: ja
translation_id: bloco-finally-java
permalink: /ja/finally-block-in-java/
share_text: >-
  finallyブロックはtryとcatchの後に、処理が失敗しても実行されます。JDBCのResultSet、Statement、Connectionを手動で閉じる際の注意点を示します。
---

`try`文には、**`finally`ブロック**と呼ばれる終了処理のブロックを付けられます。`try`ブロック内のコードが正常に終了したかどうかに関係なく実行されます。次の例の`finally`ブロック（25行目から）は、`try`ブロックで開いた`ResultSet`、`Statement`、接続（`Connection`）を閉じます。

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

ただし、`ResultSet`、`Statement`、`Connection`の`close`メソッド自身も`SQLException`をスローすることがあります。したがって、上の例はコンパイルできません。この例外を処理するか、処理しないことを宣言する必要があります。呼び出しごとに異なる処理をするなら各呼び出しにネストした`try`文を使い、そうでなければ三つの呼び出しに一つの文を使うこともできます。

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

それでも、`rs`、`s`、`c`が`null`なら、それぞれ15、22、28行目で非検査例外`NullPointerException`が発生する可能性があります。通常、非検査例外を単に捕捉して処理するのではなく、問題の原因を修正します。

そこで`close`を呼ぶ前に各変数が`null`かどうかを確認します。次の例では4、12、20行目にその検査があります。

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

これらを行っても、最初の`try`ブロック内の文が`SQLException`をスローし、その後いずれかの`close`メソッドが失敗して新たな`SQLException`をスローすると、元の例外の情報を失う可能性があります。元の例外を保持し、`Throwable`の`addSuppressed`や`getSuppressed`などを使って、`close`による例外を抑制された例外として追加できます。しかし、コードはさらに複雑になります。

こうした冗長さやリソース処理上の問題を減らすため、Javaには`try`文の終了時に閉じるリソースを指定する形式が追加されました。文が正常に終わるかどうかは問いません。この形式を**リソース付き`try`文**と呼びます（注: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>）。

---

*この記事は、Eduardo Kessler Piveta著『[Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)』の内容をもとにしています。*
