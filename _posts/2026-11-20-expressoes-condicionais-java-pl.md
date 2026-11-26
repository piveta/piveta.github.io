---
layout: post
title: "Wyrażenia i instrukcje warunkowe w Javie"
date: 2026-11-20
lang: pl
translation_id: expressoes-condicionais-java
permalink: /pl/expressions-and-conditional-statements-in-java/
share_text: >-
  Wyrażenia, bloki, if, else, operator trójargumentowy i switch.
---

## Wyrażenia i instrukcje

Wyrażenie po obliczeniu daje wartość. Może zawierać literały, zmienne, operatory, wywołania metod lub tworzenie obiektów. Te fragmenty nie są pełnym programem.

```text
x + 2 * 1
c.getBalance()
i = 20
```

Instrukcja jest jednostką wykonania. Wywołanie metody, przypisanie lub zwiększenie wartości może być instrukcją zakończoną średnikiem. Przykład wymaga dodatkowych deklaracji i klasy `Account`.

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

Nawiasy klamrowe grupują instrukcje w blok. Program odczytuje liczbę i wypisuje dwa komunikaty, jeśli warunek jest spełniony.

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

## Instrukcje warunkowe

`if` wykonuje instrukcję, gdy warunek logiczny jest prawdziwy.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else` definiuje zachowanie dla warunku fałszywego.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

Klamry pozwalają umieścić kilka instrukcji w każdej gałęzi.

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

Zagnieżdżone `if` sprawdza po potwierdzeniu pełnoletności, czy przysługuje dostęp priorytetowy.

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

Operator trójargumentowy wybiera jedną z dwóch wartości na podstawie warunku.

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

## Wybór za pomocą switch

Klasyczna instrukcja `switch` wybiera przypadek. `break` kończy jego wykonanie, a `default` obsługuje pozostałe wartości.

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

Wyrażenie `switch` używa strzałek i zwraca wartość. Kilka wartości jednego przypadku rozdziela się przecinkami.

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

Przy dopasowaniu wzorców klauzula `when` dodaje warunek do wzorca typu. Przykład rozróżnia `Integer`, `String`, `null` i pozostałe wartości.

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

Program wywołuje metodę dla czterech różnych wartości.

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

Wynik jest następujący.

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

Ostatni przykład wymaga wersji Javy obsługującej dopasowanie wzorców w `switch`.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
