---
layout: post
title: "Interfejsy w Javie"
date: 2026-10-21
lang: pl
translation_id: interfaces-em-java
permalink: /interfejsy-w-java-pl/
share_text: >-
  Dowiedz się, jak interfejsy w Javie definiują kontrakty i jak klasy je implementują.
---

Interfejsy w Javie definiuje się podobnie jak klasy. Zazwyczaj deklarują metody bez implementacji, choć Java obsługuje również metody domyślne (*default methods*) z wcześniej zdefiniowaną implementacją. Klasa implementująca interfejs może zdecydować, czy nadpisać metodę domyślną.

Interfejs deklaruje się słowem kluczowym `interface` i może on rozszerzać inne interfejsy. W przypadku interfejsów dozwolone jest wielokrotne dziedziczenie. Na przykład interfejs Javy `List` rozszerza `Collection` i `Iterable`.

Poniższy przykład deklaruje interfejs o nazwie `AccountOperations`. Klasy, które go implementują, muszą udostępnić co najmniej metody `withdraw` i `transfer`:

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

Gdy `Account` implementuje `AccountOperations`, jej podklasy dziedziczą metody i również spełniają kontrakt interfejsu. Tutaj konkretna klasa `Account` implementuje `withdraw` i `transfer`, więc podklasy nie muszą implementować ich ponownie:

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // Konkretna implementacja withdraw
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // Konkretna implementacja transfer
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

Inną możliwością jest przeniesienie implementacji `withdraw`, `deposit` i `transfer` do interfejsu `AccountOperations` jako metod `default`. Interfejs musi też deklarować `getBalance` i `setBalance`:

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

Uproszczona klasa `Account` wyglądałaby wtedy tak:

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

Oddzielenie interfejsu od `Account` może dać klasom większą elastyczność w przechowywaniu i zarządzaniu saldem. Na przykład framework kolekcji Javy zawiera interfejs `List`, który określa operacje dostępne dla listy. Konkretne implementacje, takie jak `ArrayList` i `LinkedList`, używają różnych strategii przechowywania i dostępu: pierwsza korzysta z tablicy, a druga z listy dwukierunkowej.

---

*Ten artykuł adaptuje treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kesslera Pivety</a>.*

## Powiązane artykuły

- [Podstawowe pojęcia programowania obiektowego](/oop-basics-java-pl/)
- [Klasy w Javie](/klasy-w-java-pl/)
- [Dziedziczenie w Javie](/dziedziczenie-w-java-pl/)
- [Polimorfizm w Javie](/polymorphism-in-java-pl/)
- [Linki o OOP i Javie](/oop-java-links-pl/)
- [Ćwiczenia z programowania obiektowego](/oop-exercises-pl/)
