---
layout: post
title: "Herencia en Java"
date: 2026-10-21
lang: es
translation_id: heranca-em-java
permalink: /herencia-en-java/
share_text: >-
  Introducción a la herencia en Java, la sobrescritura de métodos, la conversión entre subtipos y las clases abstractas.
---

La **herencia** es un mecanismo de composición que permite a las clases reutilizar la interfaz y el comportamiento de clases existentes, extendiendo su funcionalidad. Una clase que extiende otra mediante herencia se denomina **subclase** de esta, y la clase extendida se denomina **superclase**.

Java permite herencia simple para las clases (la herencia múltiple está disponible para las interfaces), y las subclases son subtipos de su superclase. La herencia se declara en la subclase con la palabra clave `extends`: `Clase extends SuperClase`. Una clase sin superclase declarada explícitamente es implícitamente una subclase de `Object`, la raíz de la jerarquía de clases de Java.

Consideremos la clase `CheckingAccount` que aparece a continuación. Extiende `Account` y añade un campo, métodos para leerlo y modificarlo, y un constructor. Como `Account` no tiene un constructor sin argumentos, el constructor de `CheckingAccount` llama al constructor de la superclase mediante `super`:

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

Las subclases suelen tener **métodos sobrescritos**: métodos declarados en una superclase cuyo comportamiento una subclase amplía o reemplaza. Aquí, `CheckingAccount` sobrescribe el método `withdraw` de `Account` al declarar un método con la misma firma[^6]. Primero invoca el método de la superclase con `super` y luego calcula una comisión mediante `deductFee`, que resta del saldo el 1 % del importe de la operación:

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // Otros constructores, campos y métodos.
}
```

Por ejemplo, si una `CheckingAccount` tiene inicialmente un saldo de 100.00 y retiramos 50.00, el saldo restante es 49.50, porque se cobran 0.50 de comisión:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

Según el principio de sustitución de Liskov, podemos asignar objetos de una subclase allí donde se espera un objeto de la superclase: toda instancia de `CheckingAccount` también es una instancia de `Account`. Lo contrario no siempre es cierto, ya que un `Account` podría ser, por ejemplo, un `SavingsAccount`. En esos casos hace falta una conversión explícita (*cast*).

En el siguiente ejemplo, `checkingAccount` es de tipo `CheckingAccount` y se refiere a una instancia de esa clase. La variable `account` es de tipo `Account` y se asigna al mismo objeto. Esta asignación no requiere conversión. La asignación inversa requiere un *cast* explícito:

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // Un CheckingAccount es un Account.
checkingAccount = (CheckingAccount) account; // Cast explícito válido.
```

Supongamos que `SavingsAccount` es otra subclase de `Account`. En el ejemplo siguiente, `account` se refiere a un `CheckingAccount`. La conversión a `SavingsAccount` falla durante la ejecución porque el objeto no es un `SavingsAccount`:

```java
Account account = new CheckingAccount(100.00);
// El cast explícito siguiente falla durante la ejecución.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

Los IDE modernos advierten sobre conversiones claramente incorrectas, pero a veces el resultado no se conoce de antemano. Por ejemplo, los argumentos de un método solo se conocen cuando se lo invoca. Por eso, los *casts* incorrectos pueden causar excepciones de ejecución de tipo `ClassCastException`[^7].

Como `Account` puede tener varios subtipos, como `CheckingAccount`, `SavingsAccount` y quizá `InvestmentAccount`, podemos declararla abstracta para que solo se puedan crear instancias de sus subclases:

```java
public abstract class Account {
    // Campos y métodos comunes a todos los tipos de cuenta.
}
```

Ya no podemos instanciar `Account` directamente. Debemos usar un constructor de una de sus subclases. El ejemplo anterior puede utilizar `CheckingAccount`:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: En Java, la firma de un método consta de su nombre, sus parámetros de tipo (si los hay) y sus parámetros formales. Consulta la [especificación del lenguaje Java](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2).

[^7]: Consulta la [documentación de la API de ClassCastException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html).

---

*Este artículo adapta contenido del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artículos relacionados

- [Conceptos básicos de orientación a objetos](/conceptos-basicos-de-poo/)
- [Clases en Java](/clases-en-java/)
- [Polimorfismo en Java](/polimorfismo-en-java/)
- [Interfaces en Java](/interfaces-en-java/)
- [Enlaces sobre POO y Java](/enlaces-poo-java/)
- [Ejercicios de programación orientada a objetos](/ejercicios-programacion-orientada-objetos/)
