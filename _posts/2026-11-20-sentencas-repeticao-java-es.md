---
layout: post
title: "Bucles de repetición en Java"
date: 2026-11-20
lang: es
translation_id: sentencas-repeticao-java
permalink: /es/loops-in-java/
share_text: >-
  for, for-each, while y do-while con ejemplos de conteo y sumas del libro.
---

Los bucles repiten una sentencia o un bloque. En un `for`, la inicialización, la condición y la actualización aparecen en la cabecera. Este ejemplo imprime del 1 al 5:

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

El libro utiliza otro `for` para sumar la serie `1/1 + 4/2 + 7/3 + … + 100/34`: el numerador aumenta de tres en tres y el denominador de uno en uno:

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

El resultado es `93.76358001910911`. `String.format("%.2f", sum)` puede mostrar dos decimales con la configuración regional predeterminada:

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

Con `Locale.US`, el separador decimal es el punto:

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

El **for-each** ejecuta su cuerpo una vez por cada elemento de un arreglo o de un `Iterable`. El libro recorre primero un arreglo de enteros:

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

Después recorre una lista de nombres:

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

El bucle `while` comprueba la condición antes de cada iteración. La misma serie puede sumarse así:

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

`do-while` comprueba la condición después del cuerpo y, por tanto, lo ejecuta al menos una vez:

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

Los tres bucles de la serie producen el mismo resultado. El momento de comprobar la condición ayuda a elegir la construcción adecuada.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
