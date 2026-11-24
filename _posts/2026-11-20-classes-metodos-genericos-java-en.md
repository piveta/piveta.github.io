---
layout: post
title: "Generic classes and methods in Java"
date: 2026-11-20
lang: en
translation_id: classes-metodos-genericos-java
permalink: /en/generic-classes-and-methods-in-java/
share_text: >-
  Generic types let classes and methods work with different types while preserving type safety. See Adapter<T> and generic methods with parameters and return values.
---

**Parametric polymorphism** lets a class, interface, record, or method adapt to a type specified when it is used. In Java, generics promote code reuse and avoid unnecessary casts. The collections framework uses them extensively: `List<String>` and `List<Integer>` share the same interface, but the compiler checks each list's element type.

Consider an `Adapter` class that stores an object. Without a type parameter, its field, constructor, and methods use `Object`:

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

This class can hold any object, but it cannot restrict a particular adapter to one type. By declaring `T` alongside the class name, the same implementation works with the type chosen by its client:

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

For example, this client creates an `Adapter<String>`. Its constructor and `set` method accept a `String`, and `get` returns a `String`:

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

The program prints `Test` and then `New Value`.

## Generic methods

A **method** may also declare a type parameter before its return type. Here, `print` accepts lists with different element types while retaining compile-time type checking:

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

The type parameter can determine the return type as well. `first` receives a `List<T>` and returns a `T`. A list of integers therefore produces an `Integer`, while a list of names produces a `String`:

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

The program prints `1` and `Mary`. The intermediate variables make the types explicit; when they are unnecessary, the expressions can be used directly:

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## Bounding a method's type parameter

The `multiply` method accepts lists whose elements are `Number` or one of its subtypes. The bound `<T extends Number>` allows the method to call `doubleValue()` on each element:

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

It can be called with either a list of `Integer` or a list of `Double`:

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

The compiler checks the type parameter for each call. The method itself remains a single implementation.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
