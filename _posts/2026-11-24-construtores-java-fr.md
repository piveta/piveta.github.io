---
layout: post
title: "Les constructeurs en Java"
date: 2026-11-24
lang: fr
translation_id: construtores-java
permalink: /fr/constructors-in-java/
share_text: "Les constructeurs en Java"
---

Un constructeur initialise un objet lors de sa création. Dans la classe `Account` du livre, il reçoit le solde initial et l’affecte avec `setBalance`. Le premier extrait omet les autres champs et méthodes.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

Avec `new Account(100.00)`, le code client crée un compte dont le solde est de 100, retire 50 et dépose 100. Le solde affiché est `150.0`.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

Le compilateur fournit un constructeur par défaut lorsqu’une classe ordinaire n’en déclare aucun. Dès que `Account(Double value)` est déclaré, ce constructeur implicite disparaît. Pour permettre aussi `new Account()`, déclarez explicitement un constructeur sans argument. Une sous-classe n’hérite pas des constructeurs d’`Account`, mais peut en appeler un avec `super(value)`.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Article adapté de [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

