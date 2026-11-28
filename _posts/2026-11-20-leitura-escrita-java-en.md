---
layout: post
title: "Reading and writing on the Java console"
date: 2026-11-20
lang: en
translation_id: leitura-escrita-java
permalink: /en/reading-and-writing-on-the-java-console/
share_text: >-
  Use IO, Scanner, and readln to display and read values in Java 25 programs.
---

Many programs receive input, process it, and present a result. In Java 25, the `IO` class simplifies console output through `print` and `println`, and input through `readln`. The compact source file examples in this chapter may require *preview* features to be enabled.

## Writing values

`print` writes without appending a line break; `println` ends the line. The book statically imports `java.lang.IO` so these methods can be called without a class prefix:

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

Variables `a` and `b` contain 10 and 20. Since the first call does not end the line, the output is `Result: Sum of a and b: 30` on a single line.

## Reading with `Scanner`

`Scanner` reads standard input. Here, `nextLine()` reads text and `nextInt()` reads the age. Another `nextLine()` call consumes the line break left after `nextInt()` before the address is read:

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

## Reading with `IO.readln`

`readln` receives a prompt and returns a `String`. The same example can use the static import of `IO`:

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

Because the age arrives as a `String`, the program converts it with `Integer.parseInt`. Input that does not represent an integer causes a `NumberFormatException`; the book's example does not handle that exception. Console input serves to introduce the language, although applications may also receive data through forms and graphical interfaces.

Single-line comments start with `//`; multiline comments use `/*` and `*/`:

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
