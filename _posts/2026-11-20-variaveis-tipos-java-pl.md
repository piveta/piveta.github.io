---
layout: post
title: "Zmienne i typy w Javie"
date: 2026-11-20
lang: pl
translation_id: variaveis-tipos-java
permalink: /pl/variables-and-types-in-java/
share_text: >-
  Zmienne lokalne, wnioskowanie z var, typy proste i referencyjne.
---

Zmienna lokalna ma nazwę, typ i zakres. Przed użyciem trzeba jej nadać wartość, ponieważ Java nie przypisuje zmiennym lokalnym wartości domyślnych.

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

Jeśli deklaracja określa typ listy, kompilator może wywnioskować argument typu oznaczony przez `<>`.

```java
ArrayList<Double> list = new ArrayList<>();
```

Przy `var` kompilator ustala typ na podstawie obowiązkowego inicjalizatora. Dlatego w przykładzie konstruktor otrzymuje jawny argument `Double`.

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Java rozróżnia wielkie i małe litery. Nazwy klas i interfejsów zaczynają się zwykle od wielkiej litery, nazwy zmiennych i metod od małej, a w nazwach stałych używa się wielkich liter i podkreśleń.

## Typy proste

Są to `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` i `char`.

```java
void main() {
    byte b;
    short s;
    int x, y, z;
    long l;
    float f;
    double d;
    boolean test;
    char c;
}
```

Do inicjalizacji można użyć literałów. Przyrostek `L` oznacza `long`, a `f` oznacza `float`.

```java
void main() {
    byte b = 10;
    short s = 20;
    int x = 10, y = 20, z = 30;
    long l = 100L;
    float f = 12.3f;
    double d = 20.45;
    boolean test = true;
    char c = 'a';
}
```

Literały całkowite można zapisać binarnie z `0b` lub szesnastkowo z `0x`.

## Typy referencyjne

Klasy, interfejsy, wyliczenia, rekordy i tablice są typami referencyjnymi. Literał `String` zapisuje się w cudzysłowie.

```java
void main() {
    String s = "This is a string...";
}
```

Klasy opakowujące reprezentują wartości proste jako obiekty. Inne przykłady w rozdziale często korzystają także z API kolekcji.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
