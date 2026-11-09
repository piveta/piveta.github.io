---
layout: post
title: "Gränssnitt i Java"
date: 2026-10-21
lang: sv
translation_id: interfaces-em-java
permalink: /granssnitt-i-java-sv/
share_text: >-
  Lär dig hur Java-gränssnitt definierar kontrakt och hur klasser implementerar dem.
---

I Java definieras gränssnitt på ett sätt som liknar klasser. Gränssnitt deklarerar vanligtvis metoder utan implementation, men Java stöder även standardmetoder (*default methods*) med en fördefinierad implementation. En klass som implementerar ett gränssnitt kan välja om den ska överskugga en standardmetod.

Ett gränssnitt deklareras med nyckelordet `interface` och kan utöka andra gränssnitt. Multipelt arv är tillåtet för gränssnitt. Javas `List`-gränssnitt utökar till exempel `Collection` och `Iterable`.

Följande exempel deklarerar ett gränssnitt som heter `AccountOperations`. Klasser som implementerar det måste tillhandahålla minst metoderna `withdraw` och `transfer`:

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

När `Account` implementerar `AccountOperations` ärver dess underklasser metoderna och uppfyller också gränssnittets kontrakt. Här implementerar en konkret klass `Account` metoderna `withdraw` och `transfer`, så dess underklasser behöver inte implementera dem igen:

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // Konkret implementation av withdraw
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // Konkret implementation av transfer
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

Ett annat alternativ är att flytta implementationerna av `withdraw`, `deposit` och `transfer` till `AccountOperations`-gränssnittet som `default`-metoder. Gränssnittet måste också deklarera `getBalance` och `setBalance`:

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

Den förenklade klassen `Account` skulle då se ut så här:

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

Att frikoppla gränssnittet från `Account` kan ge klasser större flexibilitet i hur saldot lagras och hanteras. Javas samlingsramverk har till exempel gränssnittet `List`, som anger vilka operationer en lista kan utföra. Konkreta implementationer som `ArrayList` och `LinkedList` använder olika strategier för lagring och åtkomst: den första använder en array och den andra en dubbellänkad lista.

---

*Den här artikeln bygger på innehåll från boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Relaterade artiklar

- [Grundläggande begrepp inom objektorienterad programmering](/oop-basics-java-sv/)
- [Klasser i Java](/klasser-i-java-sv/)
- [Arv i Java](/arv-i-java-sv/)
- [Polymorfism i Java](/polymorfism-i-java-sv/)
- [Länkar om OOP och Java](/oop-java-links-sv/)
- [Övningar i objektorienterad programmering](/oop-exercises-sv/)
