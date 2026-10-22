---
layout: post
title: "Interfaces in Java"
date: 2026-10-21
lang: en
translation_id: interfaces-em-java
permalink: /en/interfaces-in-java/
share_text: >-
  Learn how Java interfaces define contracts and how classes implement them.
---

In Java, interfaces are defined in a way similar to classes. Interfaces commonly declare methods without implementations, although Java also supports default methods, which have a predefined implementation. A class that implements an interface can choose whether to override a default method.

An interface is declared with the `interface` keyword and can itself extend other interfaces. Multiple inheritance is allowed for interfaces. For example, Java's `List` interface extends `Collection` and `Iterable`.

The following example declares an interface named `AccountOperations`. Classes that implement it must provide at least the `withdraw` and `transfer` methods:

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

When `Account` implements `AccountOperations`, its subclasses inherit the methods and conform to the interface as well. Here, a concrete `Account` class provides implementations of `withdraw` and `transfer`, so its subclasses do not need to implement them again:

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // Concrete implementation of withdraw
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // Concrete implementation of transfer
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

Another option is to move the implementations of `withdraw`, `deposit`, and `transfer` into the `AccountOperations` interface as `default` methods. The interface must also declare `getBalance` and `setBalance`:

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

The simplified `Account` class would then be:

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

Decoupling the interface from `Account` can give classes more flexibility in how the balance is stored and managed. For example, Java's collections framework has a `List` interface that defines what a list can do. Concrete implementations such as `ArrayList` and `LinkedList` use different storage and access strategies: the first uses an array, while the second uses a doubly linked list.

---

*This article is adapted from content in <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, a book by <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Related articles

- [Basic Object-Oriented Programming Concepts](/en/basic-oop-concepts/)
- [Classes in Java](/en/classes-in-java/)
- [Inheritance in Java](/en/inheritance-in-java/)
- [Polymorphism in Java](/en/polymorphism-in-java/)
- [OOP and Java Links](/en/oop-java-links/)
- [Object-Oriented Programming Exercises](/en/object-oriented-programming-exercises/)
