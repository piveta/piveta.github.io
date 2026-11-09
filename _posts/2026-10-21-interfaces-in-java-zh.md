---
layout: post
title: "Java 中的接口"
date: 2026-10-21
lang: zh
translation_id: interfaces-em-java
permalink: /interfaces-in-java-zh/
share_text: >-
  了解 Java 接口如何定义契约，以及类如何实现接口。
---

Java 接口的定义方式与类相似。接口通常声明没有实现的方法，不过 Java 也支持带有预定义实现的默认方法。实现接口的类可以选择是否重写默认方法。

接口使用 `interface` 关键字声明，也可以扩展其他接口。接口允许多重继承。例如，Java 的 `List` 接口扩展了 `Collection` 和 `Iterable`。

下面的例子声明名为 `AccountOperations` 的接口。实现它的类至少要提供 `withdraw` 和 `transfer` 方法：

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

当 `Account` 实现 `AccountOperations` 时，它的子类会继承这些方法，也遵循该接口的契约。这里，具体类 `Account` 实现了 `withdraw` 和 `transfer`，因此子类不必再次实现它们：

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // withdraw 的具体实现
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // transfer 的具体实现
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

另一种方式是将 `withdraw`、`deposit` 和 `transfer` 的实现作为 `default` 方法移入 `AccountOperations` 接口。接口还必须声明 `getBalance` 和 `setBalance`：

```java
public interface AccountOperations {
    public Double getBalance();
    public void setBalance(Double balance);
    public default void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public default void transfer(AccountOperations destination,
                                 Double amount) {
        destination.deposit(amount);
        this.withdraw(amount);
    }
    public default void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
}
```

简化后的 `Account` 类如下：

```java
public class Account implements AccountOperations {
    private Double balance;

    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

将接口与 `Account` 解耦，可以让类更灵活地存储和管理余额。例如，Java 集合框架有一个 `List` 接口，用来定义列表能够执行的操作。`ArrayList` 和 `LinkedList` 等具体实现采用不同的存储和访问策略：前者使用数组，后者使用双向链表。

---

*本文改编自 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a> 所著《<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>》中的内容。*

## 相关文章

- [面向对象编程的基本概念](/oop-basics-java-zh/)
- [Java 中的类](/classes-in-java-zh/)
- [Java 中的继承](/inheritance-in-java-zh/)
- [Java 中的多态](/polymorphism-in-java-zh/)
- [OOP 与 Java 链接](/oop-java-links-zh/)
- [面向对象编程练习](/oop-exercises-zh/)
