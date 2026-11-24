---
layout: post
title: "Clases y métodos genéricos en Java"
date: 2026-11-20
lang: es
translation_id: classes-metodos-genericos-java
permalink: /es/generic-classes-and-methods-in-java/
share_text: >-
  Los genéricos permiten reutilizar clases y métodos con seguridad de tipos; ejemplos con Adapter<T> y métodos genéricos.
---

El **polimorfismo paramétrico** permite que una clase, interfaz, registro o método se adapte al tipo indicado al utilizarlo. En Java, los genéricos facilitan la reutilización y evitan conversiones innecesarias. Por ejemplo, `List<String>` y `List<Integer>` comparten la interfaz, pero el compilador comprueba los elementos de cada lista.

Una clase `Adapter` sin parámetro de tipo utiliza `Object` en su atributo, constructor y métodos:

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

Así puede almacenar cualquier objeto, pero no restringir un adaptador concreto a un tipo. Al declarar `T`, la misma implementación utiliza el tipo elegido por el cliente:

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

Este cliente crea un `Adapter<String>`: el constructor y `set` reciben cadenas, mientras `get` devuelve una cadena. El programa imprime `Test` y luego `New Value`:

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## Métodos genéricos

Un método también puede declarar un parámetro de tipo antes del tipo de retorno. `print` acepta listas de distintos tipos sin perder la comprobación del compilador:

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

El parámetro también puede determinar el retorno. `first` recibe `List<T>` y devuelve `T`: de una lista de enteros obtiene `Integer`; de una lista de nombres, `String`.

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

Las variables intermedias aclaran los tipos, pero se pueden usar las expresiones directamente:

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## Un parámetro de tipo con límite

`multiply` acepta listas de `Number` o de sus subtipos. `<T extends Number>` permite llamar a `doubleValue()` en cada elemento:

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

Puede llamarse tanto con una lista de `Integer` como con una de `Double`:

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

El compilador comprueba el parámetro en cada llamada; el método sigue siendo una única implementación.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
