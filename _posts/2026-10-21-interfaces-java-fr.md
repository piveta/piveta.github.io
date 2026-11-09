---
layout: post
title: "Les interfaces en Java"
date: 2026-10-21
lang: fr
translation_id: interfaces-em-java
permalink: /interfaces-java-fr/
share_text: >-
  Découvrez comment les interfaces Java définissent des contrats et comment les classes les implémentent.
---

En Java, les interfaces se définissent d’une manière proche des classes. Elles déclarent le plus souvent des méthodes sans implémentation, même si Java prend également en charge les méthodes par défaut (*default methods*), qui disposent d’une implémentation prédéfinie. Une classe qui implémente une interface peut choisir de redéfinir ou non une méthode par défaut.

Une interface se déclare avec le mot-clé `interface` et peut étendre d’autres interfaces. L’héritage multiple est autorisé pour les interfaces. Par exemple, l’interface Java `List` étend `Collection` et `Iterable`.

L’exemple suivant déclare une interface nommée `AccountOperations`. Les classes qui l’implémentent doivent fournir au moins les méthodes `withdraw` et `transfer` :

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

Lorsque `Account` implémente `AccountOperations`, ses sous-classes héritent des méthodes et respectent elles aussi le contrat de l’interface. Ici, une classe concrète `Account` implémente `withdraw` et `transfer`, de sorte que ses sous-classes n’ont pas à le faire à nouveau :

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // Implémentation concrète de withdraw
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // Implémentation concrète de transfer
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

On peut aussi déplacer les implémentations de `withdraw`, `deposit` et `transfer` dans l’interface `AccountOperations` sous forme de méthodes `default`. L’interface doit également déclarer `getBalance` et `setBalance` :

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

La classe `Account` simplifiée devient alors :

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

Dissocier l’interface d’`Account` peut offrir davantage de souplesse aux classes pour stocker et gérer le solde. Le framework de collections Java possède, par exemple, l’interface `List`, qui définit les opérations d’une liste. Des implémentations concrètes comme `ArrayList` et `LinkedList` utilisent des stratégies différentes de stockage et d’accès : la première repose sur un tableau, la seconde sur une liste doublement chaînée.

---

*Cet article adapte du contenu du livre <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, d’<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articles associés

- [Concepts fondamentaux de la programmation orientée objet](/concepts-fondamentaux-poo-fr/)
- [Classes en Java](/classes-en-java-fr/)
- [Héritage en Java](/heritage-java-fr/)
- [Polymorphisme en Java](/polymorphisme-java-fr/)
- [Liens sur la POO et Java](/liens-poo-java-fr/)
- [Exercices de programmation orientée objet](/exercices-poo-fr/)
