---
layout: post
title: "Lectura y escritura en la consola de Java"
date: 2026-11-20
lang: es
translation_id: leitura-escrita-java
permalink: /es/reading-and-writing-on-the-java-console/
share_text: >-
  Cómo utilizar IO, Scanner y readln para mostrar y leer valores en programas Java 25.
---

Muchos programas reciben datos, los procesan y presentan un resultado. En Java 25, la clase `IO` simplifica la escritura en consola con `print` y `println`, y la lectura con `readln`. Los ejemplos de archivos fuente compactos de este capítulo pueden requerir la activación de funciones *preview*.

## Escribir valores

`print` escribe sin añadir un salto de línea; `println` termina la línea. El libro importa estáticamente los métodos de `java.lang.IO` para llamarlos sin prefijo:

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

Las variables `a` y `b` contienen 10 y 20. Como la primera llamada no termina la línea, la salida es `Result: Sum of a and b: 30` en una sola línea.

## Leer con `Scanner`

`Scanner` lee la entrada estándar. Aquí, `nextLine()` lee texto y `nextInt()` lee la edad. Después de `nextInt()`, otra llamada a `nextLine()` consume el salto de línea pendiente antes de leer la dirección:

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

## Leer con `IO.readln`

`readln` recibe un mensaje y devuelve una `String`. El mismo ejemplo puede usar la importación estática de `IO`:

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

Como la edad llega como `String`, el programa la convierte con `Integer.parseInt`. Si la entrada no representa un entero, se produce una `NumberFormatException`; el ejemplo del libro no la trata. La consola sirve aquí para introducir el lenguaje, aunque las aplicaciones también pueden recibir datos mediante formularios e interfaces gráficas.

Los comentarios de una línea comienzan con `//`; los de varias líneas usan `/*` y `*/`:

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
