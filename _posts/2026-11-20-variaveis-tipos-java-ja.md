---
layout: post
title: "Javaの変数と型"
date: 2026-11-24
lang: ja
translation_id: variaveis-tipos-java
permalink: /ja/variables-and-types-in-java/
share_text: >-
  ローカル変数、varによる型推論、プリミティブ型と参照型。
---

ローカル変数には名前、型、スコープがあります。既定値は与えられないので、使用前に値を代入します。

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

宣言でリストの型を指定すると、コンパイラは`<>`の型引数を推論できます。

```java
ArrayList<Double> list = new ArrayList<>();
```

`var`を使うと、コンパイラは必須の初期化式から型を推論します。この例ではコンストラクタ側で`Double`を指定します。

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Javaでは大文字と小文字を区別します。慣例ではクラスとインターフェース名は大文字、変数とメソッド名は小文字で始め、定数名は大文字とアンダースコアで表します。

## プリミティブ型

`byte`、`short`、`int`、`long`、`float`、`double`、`boolean`、`char`が該当します。

```java
void main() {
    byte b;
    short s;
    int x, y, z;
    long l;
    float f;
    double d;
    boolean test;
    char c;
}
```

リテラルから直接初期化できます。接尾辞`L`は`long`、`f`は`float`を表します。

```java
void main() {
    byte b = 10;
    short s = 20;
    int x = 10, y = 20, z = 30;
    long l = 100L;
    float f = 12.3f;
    double d = 20.45;
    boolean test = true;
    char c = 'a';
}
```

整数リテラルには2進数の`0b`と16進数の`0x`も使えます。

## 参照型

クラス、インターフェース、列挙型、レコード、配列は参照型です。`String`のリテラルは二重引用符で囲みます。

```java
void main() {
    String s = "This is a string...";
}
```

ラッパークラスはプリミティブ値をオブジェクトとして扱うために使います。この章のほかの例ではコレクションAPIもよく使います。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
