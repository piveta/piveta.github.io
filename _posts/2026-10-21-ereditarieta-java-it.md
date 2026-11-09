---
layout: post
title: "Ereditarietà in Java"
date: 2026-10-21
lang: it
translation_id: heranca-em-java
permalink: /ereditarieta-java-it/
share_text: >-
  Introduzione all’ereditarietà in Java, all’override, alle conversioni tra sottotipi e alle classi astratte.
---

L’**ereditarietà** è un meccanismo di composizione che consente alle classi di riutilizzare l’interfaccia e il comportamento di classi esistenti, estendendone le funzionalità. Una classe che ne estende un’altra tramite ereditarietà è detta **sottoclasse**; la classe estesa è detta **superclasse**.

Java consente l’ereditarietà singola per le classi (quella multipla è disponibile per le interfacce) e le sottoclassi sono sottotipi della propria superclasse. La sottoclasse dichiara l’ereditarietà con la parola chiave `extends`: `Classe extends SuperClasse`. Una classe senza superclasse dichiarata esplicitamente è implicitamente una sottoclasse di `Object`, la radice della gerarchia delle classi Java.

Consideriamo la classe `CheckingAccount` qui sotto. Estende `Account` e aggiunge un campo, metodi per leggerlo e modificarlo e un costruttore. Poiché `Account` non ha un costruttore senza argomenti, il costruttore di `CheckingAccount` richiama quello della superclasse con `super`:

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

Le sottoclassi hanno spesso **metodi ridefiniti**: metodi dichiarati in una superclasse il cui comportamento viene esteso o sostituito da una sottoclasse. Qui, `CheckingAccount` ridefinisce il metodo `withdraw` di `Account` dichiarando un metodo con la stessa firma[^6]. Prima richiama con `super` il metodo della superclasse, poi calcola una commissione con `deductFee`, che sottrae dal saldo l’1% dell’importo dell’operazione:

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // Altri costruttori, campi e metodi.
}
```

Per esempio, se un `CheckingAccount` parte da un saldo di 100.00 e preleviamo 50.00, il saldo rimanente è 49.50 perché viene addebitata una commissione di 0.50:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

Secondo il principio di sostituzione di Liskov, possiamo assegnare oggetti di una sottoclasse ovunque sia previsto un oggetto della superclasse: ogni istanza di `CheckingAccount` è anche un’istanza di `Account`. Il contrario non è sempre vero, perché un `Account` potrebbe essere, per esempio, un `SavingsAccount`. In questi casi occorre una conversione esplicita (*cast*).

Nel seguente esempio, `checkingAccount` ha tipo `CheckingAccount` e fa riferimento a un’istanza di quella classe. La variabile `account` ha tipo `Account` e riceve lo stesso oggetto. Questa assegnazione non richiede conversioni. L’assegnazione inversa richiede un cast esplicito:

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // Un CheckingAccount è un Account.
checkingAccount = (CheckingAccount) account; // Cast esplicito valido.
```

Supponiamo che `SavingsAccount` sia un’altra sottoclasse di `Account`. Nell’esempio seguente, `account` fa riferimento a un `CheckingAccount`. Il cast a `SavingsAccount` fallisce durante l’esecuzione perché l’oggetto non è un `SavingsAccount`:

```java
Account account = new CheckingAccount(100.00);
// Il cast esplicito seguente fallisce durante l’esecuzione.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

Gli IDE moderni avvisano delle conversioni chiaramente errate, ma a volte il risultato non è noto in anticipo. Per esempio, gli argomenti di un metodo si conoscono solo quando il metodo viene chiamato. Un cast errato può quindi causare un’eccezione di runtime di tipo `ClassCastException`[^7].

Dato che `Account` può avere diversi sottotipi, come `CheckingAccount`, `SavingsAccount` e forse `InvestmentAccount`, possiamo renderla astratta in modo da creare istanze solo delle sue sottoclassi:

```java
public abstract class Account {
    // Campi e metodi comuni a tutti i tipi di conto.
}
```

Non possiamo più istanziare direttamente `Account`. Dobbiamo usare il costruttore di una sua sottoclasse, ad esempio `CheckingAccount`:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: In Java, la firma di un metodo è composta dal nome, dai parametri di tipo (se presenti) e dai parametri formali. Vedi la [specifica del linguaggio Java](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2).

[^7]: Vedi la [documentazione API di ClassCastException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html).

---

*Questo articolo adatta contenuti del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> di <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articoli correlati

- [Concetti fondamentali della programmazione orientata agli oggetti](/concetti-fondamentali-oop-it/)
- [Classi in Java](/classi-java-it/)
- [Polimorfismo in Java](/polimorfismo-java-it/)
- [Interfacce in Java](/interfacce-java-it/)
- [Link su OOP e Java](/link-oop-java-it/)
- [Esercizi di programmazione orientata agli oggetti](/esercizi-oop-it/)
