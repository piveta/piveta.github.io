---
layout: post
title: "Vererbung in Java"
date: 2026-10-21
lang: de
translation_id: heranca-em-java
permalink: /vererbung-in-java-de/
share_text: >-
  Einführung in Java-Vererbung, Methodenüberschreibung, Typumwandlungen und abstrakte Klassen.
---

**Vererbung** ist ein Kompositionsmechanismus, mit dem Klassen die Schnittstelle und das Verhalten bestehender Klassen wiederverwenden und deren Funktionalität erweitern können. Eine Klasse, die eine andere Klasse durch Vererbung erweitert, heißt **Unterklasse**; die erweiterte Klasse heißt **Oberklasse**.

Java erlaubt einfache Vererbung bei Klassen (Mehrfachvererbung ist bei Schnittstellen möglich). Unterklassen sind Subtypen ihrer Oberklasse. Die Vererbung wird in der Unterklasse mit dem Schlüsselwort `extends` deklariert: `Klasse extends Oberklasse`. Eine Klasse ohne explizit deklarierte Oberklasse ist implizit eine Unterklasse von `Object`, der Wurzel der Java-Klassenhierarchie.

Betrachten wir die folgende Klasse `CheckingAccount`. Sie erweitert `Account` und fügt ein Feld, Methoden zum Lesen und Schreiben dieses Feldes sowie einen Konstruktor hinzu. Da `Account` keinen parameterlosen Konstruktor besitzt, ruft der Konstruktor von `CheckingAccount` den Oberklassenkonstruktor mit `super` auf:

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

Unterklassen haben oft **überschriebene Methoden**: Methoden, die in einer Oberklasse deklariert sind und deren Verhalten eine Unterklasse erweitert oder ersetzt. Hier überschreibt `CheckingAccount` die Methode `withdraw` von `Account`, indem sie eine Methode mit derselben Signatur deklariert[^6]. Zuerst ruft sie mit `super` die Oberklassenmethode auf. Anschließend berechnet `deductFee` eine Gebühr, indem 1 % des Transaktionsbetrags vom Kontostand abgezogen wird:

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // Weitere Konstruktoren, Felder und Methoden.
}
```

Hat ein `CheckingAccount` anfangs beispielsweise einen Kontostand von 100.00 und heben wir 50.00 ab, verbleiben 49.50, weil eine Gebühr von 0.50 erhoben wird:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

Nach dem Liskovschen Substitutionsprinzip können wir Objekte einer Unterklasse überall dort zuweisen, wo ein Objekt der Oberklasse erwartet wird: Jede Instanz von `CheckingAccount` ist auch eine Instanz von `Account`. Umgekehrt gilt das nicht immer, denn ein `Account` könnte beispielsweise ein `SavingsAccount` sein. In solchen Fällen ist eine explizite Typumwandlung (*Cast*) erforderlich.

Im folgenden Beispiel hat `checkingAccount` den Typ `CheckingAccount` und verweist auf eine Instanz dieser Klasse. Die Variable `account` hat den Typ `Account` und erhält dieselbe Objektinstanz. Diese Zuweisung benötigt keine Umwandlung. Die umgekehrte Zuweisung erfordert einen expliziten Cast:

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // Ein CheckingAccount ist ein Account.
checkingAccount = (CheckingAccount) account; // Gültiger expliziter Cast.
```

Angenommen, `SavingsAccount` ist eine weitere Unterklasse von `Account`. Im nächsten Beispiel verweist `account` auf ein `CheckingAccount`. Die Umwandlung in `SavingsAccount` schlägt zur Laufzeit fehl, da das Objekt kein `SavingsAccount` ist:

```java
Account account = new CheckingAccount(100.00);
// Der folgende explizite Cast schlägt zur Laufzeit fehl.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

Moderne IDEs warnen vor eindeutig falschen Umwandlungen. Manchmal steht das Ergebnis jedoch nicht im Voraus fest: Die Argumente einer Methode sind beispielsweise erst beim Aufruf bekannt. Falsche Casts können daher Laufzeitausnahmen vom Typ `ClassCastException` verursachen[^7].

Da `Account` mehrere Subtypen haben kann, etwa `CheckingAccount`, `SavingsAccount` und möglicherweise `InvestmentAccount`, können wir die Klasse als abstrakt deklarieren, damit nur Instanzen ihrer Unterklassen erzeugt werden können:

```java
public abstract class Account {
    // Felder und Methoden, die allen Kontoarten gemeinsam sind.
}
```

`Account` kann nun nicht mehr direkt instanziiert werden. Wir müssen einen Konstruktor einer Unterklasse verwenden. Das vorherige Beispiel kann `CheckingAccount` verwenden:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: In Java besteht die Signatur einer Methode aus ihrem Namen, ihren Typparametern (falls vorhanden) und ihren formalen Parametern. Siehe die [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2).

[^7]: Siehe die [API-Dokumentation zu ClassCastException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html).

---

*Dieser Artikel adaptiert Inhalte aus dem Buch <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> von <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Verwandte Artikel

- [Grundlagen der objektorientierten Programmierung](/grundlagen-objektorientierte-programmierung-de/)
- [Klassen in Java](/klassen-in-java-de/)
- [Polymorphie in Java](/polymorphie-in-java-de/)
- [Schnittstellen in Java](/schnittstellen-in-java-de/)
- [Links zu OOP und Java](/oop-java-links-de/)
- [Übungen zur objektorientierten Programmierung](/oop-uebungen-de/)
