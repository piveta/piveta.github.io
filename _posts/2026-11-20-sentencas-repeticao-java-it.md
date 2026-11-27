---
layout: post
title: "Cicli in Java"
date: 2026-11-20
lang: it
translation_id: sentencas-repeticao-java
permalink: /it/loops-in-java/
share_text: >-
  for, for-each, while e do-while con esempi di conteggio e di somma.
---

Nel ciclo `for` l’intestazione contiene inizializzazione, condizione e aggiornamento. L’esempio stampa da 1 a 5.

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

Un altro `for` somma la serie `1/1 + 4/2 + 7/3 + … + 100/34`. Il numeratore aumenta di tre e il denominatore di uno.

```java
void main(){
    double sum = 0.0;
    for (int numerator = 1, denominator = 1; 
         numerator <= 100;
         numerator += 3, denominator++)
        sum += (double) numerator / denominator;
    IO.println("Sum: " + sum);
}
```

La somma è `93.76358001910911`. `String.format` può mostrare due decimali secondo le impostazioni locali.

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

`Locale.US` usa il punto come separatore decimale.

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

## Iterazione con for-each

Il corpo del ciclo viene eseguito una volta per ogni elemento di un array o di un `Iterable`.

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

Si può scorrere anche una lista di nomi.

```java
void main() {
    // Creates a list of people's names
    var people = new ArrayList<String>();
    people.add("Mary");
    people.add("Peter");
    people.add("Paul");
    // Iterates over the collection, displaying names
    for (var p : people)
        IO.println("Person's name: " + p);
}
```

## while e do-while

`while` controlla la condizione prima di ogni iterazione.

```java
void main() {
    int numerator = 1, denominator = 1;
    var sum = 0.0;
    while (numerator <= 100) {
        sum += (double) numerator / denominator;
        numerator += 3;
        denominator++;
    }
    IO.println("Sum: " + sum);
}
```

`do-while` controlla la condizione dopo il corpo, che perciò viene eseguito almeno una volta.

```java
void main() {
    int numerator = 1, denominator = 1;
    var sum = 0.0;
    do {
        sum += (double) numerator / denominator;
        numerator += 3;
        denominator++;
    } while (numerator <= 100);
    IO.println("Sum: " + sum);
}
```

I tre cicli che sommano la serie ottengono lo stesso risultato.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
