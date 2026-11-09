---
layout: post
title: "Clases en Java"
date: 2026-10-21
lang: es
translation_id: classes-em-java
permalink: /clases-en-java/
share_text: >-
  Aprende a definir clases, campos, métodos, constructores y encapsulación en Java.
---

Java admite los principales conceptos de la programación orientada a objetos, entre ellos clases, campos, métodos, herencia, interfaces, polimorfismo y encapsulación.

## Clases, campos y métodos

En Java, una clase se declara con la palabra clave `class`, un nombre y un cuerpo en el que se pueden definir campos y métodos. Más adelante se explican otros componentes opcionales. Consideremos una clase llamada `Account`. Podemos hacerla pública para que otras clases puedan acceder a ella:

```java
public class Account {
    // Cuerpo de la clase
}
```

Podemos añadir campos y métodos al cuerpo de la clase. En el siguiente ejemplo añadimos un campo `balance` de tipo `Double`[^2] y un método `withdraw`, que no devuelve ningún valor (`void`) y recibe un parámetro formal llamado `amount`, también de tipo `Double`. El método resta del saldo la cantidad recibida como argumento:

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // o balance -= amount;
    }
}
```

Del mismo modo, podemos añadir un método `deposit` que aumenta el saldo de la cuenta:

```java
public class Account {
    // Se omiten balance y withdraw
    public void deposit(Double amount) {
        balance = balance + amount; // o balance += amount;
    }
}
```

Consideremos un cliente que realiza algunas operaciones en una cuenta. Primero crea un objeto `Account` llamando a su constructor y asigna la referencia a una variable llamada `account`. Luego establece el saldo en 100.00, retira 50.00, deposita 100.00 e imprime el saldo:

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

La salida es:

```text
Balance: 150.0
```

Los métodos `withdraw` y `deposit` necesitan un objeto `Account` para ser invocados porque son métodos de instancia. En las versiones recientes de Java, `main` también puede ser un método estático o de instancia, como en este ejemplo[^3].

El ejemplo anterior muestra un cliente que utiliza campos y métodos de `Account`. El cliente está en una clase sin nombre declarada de forma implícita. Sin embargo, accede directamente a `balance`, lo que crea un acoplamiento estrecho entre las clases. Esto suele ser indeseable[^4]. Una alternativa es encapsular el acceso a `balance`, de modo que las lecturas y escrituras se realicen mediante métodos específicos. Así se reduce el acoplamiento y se permite cambiar más adelante la representación interna del saldo, siempre que se mantengan disponibles las operaciones de lectura y escritura. También es recomendable reducir la visibilidad del campo para que solo se pueda acceder a él desde dentro de la clase.

Java ofrece visibilidad de paquete (la opción predeterminada), `private`, `public` y `protected`. Estos niveles determinan qué clases pueden acceder a un campo o método. Cada nivel tiene una palabra clave asociada, excepto la visibilidad de paquete, que no utiliza ninguna.

El siguiente código mejora la encapsulación y oculta el estado interno de la clase a sus clientes. Añade métodos públicos de lectura y escritura (`getBalance` y `setBalance`), cambia la visibilidad de `balance` a `private` y actualiza el saldo mediante esos métodos. La referencia `this` distingue el campo `balance` del parámetro del método con el mismo nombre. `this.balance` se refiere al campo, no al parámetro:

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

El cliente también cambia para modificar el saldo mediante el método setter:

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Cuando no se declara ningún constructor explícito, las clases Java tienen un constructor predeterminado sin parámetros. Podemos definir otros constructores para facilitar el uso de la clase por parte de los clientes. Por ejemplo, este constructor de `Account` acepta una cantidad inicial y establece con ella el saldo. Si fuera necesario llamar al constructor de una superclase, podríamos usar `super`:

```java
public class Account {
    // Campos y métodos de Account
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

Ahora el cliente debe usar el nuevo constructor y proporcionar un saldo inicial, porque `Account` ya no tiene un constructor predeterminado sin argumentos[^5]:

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java no tiene métodos destructores. Los objetos que ya no tienen referencias se recolectan automáticamente mediante el recolector de basura.

[^2]: Aquí se usa `Double` por simplicidad. Los valores monetarios normalmente no se almacenan en variables de punto flotante, sino en tipos enteros como `long` o en `BigDecimal`.

[^3]: Consulta [JEP 512](https://openjdk.org/jeps/512).

[^4]: Aquí, «las clases» se refiere a `Account` y a la clase sin nombre declarada implícitamente que contiene `main`.

[^5]: Al definir un constructor, la clase deja de tener un constructor predeterminado. Si hace falta, también se puede definir un constructor sin argumentos.

---

*Este artículo adapta contenido del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artículos relacionados

- [Conceptos básicos de orientación a objetos](/conceptos-basicos-de-poo/)
- [Herencia en Java](/herencia-en-java/)
- [Polimorfismo en Java](/polimorfismo-en-java/)
- [Interfaces en Java](/interfaces-en-java/)
- [Enlaces sobre POO y Java](/enlaces-poo-java/)
- [Ejercicios de programación orientada a objetos](/ejercicios-programacion-orientada-objetos/)
