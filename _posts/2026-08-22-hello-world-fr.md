---
layout: post
title: "Hello World - Version traditionnelle vs. version simplifiée"
date: 2026-08-22
lang: fr
translation_id: hello-world
permalink: /hello-world-fr/
share_text: >-
  L’article suit un programme Hello World Java classique, de la classe et de main à la compilation et à l’exécution. Il présente ensuite les fichiers source compacts et les méthodes main d’instance disponibles à partir de Java 25.
---

Il est courant de commencer l’étude d’un langage de programmation en écrivant un programme appelé **Hello World**, qui affiche le texte `Hello World!` sur la sortie standard de l’appareil, généralement l’écran. En Java, nous pouvons écrire ce programme comme suit :

```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```

Dans ce programme, nous avons une classe nommée `Hello`. Dans les systèmes orientés objet, les classes permettent de modéliser des concepts du domaine d’application étudié. Les classes encapsulent à la fois les données et le comportement associés à un concept particulier.

La classe `Hello` possède une seule méthode, appelée `main`, qui reçoit un tableau de chaînes de caractères contenant les arguments de la ligne de commande fournis lors de l’exécution du programme, le cas échéant. Dans cet exemple, ces arguments ne sont pas utilisés.

La méthode `main` est statique, ce qui signifie qu’il s’agit d’une méthode de classe et non d’une méthode d’instance. Elle peut donc être appelée sans créer d’objet de la classe `Hello`.

À l’intérieur de la méthode `main`, il y a un appel à la méthode `println`. Cette méthode appartient à la classe `PrintStream` et affiche à l’écran la valeur passée en argument, suivie d’un terminateur de ligne.

La méthode `println` est appelée par l’intermédiaire du champ `out` de la classe `System`. Ce champ est de type `PrintStream` et permet d’accéder à la sortie standard du système.

## Compilation et exécution

Les programmes Java sont d’abord compilés en une représentation intermédiaire appelée **bytecode**, ce qui assure leur portabilité. Ces bytecodes sont ensuite exécutés par une machine virtuelle Java (JVM), qui les convertit en code machine adapté à la plateforme sous-jacente.

Pour compiler le programme, celui-ci doit être enregistré dans un fichier nommé `Hello.java`. En Java, les fichiers contenant des types publics portent normalement le même nom que le type.

Nous pouvons utiliser un environnement de développement intégré (**IDE**) ou invoquer directement le compilateur depuis la ligne de commande, à condition qu’un JDK soit installé.

Les programmes Java sont normalement écrits dans un IDE, qui fournit des fonctionnalités améliorant la productivité pendant le développement, telles que la navigation dans le code source, le refactoring, l’analyse statique, la compilation, les tests et le débogage.

Parmi les IDE les plus populaires pour Java, on trouve :

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

Nous pouvons également compiler directement le programme depuis la ligne de commande avec le compilateur `javac` :

```text
    javac Hello.java
```

La commande prend `Hello.java` en entrée et produit le fichier `Hello.class`, qui contient la version compilée du programme.

Après la compilation, nous pouvons exécuter le programme avec la commande `java` :

```text
    java Hello
```

La sortie sera :

```text
    Hello World!
```

## Une approche plus simple avec Java 25+

À partir de Java 25, une fonctionnalité développée en tant que *preview* depuis Java 21 est devenue définitive : **Compact Source Files and Instance Main Methods**. Elle permet d’écrire de petits programmes avec moins de code standard, en omettant la déclaration explicite de la classe et en simplifiant la méthode `main`.

Ainsi, le programme précédent peut maintenant être écrit en Java 26 (la version actuelle) comme suit :

```java
    void main() {
        IO.println("Hello World!");
    }
```

Dans ce cas, nous n’avons pas besoin de déclarer explicitement la classe ni d’écrire `public static void main(String[] args)`. Le compilateur considère que le fichier déclare implicitement une classe, et la méthode `main` peut être une méthode d’instance.

Nous pouvons également utiliser la classe `IO`, qui fournit des opérations simples d’entrée et de sortie sur la console. En Java 26, `IO` appartient au package `java.lang` et est donc implicitement disponible. Pour appeler ses méthodes, nous devons toutefois utiliser le nom de la classe, comme dans `IO.println(...)`.

Puisque cette fonctionnalité n’est plus en *preview*, nous n’avons pas besoin d’options de compilation particulières. Le programme peut être compilé normalement :

```text
    javac Hello.java
```

et exécuté de la même manière :

```text
    java Hello
```

Il est également possible d’exécuter directement un fichier source à l’aide du lanceur `java` :

```text
    java Hello.java
```

Dans ce cas, le code source est compilé en mémoire par le lanceur lui-même avant l’exécution. Ce mécanisme permet d’exécuter des programmes directement à partir de fichiers source sans produire explicitement de fichier `.class`.

L’utilisation de fichiers source compacts est particulièrement intéressante pour les petits exemples, les programmes d’apprentissage, les scripts et les expérimentations. Lorsque le programme grandit et nécessite une structure plus élaborée, nous pouvons naturellement revenir à la forme traditionnelle, avec des déclarations explicites de classes et de méthodes.

Le processus effectué par les IDE est essentiellement similaire. En plus de la compilation et de l’exécution, ils fournissent des fonctionnalités de débogage, de test, de refactoring, de création et de gestion de projets, de création de bibliothèques, de gestion des versions et bien d’autres tâches.

---

*Cet article est une adaptation de contenu du livre <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, d’<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
