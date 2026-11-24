---
layout: post
title: "Generiska klasser och metoder i Java"
date: 2026-11-20
lang: sv
translation_id: classes-metodos-genericos-java
permalink: /sv/generic-classes-and-methods-in-java/
share_text: >-
  Generiska typer gör klasser och metoder återanvändbara med typkontroll; exempel med Adapter<T>.
---

**Parametrisk polymorfism** låter en klass, ett gränssnitt, en record-typ eller en metod anpassas till en typ som anges vid användningen. Javas generiska typer underlättar återanvändning och minskar onödiga typomvandlingar. `List<String>` och `List<Integer>` delar gränssnitt, men kompilatorn kontrollerar elementtypen i varje lista.

Utan typparameter använder `Adapter` `Object` i fält, konstruktor och metoder:

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

Klassen kan lagra vilket objekt som helst, men kan inte begränsa en viss adapter till en typ. Med `T` använder samma implementation den typ som anroparen väljer:

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

Klienten skapar en `Adapter<String>`. Konstruktorn och `set` tar emot en sträng; `get` returnerar en sträng. Programmet skriver ut `Test` och sedan `New Value`:

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## Generiska metoder

En metod kan också deklarera en typparameter före returtypen. `print` tar emot listor med olika typer utan att kompilatorns typkontroll försvinner:

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

Parametern kan även bestämma returtypen. `first` tar emot `List<T>` och returnerar `T`: `Integer` för en heltalslista och `String` för en namnlista.

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

Mellanvariablerna visar typerna tydligt; uttrycken kan även användas direkt:

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## Begränsad typparameter

`multiply` tar emot listor med `Number` eller dess subtyper. Gränsen `<T extends Number>` gör det möjligt att anropa `doubleValue()` på varje element:

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

Både en lista med `Integer` och en med `Double` fungerar:

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

Kompilatorn kontrollerar typen vid varje anrop, medan metoden förblir en enda implementation.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
