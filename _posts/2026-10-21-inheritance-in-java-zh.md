---
layout: post
title: "Java 中的继承"
date: 2026-10-21
lang: zh
translation_id: heranca-em-java
permalink: /inheritance-in-java-zh/
share_text: >-
  介绍 Java 继承、方法重写、子类型转换和抽象类。
---

**继承**是一种组合机制，使类能够复用现有类的接口和行为，并扩展其功能。通过继承扩展另一个类的类称为该类的**子类**，被扩展的类称为**超类**。

Java 的类只支持单继承（接口支持多继承），子类是其超类的子类型。子类使用 `extends` 关键字声明继承，例如 `Class extends SuperClass`。没有显式声明超类的类会隐式成为 `Object` 的子类；`Object` 是 Java 类层次结构的根。

看下面的 `CheckingAccount` 类。它扩展 `Account`，并增加一个字段、用于读写该字段的方法以及一个构造器。由于 `Account` 没有无参数构造器，`CheckingAccount` 的构造器使用 `super` 调用超类构造器：

```java
public class CheckingAccount extends Account {
    private Double dailyWithdrawalLimit;
    public Double getDailyWithdrawalLimit() {
        return dailyWithdrawalLimit;
    }
    public void setDailyWithdrawalLimit(Double dailyWithdrawalLimit) {
        this.dailyWithdrawalLimit = dailyWithdrawalLimit;
    }
    public CheckingAccount(Double amount) {
        super(amount);
    }
}
```

子类通常会有**被重写的方法**：这些方法在超类中声明，其行为由子类扩展或替换。这里，`CheckingAccount` 声明了一个具有相同签名[^6]的方法，从而重写了 `Account` 的 `withdraw` 方法。它先通过 `super` 调用超类方法，再调用 `deductFee` 计算手续费，从余额中扣除交易金额的 1%：

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // 其他构造器、字段和方法
}
```

例如，如果 `CheckingAccount` 的初始余额为 100.00，取出 50.00 后，余额会变成 49.50，因为收取了 0.50 的手续费：

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

根据里氏替换原则，需要超类对象的地方可以使用子类对象：每个 `CheckingAccount` 实例也是一个 `Account` 实例。反过来则不一定成立，因为一个 `Account` 也可能是 `SavingsAccount`。这种情况下需要显式转换（*cast*）。

在下面的例子中，`checkingAccount` 的类型是 `CheckingAccount`，并引用该类的一个实例。`account` 的类型是 `Account`，并被赋值为同一个对象。此赋值不需要转换。反向赋值则需要显式类型转换：

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // CheckingAccount 是一种 Account。
checkingAccount = (CheckingAccount) account; // 有效的显式转换。
```

假设 `SavingsAccount` 是 `Account` 的另一个子类。在下面的例子中，`account` 引用一个 `CheckingAccount`。由于该对象并不是 `SavingsAccount`，将其转换为 `SavingsAccount` 会在运行时失败：

```java
Account account = new CheckingAccount(100.00);
// 下面的显式转换会在运行时失败。
SavingsAccount savingsAccount = (SavingsAccount) account;
```

现代 IDE 会对明显错误的转换发出警告，但有时事先无法确定结果。例如，方法的参数只有在方法调用时才确定。因此，错误的类型转换可能导致 `ClassCastException` 类型的运行时异常[^7]。

由于 `Account` 可以有多个子类型，例如 `CheckingAccount`、`SavingsAccount`，甚至 `InvestmentAccount`，我们可以将它声明为抽象类，使其只能创建子类实例：

```java
public abstract class Account {
    // 所有账户类型共有的字段和方法
}
```

现在不能直接实例化 `Account`。必须使用其某个子类的构造器，例如 `CheckingAccount`：

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: 在 Java 中，方法签名由方法名、类型参数（如果有）和形式参数构成。参见 [Java 语言规范](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2)。

[^7]: 参见 [ClassCastException API 文档](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html)。

---

*本文改编自 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a> 所著《<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>》中的内容。*

## 相关文章

- [面向对象编程的基本概念](/oop-basics-java-zh/)
- [Java 中的类](/classes-in-java-zh/)
- [Java 中的多态](/polymorphism-in-java-zh/)
- [Java 中的接口](/interfaces-in-java-zh/)
- [OOP 与 Java 链接](/oop-java-links-zh/)
- [面向对象编程练习](/oop-exercises-zh/)
