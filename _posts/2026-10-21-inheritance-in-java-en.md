---
layout: post
title: "Inheritance in Java"
date: 2026-10-21
lang: en
translation_id: heranca-em-java
permalink: /en/inheritance-in-java/
share_text: >-
  An introduction to Java inheritance, overriding, subtype conversion, and abstract classes.
---

**Inheritance** is a composition mechanism that allows classes to reuse the interface and behavior of existing classes by extending their functionality. A class that extends another class through inheritance is called its **subclass**, while the extended class is called its **superclass**.

Java allows single inheritance for classes (multiple inheritance is available for interfaces), and subclasses are subtypes of their superclass. Inheritance is declared in the subclass with the `extends` keyword: `Class extends SuperClass`. A class without an explicitly declared superclass is implicitly a subclass of `Object`, the root of Java's class hierarchy.

Consider the `CheckingAccount` class below. It extends `Account` and adds a field, methods to read and write that field, and a constructor. Because `Account` has no no-argument constructor, the `CheckingAccount` constructor calls the superclass constructor with `super`:

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

Subclasses commonly have **overridden methods**: methods declared in a superclass whose behavior is extended or replaced by a subclass. Here, `CheckingAccount` overrides `Account`'s `withdraw` method by declaring a method with the same signature[^6]. It first invokes the superclass method with `super`, then calculates a withdrawal fee through `deductFee`, which subtracts 1% of the transaction amount from the balance:

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // Other constructors, fields, and methods.
}
```

For example, if a `CheckingAccount` starts with a balance of 100.00 and we withdraw 50.00, the remaining balance is 49.50 because 0.50 is charged as a fee:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

Under the Liskov substitution principle, we can assign subclass objects wherever a superclass object is expected: every instance of `CheckingAccount` is also an instance of `Account`. The reverse is not always true, since an `Account` could be a `SavingsAccount`, for example. In those cases, an explicit conversion (a *cast*) is required.

In the following example, `checkingAccount` has type `CheckingAccount` and refers to an instance of that class. The variable `account` has type `Account` and is assigned the same object. This assignment needs no conversion. The reverse assignment requires an explicit cast:

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // A CheckingAccount is an Account.
checkingAccount = (CheckingAccount) account; // Explicit cast, valid.
```

Suppose `SavingsAccount` is another subclass of `Account`. In the next example, `account` refers to a `CheckingAccount`. Casting it to `SavingsAccount` fails at runtime because the object is not a `SavingsAccount`:

```java
Account account = new CheckingAccount(100.00);
// The explicit cast below fails at runtime.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

Modern IDEs warn about conversions that are clearly incorrect, but sometimes the result is not known in advance. For example, a method's arguments are only known when the method is called. Incorrect casts can therefore cause runtime exceptions of type `ClassCastException`[^7].

Since `Account` can have several subtypes, such as `CheckingAccount`, `SavingsAccount`, and possibly `InvestmentAccount`, we can make it abstract so that only instances of its subclasses can be created:

```java
public abstract class Account {
    // Fields and methods common to all account types.
}
```

We can no longer instantiate `Account` directly. We must use a constructor from one of its subclasses. The earlier example can use `CheckingAccount`:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: In Java, a method signature consists of its name, its type parameters (if any), and its formal parameters. See [the Java Language Specification](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2).

[^7]: See the [ClassCastException API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html).

---

*This article is adapted from content in <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, a book by <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Related articles

- [Basic Object-Oriented Programming Concepts](/en/basic-oop-concepts/)
- [Classes in Java](/en/classes-in-java/)
- [Polymorphism in Java](/en/polymorphism-in-java/)
- [Interfaces in Java](/en/interfaces-in-java/)
- [OOP and Java Links](/en/oop-java-links/)
- [Object-Oriented Programming Exercises](/en/object-oriented-programming-exercises/)
