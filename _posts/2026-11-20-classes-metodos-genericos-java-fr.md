---
layout: post
title: "Classes et méthodes génériques en Java"
date: 2026-11-24
lang: fr
translation_id: classes-metodos-genericos-java
permalink: /fr/generic-classes-and-methods-in-java/
share_text: >-
  Les génériques permettent de réutiliser classes et méthodes tout en conservant la sûreté des types.
---

Le **polymorphisme paramétrique** permet à une classe, une interface, un record ou une méthode de s'adapter au type indiqué lors de son utilisation. En Java, les génériques favorisent la réutilisation et évitent des conversions inutiles. `List<String>` et `List<Integer>` partagent la même interface, mais le compilateur vérifie les éléments de chacune.

Sans paramètre de type, `Adapter` emploie `Object` pour son champ, son constructeur et ses méthodes :

```java
public class Adapter{
    Object object;
    public Object get(){
        return object;
    }
    public void set(Object value){
        object = value;
    }
    public Adapter(Object initial){
       object = initial;
    }
}
```

La classe peut recevoir n'importe quel objet, sans toutefois limiter un adaptateur donné à un seul type. Avec `T`, la même implémentation utilise le type choisi par le client :

```java
public class Adapter<T>{
    T object;
    public T get(){
        return object;
    }
    public void set(T value){
        object = value;
    }
    public Adapter(T initial){
        object = initial;
    }
}
```

Ce client crée un `Adapter<String>`. Le constructeur et `set` acceptent une chaîne, et `get` en renvoie une. Le programme affiche `Test` puis `New Value` :

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## Méthodes génériques

Une méthode peut aussi déclarer un paramètre de type avant son type de retour. `print` accepte des listes de types différents tout en gardant la vérification du compilateur :

```java
public static <T> void print(List<T> list){
    for (T element : list)
        IO.println(element);
}
void main(){
    List<Integer> integers = List.of(1, 2, 3, 4);
    List<String> names = List.of("Mary", "John", "Carol");
    print(integers);
    print(names);
}
```

Le paramètre peut également déterminer le type de retour. `first` reçoit `List<T>` et renvoie `T` : `Integer` pour une liste d'entiers, `String` pour une liste de noms.

```java
public static <T> T first(List<T> list) {
    return list.isEmpty() ? null : list.get(0);
}
void main(){
    List<Integer> integers = List.of(1, 2, 3, 4);
    List<String> names = List.of("Mary", "John", "Carol");
    Integer integer = first(integers);
    String name = first(names);
    IO.println(integer);
    IO.println(name);
}
```

Les variables intermédiaires rendent les types explicites ; les expressions peuvent aussi être utilisées directement :

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## Paramètre de type borné

`multiply` accepte des listes de `Number` ou de ses sous-types. La borne `<T extends Number>` permet d'appeler `doubleValue()` sur chaque élément :

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

Une liste d'`Integer` ou de `Double` peut être passée :

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

Le compilateur vérifie le type à chaque appel ; la méthode reste une seule implémentation.

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
