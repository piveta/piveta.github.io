---
layout: post
title: "Java generics exercises"
date: 2026-11-20
lang: en
translation_id: exercicios-tipos-genericos-java
permalink: /en/java-generics-exercises/
share_text: >-
  Ten exercises on generic classes and methods, wildcards, inheritance, type erasure, Optional<T>, and Box<T>.
---

The following exercises are based on the generics chapter of **Orientação a Objetos com Java**. The supplied code follows the book's examples, with identifiers, comments, and messages translated into English.

1. Study the main interfaces of the Java collections framework. Identify how their generic types allow data structures to be used in different contexts without changing their classes or interfaces.

2. Create a static method named `max` that receives two comparable objects, that is, objects implementing `Comparable`, and returns the greater one. Use generics to define its parameters.

3. Create a static method that receives a list parameterized with any type and prints it. Use a wildcard.

4. Create a static method that receives a list parameterized with a numeric type and sums its elements. Use a wildcard with `extends` so that it accepts only lists of numbers (`Number`).

5. Consider this class hierarchy:

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   The following method receives a list of `Instrument` objects or objects of its subclasses and prints its elements:

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   Pass a list of `Guitar` objects and then a list of `Flute` objects. Next, try to add a new instrument to the list inside the method and observe what the compiler reports.

6. Implement a generic method that receives a list of elements that are both `Number` and `Comparable`, and returns the greatest element.

7. Create the three methods below, implement their bodies, and test them with lists of `Car`, `Motorcycle`, and `Vehicle`:

   ```java
   void printInvariant(List<Vehicle> list){
       // Implement
   }
   void printCovariant(List<? extends Vehicle> list){
       // Implement
   }
   void printContravariant(List<? super Vehicle> list){
       // Implement
   }
   ```

8. Try to implement `boolean checkList(Object obj)` so that it returns `true` only when `obj` is a `List<String>`. Determine whether this is directly possible in Java, and propose an alternative using `List<?>` or `List<Object>`.

9. Study the documentation for `Optional<T>`. Create `public static <T> void printOptional(Optional<T> opt)` to print its value when present, or *empty* otherwise. Test it with `Optional<String>` and `Optional<Integer>`.

10. Create a generic `Box<T>` class that stores one item of type `T`:

    - `public void store(T item)` stores the item and must reject `null`.
    - `public T get()` returns the stored item.
    - `public static <T extends Comparable<T>> boolean compare(Box<T> b1, Box<T> b2)` returns `true` if the first box's item is greater, using `compareTo`.

    Also create `compareWithInheritance` to compare boxes of different types that share an inheritance relationship. Use `<? extends T>` or `<? super T>`. Test it with the examples from the book:

    ```java
     Box<Integer> box1 = new Box<>();
     Box<Integer> box2 = new Box<>();
     box1.store(10);
     box2.store(5);
     boolean result = Box.compare(box1, box2); // true

     Box<Double> box3 = new Box<>();
     Box<Integer> box4 = new Box<>();
     box3.store(7.5);
     box4.store(5);
     boolean result2 = Box.compareWithInheritance(box3,
        box4); // true
    ```

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
