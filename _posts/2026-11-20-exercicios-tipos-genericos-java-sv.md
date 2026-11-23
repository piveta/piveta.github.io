---
layout: post
title: "Övningar om Java-generics"
date: 2026-11-20
lang: sv
translation_id: exercicios-tipos-genericos-java
permalink: /sv/java-generics-exercises/
share_text: >-
  Tio uppgifter om generiska metoder, wildcards, arv, Optional<T> och Box<T>.
---

Övningarna bygger på kapitlet om generiska typer i **Orientação a Objetos com Java**. Kodens struktur följer boken; identifierare, kommentarer och meddelanden är på engelska.

1. Studera de viktigaste gränssnitten i Javas collections-ramverk och hur generiska typer gör strukturer återanvändbara utan ändringar i klasserna.
2. Skapa den statiska generiska metoden `max` som tar emot två `Comparable`-objekt och returnerar det större.
3. Skapa en statisk metod som tar emot och skriver ut en lista av valfri typ. Använd ett wildcard.
4. Skapa en metod som summerar en numerisk lista. Använd `extends` så att endast listor av `Number` accepteras.
5. Betrakta följande klasshierarki:

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   Metoden nedan tar emot en lista med instrument eller subtyper:

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   Skicka in listor med `Guitar` och `Flute`. Försök sedan lägga till ett instrument inne i metoden och se kompileringsfelet.
6. Implementera en generisk metod som tar emot element som är både `Number` och `Comparable` och returnerar det största.
7. Implementera dessa metoder och testa med listor av `Car`, `Motorcycle` och `Vehicle`:

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

8. Försök skriva `boolean checkList(Object obj)` så att bara `List<String>` identifieras. Undersök om Java tillåter detta direkt och föreslå en lösning med `List<?>` eller `List<Object>`.
9. Studera `Optional<T>` och skapa `printOptional(Optional<T> opt)` som skriver ut värdet eller *empty*. Testa med `Optional<String>` och `Optional<Integer>`.
10. Skapa `Box<T>` med `store(T item)` (avvisa `null`), `get()` och `compare(Box<T> b1, Box<T> b2)` med `compareTo`. Lägg till `compareWithInheritance` för boxar med olika, besläktade typer med `<? extends T>` eller `<? super T>`. Testa:

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

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
