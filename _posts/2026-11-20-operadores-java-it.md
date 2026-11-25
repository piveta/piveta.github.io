---
layout: post
title: "Operatori in Java"
date: 2026-11-20
lang: it
translation_id: operadores-java
permalink: /it/operators-in-java/
share_text: >-
  Operatori aritmetici, di assegnazione e di confronto con gli esempi del libro.
---

## Operatori aritmetici

`+`, `-`, `*`, `/` e `%` indicano somma, sottrazione, moltiplicazione, divisione e resto. La precedenza determina il raggruppamento delle operazioni. `++` e `--` modificano una variabile di un’unità.

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

In `y = x++`, `y` riceve il valore precedente, 10. Poi `x` diventa 11.

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

In `y = ++x`, l’incremento avviene prima dell’assegnazione. Entrambe le variabili valgono 11.

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Altri operatori unari sono `+`, `-`, `~` e `!`.

## Assegnazione

`=` assegna alla variabile a sinistra il valore dell’espressione a destra.

```java
int age;
String name;
Double height;
```

L’assegnazione può seguire la dichiarazione.

```java
age = 20;
name = "Mary";
height = 1.70;
```

Oppure si può inizializzare una variabile nella dichiarazione.

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

## Assegnazione composta

`+=`, `-=`, `*=`, `/=` e `%=` combinano un’operazione con l’assegnazione.

```java
void main() {
    int a = 10;
    a += 10;
    IO.println("a = " + a);
    a -= 10;
    IO.println("a = " + a); 
    a *= 10;
    IO.println("a = " + a); 
    a /= 10;
    IO.println("a = " + a); 
    a %= 3;
    IO.println("a = " + a); 
}
```

I valori vengono mostrati in quest’ordine.

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

L’assegnazione composta tiene conto del tipo dell’espressione a sinistra e la valuta una sola volta. Esistono forme composte anche per gli spostamenti e le operazioni sui bit.

## Confronti

`==`, `!=`, `>`, `>=`, `<` e `<=` producono un valore booleano.

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age == 10)
        IO.println("Age equals 10 years");
    if (age != 20)
        IO.println("Age differs from 20 years");
    if (age > 30)
        IO.println("Age is over 30 years");
    if (age <= 80)
        IO.println("Age is at most 80 years");
}
```

Immettendo 10, risultano vere tre condizioni perché gli `if` sono indipendenti. `Integer.parseInt` converte il testo letto in un intero.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
