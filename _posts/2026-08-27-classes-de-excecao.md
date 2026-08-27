---
layout: post
title: "Classes de exceção em Java"
date: 2026-08-27
---

Durante a execução de programas, podem ocorrer situações que exigem algum tratamento especial. Elas podem representar condições anormais ou errôneas, situações que não foram previstas pelo programador ou mesmo fluxos alternativos de execução. Essas condições são chamadas de **exceções**.

Em Java, as exceções são representadas por objetos pertencentes à classe `Throwable` ou a alguma de suas subclasses. A hierarquia de exceções é importante para entender quais exceções podem ser lançadas, capturadas e tratadas pelos programas.

## `Throwable`

`Throwable` é a classe-base da hierarquia de exceções em Java. Objetos dessa classe armazenam informações sobre uma determinada ocorrência e permitem que essas informações sejam transferidas desde o ponto em que a exceção ocorreu até o código responsável pelo seu tratamento.

Somente objetos pertencentes a `Throwable` ou a uma de suas subclasses podem ser lançados pela JVM ou pelo programador por meio de `throw`. Da mesma forma, uma cláusula `catch` só pode capturar objetos dessa hierarquia.

Entre os principais métodos de `Throwable` estão `getMessage()`, que permite obter a mensagem associada à exceção, e `printStackTrace()`, que mostra o rastreamento da pilha de execução até o ponto em que a exceção ocorreu.

A classe `Throwable` possui duas subclasses diretas: `Exception` e `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Hierarquia de Throwable"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## `Error`

A classe `Error` representa condições graves das quais, em geral, uma aplicação não consegue se recuperar. São situações anormais que normalmente não deveriam ocorrer durante a execução de um programa.

Algumas subclasses importantes de `Error` são `AssertionError`, `IOError` e `VirtualMachineError`. Esta última possui, entre outras, subclasses como `InternalError`, `OutOfMemoryError`, `StackOverflowError` e `UnknownError`.

Erros podem ser lançados pela própria JVM, muitas vezes em consequência de condições detectadas pelo sistema operacional ou pelo ambiente de execução. Também podem ser produzidos explicitamente pelo programador, por exemplo, por meio de `assert` ou `throw`.

<img src="/images/exceptionsError.png"
     alt="Error e suas subclasses"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## `Exception`

A classe `Exception` representa exceções que, em determinadas situações, podem ser tratadas e das quais a aplicação pode se recuperar.

Entre suas subclasses estão `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException` e `RuntimeException`.

As exceções de `Exception` que não são subclasses de `RuntimeException` são chamadas de **exceções verificadas** (*checked exceptions*). O compilador exige que elas sejam consideradas explicitamente pelo programa. Isso pode ser feito capturando a exceção com uma cláusula `catch` ou declarando, por meio de `throws`, que o método pode lançá-la.

<img src="/images/descendentesException.png"
     alt="Exception e suas descendentes"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## `RuntimeException`

Entre as subclasses de `Exception`, destaca-se `RuntimeException`. Ela e suas subclasses são chamadas de **exceções em tempo de execução**.

`RuntimeException` e suas subclasses são exceções não verificadas (*unchecked exceptions*). O compilador não exige que sejam tratadas explicitamente com `try`/`catch` nem que sejam declaradas com `throws`.

Esse tipo de exceção normalmente representa erros lógicos ou usos incorretos de um programa. Exemplos comuns incluem:

- `ClassCastException`: ocorre quando uma conversão explícita de tipos não é possível.
- `IllegalArgumentException`: indica que um método recebeu um argumento considerado inválido ou inadequado.
- `IndexOutOfBoundsException`: ocorre quando se tenta acessar uma posição inexistente de uma estrutura indexada.
- `NullPointerException`: ocorre quando uma operação é realizada sobre uma referência `null`.

Um método que pode lançar uma `RuntimeException` não precisa declarar essa possibilidade com `throws`. Naturalmente, ainda é possível capturar e tratar essas exceções com `try` e `catch`.

Na prática, muitas `RuntimeException` indicam problemas que poderiam ser evitados pelo próprio programa. Quando uma delas ocorre, normalmente é importante investigar sua causa e corrigir o problema em vez de simplesmente capturar a exceção.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException e suas descendentes"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exceções verificadas e não verificadas

Uma distinção importante na hierarquia de exceções de Java é entre exceções **verificadas** e **não verificadas**.

As exceções verificadas são subclasses de `Exception` que não pertencem à hierarquia de `RuntimeException`. Elas precisam ser tratadas ou declaradas explicitamente pelo programa.

Já as exceções não verificadas incluem tanto `RuntimeException` e suas subclasses quanto `Error` e suas subclasses. O compilador não exige seu tratamento explícito.

De forma simplificada, podemos visualizar a hierarquia da seguinte maneira:

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

Essa organização permite que o tratamento seja feito em diferentes níveis da hierarquia. Uma cláusula `catch` pode, por exemplo, capturar uma exceção específica ou uma de suas superclasses, dependendo do comportamento desejado.

Conhecer essa hierarquia é fundamental para compreender o mecanismo de tratamento de exceções em Java e para decidir quais exceções devem ser tratadas, quais devem ser propagadas e quais representam erros que precisam ser corrigidos no próprio programa.

---

*Este artigo é uma adaptação de conteúdo do livro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
