---
layout: post
title: "Les classes en Java"
date: 2026-10-21
lang: fr
translation_id: classes-em-java
permalink: /classes-en-java-fr/
share_text: >-
  Apprenez à définir des classes Java, des champs, des méthodes, des constructeurs et l’encapsulation.
---

Java prend en charge les principaux concepts de la programmation orientée objet, notamment les classes, les champs, les méthodes, l’héritage, les interfaces, le polymorphisme et l’encapsulation.

## Classes, champs et méthodes

En Java, une classe se déclare avec le mot-clé `class`, un nom et un corps dans lequel on peut définir des champs et des méthodes. D’autres éléments facultatifs sont présentés plus loin. Considérons une classe appelée `Account`. On peut la déclarer `public` afin que les autres classes puissent y accéder :

```java
public class Account {
    // Corps de la classe
}
```

On peut ajouter des champs et des méthodes au corps de la classe. Dans l’exemple suivant, on ajoute un champ `balance` de type `Double`[^2] et une méthode `withdraw`, qui ne renvoie aucune valeur (`void`) et reçoit un paramètre formel nommé `amount`, également de type `Double`. La méthode soustrait du solde le montant transmis en argument :

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // ou balance -= amount;
    }
}
```

De même, on peut ajouter une méthode `deposit` qui augmente le solde du compte :

```java
public class Account {
    // balance et withdraw omis
    public void deposit(Double amount) {
        balance = balance + amount; // ou balance += amount;
    }
}
```

Considérons un client qui effectue quelques opérations sur un compte. Il crée d’abord un objet `Account` en appelant son constructeur et affecte sa référence à une variable nommée `account`. Il fixe ensuite le solde à 100.00, retire 50.00, dépose 100.00 et affiche le solde :

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

La sortie est :

```text
Balance: 150.0
```

Les méthodes `withdraw` et `deposit` nécessitent un objet `Account` pour être invoquées, car ce sont des méthodes d’instance. Dans les versions récentes de Java, `main` peut également être une méthode statique ou une méthode d’instance, comme dans cet exemple[^3].

L’exemple précédent présente un client qui utilise les champs et les méthodes de `Account`. Ce client se trouve dans une classe sans nom déclarée implicitement. Il accède toutefois directement à `balance`, ce qui crée un couplage fort entre les classes, généralement indésirable[^4]. Une solution consiste à encapsuler l’accès à `balance` afin que la lecture et l’écriture passent par des méthodes dédiées. Le couplage diminue et la représentation interne du solde pourra évoluer, à condition que les opérations de lecture et d’écriture restent disponibles. Il est également recommandé de réduire la visibilité du champ pour que seul le code de la classe puisse y accéder.

Java propose les visibilités de paquet (par défaut), `private`, `public` et `protected`. Elles déterminent quelles classes peuvent accéder à un champ ou à une méthode. Chaque niveau possède un mot-clé, sauf la visibilité de paquet, qui n’en utilise aucun.

Le code suivant améliore l’encapsulation et masque l’état interne de la classe à ses clients. Il ajoute des méthodes publiques de lecture et d’écriture (`getBalance` et `setBalance`), rend `balance` privé et met à jour le solde au moyen de ces méthodes. La référence `this` distingue le champ `balance` du paramètre de méthode portant le même nom. `this.balance` désigne le champ, et non le paramètre :

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

Le client est lui aussi modifié : il change maintenant le solde avec la méthode setter :

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

En l’absence de constructeur explicitement déclaré, les classes Java possèdent un constructeur par défaut sans paramètre. On peut en définir d’autres pour faciliter leur utilisation par les clients. Par exemple, ce constructeur de `Account` accepte un montant initial et l’utilise pour fixer le solde. S’il fallait appeler le constructeur d’une superclasse, on pourrait employer `super` :

```java
public class Account {
    // Champs et méthodes de Account
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

Le client doit désormais utiliser le nouveau constructeur et fournir un solde initial, car `Account` n’a plus de constructeur par défaut sans argument[^5] :

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java ne possède pas de méthodes destructrices. Les objets qui ne sont plus référencés sont automatiquement récupérés par le ramasse-miettes.

[^2]: `Double` est utilisé ici par simplicité. Les valeurs monétaires ne sont généralement pas stockées dans des variables à virgule flottante, mais dans des types entiers comme `long` ou dans `BigDecimal`.

[^3]: Voir [JEP 512](https://openjdk.org/jeps/512).

[^4]: Ici, « les classes » désigne `Account` et la classe sans nom déclarée implicitement qui contient `main`.

[^5]: Dès qu’on définit un constructeur, la classe ne possède plus de constructeur par défaut. On peut aussi définir un constructeur sans argument si nécessaire.

---

*Cet article adapte du contenu du livre <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, d’<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articles associés

- [Concepts fondamentaux de la programmation orientée objet](/concepts-fondamentaux-poo-fr/)
- [Héritage en Java](/heritage-java-fr/)
- [Polymorphisme en Java](/polymorphisme-java-fr/)
- [Interfaces en Java](/interfaces-java-fr/)
- [Liens sur la POO et Java](/liens-poo-java-fr/)
- [Exercices de programmation orientée objet](/exercices-poo-fr/)
