---
layout: post
title: "Boucles en Java"
date: 2026-11-20
lang: fr
translation_id: sentencas-repeticao-java
permalink: /fr/loops-in-java/
share_text: >-
  Exemples de comptage et de sommes avec for, for-each, while et do-while.
---

Une boucle `for` regroupe initialisation, condition et mise à jour. Cet exemple affiche les nombres de 1 à 5 :

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

Un autre `for` calcule la série `1/1 + 4/2 + 7/3 + … + 100/34` :

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

Le résultat est `93.76358001910911`. `String.format` peut afficher deux décimales avec la locale par défaut :

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

Avec `Locale.US`, le séparateur décimal est le point :

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

La boucle for-each parcourt chaque élément d’un tableau ou d’un `Iterable` :

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

Elle peut également parcourir une liste de noms :

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

`while` vérifie sa condition avant chaque itération :

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

`do-while` la vérifie après le corps, qui s’exécute donc au moins une fois :

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

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
