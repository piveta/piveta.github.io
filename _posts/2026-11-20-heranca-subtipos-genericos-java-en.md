---
layout: post
title: "Inheritance and subtypes with Java generics"
date: 2026-11-24
lang: en
translation_id: heranca-subtipos-genericos-java
permalink: /en/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car> is not List<Vehicle>. Learn invariance, reading through extends, and writing through super in Java generics.
---

Java generic types are **invariant** by default: even if `Car` extends `Vehicle`, `List<Car>` is not a subtype of `List<Vehicle>`. Wildcards with `extends` and `super` express useful relationships at the point where a generic type is used.

## Invariance

Consider the classes in the book's example. `Car` and `Motorcycle` extend `Vehicle`:

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

A list of cars cannot be assigned to a variable declared as a list of vehicles. The assignment below produces a **compile-time error**:

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

This rule preserves type safety. If the assignment compiled, a `Motorcycle` could be added through `vehicles`, even though the underlying object would still be a list of cars. The following fragment is **hypothetical**, not runnable code:

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## Covariant use: `extends`

When a method needs to **read** elements from a list of vehicles or any subtype, it can accept `List<? extends Vehicle>`. Every element read is at least a `Vehicle`:

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

This method accepts `List<Vehicle>`, `List<Car>`, and `List<Motorcycle>`. It cannot add a `Car`, because the received list might be a list of motorcycles. The type behind the wildcard is unknown.

## Contravariant use: `super`

When the goal is to **add** cars, a method can accept a list of `Car` or one of its supertypes:

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

Thus `List<Car>`, `List<Vehicle>`, and `List<Object>` are valid arguments. When reading an element from such a list, the only statically guaranteed type is `Object`.

Covariance and contravariance here describe **wildcard uses**, such as `List<? extends Vehicle>` and `List<? super Car>`. The declaration of `List<T>` remains invariant.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
