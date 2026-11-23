---
layout: post
title: "Ejercicios de genéricos de Java"
date: 2026-11-20
lang: es
translation_id: exercicios-tipos-genericos-java
permalink: /es/java-generics-exercises/
share_text: >-
  Diez ejercicios sobre métodos genéricos, comodines, herencia, Optional<T> y Box<T>.
---

Estos ejercicios proceden del capítulo de genéricos de **Orientação a Objetos com Java**. El código conserva la estructura del libro, con identificadores, comentarios y mensajes en inglés.

1. Estudie las principales interfaces del framework de colecciones de Java y cómo sus genéricos permiten reutilizar estructuras de datos sin modificar sus clases.
2. Cree un método estático `max` que reciba dos objetos `Comparable` y devuelva el mayor, utilizando parámetros genéricos.
3. Cree un método estático que reciba e imprima una lista de cualquier tipo. Utilice un comodín.
4. Cree un método estático que sume una lista numérica. Utilice `extends` para aceptar únicamente listas de `Number`.
5. Considere esta jerarquía:

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   El método siguiente recibe una lista de instrumentos o de sus subclases:

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   Pase listas de `Guitar` y de `Flute`. Después intente añadir un instrumento dentro del método y observe el error de compilación.
6. Implemente un método genérico que reciba elementos que sean `Number` y `Comparable` y devuelva el mayor.
7. Implemente estos tres métodos y pruébelos con listas de `Car`, `Motorcycle` y `Vehicle`:

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

8. Intente implementar `boolean checkList(Object obj)` para reconocer solo `List<String>`. Investigue si Java lo permite directamente y proponga una alternativa con `List<?>` o `List<Object>`.
9. Estudie `Optional<T>` y cree `printOptional(Optional<T> opt)` para mostrar su valor o *empty*. Pruebe con `Optional<String>` y `Optional<Integer>`.
10. Cree `Box<T>` para almacenar un elemento. `store(T item)` debe rechazar `null`; `get()` lo devuelve; `compare(Box<T> b1, Box<T> b2)` compara mediante `compareTo`. Añada `compareWithInheritance` para cajas de tipos distintos relacionados por herencia, usando `<? extends T>` o `<? super T>`. Pruebe:

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

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
