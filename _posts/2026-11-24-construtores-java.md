---
layout: post
title: "Construtores em Java"
date: 2026-11-24
lang: pt-BR
translation_id: construtores-java
permalink: /construtores-java/
share_text: "Construtores em Java"
---

Um construtor inicializa um objeto quando ele é criado. Na classe `Conta` do livro, o construtor recebe o saldo inicial e o configura com `setSaldo`. Os demais atributos e métodos da classe foram omitidos do primeiro trecho.

```java
public class Conta{
    // Atributos e métodos de Conta
    public Conta(Double valor){
        setSaldo(valor);
    }
}
```

Com `new Conta(100.00)`, o cliente cria a conta com saldo 100, saca 50 e deposita 100. O saldo impresso é `150.0`.

```java
void main(){
    var c = new Conta(100.00);
    c.sacar(50.00);
    c.depositar(100.00);
    IO.println("Saldo: " + c.getSaldo());
}
```

O compilador fornece um construtor padrão quando uma classe comum não declara nenhum construtor. Ao declarar `Conta(Double valor)`, esse construtor implícito deixa de existir. Para aceitar também `new Conta()`, declare explicitamente um construtor sem argumentos. Uma subclasse não herda construtores de `Conta`, mas pode chamar um deles com `super(valor)`.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Artigo baseado em [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

