---
layout: post
title: "Java 控制台的输入与输出"
date: 2026-11-20
lang: zh
translation_id: leitura-escrita-java
permalink: /zh/reading-and-writing-on-the-java-console/
share_text: >-
  使用 IO、Scanner 和 readln 读取与显示数据。
---

Java 25 的 `IO` 提供输出方法 `print`、`println` 和输入方法 `readln`。静态导入后可以直接调用这些方法。

## 输出数据

`print` 不换行，`println` 会结束当前行。

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

10 和 20 的和与提示文字显示在同一行。

## 使用 Scanner 读取

`nextLine()` 读取一行，`nextInt()` 读取整数。读取年龄后再次调用 `nextLine()`，消耗剩余的换行符，再读取地址。

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

## 使用 IO.readln 读取

`readln` 显示提示并返回 `String`。`Integer.parseInt` 将表示年龄的字符串转换成整数。

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

输入无法转换为整数时会抛出 `NumberFormatException`，本例未处理该异常。控制台适合练习，实际应用也可通过表单或图形界面读取输入。

单行注释以 `//` 开头，多行注释写在 `/*` 与 `*/` 之间。

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

使用紧凑源文件的示例可能需要开启预览功能。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
