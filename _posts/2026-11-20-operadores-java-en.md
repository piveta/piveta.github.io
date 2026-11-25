---
layout: post
title: "Operators in Java"
date: 2026-11-20
lang: en
translation_id: operadores-java
permalink: /en/operators-in-java/
share_text: >-
  Arithmetic, assignment, and relational operators, with examples from the introductory chapter.
---

## Arithmetic operators

Operators act on values, variables, and expressions. The main binary **arithmetic operators** are `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), and `%` (remainder). Operator precedence affects how expressions are evaluated.

### Increment and decrement

`++` and `--` change a numeric variable by one. As standalone statements, these postfix operators take `x` from 10 to 11 and then back to 10:

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

When an expression uses the value, the operator's position matters. In `y = x++`, `y` receives the old value of `x` before the increment. At the end, `x` is 11 and `y` is 10:

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

In `y = ++x`, the increment happens before assignment. Both variables become 11:

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Other unary operators include `+`, `-`, `~` (bitwise complement), and `!` (logical negation). Binary operators have two operands; their evaluation also follows the language's precedence and order rules.

## Assignment operators

The `=` operator assigns the value of the expression on its right to the variable on its left. A variable may be declared and assigned later:

```java
int age;
String name;
Double height;
```

```java
age = 20;
name = "Mary";
height = 1.70;
```

It can also be initialized in its declaration when a value is available:

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

### Compound assignment

Operators such as `+=`, `-=`, `*=`, `/=`, and `%=` combine an operation with assignment. The book repeatedly modifies variable `a`:

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

The values printed, in order, are:

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

Compound assignment is not always a simple textual substitution: the language specification accounts for the left-hand type and evaluates that expression only once. Java also has compound assignments for shifts and bitwise operations.

## Relational operators

**Relational operators** compare two operands and produce `true` or `false`. The main ones are `==` (equal), `!=` (not equal), `>` (greater), `>=` (greater or equal), `<` (less), and `<=` (less or equal). Their results commonly appear in `if` statements and loop conditions.

The book's example reads an age and tests several relations independently:

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

For input 10, the program displays “Age equals 10 years,” “Age differs from 20 years,” and “Age is at most 80 years.” Because each test is a separate `if`, more than one message may appear. `Integer.parseInt` converts the string returned by `IO.readln` to an integer.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
