---
layout: post
title: "Generische Klassen und Methoden in Java"
date: 2026-11-20
lang: de
translation_id: classes-metodos-genericos-java
permalink: /de/generic-classes-and-methods-in-java/
share_text: >-
  Generische Typen ermöglichen wiederverwendbare Klassen und Methoden mit Typsicherheit; Beispiele mit Adapter<T>.
---

**Parametrischer Polymorphismus** lässt Klassen, Schnittstellen, Records und Methoden mit einem beim Gebrauch angegebenen Typ arbeiten. Java-Generics fördern Wiederverwendung und vermeiden unnötige Typumwandlungen. `List<String>` und `List<Integer>` nutzen dieselbe Schnittstelle, während der Compiler die jeweiligen Elementtypen prüft.

Ohne Typparameter verwendet `Adapter` für Feld, Konstruktor und Methoden `Object`:

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

Die Klasse kann beliebige Objekte speichern, aber einen bestimmten Adapter nicht auf einen Typ beschränken. Mit `T` verwendet dieselbe Implementierung den vom Aufrufer gewählten Typ:

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

Der folgende Client erzeugt `Adapter<String>`. Konstruktor und `set` erwarten `String`, `get` liefert `String`. Ausgegeben werden `Test` und `New Value`:

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## Generische Methoden

Auch Methoden deklarieren Typparameter, und zwar vor dem Rückgabetyp. `print` nimmt Listen verschiedener Typen an, ohne die Typprüfung aufzugeben:

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

Der Typparameter kann zugleich den Rückgabetyp bestimmen. `first` nimmt `List<T>` entgegen und gibt `T` zurück: bei ganzen Zahlen `Integer`, bei Namen `String`.

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

Zwischenvariablen verdeutlichen die Typen; die Ausdrücke können auch direkt verwendet werden:

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## Begrenzter Typparameter

`multiply` akzeptiert Listen von `Number` oder Untertypen. Die Schranke `<T extends Number>` erlaubt den Aufruf von `doubleValue()`:

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

Sowohl eine `Integer`- als auch eine `Double`-Liste kann übergeben werden:

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

Der Compiler prüft den Typparameter bei jedem Aufruf; die Methode bleibt eine einzige Implementierung.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
