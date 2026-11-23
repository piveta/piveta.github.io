---
layout: post
title: "Übungen zu Java-Generics"
date: 2026-11-20
lang: de
translation_id: exercicios-tipos-genericos-java
permalink: /de/java-generics-exercises/
share_text: >-
  Zehn Übungen zu generischen Methoden, Wildcards, Vererbung, Optional<T> und Box<T>.
---

Diese Aufgaben stammen aus dem Generics-Kapitel von **Orientação a Objetos com Java**. Die Code-Struktur folgt dem Buch; Bezeichner, Kommentare und Ausgaben stehen auf Englisch.

1. Untersuchen Sie die wichtigsten Schnittstellen des Java-Collections-Frameworks und erklären Sie, wie Generics ihre Wiederverwendung ohne Änderungen an den Klassen ermöglichen.
2. Schreiben Sie eine statische generische Methode `max`, die zwei `Comparable`-Objekte entgegennimmt und das größere zurückgibt.
3. Schreiben Sie eine statische Methode, die eine Liste beliebigen Typs entgegennimmt und ausgibt. Verwenden Sie eine Wildcard.
4. Schreiben Sie eine Methode, die eine numerische Liste summiert. Beschränken Sie sie mit `extends` auf `Number`-Listen.
5. Betrachten Sie folgende Hierarchie:

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   Diese Methode nimmt eine Liste von Instrumenten oder Untertypen entgegen:

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   Übergeben Sie Listen von `Guitar` und `Flute`. Versuchen Sie anschließend, innerhalb der Methode ein Instrument hinzuzufügen, und beobachten Sie den Kompilierfehler.
6. Implementieren Sie eine generische Methode, die Elemente annimmt, die sowohl `Number` als auch `Comparable` sind, und das größte zurückgibt.
7. Implementieren und testen Sie diese Methoden mit Listen von `Car`, `Motorcycle` und `Vehicle`:

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

8. Versuchen Sie, `boolean checkList(Object obj)` so zu schreiben, dass nur `List<String>` erkannt wird. Prüfen Sie, ob Java dies direkt erlaubt, und schlagen Sie eine Alternative mit `List<?>` oder `List<Object>` vor.
9. Studieren Sie `Optional<T>` und schreiben Sie `printOptional(Optional<T> opt)`, das einen Wert oder *empty* ausgibt. Testen Sie `Optional<String>` und `Optional<Integer>`.
10. Erstellen Sie `Box<T>` mit `store(T item)` (kein `null`), `get()` und `compare(Box<T> b1, Box<T> b2)` mittels `compareTo`. Ergänzen Sie `compareWithInheritance` für Boxen verschiedener, durch Vererbung verbundener Typen mit `<? extends T>` oder `<? super T>`. Testen Sie:

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

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
