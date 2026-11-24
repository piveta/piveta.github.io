---
layout: post
title: "Klasy i metody generyczne w Javie"
date: 2026-11-20
lang: pl
translation_id: classes-metodos-genericos-java
permalink: /pl/generic-classes-and-methods-in-java/
share_text: >-
  Typy generyczne umożliwiają ponowne użycie klas i metod z kontrolą typów; przykłady z Adapter<T>.
---

**Polimorfizm parametryczny** pozwala klasie, interfejsowi, rekordowi lub metodzie działać z typem wskazanym podczas użycia. W Javie generyki ułatwiają ponowne wykorzystanie kodu i ograniczają zbędne rzutowania. `List<String>` i `List<Integer>` mają ten sam interfejs, ale kompilator sprawdza typ elementów każdej listy.

Bez parametru typu klasa `Adapter` używa `Object` w polu, konstruktorze i metodach:

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

Może przechować dowolny obiekt, lecz nie ogranicza konkretnego adaptera do jednego typu. Po zadeklarowaniu `T` ta sama implementacja używa typu wybranego przez klienta:

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

Klient tworzy `Adapter<String>`. Konstruktor i `set` przyjmują napis, a `get` go zwraca. Program wypisuje `Test`, a potem `New Value`:

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## Metody generyczne

Metoda również może zadeklarować parametr typu przed typem wyniku. `print` przyjmuje listy różnych typów, zachowując kontrolę kompilatora:

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

Parametr może określać także typ wyniku. `first` przyjmuje `List<T>` i zwraca `T`: `Integer` dla listy liczb całkowitych lub `String` dla listy nazw.

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

Zmienne pośrednie pokazują typy; można też użyć wyrażeń bezpośrednio:

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## Ograniczony parametr typu

`multiply` przyjmuje listy `Number` lub jego podtypów. Ograniczenie `<T extends Number>` pozwala wywołać `doubleValue()` dla każdego elementu:

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

Można przekazać listę `Integer` albo `Double`:

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

Kompilator sprawdza parametr przy każdym wywołaniu, a metoda pozostaje jedną implementacją.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
