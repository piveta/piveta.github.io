---
layout: post
title: "Espressioni e istruzioni condizionali in Java"
date: 2026-11-20
lang: it
translation_id: expressoes-condicionais-java
permalink: /it/expressions-and-conditional-statements-in-java/
share_text: >-
  Espressioni, blocchi, if, else, operatore ternario e switch.
---

## Espressioni e istruzioni

Un’espressione produce un valore. Può contenere letterali, variabili, operatori, chiamate a metodi o creazioni di oggetti.

```text
x + 2 * 1
c.getBalance()
i = 20
```

Un’istruzione è un’unità eseguibile. Chiamate a metodi, assegnazioni e incrementi possono essere istruzioni e terminano con un punto e virgola. Questi frammenti dipendono da dichiarazioni esterne.

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

Le parentesi graffe raggruppano istruzioni in un blocco. Il programma legge un intero e stampa due messaggi se la condizione è vera.

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

## Istruzioni condizionali

`if` esegue l’istruzione controllata quando la condizione booleana è vera.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else` definisce il comportamento quando la condizione è falsa.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

Le parentesi graffe permettono di eseguire più istruzioni nello stesso ramo.

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

Un `if` annidato controlla l’accesso prioritario dopo la verifica della maggiore età.

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

L’operatore ternario sceglie uno di due valori in base alla condizione.

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

## Scelta con switch

L’istruzione `switch` seleziona un caso. `break` lo termina e `default` gestisce gli altri valori.

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

L’espressione `switch` con frecce restituisce un valore. Più valori dello stesso caso si separano con virgole.

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

Con il pattern matching, una guardia `when` aggiunge una condizione al controllo del tipo. L’esempio gestisce `Integer`, `String`, `null` e gli altri valori.

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

Il programma chiama il metodo con quattro valori diversi.

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

Il risultato è il seguente.

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

L’ultimo esempio richiede una versione di Java che supporti il pattern matching in `switch`.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
