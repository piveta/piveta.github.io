---
layout: post
title: "Constructors in Java"
date: 2026-11-24
lang: en
translation_id: construtores-java
permalink: /en/constructors-in-java/
share_text: "Constructors in Java"
---

A constructor initializes an object when it is created. In the book’s `Account` class, the constructor receives the initial balance and sets it through `setBalance`. The first excerpt omits the remaining fields and methods.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

With `new Account(100.00)`, the caller opens an account with a balance of 100, withdraws 50, and deposits 100. The printed balance is `150.0`.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

The compiler provides a default constructor when an ordinary class declares no constructors. Once `Account(Double value)` is declared, that implicit constructor is no longer available. To support `new Account()` as well, declare a no-argument constructor explicitly. A subclass does not inherit constructors from `Account`, but it can invoke one with `super(value)`.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Based on [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

