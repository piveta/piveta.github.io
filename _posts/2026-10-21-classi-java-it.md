---
layout: post
title: "Le classi in Java"
date: 2026-10-21
lang: it
translation_id: classes-em-java
permalink: /classi-java-it/
share_text: >-
  Scopri come definire classi, campi, metodi, costruttori e incapsulamento in Java.
---

Java supporta i principali concetti della programmazione orientata agli oggetti, tra cui classi, campi, metodi, ereditarietà, interfacce, polimorfismo e incapsulamento.

## Classi, campi e metodi

In Java, una classe si dichiara con la parola chiave `class`, un nome e un corpo in cui è possibile definire campi e metodi. Altri componenti facoltativi saranno illustrati più avanti. Consideriamo una classe chiamata `Account`. Possiamo dichiararla `public` affinché le altre classi possano accedervi:

```java
public class Account {
    // Corpo della classe
}
```

Possiamo aggiungere campi e metodi al corpo della classe. Nell’esempio seguente aggiungiamo un campo `balance` di tipo `Double`[^2] e un metodo `withdraw`, che non restituisce alcun valore (`void`) e riceve un parametro formale chiamato `amount`, anch’esso di tipo `Double`. Il metodo sottrae dal saldo l’importo passato come argomento:

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // oppure balance -= amount;
    }
}
```

Allo stesso modo, possiamo aggiungere un metodo `deposit` che aumenta il saldo del conto:

```java
public class Account {
    // balance e withdraw omessi
    public void deposit(Double amount) {
        balance = balance + amount; // oppure balance += amount;
    }
}
```

Consideriamo un client che esegue alcune operazioni su un conto. Prima crea un oggetto `Account` chiamandone il costruttore e assegna il riferimento a una variabile chiamata `account`. Poi imposta il saldo a 100.00, preleva 50.00, deposita 100.00 e stampa il saldo:

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

L’output è:

```text
Balance: 150.0
```

Per invocare i metodi `withdraw` e `deposit` serve un oggetto `Account`, perché sono metodi di istanza. Nelle versioni recenti di Java, anche `main` può essere un metodo statico o di istanza, come in questo esempio[^3].

L’esempio precedente mostra un client che usa campi e metodi di `Account`. Il client si trova in una classe senza nome dichiarata implicitamente. Tuttavia, accede direttamente a `balance`, creando un forte accoppiamento tra le classi, generalmente indesiderabile[^4]. Una soluzione consiste nell’incapsulare l’accesso a `balance`, facendo passare letture e scritture attraverso metodi dedicati. Così l’accoppiamento diminuisce e la rappresentazione interna del saldo potrà cambiare in seguito, purché le operazioni di lettura e scrittura restino disponibili. È inoltre buona norma ridurre la visibilità del campo affinché sia accessibile soltanto dall’interno della classe.

Java offre la visibilità di package (predefinita), `private`, `public` e `protected`. Questi livelli determinano quali classi possono accedere a un campo o a un metodo. Ogni livello ha una parola chiave associata, tranne la visibilità di package, che non ne usa alcuna.

Il codice seguente migliora l’incapsulamento e nasconde lo stato interno della classe ai client. Aggiunge metodi pubblici di lettura e scrittura (`getBalance` e `setBalance`), rende `balance` privato e aggiorna il saldo tramite questi metodi. Il riferimento `this` distingue il campo `balance` dal parametro del metodo con lo stesso nome. `this.balance` indica il campo, non il parametro:

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

Anche il client viene modificato e ora cambia il saldo tramite il metodo setter:

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Se non viene dichiarato esplicitamente alcun costruttore, le classi Java hanno un costruttore predefinito senza parametri. Possiamo definirne altri per agevolare l’uso della classe da parte dei client. Per esempio, questo costruttore di `Account` accetta un importo iniziale e lo usa per impostare il saldo. Se fosse necessario chiamare il costruttore di una superclasse, potremmo usare `super`:

```java
public class Account {
    // Campi e metodi di Account
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

Il client ora deve usare il nuovo costruttore e fornire un saldo iniziale, perché `Account` non ha più un costruttore predefinito senza argomenti[^5]:

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java non dispone di metodi distruttori. Gli oggetti che non sono più referenziati vengono raccolti automaticamente dal garbage collector.

[^2]: `Double` è usato qui per semplicità. Gli importi monetari normalmente non vengono memorizzati in variabili in virgola mobile, ma in tipi interi come `long` oppure in `BigDecimal`.

[^3]: Vedi [JEP 512](https://openjdk.org/jeps/512).

[^4]: Qui, “le classi” indica `Account` e la classe senza nome dichiarata implicitamente che contiene `main`.

[^5]: Quando definiamo un costruttore, la classe non ha più un costruttore predefinito. Se serve, possiamo definire anche un costruttore senza argomenti.

---

*Questo articolo adatta contenuti del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> di <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articoli correlati

- [Concetti fondamentali della programmazione orientata agli oggetti](/concetti-fondamentali-oop-it/)
- [Ereditarietà in Java](/ereditarieta-java-it/)
- [Polimorfismo in Java](/polimorfismo-java-it/)
- [Interfacce in Java](/interfacce-java-it/)
- [Link su OOP e Java](/link-oop-java-it/)
- [Esercizi di programmazione orientata agli oggetti](/esercizi-oop-it/)
