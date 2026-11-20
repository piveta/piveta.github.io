---
layout: post
title: "Javaのリソース付きtry文"
date: 2026-11-18
lang: ja
translation_id: try-com-recursos-java
permalink: /ja/try-with-resources-in-java/
share_text: >-
  リソース付きtry文はAutoCloseableオブジェクトを自動的に閉じます。JDBCの接続、文、結果セットを一つのtry文で管理する例を示します。
---

リソース管理を改善するため、Java 7以降では、`try`文の実行が終わったときに閉じるリソースをその文の中で指定できます。言語仕様によれば、`try`文には`AutoCloseable`インターフェースを実装するリソースを一つ以上指定できます。ドキュメントによると、標準ライブラリの100を超えるクラスがこのインターフェースを実装しています。定義は次のとおりです。

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

リソース付き`try`文の構文は次のとおりです。

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

リソースは括弧内に指定します。通常はローカル変数の宣言、または確実に代入済みで実質的にfinalな変数へのアクセスです（再代入されていない変数を指し、`final`修飾子は必須ではありません）。JDBCの問い合わせでは、接続、文、結果セットを閉じる必要があります。次の例では、`c`（5行目）、`s`（8行目）、`rs`（9行目）の宣言と初期化をリソース指定部に置いています。

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

この方法なら`finally`ブロックは不要です。指定したリソースはすべてJavaの実行環境によって自動的に閉じられます。コードが簡潔になり、リソースを閉じ忘れる可能性も下がるため、リソースを扱うコードでは推奨される方法です。

---

*この記事は、Eduardo Kessler Piveta著『[Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)』の内容をもとにしています。*
