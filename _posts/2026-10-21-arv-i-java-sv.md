---
layout: post
title: "Arv i Java"
date: 2026-10-21
lang: sv
translation_id: heranca-em-java
permalink: /arv-i-java-sv/
share_text: >-
  En introduktion till arv i Java, åsidosättning, typkonvertering och abstrakta klasser.
---

**Arv** är en kompositionsmekanism som gör det möjligt för klasser att återanvända gränssnitt och beteende från befintliga klasser och utöka deras funktioner. En klass som utökar en annan klass genom arv kallas dess **underklass**, medan den utökade klassen kallas **superklass**.

Java tillåter enkelarv för klasser (gränssnitt kan använda multipelt arv), och underklasser är subtyper till sina superklasser. Arv deklareras i underklassen med nyckelordet `extends`: `Klass extends Superklass`. En klass utan uttryckligen deklarerad superklass är implicit en underklass till `Object`, roten i Javas klasshierarki.

Titta på klassen `CheckingAccount` nedan. Den utökar `Account` och lägger till ett fält, metoder för att läsa och skriva fältet samt en konstruktor. Eftersom `Account` saknar en konstruktor utan argument anropar konstruktorn i `CheckingAccount` superklassens konstruktor med `super`:

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

Underklasser har ofta **överskuggade metoder**: metoder som deklareras i en superklass och vars beteende utökas eller ersätts av en underklass. Här överskuggar `CheckingAccount` metoden `withdraw` i `Account` genom att deklarera en metod med samma signatur[^6]. Först anropar den superklassens metod med `super`. Sedan beräknar `deductFee` en avgift som drar 1 % av transaktionsbeloppet från saldot:

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // Andra konstruktorer, fält och metoder.
}
```

Om ett `CheckingAccount` till exempel börjar med ett saldo på 100.00 och vi tar ut 50.00 återstår 49.50, eftersom en avgift på 0.50 dras:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

Enligt Liskovs substitutionsprincip kan vi tilldela objekt från en underklass där ett objekt från superklassen förväntas: varje instans av `CheckingAccount` är även en instans av `Account`. Det omvända gäller inte alltid, eftersom ett `Account` exempelvis kan vara ett `SavingsAccount`. Då krävs en uttrycklig konvertering (*cast*).

I följande exempel har `checkingAccount` typen `CheckingAccount` och refererar till en instans av den klassen. Variabeln `account` har typen `Account` och tilldelas samma objekt. Den tilldelningen kräver ingen konvertering. Tilldelningen åt andra hållet kräver en uttrycklig cast:

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // Ett CheckingAccount är ett Account.
checkingAccount = (CheckingAccount) account; // Giltig uttrycklig cast.
```

Anta att `SavingsAccount` är en annan underklass till `Account`. I nästa exempel refererar `account` till ett `CheckingAccount`. Att casta det till `SavingsAccount` misslyckas vid körning eftersom objektet inte är ett `SavingsAccount`:

```java
Account account = new CheckingAccount(100.00);
// Den uttryckliga casten nedan misslyckas vid körning.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

Moderna IDE:er varnar för uppenbart felaktiga konverteringar, men ibland är resultatet inte känt i förväg. En metods argument är till exempel inte kända förrän metoden anropas. Felaktiga casts kan därför orsaka ett körningsundantag av typen `ClassCastException`[^7].

Eftersom `Account` kan ha flera subtyper, till exempel `CheckingAccount`, `SavingsAccount` och kanske `InvestmentAccount`, kan vi göra klassen abstrakt så att endast instanser av dess underklasser kan skapas:

```java
public abstract class Account {
    // Fält och metoder som är gemensamma för alla kontotyper.
}
```

Vi kan inte längre instansiera `Account` direkt. Vi måste använda en konstruktor från en av dess underklasser, exempelvis `CheckingAccount`:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: I Java består en metodsignatur av metodens namn, typparametrar (om sådana finns) och formella parametrar. Se [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2).

[^7]: Se [API-dokumentationen för ClassCastException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html).

---

*Den här artikeln bygger på innehåll från boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Relaterade artiklar

- [Grundläggande begrepp inom objektorienterad programmering](/oop-basics-java-sv/)
- [Klasser i Java](/klasser-i-java-sv/)
- [Polymorfism i Java](/polymorphism-in-java-sv/)
- [Gränssnitt i Java](/interfaces-in-java-sv/)
- [Länkar om OOP och Java](/oop-java-links-sv/)
- [Övningar i objektorienterad programmering](/oop-exercises-sv/)
