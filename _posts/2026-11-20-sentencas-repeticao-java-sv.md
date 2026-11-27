---
layout: post
title: "Loopar i Java"
date: 2026-11-20
lang: sv
translation_id: sentencas-repeticao-java
permalink: /sv/loops-in-java/
share_text: >-
  for, for-each, while och do-while med exempel på räkning och summering.
---

Huvudet på en `for`-loop innehåller initiering, villkor och uppdatering. Exemplet skriver ut 1 till 5.

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

Nästa `for` summerar serien `1/1 + 4/2 + 7/3 + … + 100/34`. Täljaren ökar med tre och nämnaren med ett.

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

Summan är `93.76358001910911`. `String.format` kan visa två decimaler enligt standardinställningen för språk och region.

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

`Locale.US` använder en punkt som decimaltecken.

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

## Iterera med for-each

Loopen kör kroppen en gång för varje element i en array eller ett `Iterable`.

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

Nästa exempel går igenom en lista med namn.

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

## while och do-while

`while` testar villkoret före varje varv.

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

`do-while` testar villkoret efter kroppen. Kroppen körs därför minst en gång.

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

Alla tre looparna som summerar serien ger samma resultat.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
