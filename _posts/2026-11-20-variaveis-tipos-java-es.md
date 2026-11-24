---
layout: post
title: "Variables y tipos en Java"
date: 2026-11-20
lang: es
translation_id: variaveis-tipos-java
permalink: /es/variables-and-types-in-java/
share_text: >-
  Declaraciones, inferencia con var, tipos primitivos y tipos de referencia en Java.
---

Una variable tiene nombre, tipo y ámbito. Las **variables locales**, declaradas en un método, deben inicializarse antes de su uso; Java no les asigna un valor predeterminado.

El ejemplo declara una cadena, un entero y una lista de valores `Double`:

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

Cuando la declaración indica el tipo de la lista, el constructor puede inferirlo con `<>`:

```java
ArrayList<Double> list = new ArrayList<>();
```

Con `var`, el compilador infiere el tipo a partir de la inicialización, que es obligatoria. En este caso el constructor debe indicar `Double`:

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Por convención, los nombres de clases e interfaces comienzan con mayúscula; los de variables y métodos, con minúscula; las constantes usan mayúsculas y guiones bajos. Java distingue mayúsculas y minúsculas.

## Tipos primitivos

Los tipos primitivos incluyen `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` y `char`. El libro declara variables de estos tipos:

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

Se pueden inicializar directamente con literales. El sufijo `L` indica `long` y `f` indica `float`:

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

Los enteros también admiten literales binarios con `0b` y hexadecimales con `0x`.

## Tipos de referencia

Clases, interfaces, enumeraciones, registros y arreglos son tipos de referencia. Una `String` puede crearse entre comillas dobles:

```java
void main() {
    String s = "This is a string...";
}
```

Java proporciona clases *wrapper* para representar valores primitivos como objetos. El capítulo menciona arreglos y matrices, pero usa con más frecuencia la API de colecciones.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
