---
layout: post
title: "Vererbung und Untertypen bei Java-Generics"
date: 2026-11-24
lang: de
translation_id: heranca-subtipos-genericos-java
permalink: /de/inheritance-and-subtypes-with-java-generics/
share_text: >-
  Warum List<Car> keine List<Vehicle> ist und wie extends und super das Lesen und Schreiben ermöglichen.
---

Generische Typen sind in Java standardmäßig **invariant**: Auch wenn `Car` von `Vehicle` erbt, ist `List<Car>` kein Untertyp von `List<Vehicle>`. Wildcards mit `extends` und `super` beschreiben Beziehungen beim Gebrauch eines generischen Typs.

## Invarianz

Im Beispiel erben `Car` und `Motorcycle` von `Vehicle`:

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

Eine Liste von Autos darf keiner Variablen vom Typ `List<Vehicle>` zugewiesen werden. Diese Zuweisung verursacht einen **Kompilierfehler**:

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

Die Regel schützt die Typsicherheit: Andernfalls könnte man über `vehicles` ein Motorrad in die eigentliche Autoliste einfügen. Das folgende Fragment ist **hypothetisch** und kein gültiges Programm:

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## Kovarianter Gebrauch: `extends`

Zum **Lesen** von Fahrzeugen oder Untertypen eignet sich `List<? extends Vehicle>`. Jedes gelesene Element ist mindestens ein `Vehicle`:

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

Die Methode akzeptiert `List<Vehicle>`, `List<Car>` und `List<Motorcycle>`. Ein `Car` lässt sich nicht hinzufügen, da der konkrete Listentyp unbekannt ist.

## Kontravarianter Gebrauch: `super`

Zum **Hinzufügen** von Autos kann eine Liste von `Car` oder einem Obertyp entgegengenommen werden:

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

`List<Car>`, `List<Vehicle>` und `List<Object>` sind gültig. Beim Lesen ist nur `Object` garantiert. Kovarianz und Kontravarianz beziehen sich hier auf den **Wildcard-Gebrauch**; `List<T>` bleibt invariant.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
