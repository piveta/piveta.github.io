---
layout: post
title: "Java 运算符"
date: 2026-11-20
lang: zh
translation_id: operadores-java
permalink: /zh/operators-in-java/
share_text: >-
  通过书中的示例学习算术、赋值和比较运算符。
---

## 算术运算符

`+`、`-`、`*`、`/`、`%` 分别表示加、减、乘、除和取余。优先级决定表达式如何分组。`++` 和 `--` 使变量加一或减一。

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

执行 `y = x++` 时，`y` 先得到旧值 10，随后 `x` 变成 11。

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

执行 `y = ++x` 时，先递增，两者都变成 11。

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

其他一元运算符包括 `+`、`-`、`~` 和 `!`。

## 赋值运算符

`=` 将右侧表达式的值赋给左侧变量。

```java
int age;
String name;
Double height;
```

可以先声明变量，随后再赋值。

```java
age = 20;
name = "Mary";
height = 1.70;
```

也可以在声明时直接初始化。

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

## 复合赋值

`+=`、`-=`、`*=`、`/=` 和 `%=` 将运算和赋值合在一起。

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

程序按以下顺序输出各值。

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

复合赋值只对左侧表达式求值一次，并考虑其类型。移位和按位运算也有复合赋值形式。

## 比较运算符

`==`、`!=`、`>`、`>=`、`<` 和 `<=` 返回布尔值。

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

输入 10 时有三个条件成立，因为各个 `if` 独立判断。`Integer.parseInt` 将输入转换为整数。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
