---
layout: post
title: "Le polymorphisme en Java"
date: 2026-10-21
lang: fr
translation_id: polimorfismo-em-java
permalink: /polymorphisme-java-fr/
share_text: >-
  Introduction au polymorphisme ad hoc, paramétrique et de sous-type, avec des exemples Java.
---

En programmation orientée objet, le **polymorphisme** est la capacité d’une opération à se comporter différemment selon la classe de l’objet concerné. Ses principales formes sont les suivantes :

- **Polymorphisme ad hoc (ou surcharge)** : des méthodes de même nom peuvent avoir des paramètres différents ; l’appel choisit la version compatible avec ses arguments.
- **Polymorphisme paramétrique** : les classes et méthodes génériques fonctionnent avec des types qui sont précisés au moment de leur utilisation.
- **Polymorphisme de sous-type** : une sous-classe peut redéfinir une méthode et l’implémentation exécutée dépend de la classe concrète de l’objet.

Les exemples suivants montrent ces trois formes en Java, en commençant par la surcharge. La classe `Figure` possède deux méthodes surchargées nommées `resize`. La première reçoit un `percentage` de type `Double` ; la seconde reçoit deux coordonnées, `x` et `y`, de type `Integer`.

```java
public class Figure {
    public void resize(Double percentage) {
        // Redimensionnement en pourcentage
    }
    public void resize(Integer x, Integer y) {
        // Redimensionnement selon les coordonnées
    }
}
```

Pour le **polymorphisme paramétrique**, on peut créer des types paramétrés à l’aide de `<` et `>`. La classe `ArrayList`, par exemple, possède un paramètre de type `E` qui précise le type des objets que la liste peut stocker. Ce paramètre sert aussi de paramètre formel à la méthode `add`. Le type attendu par `add` est donc celui indiqué lors de l’instanciation d’`ArrayList`. Notez qu’elle étend `AbstractList` et implémente notamment les interfaces `List`, `RandomAccess`, `Cloneable` et `Serializable`, avec le même type `E`.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // Implémentation de add
    }
    // Autres méthodes et champs de la classe
}
```

On peut ainsi créer une liste de chaînes de caractères avec le paramètre de type `String` et y ajouter des éléments en appelant `add`[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

Dans ce cas, le compilateur attend un `String` comme argument de `add`. Un objet d’un autre type provoque une erreur de compilation. Pour créer une liste d’entiers, on peut transmettre un autre type à `ArrayList`, ici `Integer` :

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

Pour le **polymorphisme de sous-type**, supposons que la classe `Figure` possède une méthode `draw`, qui peut également être appelée sur les objets des classes `Triangle`, `Circle` et `Rectangle`. Chacune de ces classes redéfinit cette méthode pour mettre en œuvre son propre comportement de dessin. Dans le code suivant, chaque appel à `draw` invoque une implémentation différente, selon que l’objet affecté à `figure` est un `Circle`, un `Triangle` ou un `Rectangle`.

```java
Figure figure = new Circle(10);
// Appelle la méthode draw de Circle
figure.draw();
figure = new Triangle(20);
// Appelle la méthode draw de Triangle
figure.draw();
figure = new Rectangle(10, 20);
// Appelle la méthode draw de Rectangle
figure.draw();
```

[^8]: Pour utiliser `ArrayList`, il faut généralement l’importer avec `import java.util.ArrayList;`. Les importations ne sont pas nécessaires dans les fichiers source compacts. Dans les fichiers source classiques, on peut importer le module `java.base` avec `import module java.base;`.

---

*Cet article adapte du contenu du livre <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, d’<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articles associés

- [Concepts fondamentaux de la programmation orientée objet](/concepts-fondamentaux-poo-fr/)
- [Classes en Java](/classes-en-java-fr/)
- [Héritage en Java](/heritage-java-fr/)
- [Interfaces en Java](/interfaces-java-fr/)
- [Liens sur la POO et Java](/liens-poo-java-fr/)
- [Exercices de programmation orientée objet](/exercices-poo-fr/)
