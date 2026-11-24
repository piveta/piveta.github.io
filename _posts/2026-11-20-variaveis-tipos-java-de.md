---
layout: post
title: "Variablen und Typen in Java"
date: 2026-11-24
lang: de
translation_id: variaveis-tipos-java
permalink: /de/variables-and-types-in-java/
share_text: >-
  Lokale Variablen, Typinferenz, primitive Typen und Referenztypen.
---

Eine lokale Variable hat einen Namen, einen Typ und einen Gültigkeitsbereich. Vor der Verwendung muss ihr ein Wert zugewiesen werden. Java vergibt für lokale Variablen keine Standardwerte.

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

Der Diamantoperator `<>` erlaubt dem Compiler, das Typargument aus der Deklaration abzuleiten.

```java
ArrayList<Double> list = new ArrayList<>();
```

Bei `var` leitet der Compiler den Typ aus dem erforderlichen Initialisierer ab. Hier liefert `ArrayList<Double>` die Information.

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Java unterscheidet Groß- und Kleinschreibung. Klassen und Schnittstellen beginnen üblicherweise mit einem Großbuchstaben, Variablen und Methoden mit einem Kleinbuchstaben. Konstanten verwenden Großbuchstaben und Unterstriche.

## Primitive Typen

Zu ihnen zählen `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` und `char`.

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

Literale können diese Variablen unmittelbar initialisieren. `L` kennzeichnet `long`, `f` kennzeichnet `float`.

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

Ganzzahlliterale können auch binär (`0b`) oder hexadezimal (`0x`) geschrieben werden.

## Referenztypen

Klassen, Schnittstellen, Aufzählungen, Records und Arrays sind Referenztypen. Eine Zeichenkette kann als Literal in doppelten Anführungszeichen stehen.

```java
void main() {
    String s = "This is a string...";
}
```

Wrapper-Klassen stellen primitive Werte als Objekte dar. Für Sammlungen verwendet das Buch häufig die Collections-API.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
