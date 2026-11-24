---
layout: post
title: "Ereditarietà e sottotipi con i generici Java"
date: 2026-11-24
lang: it
translation_id: heranca-subtipos-genericos-java
permalink: /it/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car> non è List<Vehicle>: invarianza, lettura con extends e scrittura con super.
---

I tipi generici Java sono **invarianti** per impostazione predefinita: anche se `Car` estende `Vehicle`, `List<Car>` non è sottotipo di `List<Vehicle>`. I wildcard `extends` e `super` esprimono altre relazioni nel punto d'uso.

## Invarianza

Nell'esempio, `Car` e `Motorcycle` estendono `Vehicle`:

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

Non si può assegnare una lista di auto a una variabile `List<Vehicle>`. L'assegnazione seguente genera un **errore di compilazione**:

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

La regola tutela la sicurezza dei tipi. Altrimenti, tramite `vehicles` sarebbe possibile inserire una moto in una lista che in realtà contiene auto. Il frammento seguente è **ipotetico**, non eseguibile:

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## Uso covariante: `extends`

Per **leggere** veicoli o sottotipi, un metodo può ricevere `List<? extends Vehicle>`. Ogni elemento letto è almeno un `Vehicle`:

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

Il metodo accetta `List<Vehicle>`, `List<Car>` e `List<Motorcycle>`, ma non può aggiungere un `Car`, perché il tipo concreto della lista è sconosciuto.

## Uso controvariante: `super`

Per **aggiungere** auto, un metodo può ricevere una lista di `Car` o di un suo supertipo:

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

Sono validi `List<Car>`, `List<Vehicle>` e `List<Object>`. In lettura, l'unico tipo garantito è `Object`. Covarianza e controvarianza descrivono questi **usi con wildcard**; `List<T>` resta invariante.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
