---
layout: post
title: "Javaの演算子"
date: 2026-11-20
lang: ja
translation_id: operadores-java
permalink: /ja/operators-in-java/
share_text: >-
  算術、代入、比較の演算子を本書の例で学びます。
---

## 算術演算子

`+`、`-`、`*`、`/`、`%`は加算、減算、乗算、除算、剰余を表します。式の評価には優先順位が関係します。`++`と`--`は変数を1ずつ増減します。

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

`y = x++`では、増加前の10を`y`に代入します。その後`x`は11になります。

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

`y = ++x`では、増加が先です。両方が11になります。

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

単項演算子には`+`、`-`、`~`、`!`もあります。

## 代入演算子

`=`は右辺の式の値を左辺の変数に代入します。

```java
int age;
String name;
Double height;
```

変数を宣言した後に代入できます。

```java
age = 20;
name = "Mary";
height = 1.70;
```

宣言と同時に初期化することもできます。

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

## 複合代入

`+=`、`-=`、`*=`、`/=`、`%=`は演算と代入を組み合わせます。

```java
void main() {
    int a = 10;
    a += 10;
    IO.println("a = " + a);
    a -= 10;
    IO.println("a = " + a); 
    a *= 10;
    IO.println("a = " + a); 
    a /= 10;
    IO.println("a = " + a); 
    a %= 3;
    IO.println("a = " + a); 
}
```

次の順で値が表示されます。

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

複合代入では左辺を一度だけ評価し、左辺の型も考慮します。シフト演算やビット演算にも複合代入が使えます。

## 比較演算子

`==`、`!=`、`>`、`>=`、`<`、`<=`は真偽値を返します。

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age == 10)
        IO.println("Age equals 10 years");
    if (age != 20)
        IO.println("Age differs from 20 years");
    if (age > 30)
        IO.println("Age is over 30 years");
    if (age <= 80)
        IO.println("Age is at most 80 years");
}
```

10を入力すると三つの条件が真になります。`if`はそれぞれ独立しており、入力は`Integer.parseInt`で整数に変換します。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
