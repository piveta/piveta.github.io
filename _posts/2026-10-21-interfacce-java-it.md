---
layout: post
title: "Le interfacce in Java"
date: 2026-10-21
lang: it
translation_id: interfaces-em-java
permalink: /interfacce-java-it/
share_text: >-
  Scopri come le interfacce Java definiscono contratti e come le classi le implementano.
---

In Java, le interfacce si definiscono in modo simile alle classi. Di solito dichiarano metodi senza implementazione, ma Java supporta anche i metodi predefiniti (*default methods*), dotati di un’implementazione già definita. Una classe che implementa un’interfaccia può scegliere se ridefinire un metodo predefinito.

Un’interfaccia si dichiara con la parola chiave `interface` e può estendere altre interfacce. Per le interfacce è consentita l’ereditarietà multipla. Per esempio, l’interfaccia Java `List` estende `Collection` e `Iterable`.

L’esempio seguente dichiara un’interfaccia chiamata `AccountOperations`. Le classi che la implementano devono fornire almeno i metodi `withdraw` e `transfer`:

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

Quando `Account` implementa `AccountOperations`, le sue sottoclassi ereditano i metodi e rispettano anch’esse il contratto dell’interfaccia. Qui una classe concreta `Account` implementa `withdraw` e `transfer`, quindi le sottoclassi non devono farlo di nuovo:

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // Implementazione concreta di withdraw
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // Implementazione concreta di transfer
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

Un’altra possibilità è spostare le implementazioni di `withdraw`, `deposit` e `transfer` nell’interfaccia `AccountOperations` come metodi `default`. L’interfaccia deve inoltre dichiarare `getBalance` e `setBalance`:

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

La classe `Account` semplificata diventa quindi:

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

Disaccoppiare l’interfaccia da `Account` può offrire alle classi maggiore flessibilità nel modo di memorizzare e gestire il saldo. Per esempio, il framework delle collezioni Java ha l’interfaccia `List`, che definisce le operazioni disponibili per un elenco. Implementazioni concrete come `ArrayList` e `LinkedList` usano strategie diverse per memorizzazione e accesso: la prima si basa su un array, la seconda su una lista doppiamente concatenata.

---

*Questo articolo adatta contenuti del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> di <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articoli correlati

- [Concetti fondamentali della programmazione orientata agli oggetti](/concetti-fondamentali-oop-it/)
- [Classi in Java](/classi-java-it/)
- [Ereditarietà in Java](/ereditarieta-java-it/)
- [Polimorfismo in Java](/polimorfismo-java-it/)
- [Link su OOP e Java](/link-oop-java-it/)
- [Esercizi di programmazione orientata agli oggetti](/esercizi-oop-it/)
