---
layout: post
title: "Operatoren in Java"
date: 2026-11-20
lang: de
translation_id: operadores-java
permalink: /de/operators-in-java/
share_text: >-
  Arithmetik, Zuweisung und Vergleich anhand der Buchbeispiele.
---

## Arithmetische Operatoren

`+`, `-`, `*`, `/` und `%` stehen für Addition, Subtraktion, Multiplikation, Division und Rest. Die Rangfolge bestimmt die Gruppierung. `++` und `--` ändern einen Wert um eins.

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

Bei `y = x++` erhält `y` den alten Wert 10. Danach hat `x` den Wert 11.

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Bei `y = ++x` wird zuerst erhöht. Beide Variablen haben danach den Wert 11.

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Zu den weiteren unären Operatoren gehören `+`, `-`, `~` und `!`.

## Zuweisung

`=` weist der Variablen links den Wert des Ausdrucks rechts zu.

```java
int age;
String name;
Double height;
```

Die Zuweisung kann nach der Deklaration erfolgen.

```java
age = 20;
name = "Mary";
height = 1.70;
```

Alternativ lässt sich der Wert direkt in der Deklaration angeben.

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

## Zusammengesetzte Zuweisung

`+=`, `-=`, `*=`, `/=` und `%=` verbinden Berechnung und Zuweisung.

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

Das Programm gibt diese Werte in der angegebenen Reihenfolge aus.

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

Bei zusammengesetzten Zuweisungen wird der linke Ausdruck einmal ausgewertet und sein Typ berücksichtigt. Java bietet solche Operatoren auch für Verschiebungen und bitweise Operationen.

## Vergleiche

`==`, `!=`, `>`, `>=`, `<` und `<=` liefern einen booleschen Wert.

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

Bei Eingabe 10 treffen drei Vergleiche zu, weil jedes `if` separat geprüft wird. `Integer.parseInt` wandelt die Eingabe in eine Ganzzahl um.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
