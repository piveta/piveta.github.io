---
layout: post
title: "Konstruktorer i Java"
date: 2026-11-24
lang: sv
translation_id: construtores-java
permalink: /sv/constructors-in-java/
share_text: "Konstruktorer i Java"
---

En konstruktor initialiserar ett objekt när det skapas. I bokens klass `Account` tar konstruktorn emot det inledande saldot och anger det via `setBalance`. Det första kodutdraget utelämnar övriga fält och metoder.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

Med `new Account(100.00)` skapar anroparen ett konto med saldot 100, tar ut 50 och sätter in 100. Saldot som skrivs ut är `150.0`.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

Kompilatorn tillhandahåller en standardkonstruktor när en vanlig klass saknar deklarerade konstruktorer. När `Account(Double value)` deklareras finns den implicita konstruktorn inte längre. Deklarera uttryckligen en konstruktor utan argument om även `new Account()` ska fungera. En underklass ärver inte konstruktorerna i `Account`, men kan anropa en av dem med `super(value)`.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Baserat på boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

