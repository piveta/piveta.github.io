---
layout: post
title: "Expressions and conditional statements in Java"
date: 2026-11-20
lang: en
translation_id: expressoes-condicionais-java
permalink: /en/expressions-and-conditional-statements-in-java/
share_text: >-
  Expressions, blocks, if, else, the ternary operator, and switch in the book's examples.
---

## Expressions and statements

An **expression** is evaluated to a value. It may combine literals, variables, operators, method calls, or object construction. The book uses these fragments as examples of expressions; by themselves, they do not form a complete program:

```text
x + 2 * 1
c.getBalance()
i = 20
```

A **statement** is an executable unit. Method calls, assignments, and increments can be statements in the appropriate context and end with `;`. This fragment also depends on declarations and an `Account` class not shown here:

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

Besides expression statements, Java has variable declarations and control statements such as `if`, `while`, and `for`. Braces group statements into a **block**. This program reads an integer, tests a condition, and runs two output statements inside a block:

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

The condition determines whether that block runs. Loops instead repeat statements while their own control rules hold.

## Conditional statements

A conditional statement selects an execution path using a Boolean expression. In the simplest form, `if` runs its controlled statement only when the condition is true:

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else` specifies what happens when the condition is false:

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

Braces group multiple statements in either path. The example prints two messages for each result:

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

Conditions can also be **nested**. After confirming adulthood, the program checks whether priority access applies:

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

The **ternary operator** is an expression: it tests a condition and selects one of two values. Here its result becomes part of the final message:

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

### Choosing among several paths

A `switch` statement selects a case, uses `break` to end it, and has `default` for other values:

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

A **`switch` expression** uses arrows, separates multiple values with commas, and produces a result without `break` in each case:

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

The book also demonstrates **pattern matching** with `when` guards, combining an object's type with an additional condition. The method handles `Integer`, `String`, `null`, and other types:

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

Its client calls the method with four different values:

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

The translated output is:

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

These three `switch` forms illustrate how the language has evolved. The final example requires a Java version that supports pattern matching in `switch`.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
