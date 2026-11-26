---
layout: post
title: "Java 表达式与条件语句"
date: 2026-11-20
lang: zh
translation_id: expressoes-condicionais-java
permalink: /zh/expressions-and-conditional-statements-in-java/
share_text: >-
  表达式、代码块、if、else、三元运算符和 switch。
---

## 表达式和语句

表达式求值后得到一个值，可以包含字面量、变量、运算符、方法调用或对象创建。这些片段不能单独构成完整程序。

```text
x + 2 * 1
c.getBalance()
i = 20
```

语句是执行单位。方法调用、赋值和递增可以构成以分号结尾的语句。本例还依赖其他声明和 `Account` 类。

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

花括号将多条语句组合成代码块。程序读取一个整数，并在条件成立时输出两条消息。

```java
void main() {
    int x = Integer.parseInt(
            IO.readln("Enter an integer: "));
    if (x < 10) {  
        IO.println("X is less than 10."); 
        IO.println("Initialize X with another value."); 
    }
}
```

## 条件语句

`if` 在布尔条件为真时执行相应语句。

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else` 指定条件为假时的行为。

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

花括号允许每个分支包含多条语句。

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
    }
    else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

检查是否成年后，可用嵌套的 `if` 判断是否具有优先权限。

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
        if (age >= 65)
            IO.println("Priority access granted");
    } else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

三元运算符根据条件在两个值之间选择。

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age: "));
    // The ternary operator has this syntax: 
		// (expr) ? true : false
    String message = ((age >= 18) ? "At least" : "Under") + 
                 " 18 years old";
    IO.println(message);
}
```

## 使用 switch 分支

传统 `switch` 语句选择匹配的分支，`break` 结束该分支，`default` 处理其他值。

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message;
    switch (age) {
        case 0: case 1: case 2: case 3: case 4: case 5:
            message = "Very young";
            break;
        case 18:
            message = "Reaching adulthood";
            break;
        case 65:
            message = "Entering senior years";
            break;
        default:
            message = "No special case";
            break;
        }
        IO.println(message);
}
```

带箭头的 `switch` 表达式会产生结果。同一分支的多个值用逗号分隔。

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message = switch (age) {
        case 0, 1, 2, 3, 4, 5 -> "Very young";
        case 18 -> "Reaching adulthood";
        case 65 -> "Entering senior years";
        default -> "No special case";
    };
    IO.println(message);
}
```

模式匹配可用 `when` 为类型模式添加条件。示例区分 `Integer`、`String`、`null` 和其他值。

```java
private static String age(Object ageObject) {
    return switch (ageObject) {
        case Integer i when i >= 65 -> 
            "[Integer] Adult: " + i + 
            "\nPriority access granted.";
        case Integer i when i >= 18 -> 
            "[Integer] Adult: " + i + 
             "\nAccess granted.";
        case Integer i -> "[Integer] Minor: " + 
                i + "\nAccess denied.";
        case String s -> 
            "[String] Age provided as text: " + s;
        case null -> "[null] Age not provided";
        default -> "Unexpected data type: " + 
                ageObject.getClass().getName();
    };
}
```

主程序用四个不同的值调用该方法。

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

输出如下。

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

最后一个示例需要支持 `switch` 模式匹配的 Java 版本。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
