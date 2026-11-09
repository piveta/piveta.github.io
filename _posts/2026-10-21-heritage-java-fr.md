---
layout: post
title: "L’héritage en Java"
date: 2026-10-21
lang: fr
translation_id: heranca-em-java
permalink: /heritage-java-fr/
share_text: >-
  Introduction à l’héritage en Java, à la redéfinition de méthodes, aux conversions de sous-types et aux classes abstraites.
---

L’**héritage** est un mécanisme de composition qui permet aux classes de réutiliser l’interface et le comportement de classes existantes en étendant leurs fonctionnalités. Une classe qui en étend une autre par héritage est appelée sa **sous-classe** ; la classe étendue est appelée sa **superclasse**.

Java autorise l’héritage simple pour les classes (l’héritage multiple est possible avec les interfaces), et les sous-classes sont des sous-types de leur superclasse. La sous-classe déclare l’héritage avec le mot-clé `extends` : `Classe extends SuperClasse`. Une classe sans superclasse explicitement déclarée est implicitement une sous-classe d’`Object`, la racine de la hiérarchie des classes Java.

Considérons la classe `CheckingAccount` ci-dessous. Elle étend `Account` et ajoute un champ, des méthodes pour le lire et le modifier ainsi qu’un constructeur. Comme `Account` n’a pas de constructeur sans argument, le constructeur de `CheckingAccount` appelle celui de la superclasse avec `super` :

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

Les sous-classes possèdent souvent des **méthodes redéfinies** : des méthodes déclarées dans une superclasse dont une sous-classe étend ou remplace le comportement. Ici, `CheckingAccount` redéfinit la méthode `withdraw` d’`Account` en déclarant une méthode de même signature[^6]. Elle appelle d’abord la méthode de la superclasse avec `super`, puis calcule des frais à l’aide de `deductFee`, qui retranche du solde 1 % du montant de la transaction :

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // Autres constructeurs, champs et méthodes.
}
```

Par exemple, si un `CheckingAccount` possède un solde initial de 100.00 et qu’on retire 50.00, il reste 49.50, car des frais de 0.50 sont prélevés :

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

Selon le principe de substitution de Liskov, on peut affecter un objet de sous-classe là où un objet de superclasse est attendu : toute instance de `CheckingAccount` est aussi une instance d’`Account`. L’inverse n’est pas toujours vrai, car un `Account` peut être un `SavingsAccount`, par exemple. Dans ces cas, une conversion explicite (*cast*) est nécessaire.

Dans l’exemple suivant, `checkingAccount` est de type `CheckingAccount` et référence une instance de cette classe. La variable `account`, de type `Account`, reçoit la même référence. Cette affectation ne demande aucune conversion. L’affectation inverse exige un *cast* explicite :

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // Un CheckingAccount est un Account.
checkingAccount = (CheckingAccount) account; // Cast explicite valide.
```

Supposons que `SavingsAccount` soit une autre sous-classe d’`Account`. Dans l’exemple suivant, `account` référence un `CheckingAccount`. Le cast en `SavingsAccount` échoue à l’exécution, car l’objet n’est pas un `SavingsAccount` :

```java
Account account = new CheckingAccount(100.00);
// Le cast explicite ci-dessous échoue à l’exécution.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

Les IDE modernes signalent les conversions manifestement incorrectes, mais le résultat n’est parfois pas connu à l’avance. Les arguments d’une méthode, par exemple, ne sont connus qu’au moment de l’appel. Un cast incorrect peut donc provoquer une exception d’exécution de type `ClassCastException`[^7].

Puisqu’`Account` peut avoir plusieurs sous-types, comme `CheckingAccount`, `SavingsAccount` et éventuellement `InvestmentAccount`, on peut la rendre abstraite afin de ne créer que des instances de ses sous-classes :

```java
public abstract class Account {
    // Champs et méthodes communs à tous les types de compte.
}
```

On ne peut plus instancier directement `Account`. Il faut utiliser le constructeur d’une de ses sous-classes, par exemple `CheckingAccount` :

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: En Java, la signature d’une méthode comprend son nom, ses paramètres de type éventuels et ses paramètres formels. Voir la [spécification du langage Java](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2).

[^7]: Voir la [documentation de l’API ClassCastException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html).

---

*Cet article adapte du contenu du livre <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, d’<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articles associés

- [Concepts fondamentaux de la programmation orientée objet](/concepts-fondamentaux-poo-fr/)
- [Classes en Java](/classes-en-java-fr/)
- [Polymorphisme en Java](/polymorphisme-java-fr/)
- [Interfaces en Java](/interfaces-java-fr/)
- [Liens sur la POO et Java](/liens-poo-java-fr/)
- [Exercices de programmation orientée objet](/exercices-poo-fr/)
