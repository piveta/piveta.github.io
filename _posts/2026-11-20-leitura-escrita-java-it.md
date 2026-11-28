---
layout: post
title: "Lettura e scrittura nella console Java"
date: 2026-11-20
lang: it
translation_id: leitura-escrita-java
permalink: /it/reading-and-writing-on-the-java-console/
share_text: >-
  Leggere e mostrare valori con IO, Scanner e readln.
---

In Java 25, `IO` offre `print`, `println` e `readln` per interagire con la console. L’importazione statica permette di chiamarli senza indicare la classe.

## Scrivere valori

`print` non aggiunge un a capo. `println` termina la riga.

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

Le due chiamate mostrano su una sola riga la somma di 10 e 20.

## Leggere con Scanner

`nextLine()` legge una riga e `nextInt()` un intero. Dopo l’intero, un’altra chiamata a `nextLine()` consuma il fine riga prima dell’indirizzo.

```java
import java.util.Scanner;
void main(){
    var s = new Scanner(System.in);
    IO.println("Name: ");
    var name = s.nextLine(); 
    IO.println("Age: ");
    var age = s.nextInt(); 
    s.nextLine(); // Consumes the line break
    IO.println("Address: ");
    var address = s.nextLine(); 
    IO.println("Entered data:");
    IO.println("Name: " + name + ", Age: " + age);
    IO.println("Address: " + address);
}
```

## Leggere con IO.readln

`readln` mostra un messaggio di richiesta e restituisce una `String`. `Integer.parseInt` converte in intero il testo dell’età.

```java
import static java.lang.IO.*; 
void main(){
    var name = readln("Name: ");
    var age = Integer.parseInt(readln("Age: ")); 
    var address = readln("Address: ");
    println("Entered data:");
    println("Name: " + name + ", Age: " + age);
    println("Address: " + address);
}
```

Se il testo non è un intero valido, viene generata una `NumberFormatException`. L’esempio non la gestisce. La console è utile per esercitarsi. Altre applicazioni usano moduli e interfacce grafiche.

I commenti su una riga iniziano con `//`. Quelli su più righe sono delimitati da `/*` e `*/`.

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

Gli esempi con file sorgente compatti possono richiedere funzionalità in anteprima.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
