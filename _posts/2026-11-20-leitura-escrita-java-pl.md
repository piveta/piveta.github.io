---
layout: post
title: "Odczyt i zapis w konsoli Javy"
date: 2026-11-20
lang: pl
translation_id: leitura-escrita-java
permalink: /pl/reading-and-writing-on-the-java-console/
share_text: >-
  Odczyt i wyświetlanie wartości za pomocą IO, Scanner i readln.
---

W Javie 25 klasa `IO` udostępnia `print` i `println` do wyświetlania oraz `readln` do odczytu. Import statyczny pozwala wywoływać je bez nazwy klasy.

## Wyświetlanie wartości

`print` nie dodaje znaku końca wiersza. `println` kończy wiersz.

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

Wynik dodawania 10 i 20 pojawia się w jednym wierszu.

## Odczyt za pomocą Scanner

`nextLine()` odczytuje wiersz tekstu, a `nextInt()` liczbę całkowitą. Dodatkowe `nextLine()` usuwa pozostawiony znak końca wiersza przed odczytem adresu.

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

## Odczyt za pomocą IO.readln

`readln` wyświetla komunikat i zwraca `String`. `Integer.parseInt` zamienia tekst opisujący wiek na liczbę całkowitą.

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

Niepoprawny tekst powoduje wyjątek `NumberFormatException`, którego przykład nie obsługuje. Konsola służy do nauki, a aplikacje mogą korzystać z formularzy i interfejsów graficznych.

Komentarz jednowierszowy zaczyna się od `//`. Wielowierszowy umieszcza się między `/*` i `*/`.

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

Przykłady ze zwartymi plikami źródłowymi mogą wymagać włączenia funkcji eksperymentalnych.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
