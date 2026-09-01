---
layout: post
title: "Clases de excepción en Java"
date: 2026-08-27
lang: es
translation_id: classes-de-excecao
permalink: /es/clases-de-excepcion/
image: /images/descendentesThrowable.png
---
Durante la ejecución de programas, pueden ocurrir situaciones que requieren algún tratamiento especial. Estas pueden representar condiciones anormales o erróneas, situaciones que no fueron previstas por el programador o incluso flujos alternativos de ejecución. Estas condiciones se denominan **excepciones**.

En Java, las excepciones se representan mediante objetos pertenecientes a la clase `Throwable` o a alguna de sus subclases. La jerarquía de excepciones es importante para comprender qué excepciones pueden ser lanzadas, capturadas y tratadas por los programas.

## Throwable

`Throwable` es la clase base de la jerarquía de excepciones en Java. Los objetos de esta clase almacenan información sobre una determinada ocurrencia y permiten que esa información sea transferida desde el punto en que ocurrió la excepción hasta el código responsable de su tratamiento.

Solo los objetos pertenecientes a `Throwable` o a una de sus subclases pueden ser lanzados por la JVM o por el programador mediante `throw`. Del mismo modo, una cláusula `catch` solo puede capturar objetos de esta jerarquía.

Entre los principales métodos de `Throwable` se encuentran `getMessage()`, que permite obtener el mensaje asociado a la excepción, y `printStackTrace()`, que muestra el rastreo de la pila de ejecución hasta el punto en que ocurrió la excepción.

La clase `Throwable` tiene dos subclases directas: `Exception` y `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Jerarquía de Throwable"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

La clase `Error` representa condiciones graves de las que, en general, una aplicación no puede recuperarse. Son situaciones anormales que normalmente no deberían ocurrir durante la ejecución de un programa.

Algunas subclases importantes de `Error` son `AssertionError`, `IOError` y `VirtualMachineError`. Esta última posee, entre otras, subclases como `InternalError`, `OutOfMemoryError`, `StackOverflowError` y `UnknownError`.

Los errores pueden ser lanzados por la propia JVM, muchas veces como consecuencia de condiciones detectadas por el sistema operativo o por el entorno de ejecución. También pueden ser producidos explícitamente por el programador, por ejemplo, mediante `assert` o `throw`.

<img src="/images/exceptionsError.png"
     alt="Error y sus subclases"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

La clase `Exception` representa excepciones que, en determinadas situaciones, pueden ser tratadas y de las que la aplicación puede recuperarse.

Entre sus subclases se encuentran `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException` y `RuntimeException`.

Las excepciones de `Exception` que no son subclases de `RuntimeException` se denominan **excepciones verificadas** (*checked exceptions*). El compilador exige que sean consideradas explícitamente por el programa. Esto puede hacerse capturando la excepción con una cláusula `catch` o declarando, mediante `throws`, que el método puede lanzarla.

<img src="/images/descendentesException.png"
     alt="Exception y sus subclases"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

Entre las subclases de `Exception`, destaca `RuntimeException`. Esta y sus subclases se denominan **excepciones en tiempo de ejecución**.

`RuntimeException` y sus subclases son excepciones no verificadas (*unchecked exceptions*). El compilador no exige que sean tratadas explícitamente con `try`/`catch` ni que sean declaradas mediante `throws`.

Este tipo de excepción normalmente representa errores lógicos o usos incorrectos de un programa. Algunos ejemplos comunes son:

- `ClassCastException`: ocurre cuando no es posible realizar una conversión explícita de tipos.
- `IllegalArgumentException`: indica que un método recibió un argumento considerado inválido o inadecuado.
- `IndexOutOfBoundsException`: ocurre cuando se intenta acceder a una posición inexistente de una estructura indexada.
- `NullPointerException`: ocurre cuando se realiza una operación sobre una referencia `null`.

Un método que puede lanzar una `RuntimeException` no necesita declarar esta posibilidad mediante `throws`. Naturalmente, aún es posible capturar y tratar estas excepciones con `try` y `catch`.

En la práctica, muchas `RuntimeException` indican problemas que podrían evitarse mediante el propio programa. Cuando ocurre una de ellas, normalmente es importante investigar su causa y corregir el problema en lugar de simplemente capturar la excepción.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException y sus subclases"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">
     
## Excepciones verificadas y no verificadas

Una distinción importante en la jerarquía de excepciones de Java es entre excepciones **verificadas** y **no verificadas**.

`Throwable` y todas sus subclases que no son subclases de `RuntimeException` o `Error` se denominan **excepciones verificadas**. Por otro lado, `RuntimeException` y sus subclases, así como `Error` y sus subclases, se denominan **excepciones no verificadas**.

Las excepciones verificadas deben ser tratadas o declaradas explícitamente por el programa. Esto significa que, cuando un método puede lanzar una excepción verificada, esta debe ser tratada por una cláusula `catch` o declarada en la cláusula `throws` del método.

Por otro lado, las excepciones no verificadas no necesitan ser tratadas ni declaradas explícitamente. El compilador no exige que `RuntimeException`, `Error` o sus subclases sean capturadas o declaradas.

De forma simplificada, podemos visualizar la jerarquía de la siguiente manera:

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

Esta organización permite que el tratamiento se realice en diferentes niveles de la jerarquía. Una cláusula `catch` puede, por ejemplo, capturar una excepción específica o una de sus superclases, dependiendo del comportamiento deseado.

Conocer esta jerarquía es fundamental para comprender el mecanismo de tratamiento de excepciones en Java y para decidir qué excepciones deben ser tratadas, cuáles deben ser propagadas y cuáles representan errores que deben corregirse en el propio programa.

Este artículo es una adaptación de contenido del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.
