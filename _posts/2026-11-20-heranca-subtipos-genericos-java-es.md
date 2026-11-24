---
layout: post
title: "Herencia y subtipos con genéricos de Java"
date: 2026-11-24
lang: es
translation_id: heranca-subtipos-genericos-java
permalink: /es/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car> no es List<Vehicle>: invariancia, lectura con extends y escritura con super.
---

Los tipos genéricos de Java son **invariantes** por defecto. Aunque `Car` extienda `Vehicle`, `List<Car>` no es subtipo de `List<Vehicle>`. Los comodines `extends` y `super` permiten otras relaciones en el punto de uso.

## Invariancia

En el ejemplo, `Car` y `Motorcycle` extienden `Vehicle`:

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

No se puede asignar una lista de coches a una variable de tipo `List<Vehicle>`. Esta asignación da un **error de compilación**:

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

La prohibición protege la seguridad de tipos. Si compilara, se podría añadir una motocicleta a una lista que realmente contiene coches. El siguiente fragmento es **hipotético**, no un programa válido:

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## Uso covariante: `extends`

Para **leer** vehículos o subtipos, un método puede recibir `List<? extends Vehicle>`. Cada elemento leído es como mínimo un `Vehicle`:

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

Acepta `List<Vehicle>`, `List<Car>` y `List<Motorcycle>`, pero no puede añadir un `Car`: se desconoce el tipo concreto de la lista.

## Uso contravariante: `super`

Para **añadir** coches, el método puede recibir una lista de `Car` o de una superclase:

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

Acepta `List<Car>`, `List<Vehicle>` y `List<Object>`. Al leer un elemento, solo se garantiza `Object`. La covariancia y la contravariancia describen estos **usos con comodines**; la declaración de `List<T>` sigue siendo invariante.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
