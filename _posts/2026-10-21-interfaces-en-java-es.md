---
layout: post
title: "Interfaces en Java"
date: 2026-10-21
lang: es
translation_id: interfaces-em-java
permalink: /interfaces-en-java/
share_text: >-
  Aprende cómo las interfaces de Java definen contratos y cómo las implementan las clases.
---

En Java, las interfaces se definen de manera similar a las clases. Normalmente declaran métodos sin implementación, aunque Java también admite métodos predeterminados (*default methods*), que tienen una implementación predefinida. Una clase que implementa una interfaz puede decidir si sobrescribe un método predeterminado.

Una interfaz se declara con la palabra clave `interface` y puede extender otras interfaces. Las interfaces admiten herencia múltiple. Por ejemplo, la interfaz `List` de Java extiende `Collection` e `Iterable`.

El siguiente ejemplo declara una interfaz llamada `AccountOperations`. Las clases que la implementen deben proporcionar al menos los métodos `withdraw` y `transfer`:

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

Cuando `Account` implementa `AccountOperations`, sus subclases heredan los métodos y también cumplen el contrato de la interfaz. Aquí, una clase concreta `Account` implementa `withdraw` y `transfer`, así que sus subclases no tienen que volver a implementarlos:

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // Implementación concreta de withdraw
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // Implementación concreta de transfer
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

Otra opción es mover las implementaciones de `withdraw`, `deposit` y `transfer` a la interfaz `AccountOperations` como métodos `default`. La interfaz también debe declarar `getBalance` y `setBalance`:

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

La clase `Account` simplificada quedaría así:

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

Desacoplar la interfaz de `Account` puede dar más flexibilidad a las clases para almacenar y gestionar el saldo. Por ejemplo, el marco de colecciones de Java tiene la interfaz `List`, que define las operaciones de una lista. Implementaciones concretas como `ArrayList` y `LinkedList` utilizan estrategias distintas de almacenamiento y acceso: la primera usa un arreglo y la segunda, una lista doblemente enlazada.

---

*Este artículo adapta contenido del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artículos relacionados

- [Conceptos básicos de orientación a objetos](/conceptos-basicos-de-poo/)
- [Clases en Java](/clases-en-java/)
- [Herencia en Java](/herencia-en-java/)
- [Polimorfismo en Java](/polimorfismo-en-java/)
- [Enlaces sobre POO y Java](/enlaces-poo-java/)
- [Ejercicios de programación orientada a objetos](/ejercicios-programacion-orientada-objetos/)
