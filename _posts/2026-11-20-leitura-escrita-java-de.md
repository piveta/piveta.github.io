---
layout: post
title: "Ein- und Ausgabe in der Java-Konsole"
date: 2026-11-20
lang: de
translation_id: leitura-escrita-java
permalink: /de/reading-and-writing-on-the-java-console/
share_text: >-
  Werte mit IO und Scanner lesen und anzeigen.
---

Programme lesen Daten, verarbeiten sie und geben Ergebnisse aus. In Java 25 stellt `IO` die Methoden `print`, `println` und `readln` bereit. Der statische Import erlaubt Aufrufe ohne Klassennamen.

## Werte ausgeben

`print` hängt keinen Zeilenumbruch an. `println` beendet die Zeile.

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

`a` und `b` ergeben 30. Beide Ausgaben stehen in einer Zeile.

## Mit Scanner lesen

`nextLine()` liest Text, `nextInt()` eine ganze Zahl. Ein weiterer Aufruf von `nextLine()` verbraucht den verbleibenden Zeilenumbruch.

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

## Mit IO.readln lesen

`readln` zeigt eine Eingabeaufforderung an und gibt eine `String` zurück. `Integer.parseInt` wandelt die eingegebene Altersangabe in eine ganze Zahl um.

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

Ungültiger Text löst eine `NumberFormatException` aus, die das Beispiel nicht behandelt. Konsoleneingabe eignet sich zum Einstieg. In Anwendungen kommen auch Formulare und grafische Oberflächen zum Einsatz.

Einzeilige Kommentare beginnen mit `//`. Mehrzeilige stehen zwischen `/*` und `*/`.

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
