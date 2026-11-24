---
layout: post
title: "Constructores en Java"
date: 2026-11-24
lang: es
translation_id: construtores-java
permalink: /es/constructors-in-java/
share_text: "Constructores en Java"
---

Un constructor inicializa un objeto cuando se crea. En la clase `Account` del libro, el constructor recibe el saldo inicial y lo establece con `setBalance`. El primer fragmento omite los demás atributos y métodos.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

Con `new Account(100.00)`, el cliente crea una cuenta con saldo 100, retira 50 y deposita 100. El saldo que se muestra es `150.0`.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

El compilador proporciona un constructor predeterminado cuando una clase ordinaria no declara ninguno. Al declarar `Account(Double value)`, ese constructor implícito deja de estar disponible. Para admitir también `new Account()`, declara un constructor sin argumentos de forma explícita. Una subclase no hereda los constructores de `Account`, pero puede invocar uno mediante `super(value)`.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Artículo basado en [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

