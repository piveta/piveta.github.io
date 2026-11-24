---
layout: post
title: "Variabili e tipi in Java"
date: 2026-11-24
lang: it
translation_id: variaveis-tipos-java
permalink: /it/variables-and-types-in-java/
share_text: >-
  Dichiarazioni, inferenza con var, tipi primitivi e tipi riferimento.
---

Una variabile locale ha un nome, un tipo e un ambito. Deve ricevere un valore prima di essere usata, perché Java non assegna valori predefiniti alle variabili locali.

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

Se la dichiarazione esplicita il tipo della lista, `<>` consente al compilatore di dedurre l’argomento di tipo.

```java
ArrayList<Double> list = new ArrayList<>();
```

Con `var` il tipo viene dedotto dall’inizializzatore, che è obbligatorio. Nell’esempio, `Double` compare nel costruttore.

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Java distingue maiuscole e minuscole. Per convenzione, classi e interfacce iniziano con la maiuscola, variabili e metodi con la minuscola. Le costanti usano maiuscole e caratteri di sottolineatura.

## Tipi primitivi

Sono `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` e `char`.

```java
void main() {
    byte b;
    short s;
    int x, y, z;
    long l;
    float f;
    double d;
    boolean test;
    char c;
}
```

È possibile inizializzarli con valori letterali. `L` indica un `long` e `f` un `float`.

```java
void main() {
    byte b = 10;
    short s = 20;
    int x = 10, y = 20, z = 30;
    long l = 100L;
    float f = 12.3f;
    double d = 20.45;
    boolean test = true;
    char c = 'a';
}
```

I prefissi `0b` e `0x` indicano interi binari ed esadecimali.

## Tipi riferimento

Classi, interfacce, enumerazioni, record e array sono tipi riferimento. Un letterale `String` è racchiuso tra virgolette doppie.

```java
void main() {
    String s = "This is a string...";
}
```

Le classi wrapper rappresentano valori primitivi come oggetti. Gli altri esempi del capitolo usano spesso l’API delle collezioni.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
