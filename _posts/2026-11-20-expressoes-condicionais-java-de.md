---
layout: post
title: "Ausdrücke und bedingte Anweisungen in Java"
date: 2026-11-20
lang: de
translation_id: expressoes-condicionais-java
permalink: /de/expressions-and-conditional-statements-in-java/
share_text: >-
  Ausdrücke, Blöcke, if, else, der ternäre Operator und switch.
---

## Ausdrücke und Anweisungen

Ein Ausdruck liefert bei der Auswertung einen Wert. Er kann Literale, Variablen, Operatoren, Methodenaufrufe oder Objekterzeugung enthalten.

```text
x + 2 * 1
c.getBalance()
i = 20
```

Eine Anweisung ist eine ausführbare Einheit. Methodenaufrufe, Zuweisungen und Inkremente können mit Semikolon als Anweisungen auftreten. Die Fragmente setzen weitere Deklarationen voraus.

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

Geschweifte Klammern gruppieren Anweisungen zu einem Block. Hier liest das Programm eine Ganzzahl und gibt bei erfüllter Bedingung zwei Meldungen aus.

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

## Bedingte Anweisungen

`if` führt die zugehörige Anweisung aus, wenn die boolesche Bedingung wahr ist.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else` legt fest, was bei einer falschen Bedingung geschieht.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

Klammern fassen mehrere Anweisungen pro Zweig zusammen.

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

Ein verschachteltes `if` prüft nach der Volljährigkeit, ob vorrangiger Zugang gewährt wird.

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

Der ternäre Operator wählt anhand der Bedingung einen von zwei Werten.

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

## Auswahl mit switch

Eine klassische `switch`-Anweisung wählt einen Fall. `break` beendet ihn, `default` deckt die übrigen Werte ab.

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

Ein `switch`-Ausdruck mit Pfeilen liefert einen Wert. Mehrere Fallwerte werden durch Kommas getrennt.

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

Beim Pattern Matching kann eine `when`-Bedingung das Typmuster weiter einschränken. Das Beispiel unterscheidet `Integer`, `String`, `null` und andere Werte.

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

Das Hauptprogramm ruft die Methode mit vier unterschiedlichen Werten auf.

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

Die Ausgabe lautet:

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

Das letzte Beispiel setzt eine Java-Version voraus, die Pattern Matching in `switch` unterstützt.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
