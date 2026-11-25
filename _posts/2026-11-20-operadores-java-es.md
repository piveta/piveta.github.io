---
layout: post
title: "Operadores en Java"
date: 2026-11-20
lang: es
translation_id: operadores-java
permalink: /es/operators-in-java/
share_text: >-
  Operadores aritméticos, de asignación y relacionales con ejemplos del libro.
---

## Operadores aritméticos

Los operadores aritméticos binarios incluyen `+` (suma), `-` (resta), `*` (multiplicación), `/` (división) y `%` (resto). La precedencia influye en la evaluación de expresiones.

### Incremento y decremento

Los operadores `++` y `--` modifican una variable numérica en una unidad. En sentencias independientes, el siguiente ejemplo cambia `x` de 10 a 11 y luego a 10:

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

En `y = x++`, se asigna a `y` el valor anterior antes de incrementar `x`; al final, `x` vale 11 e `y` vale 10:

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

En `y = ++x`, el incremento ocurre primero y ambas variables valen 11:

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Otros operadores unarios son `+`, `-`, `~` y `!`. La evaluación sigue las reglas de precedencia y orden de Java.

## Operadores de asignación

El operador `=` asigna a la variable de la izquierda el valor de la expresión de la derecha. Las variables pueden declararse y asignarse después:

```java
int age;
String name;
Double height;
```

```java
age = 20;
name = "Mary";
height = 1.70;
```

También pueden inicializarse en la declaración:

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

### Asignación compuesta

Los operadores `+=`, `-=`, `*=`, `/=` y `%=` combinan una operación y una asignación:

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

Los valores mostrados son:

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

La asignación compuesta tiene en cuenta el tipo de la expresión izquierda y la evalúa una sola vez. También hay operadores compuestos para desplazamientos y operaciones de bits.

## Operadores relacionales

Los operadores `==`, `!=`, `>`, `>=`, `<` y `<=` comparan operandos y producen `true` o `false`. El siguiente ejemplo lee una edad y evalúa condiciones independientes:

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

Con la entrada 10 se muestran los mensajes que indican que la edad es igual a 10, distinta de 20 y menor o igual que 80. Como cada `if` es independiente, pueden mostrarse varios mensajes. `Integer.parseInt` convierte a entero la cadena leída.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
