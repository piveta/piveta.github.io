---
layout: post
title: "Lire et écrire dans la console Java"
date: 2026-11-20
lang: fr
translation_id: leitura-escrita-java
permalink: /fr/reading-and-writing-on-the-java-console/
share_text: >-
  Lire et écrire dans la console Java : exemples du livre en anglais.
---

En Java 25, `IO` facilite les entrées et sorties en console. Les exemples de fichiers source compacts peuvent nécessiter l’activation des fonctionnalités preview. `print` ne termine pas la ligne, contrairement à `println` :

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

`Scanner` lit l’entrée standard. Après `nextInt()`, un appel à `nextLine()` consomme le saut de ligne avant la lecture de l’adresse :

```java
import java.util.Scanner;
void main(){
    var s = new Scanner(System.in);
    IO.println("Name: ");
    var name = s.nextLine(); 
    IO.println("Age: ");
    var age = s.nextInt(); 
    s.nextLine(); // Consumes the line break
    IO.println("Address: ");
    var address = s.nextLine(); 
    IO.println("Entered data:");
    IO.println("Name: " + name + ", Age: " + age);
    IO.println("Address: " + address);
}
```

`readln` renvoie une `String`. `Integer.parseInt` convertit l’âge en entier ; une entrée incorrecte provoque une `NumberFormatException`, non traitée dans cet exemple :

```java
import static java.lang.IO.*; 
void main(){
    var name = readln("Name: ");
    var age = Integer.parseInt(readln("Age: ")); 
    var address = readln("Address: ");
    println("Entered data:");
    println("Name: " + name + ", Age: " + age);
    println("Address: " + address);
}
```

Les commentaires utilisent `//` pour une ligne et `/* ... */` pour plusieurs lignes :

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
