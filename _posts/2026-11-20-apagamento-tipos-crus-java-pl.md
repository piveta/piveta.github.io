---
layout: post
title: "Wymazywanie typów i typy surowe w Javie"
date: 2026-11-20
lang: pl
translation_id: apagamento-tipos-crus-java
permalink: /pl/type-erasure-and-raw-types-in-java/
share_text: >-
  Wymazywanie zapewnia zgodność ze starym kodem; typy surowe tracą kontrolę elementów.
---

Java 5 wprowadziła generyki z zachowaniem zgodności z wcześniejszym kodem. Podczas **wymazywania typów** (*type erasure*) kompilator sprawdza parametry generyczne, a następnie usuwa je z reprezentacji wykonywanej przez JVM. Zastępuje je ograniczeniami, zwykle `Object` lub pierwszym zadeklarowanym ograniczeniem.

Po wymazaniu `Adapter<T>` przypomina w przybliżeniu klasę używającą `Object`:

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

Kod klienta bez parametrów typu wyglądałby tak:

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

Fragmenty **ilustrują** proces, nie są dosłownym zapisem bajtkodu. Argumenty typów nie są dostępne podczas działania w taki sam sposób jak podczas kompilacji, co ogranicza niektóre operacje refleksji.

## Typy surowe

Lista z parametrem kontroluje typ elementów:

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

*Typ surowy* pomija argument typu w deklaracji i konstruktorze:

```java
void main(){
    List names = new ArrayList();
}
```

Tracimy wtedy kontrolę oferowaną przez `List<String>`; lista może zawierać napis i liczbę całkowitą:

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>` oznacza listę elementów **nieznanego typu**, do której nie można dodawać dowolnych wartości poza `null`. Surowa `List` przyjmuje je bez takiej kontroli. W nowym kodzie używaj parametru typu lub symbolu wieloznacznego; typ surowy przydaje się głównie przy starszych bibliotekach.

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
