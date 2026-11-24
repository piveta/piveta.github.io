---
layout: post
title: "Type erasure and raw types in Java"
date: 2026-11-20
lang: en
translation_id: apagamento-tipos-crus-java
permalink: /en/type-erasure-and-raw-types-in-java/
share_text: >-
  Learn how Java erases generic type parameters at compile time, why raw types support older code, and what type safety they give up.
---

Java 5 introduced generics while preserving compatibility with earlier code. The compiler therefore uses **type erasure**: it checks generic types during compilation and removes their type parameters from the representation executed by the JVM. Type parameters are replaced by their bounds, usually `Object` or the first declared bound.

For example, after erasure, the book's generic `Adapter<T>` class resembles a class that works with `Object`:

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

The corresponding client, written without type parameters, would look like this:

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

These fragments **illustrate** erasure; they are not literal transcriptions of bytecode. The type information that helps the compiler reject incompatible uses is not available in the same way at runtime. This limits some operations that need to recognize generic type arguments during execution.

## Raw types

Java also permits a generic type to be used **without its type argument** so that older code remains valid. First, compare a parameterized list:

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

With a *raw type*, both the declaration and construction omit the type argument:

```java
void main(){
    List names = new ArrayList();
}
```

That choice loses the element checking a `List<String>` would provide. The following code accepts both a string and an integer in the same list:

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List` and `List<?>` do not mean the same thing. `List<?>` is a list of an **unknown type**: you cannot add an arbitrary element, apart from `null`. A raw `List` accepts elements without the checks provided by a type argument.

In new code, provide the appropriate type argument or use a wildcard when the type is unknown. Raw types are mainly useful when interacting with legacy libraries.

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
