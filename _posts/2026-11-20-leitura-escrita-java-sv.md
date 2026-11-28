---
layout: post
title: "Inmatning och utmatning i Javas konsol"
date: 2026-11-20
lang: sv
translation_id: leitura-escrita-java
permalink: /sv/reading-and-writing-on-the-java-console/
share_text: >-
  Läs och visa värden med IO, Scanner och readln.
---

I Java 25 har `IO` metoderna `print` och `println` för utmatning och `readln` för inmatning. Statisk import gör att de kan anropas utan klassnamn.

## Visa värden

`print` lägger inte till en radbrytning. `println` avslutar raden.

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

Summan av 10 och 20 visas tillsammans med texten på en rad.

## Läs med Scanner

`nextLine()` läser en rad och `nextInt()` läser ett heltal. Ett extra anrop till `nextLine()` tar hand om radbrytningen före adressen.

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

## Läs med IO.readln

`readln` visar en uppmaning och returnerar en `String`. `Integer.parseInt` omvandlar texten för åldern till ett heltal.

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

Ogiltig inmatning orsakar `NumberFormatException`, som exemplet inte hanterar. Konsolen är praktisk för övningar. Program kan också använda formulär och grafiska gränssnitt.

Enradiga kommentarer börjar med `//`. Kommentarer på flera rader omges av `/*` och `*/`.

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

Exemplen med kompakta källfiler kan kräva att förhandsfunktioner aktiveras.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
