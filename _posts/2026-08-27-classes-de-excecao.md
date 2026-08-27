---
layout: post
title: "Classes de exceção"
date: 2026-08-27
---

Esta seção descreve as classes básicas de exceções de Java, iniciando pela classe `Throwable`. A seguir, são descritas, respectivamente, as classes `Error`, `Exception` e `RuntimeException`.

## `Throwable`

Em Java, exceções são representadas através de objetos descendentes, direta ou indiretamente, da classe `Throwable`. Tais objetos são usados para armazenar informações acerca de uma determinada exceção e passam dados desde o ponto em que ocorreu a exceção até o seu bloco de tratamento.

Apenas objetos desta classe, ou de suas subclasses, podem ser lançados pela JVM ou pelo programador, via `throw`. Tais objetos também são os únicos que podem ser capturados por uma cláusula `catch`. Os construtores de `Throwable`, além do construtor padrão, permitem que seja informada uma mensagem e, opcionalmente, uma causa da exceção. No caso de exceções encadeadas, a causa é um objeto `Throwable` também.

Dentre os principais métodos de `Throwable` estão `getMessage`, que obtém a mensagem associada à exceção, e `printStackTrace`, que mostra o rastreamento da pilha de execução, que ajuda a entender as chamadas feitas até a ocorrência da exceção.

A classe `Throwable` possui, originalmente, duas subclasses diretas: `Error` e `Exception`.

A figura a seguir mostra a hierarquia das principais **classes de exceção**, nome dado a `Throwable` e suas descendentes, em Java.

<iframe src="{{ '/images/descendentesThrowable.pdf' | relative_url }}"
        width="100%"
        height="600"
        style="border: none;">
</iframe>

*Figura 1 — `Throwable` e suas descendentes.*

## `Error`

A classe `Error` é usada para representar objetos de todas as exceções para as quais os programas de usuários possivelmente não são capazes de se recuperar. Tais exceções são tipicamente condições anormais que supostamente não deveriam acontecer. Esta classe e suas subclasses são coletivamente conhecidas como **classes de erro**.

A figura a seguir mostra a classe `Error` e algumas de suas subclasses, incluindo `AssertionError`, `IOError` e `VirtualMachineError`, que representam, respectivamente, falhas em asserções, falhas graves de entrada e/ou saída, e problemas com a JVM ou com a alocação de recursos.

Entre as subclasses de `VirtualMachineError` estão `InternalError`, `OutOfMemoryError`, `StackOverflowError` e `UnknownError`.

<iframe src="{{ '/images/exceptionsError.pdf' | relative_url }}"
        width="100%"
        height="600"
        style="border: none;">
</iframe>

*Figura 2 — `Error` e suas descendentes.*

Quem lança os erros é a JVM, muitas vezes motivada pelo sistema operacional, ou o usuário, via `assert` ou `throw`.

## `Exception`

Já a classe `Exception` é usada para representar objetos de todas as exceções para as quais os programas de usuários podem querer se recuperar. Dentre as mais utilizadas estão `ApplicationException`, `ClassNotFoundException`, `IOException`, `SQLException` e `RuntimeException`.

`Exception` e suas descendentes que não estendem `RuntimeException` são chamadas de **exceções verificadas** e precisam ser gerenciadas explicitamente pelos programas, através de sentenças `try` ou por cláusulas `throws` em métodos, por exemplo.

A figura a seguir mostra algumas das subclasses de `Exception`, bem como a quantidade de classes adicionais.

<iframe src="{{ '/images/descendentesException.pdf' | relative_url }}"
        width="100%"
        height="600"
        style="border: none;">
</iframe>

*Figura 3 — `Exception` e algumas de suas descendentes verificadas.*

Há cerca de oitenta exceções listadas na documentação da linguagem como descendentes diretas de `Exception`.

## `RuntimeException`

Dentre as subclasses de `Exception`, destaca-se `RuntimeException`. A classe `RuntimeException` e suas subclasses são denominadas, pela especificação da linguagem, **classes de exceção em tempo de execução**.

Classes de erro e classes de exceção em tempo de execução são consideradas como **exceções não verificadas** pelo compilador e não precisam ser tratadas ou consideradas explicitamente pelos programadores.

`RuntimeException` é utilizada para representar exceções não verificadas causadas por erros lógicos ou por uso incorreto de programas, e não por falhas do ambiente de execução. A biblioteca padrão da linguagem fornece mais de cinquenta subclasses de `RuntimeException`. Algumas das mais utilizadas são `ClassCastException`, `IllegalArgumentException`, `IndexOutOfBoundsException` e `NullPointerException`.

Métodos que podem lançar uma `RuntimeException` não precisam envolver o código em uma sentença `try` ou usar uma sentença `throws` para informar que o método lança a exceção. No entanto, é possível capturar tais exceções e tratá-las usando uma sentença `try` que contenha uma cláusula `catch` que capture tais exceções.

Tipicamente, exceções do tipo `RuntimeException` são evitáveis programaticamente (normalmente são erros de programação). Logo, comumente, quando ocorrem, deve-se procurar a causa de sua ocorrência e efetuar a correção.

Dentre as principais subclasses de `RuntimeException` estão:

- **`ClassCastException`**: lançada quando há um erro de conversão explícita de tipos (os tipos não são compatíveis para que a conversão ocorra). É um caso típico de problemas com o uso de herança ou com o uso de coleções legadas, sem tipos genéricos.

- **`NullPointerException`**: lançada quando tentamos acessar uma referência nula. Por exemplo, ao chamar `veiculo.ligar()`, quando `veiculo` contém `null`.

- **`IllegalArgumentException`**: é usada quando um método recebe um parâmetro considerado ilegal ou inapropriado. Comumente usada para verificar valores fora de uma faixa predeterminada, dentre outras coisas. Por exemplo, tentar informar uma idade negativa ou maior que o esperado (ex.: 150 anos) para uma pessoa. Nesse caso, o programador testa os limites dentro do método e, caso o valor não esteja de acordo, lança uma exceção com uma cláusula `throw`.

A figura a seguir mostra a classe `RuntimeException` e algumas de suas descendentes.

<iframe src="{{ '/images/descendentesRuntimeException2.pdf' | relative_url }}"
        width="100%"
        height="600"
        style="border: none;">
</iframe>

*Figura 4 — `RuntimeException` e suas descendentes.*
