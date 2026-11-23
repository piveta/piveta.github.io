---
layout: post
title: "Esercizi sui generici Java"
date: 2026-11-20
lang: it
translation_id: exercicios-tipos-genericos-java
permalink: /it/java-generics-exercises/
share_text: >-
  Dieci esercizi su metodi generici, wildcard, ereditarietà, Optional<T> e Box<T>.
---

Gli esercizi derivano dal capitolo sui generici di **Orientação a Objetos com Java**. La struttura del codice segue il libro; identificatori, commenti e messaggi sono in inglese.

1. Studiate le interfacce principali del framework Collections e spiegate come i generici consentono di riutilizzare le strutture senza modificare le classi.
2. Create un metodo statico generico `max` che riceva due oggetti `Comparable` e restituisca il maggiore.
3. Create un metodo statico che riceva e stampi una lista di qualsiasi tipo. Usate un wildcard.
4. Create un metodo statico che sommi una lista numerica. Usate `extends` per ammettere solo liste di `Number`.
5. Considerate questa gerarchia:

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   Il metodo seguente riceve una lista di strumenti o di loro sottoclassi:

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   Passate una lista di `Guitar` e una di `Flute`. Poi provate ad aggiungere uno strumento dentro il metodo e osservate l'errore di compilazione.
6. Implementate un metodo generico che riceva elementi sia `Number` sia `Comparable` e restituisca il maggiore.
7. Implementate questi tre metodi e provateli con liste di `Car`, `Motorcycle` e `Vehicle`:

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

8. Provate a scrivere `boolean checkList(Object obj)` affinché riconosca solo `List<String>`. Verificate se Java lo consente direttamente e proponete un'alternativa con `List<?>` o `List<Object>`.
9. Studiate `Optional<T>` e create `printOptional(Optional<T> opt)` per stampare il valore o *empty*. Provate `Optional<String>` e `Optional<Integer>`.
10. Create `Box<T>` con `store(T item)` (rifiuta `null`), `get()` e `compare(Box<T> b1, Box<T> b2)` mediante `compareTo`. Aggiungete `compareWithInheritance` per scatole di tipi diversi legati da ereditarietà, usando `<? extends T>` o `<? super T>`. Provate:

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

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
