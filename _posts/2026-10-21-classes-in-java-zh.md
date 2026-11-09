---
layout: post
title: "Java 中的类"
date: 2026-10-21
lang: zh
translation_id: classes-em-java
permalink: /classes-in-java-zh/
share_text: >-
  学习如何在 Java 中定义类、字段、方法、构造器和封装。
---

Java 支持面向对象编程的主要概念，包括类、字段、方法、继承、接口、多态和封装。

## 类、字段和方法

在 Java 中，类由 `class` 关键字、名称以及定义字段和方法的主体组成。其他可选组成部分将在后文介绍。假设有一个名为 `Account` 的类。我们可以将它声明为 `public`，使其他类能够访问它：

```java
public class Account {
    // 类主体
}
```

我们可以在类主体中添加字段和方法。下面的例子添加一个 `Double` 类型的 `balance` 字段[^2]，以及一个 `withdraw` 方法。该方法不返回值（`void`），并接收一个名为 `amount`、类型同样为 `Double` 的形式参数。方法会从余额中减去作为实参传入的金额：

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // 或 balance -= amount;
    }
}
```

同样，我们可以添加一个增加账户余额的 `deposit` 方法：

```java
public class Account {
    // 省略 balance 和 withdraw
    public void deposit(Double amount) {
        balance = balance + amount; // 或 balance += amount;
    }
}
```

考虑一个对账户执行若干操作的客户端。它首先调用构造器创建一个 `Account` 对象，并将对象引用赋给名为 `account` 的变量。接着将余额设为 100.00，取出 50.00，存入 100.00，然后打印余额：

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

输出为：

```text
Balance: 150.0
```

`withdraw` 和 `deposit` 是实例方法，因此调用它们需要一个 `Account` 对象。在较新的 Java 版本中，`main` 也可以是静态方法或实例方法，如本例所示[^3]。

前面的例子展示了客户端如何使用 `Account` 的字段和方法。客户端位于一个隐式声明的无名类中。不过，它直接访问 `balance`，导致类之间产生紧密耦合。这通常不理想[^4]。一种替代方案是封装对 `balance` 的访问，通过专门的方法进行读写。这样可以降低耦合，并允许以后更改余额的内部表示，只要读写操作仍然可用即可。将字段的可见性降低，使其只能在类内部访问，也是一种良好做法。

Java 提供包级可见性（默认）、`private`、`public` 和 `protected`。这些级别决定哪些类可以访问某个字段或方法。除包级可见性外，每个级别都有对应的关键字。

下面的代码改进了封装，并向客户端隐藏类的内部状态。它添加公开的读写方法（`getBalance` 和 `setBalance`），将 `balance` 的可见性改为 `private`，并通过这些方法更新余额。`this` 引用用于区分字段 `balance` 与同名的方法参数。`this.balance` 指的是字段，而不是参数：

```java
public class Account {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
}
```

客户端也做了相应修改，通过 setter 方法更新余额：

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

如果没有显式声明构造器，Java 类会有一个无参数的默认构造器。我们也可以定义其他构造器，方便客户端使用类。例如，下面的 `Account` 构造器接收初始金额，并用它设置余额。如果需要调用超类的构造器，可以使用 `super`：

```java
public class Account {
    // Account 的字段和方法
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

现在 `Account` 已经没有无参数默认构造器，因此客户端必须使用新的构造器并提供初始余额[^5]：

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java 没有析构方法。不再被引用的对象会由垃圾回收器自动回收。

[^2]: 为了简单起见，这里使用 `Double`。货币值通常不会存储在浮点变量中，而会存储在 `long` 等整数类型或 `BigDecimal` 中。

[^3]: 参见 [JEP 512](https://openjdk.org/jeps/512)。

[^4]: 这里的“这些类”指 `Account`，以及隐式声明并包含 `main` 的无名类。

[^5]: 定义构造器后，类就不再拥有默认构造器。如果需要，也可以另外定义无参数构造器。

---

*本文改编自 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a> 所著《<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>》中的内容。*

## 相关文章

- [面向对象编程的基本概念](/oop-basics-java-zh/)
- [Java 中的继承](/inheritance-in-java-zh/)
- [Java 中的多态](/polymorphism-in-java-zh/)
- [Java 中的接口](/interfaces-in-java-zh/)
- [OOP 与 Java 链接](/oop-java-links-zh/)
- [面向对象编程练习](/oop-exercises-zh/)
