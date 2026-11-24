---
layout: post
title: "Variabler och typer i Java"
date: 2026-11-24
lang: sv
translation_id: variaveis-tipos-java
permalink: /sv/variables-and-types-in-java/
share_text: >-
  Lokala variabler, typinferens, primitiva typer och referenstyper.
---

En lokal variabel har ett namn, en typ och en räckvidd. Java ger den inget standardvärde, så den måste tilldelas ett värde innan den används.

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

Om deklarationen anger listans typ kan kompilatorn härleda typargumentet i `<>`.

```java
ArrayList<Double> list = new ArrayList<>();
```

Med `var` härleder kompilatorn typen från det obligatoriska uttrycket som ger startvärdet. I exemplet anges därför `Double` vid konstruktoranropet.

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Java skiljer på stora och små bokstäver. Klass- och gränssnittsnamn börjar normalt med stor bokstav, variabel- och metodnamn med liten. Konstanter skrivs med stora bokstäver och understreck.

## Primitiva typer

Hit hör `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` och `char`.

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

De kan initieras direkt med literaler. Ändelsen `L` markerar `long` och `f` markerar `float`.

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

Heltalsliteraler kan också skrivas binärt med `0b` eller hexadecimalt med `0x`.

## Referenstyper

Klasser, gränssnitt, uppräkningstyper, records och arrayer är referenstyper. En strängliteral omges av dubbla citattecken.

```java
void main() {
    String s = "This is a string...";
}
```

Omslagsklasser representerar primitiva värden som objekt. Kapitlets övriga exempel använder ofta samlingsbiblioteket.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
