---
layout: post
title: "Ćwiczenia z generyków Javy"
date: 2026-11-20
lang: pl
translation_id: exercicios-tipos-genericos-java
permalink: /pl/java-generics-exercises/
share_text: >-
  Dziesięć zadań o metodach generycznych, wildcardach, dziedziczeniu, Optional<T> i Box<T>.
---

Ćwiczenia pochodzą z rozdziału o generykach w **Orientação a Objetos com Java**. Struktura kodu odpowiada książce; identyfikatory, komentarze i komunikaty są po angielsku.

1. Poznaj główne interfejsy frameworka kolekcji Javy i wyjaśnij, jak generyki umożliwiają ponowne wykorzystanie struktur bez zmian w klasach.
2. Utwórz statyczną metodę generyczną `max`, która przyjmuje dwa obiekty `Comparable` i zwraca większy.
3. Utwórz metodę statyczną przyjmującą i wypisującą listę dowolnego typu. Użyj symbolu wieloznacznego.
4. Utwórz metodę sumującą listę liczb. Użyj `extends`, aby przyjmowała tylko listy `Number`.
5. Rozważ następującą hierarchię:

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   Metoda poniżej przyjmuje listę instrumentów lub ich podtypów:

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   Przekaż listy `Guitar` i `Flute`. Następnie spróbuj dodać instrument wewnątrz metody i sprawdź błąd kompilacji.
6. Napisz metodę generyczną przyjmującą elementy będące zarówno `Number`, jak i `Comparable`, która zwraca największy.
7. Zaimplementuj te metody i przetestuj je listami `Car`, `Motorcycle` i `Vehicle`:

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

8. Spróbuj napisać `boolean checkList(Object obj)`, aby rozpoznawała wyłącznie `List<String>`. Sprawdź, czy Java pozwala na to bezpośrednio, i zaproponuj rozwiązanie z `List<?>` lub `List<Object>`.
9. Poznaj `Optional<T>` i napisz `printOptional(Optional<T> opt)`, wypisującą wartość lub *empty*. Testuj z `Optional<String>` i `Optional<Integer>`.
10. Utwórz `Box<T>` z `store(T item)` (bez `null`), `get()` i `compare(Box<T> b1, Box<T> b2)` używającą `compareTo`. Dodaj `compareWithInheritance` dla pudełek różnych typów powiązanych dziedziczeniem z `<? extends T>` lub `<? super T>`. Przetestuj:

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

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
