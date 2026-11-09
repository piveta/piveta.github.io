---
layout: post
title: "Schnittstellen in Java"
date: 2026-10-21
lang: de
translation_id: interfaces-em-java
permalink: /schnittstellen-in-java-de/
share_text: >-
  Erfahre, wie Java-Schnittstellen Verträge festlegen und wie Klassen sie implementieren.
---

In Java werden Schnittstellen ähnlich wie Klassen definiert. Üblicherweise deklarieren sie Methoden ohne Implementierung. Java unterstützt jedoch auch Standardmethoden (*default methods*) mit einer vorgegebenen Implementierung. Eine Klasse, die eine Schnittstelle implementiert, kann eine solche Standardmethode überschreiben.

Eine Schnittstelle wird mit dem Schlüsselwort `interface` deklariert und kann andere Schnittstellen erweitern. Bei Schnittstellen ist Mehrfachvererbung zulässig. So erweitert die Java-Schnittstelle `List` die Schnittstellen `Collection` und `Iterable`.

Das folgende Beispiel deklariert eine Schnittstelle namens `AccountOperations`. Klassen, die sie implementieren, müssen mindestens die Methoden `withdraw` und `transfer` bereitstellen:

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

Wenn `Account` `AccountOperations` implementiert, erben ihre Unterklassen die Methoden und erfüllen ebenfalls den Vertrag der Schnittstelle. Hier implementiert eine konkrete Klasse `Account` die Methoden `withdraw` und `transfer`; ihre Unterklassen müssen sie daher nicht erneut implementieren:

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // Konkrete Implementierung von withdraw
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // Konkrete Implementierung von transfer
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

Alternativ können die Implementierungen von `withdraw`, `deposit` und `transfer` als `default`-Methoden in die Schnittstelle `AccountOperations` verschoben werden. Außerdem muss die Schnittstelle `getBalance` und `setBalance` deklarieren:

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

Die vereinfachte Klasse `Account` sieht dann so aus:

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

Wenn die Schnittstelle von `Account` entkoppelt wird, können Klassen den Kontostand flexibler speichern und verwalten. Das Java-Collections-Framework besitzt beispielsweise die Schnittstelle `List`, die festlegt, welche Operationen eine Liste anbietet. Konkrete Implementierungen wie `ArrayList` und `LinkedList` verwenden unterschiedliche Speicher- und Zugriffsstrategien: Erstere verwendet ein Array, Letztere eine doppelt verkettete Liste.

---

*Dieser Artikel adaptiert Inhalte aus dem Buch <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> von <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Verwandte Artikel

- [Grundlagen der objektorientierten Programmierung](/grundlagen-objektorientierte-programmierung-de/)
- [Klassen in Java](/klassen-in-java-de/)
- [Vererbung in Java](/vererbung-in-java-de/)
- [Polymorphie in Java](/polymorphie-in-java-de/)
- [Links zu OOP und Java](/oop-java-links-de/)
- [Übungen zur objektorientierten Programmierung](/oop-uebungen-de/)
