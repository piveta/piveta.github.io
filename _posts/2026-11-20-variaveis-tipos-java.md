---
layout: post
title: "Variáveis e tipos em Java"
date: 2026-11-20
lang: pt-BR
translation_id: variaveis-tipos-java
permalink: /variaveis-tipos-java/
share_text: >-
  Declaração, inferência com var, tipos primitivos e tipos de referência nos exemplos do capítulo inicial.
---

Uma variável tem nome, tipo e escopo. Aqui tratamos das **variáveis locais**, declaradas no corpo de um método. Elas precisam receber um valor antes de serem usadas; Java não atribui um valor padrão às variáveis locais.

Estas declarações do livro mostram uma `String`, um `int` e uma lista de `Double`:

```java
void main(){
    String nome = "Maria";
    int i = 10;
    ArrayList<Double> lista = new ArrayList<Double>();
}
```

Quando a declaração já informa o tipo da lista, o construtor pode inferir seu argumento de tipo com `<>`:

```java
ArrayList<Double> lista = new ArrayList<>();
```

Com `var`, o compilador infere o tipo da variável pela expressão de inicialização, que passa a ser obrigatória. No caso da lista, o construtor precisa indicar `Double`, pois a declaração não fornece mais essa informação:

```java
var nome = "Maria";
var i = 10;
var lista = new ArrayList<Double>();
```

Pela convenção usada em Java, classes e interfaces começam com maiúscula; variáveis e métodos, com minúscula; constantes usam maiúsculas e sublinhados. Nomes diferenciam letras maiúsculas de minúsculas.

## Tipos primitivos

Os primitivos incluem `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` e `char`. O livro primeiro declara variáveis desses tipos:

```java
void main() {
    byte b;
    short s;
    int x, y, z;
    long l;
    float f;
    double d;
    boolean teste;
    char c;
}
```

Valores literais podem inicializá-las diretamente. O sufixo `L` marca um literal `long` e `f` marca um `float`:

```java
void main() {
    byte b = 10;
    short s = 20;
    int x = 10, y = 20, z = 30;
    long l = 100L;
    float f = 12.3f;
    double d = 20.45;
    boolean teste = true;
    char c = 'a';
}
```

Os inteiros também admitem literais binários (`0b`) e hexadecimais (`0x`). Entre os tipos numéricos, `int` e `double` são escolhas frequentes nos exemplos do capítulo.

## Tipos de referência

Classes, interfaces, enumerações, registros e vetores são tipos de referência. Uma `String` pode ser criada com aspas duplas:

```java
void main() {
    String s = "Esta é uma string...";
}
```

Java também oferece classes *wrapper* para representar valores primitivos como objetos. O capítulo menciona vetores e matrizes, mas deixa seu estudo detalhado para outros contextos; a API de coleções é usada com mais frequência nos exemplos do livro.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
