---
layout: post
title: "Klasy w Javie"
date: 2026-10-21
lang: pl
translation_id: classes-em-java
permalink: /klasy-w-java-pl/
share_text: >-
  Dowiedz się, jak definiować klasy, pola, metody, konstruktory i enkapsulację w Javie.
---

Java obsługuje najważniejsze pojęcia programowania obiektowego, w tym klasy, pola, metody, dziedziczenie, interfejsy, polimorfizm i enkapsulację.

## Klasy, pola i metody

W Javie klasę deklaruje się za pomocą słowa kluczowego `class`, nazwy oraz treści, w której można zdefiniować pola i metody. Inne opcjonalne elementy omówimy dalej. Rozważmy klasę o nazwie `Account`. Możemy zadeklarować ją jako `public`, aby inne klasy miały do niej dostęp:

```java
public class Account {
    // Treść klasy
}
```

Do treści klasy możemy dodać pola i metody. W kolejnym przykładzie dodajemy pole `balance` typu `Double`[^2] oraz metodę `withdraw`, która niczego nie zwraca (`void`) i przyjmuje parametr formalny `amount`, również typu `Double`. Metoda odejmuje od salda kwotę przekazaną jako argument:

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // lub balance -= amount;
    }
}
```

Podobnie możemy dodać metodę `deposit`, która zwiększa saldo konta:

```java
public class Account {
    // Pominięto balance i withdraw
    public void deposit(Double amount) {
        balance = balance + amount; // lub balance += amount;
    }
}
```

Rozważmy klienta wykonującego kilka operacji na koncie. Najpierw tworzy on obiekt `Account`, wywołując jego konstruktor, i przypisuje referencję do zmiennej `account`. Następnie ustawia saldo na 100.00, wypłaca 50.00, wpłaca 100.00 i wyświetla saldo:

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

Wynik to:

```text
Balance: 150.0
```

Metody `withdraw` i `deposit` wymagają obiektu `Account`, ponieważ są metodami instancyjnymi. W nowszych wersjach Javy `main` może być metodą statyczną albo instancyjną, jak w tym przykładzie[^3].

Poprzedni przykład pokazuje klienta korzystającego z pól i metod `Account`. Klient znajduje się w klasie bez nazwy, zadeklarowanej niejawnie. Bezpośredni dostęp do `balance` powoduje jednak silne powiązanie klas, co zwykle jest niepożądane[^4]. Można zamiast tego enkapsulować dostęp do `balance`, tak aby odczyt i zapis odbywały się przez dedykowane metody. Zmniejsza to powiązanie i pozwala później zmienić wewnętrzną reprezentację salda, pod warunkiem zachowania operacji odczytu i zapisu. Dobrą praktyką jest również ograniczenie widoczności pola, aby dostęp do niego był możliwy tylko wewnątrz klasy.

Java udostępnia widoczność pakietową (domyślną), `private`, `public` i `protected`. Określają one, które klasy mogą uzyskać dostęp do pola lub metody. Każdemu poziomowi odpowiada słowo kluczowe, z wyjątkiem widoczności pakietowej.

Poniższy kod poprawia enkapsulację i ukrywa stan wewnętrzny klasy przed klientami. Dodaje publiczne metody odczytu i zapisu (`getBalance` i `setBalance`), zmienia widoczność `balance` na `private` i aktualizuje saldo za pomocą tych metod. Referencja `this` odróżnia pole `balance` od parametru metody o tej samej nazwie. `this.balance` wskazuje pole, a nie parametr:

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

Klient również zostaje zmieniony i modyfikuje saldo za pomocą metody setter:

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Jeśli nie zadeklarowano jawnie konstruktora, klasy Javy mają domyślny konstruktor bez parametrów. Możemy zdefiniować inne konstruktory, aby ułatwić klientom korzystanie z klasy. Na przykład ten konstruktor `Account` przyjmuje kwotę początkową i ustawia nią saldo. Jeśli trzeba wywołać konstruktor nadklasy, można użyć `super`:

```java
public class Account {
    // Pola i metody Account
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

Klient musi teraz używać nowego konstruktora i podawać saldo początkowe, ponieważ `Account` nie ma już domyślnego konstruktora bezargumentowego[^5]:

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java nie ma metod destruktorów. Obiekty, do których nie ma już referencji, są automatycznie odzyskiwane przez garbage collector.

[^2]: Dla uproszczenia używamy tutaj `Double`. Wartości pieniężnych zwykle nie przechowuje się w zmiennych zmiennoprzecinkowych, lecz w typach całkowitych, takich jak `long`, albo w `BigDecimal`.

[^3]: Zobacz [JEP 512](https://openjdk.org/jeps/512).

[^4]: Określenie „klasy” odnosi się tu do `Account` oraz niejawnie zadeklarowanej klasy bez nazwy, która zawiera `main`.

[^5]: Po zdefiniowaniu konstruktora klasa nie ma już konstruktora domyślnego. W razie potrzeby można również zdefiniować konstruktor bezargumentowy.

---

*Ten artykuł adaptuje treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kesslera Pivety</a>.*

## Powiązane artykuły

- [Podstawowe pojęcia programowania obiektowego](/oop-basics-java-pl/)
- [Dziedziczenie w Javie](/inheritance-in-java-pl/)
- [Polimorfizm w Javie](/polymorphism-in-java-pl/)
- [Interfejsy w Javie](/interfaces-in-java-pl/)
- [Linki o OOP i Javie](/oop-java-links-pl/)
- [Ćwiczenia z programowania obiektowego](/oop-exercises-pl/)
