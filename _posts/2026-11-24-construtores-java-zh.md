---
layout: post
title: "Java 中的构造器"
date: 2026-11-24
lang: zh
translation_id: construtores-java
permalink: /zh/constructors-in-java/
share_text: "Java 中的构造器"
---

构造器在对象创建时初始化其状态。在书中的 `Account` 类中，构造器接收初始余额，并通过 `setBalance` 设置余额。第一个代码片段省略了其他字段和方法。

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

调用 `new Account(100.00)` 创建一个余额为 100 的账户，然后取出 50，再存入 100。程序打印的余额是 `150.0`。

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

如果普通类没有声明任何构造器，编译器会提供默认构造器。声明 `Account(Double value)` 后，这个隐式构造器就不再存在。若还要支持 `new Account()`，须显式声明无参构造器。子类不会继承 `Account` 的构造器，但可以通过 `super(value)` 调用其中一个。

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*内容改编自 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

