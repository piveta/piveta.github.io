---
layout: post
title: "Expresiones y sentencias condicionales en Java"
date: 2026-11-20
lang: es
translation_id: expressoes-condicionais-java
permalink: /es/expressions-and-conditional-statements-in-java/
share_text: >-
  Expresiones, bloques, if, else, el operador ternario y switch con ejemplos del libro.
---

## Expresiones y sentencias

Una **expresión** se evalúa y produce un valor. Puede combinar literales, variables, operadores, llamadas a métodos o construcción de objetos. Estos fragmentos no forman por sí solos un programa completo:

```text
x + 2 * 1
c.getBalance()
i = 20
```

Una **sentencia** es una unidad ejecutable. Las llamadas a métodos, asignaciones e incrementos pueden ser sentencias; este fragmento también depende de declaraciones y de una clase `Account` no incluidas:

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

Las llaves agrupan sentencias en un **bloque**. El siguiente programa lee un entero y ejecuta dos salidas si se cumple la condición:

```java
void main() {
    int x = Integer.parseInt(
            IO.readln("Enter an integer: "));
    if (x < 10) {  
        IO.println("X is less than 10."); 
        IO.println("Initialize X with another value."); 
    }
}
```

## Sentencias condicionales

Una sentencia condicional selecciona un camino según una expresión booleana. `if` ejecuta la sentencia controlada cuando la condición es verdadera:

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

Con `else` también se define el comportamiento para la condición falsa:

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

Las llaves permiten agrupar varias sentencias en cada camino:

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
    }
    else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

Las condiciones pueden **anidarse**. Después de comprobar la mayoría de edad, el programa verifica el acceso prioritario:

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
        if (age >= 65)
            IO.println("Priority access granted");
    } else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

El **operador ternario** evalúa una condición y selecciona uno de dos valores, que aquí forman parte del mensaje:

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age: "));
    // The ternary operator has this syntax: 
		// (expr) ? true : false
    String message = ((age >= 18) ? "At least" : "Under") + 
                 " 18 years old";
    IO.println(message);
}
```

## Selección entre varios caminos

Una sentencia `switch` selecciona un caso, utiliza `break` para terminarlo y `default` para los demás valores:

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message;
    switch (age) {
        case 0: case 1: case 2: case 3: case 4: case 5:
            message = "Very young";
            break;
        case 18:
            message = "Reaching adulthood";
            break;
        case 65:
            message = "Entering senior years";
            break;
        default:
            message = "No special case";
            break;
        }
        IO.println(message);
}
```

Una **expresión `switch`** usa flechas, separa valores con comas y produce un resultado sin `break` en cada caso:

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message = switch (age) {
        case 0, 1, 2, 3, 4, 5 -> "Very young";
        case 18 -> "Reaching adulthood";
        case 65 -> "Entering senior years";
        default -> "No special case";
    };
    IO.println(message);
}
```

El libro también muestra **pattern matching** con condiciones `when`, combinando el tipo del objeto con una condición adicional:

```java
private static String age(Object ageObject) {
    return switch (ageObject) {
        case Integer i when i >= 65 -> 
            "[Integer] Adult: " + i + 
            "\nPriority access granted.";
        case Integer i when i >= 18 -> 
            "[Integer] Adult: " + i + 
             "\nAccess granted.";
        case Integer i -> "[Integer] Minor: " + 
                i + "\nAccess denied.";
        case String s -> 
            "[String] Age provided as text: " + s;
        case null -> "[null] Age not provided";
        default -> "Unexpected data type: " + 
                ageObject.getClass().getName();
    };
}
```

El cliente llama al método con cuatro valores diferentes:

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

La salida traducida es:

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

El último ejemplo requiere una versión de Java que admita pattern matching en `switch`.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
