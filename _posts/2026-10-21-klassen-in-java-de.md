---
layout: post
title: "Klassen in Java"
date: 2026-10-21
lang: de
translation_id: classes-em-java
permalink: /klassen-in-java-de/
share_text: >-
  Erfahre, wie man Java-Klassen, Felder, Methoden und Konstruktoren definiert und Kapselung einsetzt.
---

Java unterstützt die zentralen Konzepte der objektorientierten Programmierung, darunter Klassen, Felder, Methoden, Vererbung, Schnittstellen, Polymorphie und Kapselung.

## Klassen, Felder und Methoden

In Java wird eine Klasse mit dem Schlüsselwort `class`, einem Namen und einem Rumpf deklariert, in dem Felder und Methoden definiert werden können. Weitere optionale Bestandteile behandeln wir später. Betrachten wir eine Klasse namens `Account`. Wir können sie als `public` deklarieren, damit andere Klassen auf sie zugreifen können:

```java
public class Account {
    // Klassenrumpf
}
```

Dem Klassenrumpf können wir Felder und Methoden hinzufügen. Im nächsten Beispiel fügen wir ein Feld `balance` vom Typ `Double`[^2] sowie eine Methode `withdraw` hinzu. Sie gibt keinen Wert zurück (`void`) und erhält einen formalen Parameter namens `amount`, ebenfalls vom Typ `Double`. Die Methode zieht den als Argument übergebenen Betrag vom Kontostand ab:

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // oder balance -= amount;
    }
}
```

Auf ähnliche Weise können wir eine Methode `deposit` hinzufügen, die den Kontostand erhöht:

```java
public class Account {
    // balance und withdraw ausgelassen
    public void deposit(Double amount) {
        balance = balance + amount; // oder balance += amount;
    }
}
```

Betrachten wir einen Client, der einige Operationen auf einem Konto ausführt. Zunächst erzeugt er durch Aufruf des Konstruktors ein Objekt der Klasse `Account` und weist dessen Referenz einer Variablen namens `account` zu. Danach setzt er den Kontostand auf 100.00, hebt 50.00 ab, zahlt 100.00 ein und gibt den Kontostand aus:

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

Die Ausgabe lautet:

```text
Balance: 150.0
```

Die Methoden `withdraw` und `deposit` benötigen ein `Account`-Objekt für ihren Aufruf, da es sich um Instanzmethoden handelt. In aktuellen Java-Versionen kann `main` wie in diesem Beispiel ebenfalls eine statische oder eine Instanzmethode sein[^3].

Im vorherigen Beispiel greift ein Client auf Felder und Methoden von `Account` zu. Der Client befindet sich in einer implizit deklarierten, namenlosen Klasse. Er greift jedoch direkt auf `balance` zu und erzeugt dadurch eine enge Kopplung zwischen den Klassen. Das ist normalerweise unerwünscht[^4]. Eine Möglichkeit besteht darin, den Zugriff auf `balance` zu kapseln, sodass Lesen und Schreiben über eigene Methoden erfolgen. Dadurch wird die Kopplung verringert, und die interne Darstellung des Kontostands kann später geändert werden, solange Lese- und Schreiboperationen verfügbar bleiben. Außerdem sollte die Sichtbarkeit des Feldes eingeschränkt werden, sodass nur die Klasse selbst darauf zugreifen kann.

Java kennt die Sichtbarkeit auf Paketebene (die Voreinstellung), `private`, `public` und `protected`. Diese Stufen bestimmen, welche Klassen auf ein Feld oder eine Methode zugreifen können. Für jede Stufe gibt es ein Schlüsselwort, außer für die Sichtbarkeit auf Paketebene.

Der folgende Code verbessert die Kapselung und verbirgt den internen Zustand der Klasse vor ihren Clients. Er ergänzt öffentliche Lese- und Schreibmethoden (`getBalance` und `setBalance`), setzt die Sichtbarkeit von `balance` auf `private` und aktualisiert den Kontostand über diese Methoden. Die Referenz `this` unterscheidet das Feld `balance` vom gleichnamigen Methodenparameter. `this.balance` bezeichnet das Feld, nicht den Parameter:

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

Auch der Client wird geändert und aktualisiert den Kontostand nun über die Setter-Methode:

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Wenn kein Konstruktor explizit deklariert wird, haben Java-Klassen einen parameterlosen Standardkonstruktor. Wir können weitere Konstruktoren definieren, um die Verwendung der Klasse für Clients zu vereinfachen. Dieser `Account`-Konstruktor akzeptiert beispielsweise einen Anfangsbetrag und setzt damit den Kontostand. Falls der Konstruktor einer Oberklasse aufgerufen werden muss, können wir `super` verwenden:

```java
public class Account {
    // Felder und Methoden von Account
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

Der Client muss nun den neuen Konstruktor verwenden und einen Anfangskontostand angeben, da `Account` keinen parameterlosen Standardkonstruktor mehr besitzt[^5]:

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java kennt keine Destruktormethoden. Objekte, auf die nicht mehr verwiesen wird, werden automatisch vom Garbage Collector eingesammelt.

[^2]: `Double` wird hier der Einfachheit halber verwendet. Geldbeträge werden üblicherweise nicht in Gleitkommazahlen gespeichert, sondern etwa in Ganzzahltypen wie `long` oder in `BigDecimal`.

[^3]: Siehe [JEP 512](https://openjdk.org/jeps/512).

[^4]: Mit „den Klassen“ sind hier `Account` und die implizit deklarierte namenlose Klasse gemeint, die `main` enthält.

[^5]: Sobald ein Konstruktor definiert ist, besitzt die Klasse keinen Standardkonstruktor mehr. Bei Bedarf können wir zusätzlich einen parameterlosen Konstruktor definieren.

---

*Dieser Artikel adaptiert Inhalte aus dem Buch <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> von <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Verwandte Artikel

- [Grundlagen der objektorientierten Programmierung](/grundlagen-objektorientierte-programmierung-de/)
- [Vererbung in Java](/vererbung-in-java-de/)
- [Polymorphie in Java](/polymorphie-in-java-de/)
- [Schnittstellen in Java](/schnittstellen-in-java-de/)
- [Links zu OOP und Java](/oop-java-links-de/)
- [Übungen zur objektorientierten Programmierung](/oop-uebungen-de/)
