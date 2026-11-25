---
layout: post
title: "Operatory w Javie"
date: 2026-11-20
lang: pl
translation_id: operadores-java
permalink: /pl/operators-in-java/
share_text: >-
  Operatory arytmetyczne, przypisania i porównania na przykładach z książki.
---

## Operatory arytmetyczne

`+`, `-`, `*`, `/` i `%` oznaczają dodawanie, odejmowanie, mnożenie, dzielenie i resztę. Priorytety określają grupowanie działań. `++` i `--` zmieniają wartość zmiennej o jeden.

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

W `y = x++` zmienna `y` otrzymuje poprzednią wartość 10. Dopiero potem `x` zmienia się na 11.

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

W `y = ++x` zwiększenie następuje przed przypisaniem. Obie zmienne mają wartość 11.

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Do innych operatorów jednoargumentowych należą `+`, `-`, `~` i `!`.

## Przypisanie

`=` zapisuje wartość wyrażenia po prawej stronie do zmiennej po lewej.

```java
int age;
String name;
Double height;
```

Wartość można przypisać po deklaracji.

```java
age = 20;
name = "Mary";
height = 1.70;
```

Można też zainicjalizować zmienną już w deklaracji.

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

## Przypisanie złożone

`+=`, `-=`, `*=`, `/=` i `%=` łączą działanie z przypisaniem.

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

Program wypisuje wartości w następującej kolejności.

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

Przypisanie złożone uwzględnia typ lewej strony i oblicza ją tylko raz. Złożone przypisania istnieją też dla przesunięć i operacji bitowych.

## Porównania

`==`, `!=`, `>`, `>=`, `<` i `<=` zwracają wartość logiczną.

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

Po podaniu 10 prawdziwe są trzy warunki, bo każde `if` działa niezależnie. `Integer.parseInt` zamienia tekst na liczbę całkowitą.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
