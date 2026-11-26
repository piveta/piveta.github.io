---
layout: post
title: "Uttryck och villkorssatser i Java"
date: 2026-11-20
lang: sv
translation_id: expressoes-condicionais-java
permalink: /sv/expressions-and-conditional-statements-in-java/
share_text: >-
  Uttryck, block, if, else, den ternära operatorn och switch.
---

## Uttryck och satser

Ett uttryck ger ett värde. Det kan innehålla literaler, variabler, operatorer, metodanrop eller objektskapande. Kodfragmenten bildar inget komplett program på egen hand.

```text
x + 2 * 1
c.getBalance()
i = 20
```

En sats är en körbar enhet. Metodanrop, tilldelningar och inkrement kan bilda satser som avslutas med semikolon. Exemplet förutsätter ytterligare deklarationer och klassen `Account`.

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

Klammerparenteser grupperar satser i ett block. Programmet läser ett heltal och skriver två meddelanden om villkoret är sant.

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

## Villkorssatser

`if` kör den tillhörande satsen när det booleska villkoret är sant.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else` anger vad som händer när villkoret är falskt.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

Klammerparenteser gör att flera satser kan köras i varje gren.

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

Ett nästlat `if` prövar villkoret för prioriterad åtkomst efter kontrollen av myndighetsåldern.

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

Den ternära operatorn väljer ett av två värden beroende på villkoret.

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

## Val med switch

En klassisk `switch` väljer ett fall. `break` avslutar det och `default` hanterar övriga värden.

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

Ett `switch`-uttryck med pilar ger ett resultat. Kommatecken skiljer flera värden i samma fall.

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

Vid mönstermatchning kan `when` lägga till ett villkor för typmönstret. Exemplet skiljer på `Integer`, `String`, `null` och andra värden.

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

Programmet anropar metoden med fyra olika värden.

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

Utdata ser ut så här.

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

Det sista exemplet kräver en Java-version som stöder mönstermatchning i `switch`.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
