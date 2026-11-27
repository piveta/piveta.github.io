---
layout: post
title: "Schleifen in Java"
date: 2026-11-20
lang: de
translation_id: sentencas-repeticao-java
permalink: /de/loops-in-java/
share_text: >-
  for, for-each, while und do-while anhand von Zähl- und Summenbeispielen.
---

Eine Zählschleife mit `for` enthält Initialisierung, Bedingung und Aktualisierung im Kopf. Dieses Beispiel gibt 1 bis 5 aus.

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

Die Reihe lautet `1/1 + 4/2 + 7/3 + … + 100/34`. Der Zähler wächst jeweils um drei und der Nenner um eins.

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

Die Summe beträgt `93.76358001910911`. `String.format` kann sie mit zwei Dezimalstellen und der voreingestellten Locale anzeigen.

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

Mit `Locale.US` erscheint ein Punkt als Dezimaltrennzeichen.

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

## Elemente mit for-each durchlaufen

Die erweiterte `for`-Schleife führt ihren Körper einmal pro Element eines Arrays oder `Iterable` aus.

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

Das zweite Beispiel durchläuft eine Liste von Namen.

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

## while und do-while

`while` prüft die Bedingung vor jedem Durchlauf.

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

`do-while` prüft die Bedingung am Ende. Der Schleifenkörper läuft daher mindestens einmal.

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

Alle drei Varianten zur Berechnung der Reihe liefern dieselbe Summe.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
