---
layout: post
title: "Klasser i Java"
date: 2026-10-21
lang: sv
translation_id: classes-em-java
permalink: /klasser-i-java-sv/
share_text: >-
  Lär dig att definiera Java-klasser, fält, metoder, konstruktorer och inkapsling.
---

Java stöder de centrala begreppen inom objektorienterad programmering, däribland klasser, fält, metoder, arv, gränssnitt, polymorfism och inkapsling.

## Klasser, fält och metoder

I Java deklareras en klass med nyckelordet `class`, ett namn och en kropp där fält och metoder kan definieras. Andra valfria delar tas upp senare. Vi kan till exempel tänka oss en klass som heter `Account`. Vi kan göra den `public` så att andra klasser kan komma åt den:

```java
public class Account {
    // Klassens kropp
}
```

Vi kan lägga till fält och metoder i klassens kropp. I nästa exempel lägger vi till fältet `balance` av typen `Double`[^2] och metoden `withdraw`. Den returnerar inget värde (`void`) och tar emot en formell parameter som heter `amount`, också av typen `Double`. Metoden drar det belopp som skickas som argument från saldot:

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // eller balance -= amount;
    }
}
```

På samma sätt kan vi lägga till metoden `deposit` som ökar kontots saldo:

```java
public class Account {
    // balance och withdraw utelämnade
    public void deposit(Double amount) {
        balance = balance + amount; // eller balance += amount;
    }
}
```

Tänk dig en klient som utför några åtgärder på ett konto. Först skapar den ett `Account`-objekt genom att anropa dess konstruktor och tilldelar referensen till en variabel som heter `account`. Sedan sätter den saldot till 100.00, tar ut 50.00, sätter in 100.00 och skriver ut saldot:

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

Resultatet blir:

```text
Balance: 150.0
```

Metoderna `withdraw` och `deposit` behöver ett `Account`-objekt för att anropas eftersom de är instansmetoder. I nyare Java-versioner kan `main` också vara en statisk metod eller en instansmetod, som i det här exemplet[^3].

Det föregående exemplet visar en klient som använder fält och metoder från `Account`. Klienten finns i en implicit deklarerad klass utan namn. Den kommer dock åt `balance` direkt, vilket skapar en stark koppling mellan klasserna. Det är vanligtvis inte önskvärt[^4]. Ett alternativ är att kapsla in åtkomsten till `balance`, så att läsning och skrivning sker via särskilda metoder. Det minskar kopplingen och gör det möjligt att senare ändra den interna representationen av saldot, så länge läs- och skrivoperationerna finns kvar. Det är också god praxis att begränsa fältets synlighet så att det bara kan kommas åt inifrån klassen.

Java har paketsynlighet (standard), `private`, `public` och `protected`. Dessa nivåer avgör vilka klasser som kan komma åt ett fält eller en metod. Alla nivåer utom paketsynlighet har ett nyckelord.

Följande kod förbättrar inkapslingen och döljer klassens interna tillstånd för klienterna. Den lägger till publika läs- och skrivmetoder (`getBalance` och `setBalance`), ändrar synligheten för `balance` till `private` och uppdaterar saldot via dessa metoder. Referensen `this` skiljer fältet `balance` från metodparametern med samma namn. `this.balance` syftar på fältet, inte parametern:

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

Klienten ändras också så att saldot ändras via setter-metoden:

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Om ingen konstruktor deklareras uttryckligen har Java-klasser en standardkonstruktor utan parametrar. Vi kan definiera andra konstruktorer för att göra klassen enklare att använda för klienter. Den här `Account`-konstruktorn tar till exempel emot ett startbelopp och sätter saldot till det. Om en konstruktor i en superklass måste anropas kan vi använda `super`:

```java
public class Account {
    // Fält och metoder i Account
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

Klienten måste nu använda den nya konstruktorn och ange ett startsaldo eftersom `Account` inte längre har någon standardkonstruktor utan argument[^5]:

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java har inga destruktormetoder. Objekt som inte längre refereras till samlas automatiskt in av skräpsamlaren.

[^2]: `Double` används här för enkelhetens skull. Pengavärden lagras vanligtvis inte i flyttalsvariabler, utan i heltalstyper som `long` eller i `BigDecimal`.

[^3]: Se [JEP 512](https://openjdk.org/jeps/512).

[^4]: Här syftar ”klasserna” på `Account` och den implicit deklarerade namnlösa klassen som innehåller `main`.

[^5]: När vi definierar en konstruktor har klassen inte längre någon standardkonstruktor. Vid behov kan vi även definiera en konstruktor utan argument.

---

*Den här artikeln bygger på innehåll från boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Relaterade artiklar

- [Grundläggande begrepp inom objektorienterad programmering](/oop-basics-java-sv/)
- [Arv i Java](/inheritance-in-java-sv/)
- [Polymorfism i Java](/polymorphism-in-java-sv/)
- [Gränssnitt i Java](/interfaces-in-java-sv/)
- [Länkar om OOP och Java](/oop-java-links-sv/)
- [Övningar i objektorienterad programmering](/oop-exercises-sv/)
