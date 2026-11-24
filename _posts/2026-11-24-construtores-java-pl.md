---
layout: post
title: "Konstruktory w Javie"
date: 2026-11-24
lang: pl
translation_id: construtores-java
permalink: /pl/constructors-in-java/
share_text: "Konstruktory w Javie"
---

Konstruktor inicjalizuje obiekt podczas jego tworzenia. W klasie `Account` z książki konstruktor przyjmuje początkowe saldo i ustawia je za pomocą `setBalance`. W pierwszym fragmencie pominięto pozostałe pola i metody.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

Wywołanie `new Account(100.00)` tworzy konto z saldem 100. Następnie program wypłaca 50 i wpłaca 100. Wyświetlone saldo wynosi `150.0`.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

Kompilator zapewnia konstruktor domyślny, jeśli zwykła klasa nie deklaruje żadnego konstruktora. Po zadeklarowaniu `Account(Double value)` ten niejawny konstruktor przestaje być dostępny. Aby umożliwić również `new Account()`, jawnie zadeklaruj konstruktor bezargumentowy. Podklasa nie dziedziczy konstruktorów klasy `Account`, ale może wywołać jeden z nich za pomocą `super(value)`.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

