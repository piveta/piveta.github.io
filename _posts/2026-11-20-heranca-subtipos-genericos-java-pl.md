---
layout: post
title: "Dziedziczenie i podtypy w generykach Javy"
date: 2026-11-24
lang: pl
translation_id: heranca-subtipos-genericos-java
permalink: /pl/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car> nie jest List<Vehicle>; niezmienniczość oraz odczyt z extends i zapis z super.
---

Typy generyczne Javy są domyślnie **niezmiennicze**: choć `Car` dziedziczy po `Vehicle`, `List<Car>` nie jest podtypem `List<Vehicle>`. Symbole wieloznaczne `extends` i `super` opisują inne relacje w miejscu użycia.

## Niezmienniczość

W przykładzie `Car` i `Motorcycle` dziedziczą po `Vehicle`:

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

Listy samochodów nie można przypisać do zmiennej `List<Vehicle>`. To przypisanie powoduje **błąd kompilacji**:

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

Reguła chroni bezpieczeństwo typów. Gdyby przypisanie było możliwe, przez `vehicles` można byłoby dodać motocykl do listy samochodów. Poniższy fragment jest **hipotetyczny**, a nie poprawny program:

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## Kowariantne użycie: `extends`

Do **odczytu** pojazdów i ich podtypów metoda może przyjmować `List<? extends Vehicle>`. Każdy odczytany element jest co najmniej `Vehicle`:

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

Metoda przyjmuje `List<Vehicle>`, `List<Car>` i `List<Motorcycle>`, ale nie może dodać `Car`, ponieważ konkretny typ listy jest nieznany.

## Kontrawariantne użycie: `super`

Do **dodawania** samochodów metoda może przyjmować listę `Car` lub jednego z jego nadtypów:

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

Pasują `List<Car>`, `List<Vehicle>` i `List<Object>`. Przy odczycie gwarantowany jest tylko `Object`. Kowariancja i kontrawariancja dotyczą tu **użycia symboli wieloznacznych**; `List<T>` pozostaje niezmienniczy.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
