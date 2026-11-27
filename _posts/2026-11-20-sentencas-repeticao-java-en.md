---
layout: post
title: "Loops in Java"
date: 2026-11-20
lang: en
translation_id: sentencas-repeticao-java
permalink: /en/loops-in-java/
share_text: >-
  for, for-each, while, and do-while with the book's counting and series examples.
---

Loops repeat a statement or a block. A counting `for` places its initialization, condition, and update in the header. This example prints the numbers from 1 through 5:

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

The book uses another `for` to add the series `1/1 + 4/2 + 7/3 + … + 100/34`. The numerator increases by three each time, and the denominator by one:

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

The result printed is `93.76358001910911`. `String.format("%.2f", sum)` can display two decimal places using the default locale; `Locale.US` uses a period as the decimal separator:

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

## Visiting elements with `for-each`

**For-each** executes its body once for each element in an array or an `Iterable`. The book first traverses an integer array:

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

It then traverses a list of names:

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

## `while` and `do-while`

`while` checks its condition before each iteration. The same series can be added this way:

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

`do-while` checks the condition **after** the body and therefore executes the body at least once. The book presents the series again in this form:

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

All three series loops produce the same result; the time of the condition check and the form of the update help determine which loop suits a given task.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
