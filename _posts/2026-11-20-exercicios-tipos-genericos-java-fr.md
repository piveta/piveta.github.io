---
layout: post
title: "Exercices sur les génériques Java"
date: 2026-11-20
lang: fr
translation_id: exercicios-tipos-genericos-java
permalink: /fr/java-generics-exercises/
share_text: >-
  Dix exercices sur méthodes génériques, jokers, héritage, Optional<T> et Box<T>.
---

Ces exercices proviennent du chapitre sur les génériques d'**Orientação a Objetos com Java**. La structure du code suit le livre, avec identifiants, commentaires et messages en anglais.

1. Étudiez les principales interfaces du framework des collections Java et l'usage des génériques qui permet de réutiliser les structures sans modifier leurs classes.
2. Créez une méthode statique générique `max` recevant deux objets `Comparable` et renvoyant le plus grand.
3. Créez une méthode statique qui reçoit et affiche une liste de n'importe quel type. Utilisez un joker.
4. Créez une méthode statique additionnant une liste numérique. Utilisez `extends` pour n'accepter que des listes de `Number`.
5. Considérez cette hiérarchie :

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   La méthode suivante reçoit une liste d'instruments ou de sous-classes :

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   Passez une liste de `Guitar`, puis une liste de `Flute`. Essayez ensuite d'ajouter un instrument dans la méthode et observez l'erreur du compilateur.
6. Implémentez une méthode générique recevant des éléments qui sont à la fois `Number` et `Comparable`, et renvoyant le plus grand.
7. Implémentez ces méthodes et testez-les avec des listes de `Car`, `Motorcycle` et `Vehicle` :

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

8. Essayez d'écrire `boolean checkList(Object obj)` pour reconnaître uniquement `List<String>`. Déterminez si Java le permet directement et proposez une alternative avec `List<?>` ou `List<Object>`.
9. Étudiez `Optional<T>` et écrivez `printOptional(Optional<T> opt)` pour afficher la valeur ou *empty*. Testez `Optional<String>` et `Optional<Integer>`.
10. Créez `Box<T>` avec `store(T item)` (refusant `null`), `get()` et `compare(Box<T> b1, Box<T> b2)` utilisant `compareTo`. Ajoutez `compareWithInheritance` pour des boîtes de types différents liés par héritage, avec `<? extends T>` ou `<? super T>`. Testez :

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

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
