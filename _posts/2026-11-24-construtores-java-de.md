---
layout: post
title: "Konstruktoren in Java"
date: 2026-11-24
lang: de
translation_id: construtores-java
permalink: /de/constructors-in-java/
share_text: "Konstruktoren in Java"
---

Ein Konstruktor initialisiert ein Objekt bei seiner Erzeugung. In der Klasse `Account` aus dem Buch erhält der Konstruktor den Anfangssaldo und setzt ihn mit `setBalance`. Der erste Ausschnitt lässt die übrigen Felder und Methoden weg.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

Mit `new Account(100.00)` erzeugt der Aufrufer ein Konto mit einem Saldo von 100, hebt 50 ab und zahlt 100 ein. Die Ausgabe zeigt den Saldo `150.0`.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

Der Compiler stellt einen Standardkonstruktor bereit, wenn eine gewöhnliche Klasse keinen Konstruktor deklariert. Sobald `Account(Double value)` deklariert ist, entfällt dieser implizite Konstruktor. Damit auch `new Account()` möglich ist, muss ein parameterloser Konstruktor ausdrücklich deklariert werden. Eine Unterklasse erbt die Konstruktoren von `Account` nicht, kann aber einen davon mit `super(value)` aufrufen.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Nach dem Buch [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

