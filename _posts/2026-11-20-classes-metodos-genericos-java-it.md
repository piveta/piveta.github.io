---
layout: post
title: "Classi e metodi generici in Java"
date: 2026-11-20
lang: it
translation_id: classes-metodos-genericos-java
permalink: /it/generic-classes-and-methods-in-java/
share_text: >-
  I generici rendono riutilizzabili classi e metodi mantenendo la sicurezza dei tipi; esempi con Adapter<T>.
---

Il **polimorfismo parametrico** consente a classi, interfacce, record e metodi di adattarsi a un tipo indicato al momento dell'uso. In Java i generici favoriscono il riuso ed evitano conversioni superflue. `List<String>` e `List<Integer>` condividono l'interfaccia, ma il compilatore verifica il tipo degli elementi.

Senza parametro di tipo, `Adapter` usa `Object` nel campo, nel costruttore e nei metodi:

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

Può conservare qualsiasi oggetto, ma non limitare un adattatore specifico a un tipo. Dichiarando `T`, la stessa implementazione usa il tipo scelto dal chiamante:

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

Il client crea un `Adapter<String>`: costruttore e `set` ricevono una stringa, mentre `get` la restituisce. Il programma stampa `Test` e `New Value`:

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## Metodi generici

Anche un metodo può dichiarare un parametro di tipo prima del tipo restituito. `print` accetta liste di tipi diversi senza rinunciare al controllo del compilatore:

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

Il parametro può determinare anche il ritorno. `first` riceve `List<T>` e restituisce `T`: `Integer` per una lista di interi, `String` per una lista di nomi.

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

Le variabili intermedie chiariscono i tipi, ma le espressioni possono essere usate direttamente:

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## Parametro di tipo limitato

`multiply` accetta liste di `Number` o dei suoi sottotipi. Il limite `<T extends Number>` permette di chiamare `doubleValue()` su ogni elemento:

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

Si possono passare sia liste di `Integer` sia liste di `Double`:

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

Il compilatore verifica il parametro a ogni chiamata; il metodo rimane una sola implementazione.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
