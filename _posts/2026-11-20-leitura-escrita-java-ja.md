---
layout: post
title: "Javaのコンソール入出力"
date: 2026-11-20
lang: ja
translation_id: leitura-escrita-java
permalink: /ja/reading-and-writing-on-the-java-console/
share_text: >-
  IOとScannerで値を表示し、入力を読み取ります。
---

Java 25の`IO`にはコンソール出力用の`print`と`println`、入力用の`readln`があります。静的インポートを使うとクラス名を付けずに呼び出せます。

## 値の出力

`print`は改行せず、`println`は行を終えます。

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

10と20の和が1行に表示されます。

## Scannerによる入力

`nextLine()`は行を、`nextInt()`は整数を読み取ります。年齢の直後に残った改行をもう一度`nextLine()`で消費してから住所を読み取ります。

```java
import java.util.Scanner;
void main(){
    var s = new Scanner(System.in);
    IO.println("Name: ");
    var name = s.nextLine(); 
    IO.println("Age: ");
    var age = s.nextInt(); 
    s.nextLine(); // Consumes the line break
    IO.println("Address: ");
    var address = s.nextLine(); 
    IO.println("Entered data:");
    IO.println("Name: " + name + ", Age: " + age);
    IO.println("Address: " + address);
}
```

## IO.readlnによる入力

`readln`は入力を促すメッセージを表示し、入力を`String`として返します。`Integer.parseInt`は年齢の文字列を整数に変換します。

```java
import static java.lang.IO.*; 
void main(){
    var name = readln("Name: ");
    var age = Integer.parseInt(readln("Age: ")); 
    var address = readln("Address: ");
    println("Entered data:");
    println("Name: " + name + ", Age: " + age);
    println("Address: " + address);
}
```

整数として解釈できない場合は`NumberFormatException`が発生します。この例では例外処理を省いています。コンソール入力は学習向けで、アプリケーションではフォームやGUIも使われます。

1行のコメントは`//`で始め、複数行のコメントは`/*`と`*/`で囲みます。

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

コンパクトソースファイルを使う例では、プレビュー機能の有効化が必要になる場合があります。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
