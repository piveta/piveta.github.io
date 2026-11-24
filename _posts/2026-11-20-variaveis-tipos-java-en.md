---
layout: post
title: "Variables and types in Java"
date: 2026-11-20
lang: en
translation_id: variaveis-tipos-java
permalink: /en/variables-and-types-in-java/
share_text: >-
  Declarations, inference with var, primitive types, and reference types in the introductory chapter.
---

A variable has a name, a type, and a scope. Here we consider **local variables**, declared inside a method. A local variable must receive a value before it is used; Java does not provide default values for local variables.

The book declares a `String`, an `int`, and a list of `Double` values:

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

When the declaration specifies the list type, the constructor can infer its type argument from `<>`:

```java
ArrayList<Double> list = new ArrayList<>();
```

With `var`, the compiler infers the variable's type from its initializer, which is required. In this example, the constructor must specify `Double`, since the declaration no longer supplies that information:

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

By Java convention, class and interface names start with uppercase letters, variable and method names with lowercase letters, and constants use uppercase letters and underscores. Names are case-sensitive.

## Primitive types

Primitive types include `byte`, `short`, `int`, `long`, `float`, `double`, `boolean`, and `char`. The book first declares variables of these types:

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

Literals can initialize them directly. The suffix `L` marks a `long` literal and `f` marks a `float` literal:

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

Integer literals also support binary (`0b`) and hexadecimal (`0x`) forms. `int` and `double` are common choices among the numeric types in this chapter.

## Reference types

Classes, interfaces, enumerations, records, and arrays are reference types. A `String` can be created with double quotes:

```java
void main() {
    String s = "This is a string...";
}
```

Java also provides *wrapper* classes that represent primitive values as objects. The chapter mentions arrays and matrices, but does not study them in detail; its other examples more often use the collections API.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
