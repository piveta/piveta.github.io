---
layout: post
title: "I costruttori in Java"
date: 2026-11-24
lang: it
translation_id: construtores-java
permalink: /it/constructors-in-java/
share_text: "I costruttori in Java"
---

Un costruttore inizializza un oggetto quando viene creato. Nella classe `Account` del libro, il costruttore riceve il saldo iniziale e lo imposta con `setBalance`. Il primo frammento omette gli altri campi e metodi.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

Con `new Account(100.00)`, il codice client crea un conto con saldo 100, preleva 50 e versa 100. Il saldo visualizzato è `150.0`.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

Il compilatore fornisce un costruttore predefinito quando una classe ordinaria non ne dichiara alcuno. Dopo aver dichiarato `Account(Double value)`, quel costruttore implicito non è più disponibile. Per consentire anche `new Account()`, dichiara esplicitamente un costruttore senza argomenti. Una sottoclasse non eredita i costruttori di `Account`, ma può invocarne uno con `super(value)`.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Articolo tratto da [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

