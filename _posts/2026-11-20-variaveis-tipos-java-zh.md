---
layout: post
title: "Java 变量与类型"
date: 2026-11-24
lang: zh
translation_id: variaveis-tipos-java
permalink: /zh/variables-and-types-in-java/
share_text: >-
  局部变量、var 类型推断、基本类型和引用类型。
---

局部变量有名称、类型和作用域。Java 不会为局部变量设置默认值，因此使用前必须赋值。

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

声明已指定列表类型时，编译器可以推断 `<>` 中的类型实参。

```java
ArrayList<Double> list = new ArrayList<>();
```

使用 `var` 时，编译器根据必需的初始化表达式推断类型。本例在构造时指定 `Double`。

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Java 区分大小写。按惯例，类和接口名以大写字母开头，变量和方法名以小写字母开头，常量用大写字母和下划线。

## 基本类型

包括 `byte`、`short`、`int`、`long`、`float`、`double`、`boolean` 和 `char`。

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

可以用字面量直接初始化。后缀 `L` 表示 `long`，`f` 表示 `float`。

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

整数字面量也可以用 `0b` 表示二进制，用 `0x` 表示十六进制。

## 引用类型

类、接口、枚举、记录和数组都是引用类型。字符串字面量使用双引号。

```java
void main() {
    String s = "This is a string...";
}
```

包装类可将基本类型的值表示为对象。本章的其他示例也经常使用集合 API。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
