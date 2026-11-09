---
layout: post
title: "Dziedziczenie w Javie"
date: 2026-10-21
lang: pl
translation_id: heranca-em-java
permalink: /dziedziczenie-w-java-pl/
share_text: >-
  Wprowadzenie do dziedziczenia w Javie, nadpisywania metod, konwersji podtypów i klas abstrakcyjnych.
---

**Dziedziczenie** to mechanizm kompozycji, który pozwala klasom ponownie wykorzystywać interfejs i zachowanie istniejących klas oraz rozszerzać ich funkcjonalność. Klasa rozszerzająca inną klasę przez dziedziczenie jest nazywana jej **podklasą**, a klasa rozszerzana — **nadklasą**.

Java dopuszcza pojedyncze dziedziczenie klas (wielokrotne dziedziczenie jest dostępne dla interfejsów), a podklasy są podtypami swoich nadklas. Dziedziczenie deklaruje się w podklasie za pomocą słowa kluczowego `extends`: `Klasa extends Nadklasa`. Klasa bez jawnie zadeklarowanej nadklasy jest niejawnie podklasą `Object`, korzenia hierarchii klas Javy.

Rozważmy klasę `CheckingAccount` poniżej. Rozszerza ona `Account` i dodaje pole, metody jego odczytu i zapisu oraz konstruktor. Ponieważ `Account` nie ma konstruktora bezargumentowego, konstruktor `CheckingAccount` wywołuje konstruktor nadklasy przez `super`:

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

Podklasy często mają **nadpisane metody**: metody zadeklarowane w nadklasie, których zachowanie podklasa rozszerza lub zastępuje. Tutaj `CheckingAccount` nadpisuje metodę `withdraw` klasy `Account`, deklarując metodę o takim samym sygnaturze[^6]. Najpierw wywołuje metodę nadklasy przez `super`, a potem oblicza opłatę za pomocą `deductFee`, które odejmuje od salda 1% kwoty transakcji:

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // Inne konstruktory, pola i metody.
}
```

Na przykład, jeśli początkowe saldo `CheckingAccount` wynosi 100.00 i wypłacimy 50.00, pozostanie 49.50, ponieważ zostanie pobrana opłata 0.50:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

Zgodnie z zasadą podstawienia Liskov możemy przypisać obiekt podklasy wszędzie tam, gdzie oczekiwany jest obiekt nadklasy: każda instancja `CheckingAccount` jest też instancją `Account`. Odwrotna sytuacja nie zawsze zachodzi, ponieważ `Account` może być na przykład `SavingsAccount`. W takich przypadkach potrzebna jest jawna konwersja (*cast*).

W kolejnym przykładzie `checkingAccount` ma typ `CheckingAccount` i wskazuje instancję tej klasy. Zmienna `account` ma typ `Account` i otrzymuje ten sam obiekt. To przypisanie nie wymaga konwersji. Przypisanie w odwrotną stronę wymaga jawnego rzutowania:

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // CheckingAccount jest Account.
checkingAccount = (CheckingAccount) account; // Poprawne jawne rzutowanie.
```

Załóżmy, że `SavingsAccount` jest inną podklasą `Account`. W następnym przykładzie `account` wskazuje `CheckingAccount`. Rzutowanie go na `SavingsAccount` zakończy się błędem w czasie wykonania, ponieważ obiekt nie jest `SavingsAccount`:

```java
Account account = new CheckingAccount(100.00);
// Poniższe jawne rzutowanie nie powiedzie się w czasie wykonania.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

Nowoczesne IDE ostrzegają przed oczywiście błędnymi konwersjami, ale czasem wynik nie jest znany z góry. Na przykład argumenty metody są znane dopiero w chwili jej wywołania. Niepoprawne rzutowanie może więc spowodować wyjątek czasu wykonania typu `ClassCastException`[^7].

Ponieważ `Account` może mieć kilka podtypów, takich jak `CheckingAccount`, `SavingsAccount`, a być może także `InvestmentAccount`, możemy uczynić ją klasą abstrakcyjną, aby można było tworzyć tylko instancje jej podklas:

```java
public abstract class Account {
    // Pola i metody wspólne dla wszystkich rodzajów kont.
}
```

Nie można już bezpośrednio tworzyć instancji `Account`. Trzeba użyć konstruktora jednej z podklas, na przykład `CheckingAccount`:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: W Javie sygnatura metody składa się z jej nazwy, parametrów typu (jeśli istnieją) i parametrów formalnych. Zobacz [specyfikację języka Java](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2).

[^7]: Zobacz [dokumentację API ClassCastException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html).

---

*Ten artykuł adaptuje treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kesslera Pivety</a>.*

## Powiązane artykuły

- [Podstawowe pojęcia programowania obiektowego](/oop-basics-java-pl/)
- [Klasy w Javie](/klasy-w-java-pl/)
- [Polimorfizm w Javie](/polymorphism-in-java-pl/)
- [Interfejsy w Javie](/interfaces-in-java-pl/)
- [Linki o OOP i Javie](/oop-java-links-pl/)
- [Ćwiczenia z programowania obiektowego](/oop-exercises-pl/)
