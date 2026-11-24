---
layout: post
title: "Variables et types en Java"
date: 2026-11-24
lang: fr
translation_id: variaveis-tipos-java
permalink: /fr/variables-and-types-in-java/
share_text: >-
  Variables et types en Java : exemples du livre en anglais.
---

Une variable locale possède un nom, un type et une portée. Elle doit recevoir une valeur avant son utilisation :

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

Quand la déclaration précise le type, le constructeur peut déduire son argument grâce à `<>` :

```java
ArrayList<Double> list = new ArrayList<>();
```

Avec `var`, le compilateur déduit le type à partir de l’initialisation obligatoire :

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Les types primitifs comprennent `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` et `char` :

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

On peut les initialiser avec des littéraux ; `L` indique un `long` et `f` un `float` :

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

Les classes, interfaces, énumérations, records et tableaux sont des types référence. Une `String` peut être créée entre guillemets :

```java
void main() {
    String s = "This is a string...";
}
```

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
