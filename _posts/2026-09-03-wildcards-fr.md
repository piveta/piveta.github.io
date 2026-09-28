---
layout: post
title: "Wildcards et bornes dans les types génériques en Java"
date: 2026-09-03
lang: fr
translation_id: wildcards-limites-java
permalink: /wildcards-bornes-types-generiques-java/
---

En plus des types génériques spécifiques, nous pouvons utiliser des **wildcards** pour exprimer des types inconnus (`<?>`), restreindre le type spécifié aux sous-types d'un type donné (`<? extends Type>`) ou inclure les supertypes (avec `<? super Type>`). Les sections suivantes décrivent respectivement les wildcards non bornées, à borne supérieure et à borne inférieure. Nous montrons ensuite comment définir plusieurs bornes pour les types génériques.

## Wildcards non bornées

Pour les types inconnus, nous utilisons le point d'interrogation comme type, ce qui permet d'utiliser n'importe quel type dans ce contexte. Par exemple, si une variable est déclarée comme `List<?>` (ou s'il s'agit d'un attribut ou d'un paramètre), elle peut recevoir des objets `List` avec n'importe quel paramètre de type valide, comme `String`, `Integer`, etc. Ces types génériques inconnus sont appelés **wildcards non bornées** (`<?>`), car ils n'imposent aucune borne de type.

Par exemple :

```java
List<?> l = new ArrayList<String>();
// ou, par exemple
l = new LinkedList<Integer>();
```

Bien que cette manière de déclarer des variables puisse sembler intéressante, elle présente des limitations. Dans ces situations, nous ne connaissons pas le type des objets contenus dans la liste. Nous ne pouvons donc pas, par exemple, ajouter des éléments à la liste (à l'exception de `null`, qui est compatible avec tout type référence en Java), car rien ne garantit que l'objet ajouté ait le même type que le paramètre de type de la liste.

Si nous essayons d'ajouter un élément à la liste (dans ce cas, `l`), nous obtenons donc une erreur à la compilation :

```java
void main(){
    List<?> l = new ArrayList<String>();
    // Compilation error: 
    //    "The method add(capture#2-of ?) in the type 
    //     List<capture#2-of ?> is not applicable 
    //     for the arguments (String)"
    l.add("Maria");
}
```

Les types non bornés sont couramment utilisés lorsque nous voulons uniquement lire les données, sans les modifier. Nous pourrions par exemple avoir une méthode qui reçoit une liste et affiche ses éléments sans préciser le type des éléments de la liste :

```java
public void print(List<?> list) {
    for (Object obj : list)
        IO.println(obj);
}
void main(){
    print(List.of(1, 2, 3));
    print(List.of("A", "B", "C"));
}
```

L'exécution de la méthode `main` afficherait :

```text
1
2
3
A
B
C
```

Ici, nous utilisons l'affichage comme exemple, mais nous pourrions parcourir les objets, les utiliser dans des *streams*, les filtrer avec `instanceof`, obtenir la taille de la liste, vérifier si un objet donné est contenu dans la liste, les transformer et les copier vers une liste typée, entre autres opérations. Ce que nous ne pouvons pas faire, c'est modifier directement la liste (avec `add` ou `set`, par exemple, sauf avec `null`).

## Wildcards à borne supérieure

Les **wildcards à borne supérieure** permettent de spécifier que seul un objet d'un type donné ou de l'un de ses sous-types (obtenus par héritage ou implémentation d'une interface) peut être utilisé comme paramètre de type. La notation `<? extends T>` indique que la wildcard doit être de type `T` ou d'un type qui étend `T`.

Par exemple, si je déclare une liste dont la wildcard étend `Number`, je peux lui affecter des objets de n'importe laquelle de ses sous-classes (comme `Double` ou `Integer`). Si `Number` était une classe concrète (elle est abstraite), nous pourrions également affecter un objet de la classe elle-même. L'exemple suivant montre précisément ce cas :

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

Comme pour les wildcards non bornées, nous ne pouvons pas ajouter d'éléments à la liste `l`, car nous ne connaissons pas exactement son type. Ainsi, les deux premiers appels à `add` produisent des erreurs de compilation :

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

Bien que nous sachions, à la lecture du code, que l'objet affecté à la variable `l` est une liste d'entiers, le compilateur sait que `l` a un type inconnu et n'autorise donc pas l'ajout de valeurs. Lors de la lecture, les valeurs sont lues comme des `Number`, qui constitue la borne supérieure.

## Wildcards à borne inférieure

Les **wildcards à borne inférieure** permettent de spécifier que seul un objet d'un type donné ou de l'un de ses supertypes peut être utilisé comme paramètre de type. La notation `<? super T>` indique que la wildcard doit être de type `T` ou d'une superclasse de `T`.

Par exemple, si je déclare une liste dont la wildcard a `Number` comme borne inférieure, je peux lui affecter des objets de n'importe laquelle de ses superclasses (dans le cas de `Number`, uniquement `Object`, puisque `Number` n'a pas de superclasse explicite).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

Il est permis d'ajouter des éléments du type de la borne inférieure (ici `Number`) ou de l'un de ses sous-types (comme `Double` ou `Integer`, par exemple). L'exemple suivant montre une liste dont la wildcard a `Number` comme borne inférieure. Dans ce cas, nous pouvons instancier une `ArrayList` de nombres (ou de sa superclasse `Object`). Nous pouvons ajouter des éléments de l'une de ses sous-classes (nous ne pouvons pas ajouter un objet de type `Number`, car il s'agit d'une classe abstraite qui ne peut pas avoir d'instances directes). L'exemple montre trois ajouts. Les deux premiers sont autorisés car les éléments sont des sous-types de `Number` (`10` est un `Integer` et `1.0` est un `Double`). Le troisième ajout n'est pas autorisé et produit une erreur de compilation, car `Object` n'est pas un descendant de `Number`.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

Si nous créions l'`ArrayList` avec `Object` comme paramètre de type, le troisième ajout resterait interdit à la compilation et produirait la même erreur (les deux premiers ajouts resteraient autorisés), car le type de la liste est toujours inconnu (nous savons seulement qu'il s'agit de `Number` ou de l'un de ses supertypes).

## Plusieurs bornes

En Java, un type générique peut avoir **plusieurs bornes**, ce qui signifie que le paramètre de type peut être restreint aux types qui étendent (ou sont) une classe spécifique et qui implémentent une ou plusieurs interfaces. La syntaxe suit la forme `<T extends Class & Interface1 & Interface2>`. Si une classe est utilisée comme borne, elle doit être spécifiée en premier, suivie des interfaces. S'il n'y a pas de classe, seuls des interfaces peuvent être listés.

Par exemple, la classe `MultipleBounds` possède un type générique `T` qui étend la classe `Number` et implémente les interfaces `Comparable<T>` et `Serializable` :

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

Dans cet exemple, `T` peut être `Number` ou un type qui hérite de `Number` et implémente également `Comparable<T>` et `Serializable`. Cela est utile lorsque nous avons besoin de plusieurs garanties, par exemple l'accès aux méthodes de la superclasse et aux contrats définis par plusieurs interfaces. Cette combinaison rend le code plus flexible tout en restant fortement typé, en évitant les erreurs à la compilation et en garantissant que toutes les méthodes requises sont disponibles pour le type générique utilisé.

---

*Cet article est adapté du contenu du livre <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, d'<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
