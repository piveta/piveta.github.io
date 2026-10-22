---
layout: post
title: "Classes in Java"
date: 2026-10-21
lang: en
translation_id: classes-em-java
permalink: /en/classes-in-java/
share_text: >-
  Learn how to define Java classes, fields, methods, constructors, and encapsulation.
---

Java supports the main concepts of object-oriented programming, including classes, fields, methods, inheritance, interfaces, polymorphism, and encapsulation.

## Classes, fields, and methods

In Java, a class is declared with the `class` keyword, a name, and a body where fields and methods can be defined. Other optional components are discussed below. Consider a class named `Account`. We can make it public so that other classes can access it:

```java
public class Account {
    // Class body
}
```

We can add fields and methods to the class body. In the next example, we add a `balance` field of type `Double`[^2] and a `withdraw` method, which returns nothing (`void`) and receives a formal parameter named `amount`, also of type `Double`. The method subtracts the amount passed as an argument from the balance:

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // or balance -= amount;
    }
}
```

Similarly, we can add a `deposit` method that increases the account balance:

```java
public class Account {
    // balance and withdraw omitted
    public void deposit(Double amount) {
        balance = balance + amount; // or balance += amount;
    }
}
```

Consider a client that performs some operations on an account. First, it creates an `Account` object by calling its constructor and assigns the reference to a variable named `account`. It then sets the account balance to 100.00, withdraws 50.00, deposits 100.00, and prints the balance:

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

The output is:

```text
Balance: 150.0
```

The `withdraw` and `deposit` methods need an `Account` object to be invoked because they are instance methods. In recent Java versions, `main` can also be either a static method or an instance method, as in this example[^3].

The previous example shows a client using fields and methods of `Account`. The client is in an implicitly declared, unnamed class. However, it accesses `balance` directly, creating tight coupling between the classes. This is usually undesirable[^4]. One alternative is to encapsulate access to `balance`, so reads and writes go through dedicated methods. This decouples the classes and allows the internal representation of the balance to change later, as long as the read and write operations remain available. It is also good practice to reduce the field's visibility so it can only be accessed from inside the class.

Java has package-private (the default), private, public, and protected visibility. These levels determine which classes can access a field or method. Each level has an associated keyword except package-private visibility, for which no keyword is used.

The following code improves encapsulation and hides the class's internal state from its clients. It adds public read and write methods (`getBalance` and `setBalance`), changes the visibility of `balance` to `private`, and updates the balance through those methods. The `this` reference disambiguates the field `balance` from the method parameter with the same name. `this.balance` refers to the field, not the parameter:

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

The client is also changed so it modifies the balance through the setter method:

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java classes have a default constructor with no parameters when no constructor is explicitly declared. We can define other constructors to make a class easier for clients to use. For example, this `Account` constructor accepts an initial amount and sets the balance with it. If a superclass constructor needed to be called, we could use `super`:

```java
public class Account {
    // Account fields and methods
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

The client must now use the new constructor and provide an initial balance because `Account` no longer has a no-argument default constructor[^5]:

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java has no destructor methods. Objects that are no longer referenced are automatically collected by the garbage collector.

[^2]: `Double` is used here for simplicity. Monetary values are usually not stored in floating-point variables, but in integer types such as `long` or in `BigDecimal`.

[^3]: See [JEP 512](https://openjdk.org/jeps/512).

[^4]: Here, “the classes” refers to `Account` and the implicitly declared, unnamed class that contains `main`.

[^5]: When we define a constructor, the class no longer has a default constructor. We can also define a no-argument constructor if needed.

---

*This article is adapted from content in <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, a book by <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Related articles

- [Basic Object-Oriented Programming Concepts](/en/basic-oop-concepts/)
- [Inheritance in Java](/en/inheritance-in-java/)
- [Polymorphism in Java](/en/polymorphism-in-java/)
- [Interfaces in Java](/en/interfaces-in-java/)
- [OOP and Java Links](/en/oop-java-links/)
- [Object-Oriented Programming Exercises](/en/object-oriented-programming-exercises/)
