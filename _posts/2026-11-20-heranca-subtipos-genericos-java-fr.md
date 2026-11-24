---
layout: post
title: "Héritage et sous-types avec les génériques Java"
date: 2026-11-24
lang: fr
translation_id: heranca-subtipos-genericos-java
permalink: /fr/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car> n'est pas List<Vehicle> : invariance, lecture avec extends et écriture avec super.
---

Les types génériques Java sont **invariants** par défaut : même si `Car` hérite de `Vehicle`, `List<Car>` n'est pas un sous-type de `List<Vehicle>`. Les jokers `extends` et `super` expriment d'autres relations au point d'utilisation.

## Invariance

Dans l'exemple, `Car` et `Motorcycle` héritent de `Vehicle` :

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

On ne peut pas affecter une liste de voitures à une variable `List<Vehicle>`. Cette affectation provoque une **erreur de compilation** :

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

Cette règle protège la sûreté des types. Sinon, `vehicles` permettrait d'ajouter une moto à une liste qui contient en réalité des voitures. Le fragment suivant est **hypothétique**, non exécutable :

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## Utilisation covariante : `extends`

Pour **lire** des véhicules ou leurs sous-types, une méthode peut recevoir `List<? extends Vehicle>`. Chaque élément lu est au moins un `Vehicle` :

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

La méthode accepte `List<Vehicle>`, `List<Car>` et `List<Motorcycle>`, mais ne peut ajouter un `Car`, car le type concret de la liste reste inconnu.

## Utilisation contravariante : `super`

Pour **ajouter** des voitures, la méthode peut recevoir une liste de `Car` ou d'un de ses super-types :

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

`List<Car>`, `List<Vehicle>` et `List<Object>` conviennent. À la lecture, seul `Object` est garanti. Covariance et contravariance caractérisent ici les **utilisations avec jokers** ; `List<T>` reste invariant.

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
