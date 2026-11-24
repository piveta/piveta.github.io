---
layout: post
title: "Arv och subtyper med Java-generics"
date: 2026-11-24
lang: sv
translation_id: heranca-subtipos-genericos-java
permalink: /sv/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car> är inte List<Vehicle>; invarians samt läsning med extends och skrivning med super.
---

Generiska typer i Java är **invarianta** som standard: även om `Car` ärver från `Vehicle` är `List<Car>` inte en subtyp av `List<Vehicle>`. Wildcards med `extends` och `super` beskriver andra relationer vid användningen.

## Invarians

I exemplet ärver `Car` och `Motorcycle` från `Vehicle`:

```java
public class Vehicle {
    public void move() {
        IO.println("Vehicle moving");
    }
}

public class Car extends Vehicle {
    public void honk() {
        IO.println("Horn sounded");
    }
}

public class Motorcycle extends Vehicle {
    public void doWheelie() {
        IO.println("Motorcycle doing a wheelie");
    }
}
```

En lista med bilar kan inte tilldelas en variabel av typen `List<Vehicle>`. Tilldelningen ger ett **kompileringsfel**:

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

Regeln skyddar typsäkerheten. Annars skulle `vehicles` kunna användas för att lägga en motorcykel i en faktisk billista. Följande kod är **hypotetisk**, inte ett giltigt program:

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## Kovariant användning: `extends`

För att **läsa** fordon eller subtyper kan en metod ta emot `List<? extends Vehicle>`. Varje läst element är minst ett `Vehicle`:

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

Metoden accepterar `List<Vehicle>`, `List<Car>` och `List<Motorcycle>`, men kan inte lägga till en `Car`, eftersom listans konkreta typ är okänd.

## Kontravariant användning: `super`

För att **lägga till** bilar kan metoden ta emot en lista med `Car` eller en supertyp:

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

`List<Car>`, `List<Vehicle>` och `List<Object>` fungerar. Vid läsning garanteras bara `Object`. Kovarians och kontravarians gäller här **användningen av wildcard**; `List<T>` förblir invariant.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
