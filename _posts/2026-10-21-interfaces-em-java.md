---
layout: post
title: "Interfaces em Java"
date: 2026-10-21
lang: pt-BR
translation_id: interfaces-em-java
permalink: /interfaces-em-java/
share_text: >-
  O artigo explica como declarar e implementar interfaces em Java, incluindo métodos padrão e o desacoplamento entre contratos e implementações.
---

Em Java, as interfaces são definidas de maneira similar às classes.
Normalmente, as interfaces não contém atributos ou métodos, embora
recentemente tenha sido adicionado suporte para métodos padrão
(*default*), que já têm uma implementação pré-definida na interface.
Desta forma, as classes que implementam a interface podem decidir se
modificam ou não o método padrão.

Uma interface é definida pela palavra chave `interface` e pode, por sua
vez, herdar de outras interfaces. Para interfaces é permitida a herança
múltipla (a interface `List`, que representa listas em Java, por
exemplo, estende as interfaces `Collection` e `Iterable`, que
representam coleções e elementos iteráveis, respectivamente).

O exemplo a seguir mostra a definição de uma interface chamada `IConta`
(linha ), que define que
as classes que a implementam devem conter a implementação de ao menos
dois métodos: `sacar` e `transferir` (linhas
 e
,
respectivamente).

``` java
public interface IConta{
    public void sacar(Double valor);
    public void transferir(Conta destino, Double valor);
}
```

Ao implementarmos a interface `IConta` na classe `Conta`, todas as
subclasses de `Conta` herdam os métodos e, desta forma, estão de acordo
com a interface. O exemplo a seguir mostra a declaração que define que
`Conta` implementa `IConta` (linha
) e a
implementação dos métodos `sacar` e `transferir` (linhas
 e
,
respectivamente). Neste exemplo específico, estamos implementando os
métodos da interface em uma classe `Conta` concreta. Desta forma, as
subclasses de `Conta` não precisam implementar esses dois métodos.

``` java
public class Conta implements IConta{
    private Double saldo;
    public Double getSaldo(){
        return saldo;
    }
    public void setSaldo(Double saldo){
        this.saldo = saldo;
    }
    // Implementação concreta de sacar
    public void sacar(Double valor){
        setSaldo(getSaldo() - valor);
    }
    public void depositar(Double valor){
        setSaldo(getSaldo() + valor);
    }
    // Implementação concreta de transferir
    public void transferir(Conta destino, Double valor){
        this.sacar(valor);
        destino.depositar(valor);
    }
}
```

Outra alternativa seria mover a implementação dos métodos `sa­car`,
`de­po­si­tar` e `trans­fe­rir` para a interface `I­Con­ta`, usando métodos
`de­fault`. Para isso, é necessário declarar também os métodos `get­Sal­do`
e `set­Sal­do` na interface:

``` java
public interface IConta{
    public Double getSaldo();
    public void setSaldo(Double saldo);
    public default void sacar(Double valor){
        setSaldo(getSaldo() - valor);
    }
    public default void transferir(IConta destino,
        Double valor) {
        destino.depositar(valor);
        this.sacar(valor);
    }
    public default void depositar(Double valor){
        setSaldo(getSaldo() + valor);
    }
}
```

E a classe `Conta` simplificada ficaria:

``` java
public class Conta implements IConta{
    private Double saldo;

    public Double getSaldo(){
        return saldo;
    }
    public void setSaldo(Double saldo){
        this.saldo = saldo;
    }
    public Conta(Double valor){
        setSaldo(valor);
    }
}
```

Desacoplar a interface da `Conta` pode dar mais flexibilidade às classes
em relação à forma pela qual o saldo é armazenado e manipulado. Por
exemplo, no framework de coleções de Java existe a interface `List` que
define o que uma lista deve fazer. As implementações concretas de
`List`, tais como `ArrayList` e `LinkedList` fornecem diferentes
estratégias de armazenamento e acesso: a primeira usa um vetor para
armazenar os dados, enquanto a segunda usa uma lista duplamente
encadeada.

---

*Este artigo é uma adaptação de conteúdo do livro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Leia também

- [Conceitos Básicos](/conceitos-basicos-poo-java/)
- [Classes em Java](/classes-em-java/)
- [Herança em Java](/heranca-em-java/)
- [Polimorfismo em Java](/polimorfismo-em-java/)
- [Links POO - Java](/links-poo-java/)
- [Exercícios](/exercicios-poo-java/)
