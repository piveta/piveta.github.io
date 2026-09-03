---
layout: post
title: "Wildcards and Bounds in Java Generic Types"
date: 2026-09-03
lang: en
translation_id: wildcards-limites-java
permalink: /wildcards-bounds-java-generic-types/
---

In addition to specific generic types, we can use **wildcards** to express unknown types (`<?>`), to restrict the specified type to include subtypes of a given type (`<? extends Type>`), or to include supertypes (using `<? super Type>`). The following sections describe unbounded, upper-bounded, and lower-bounded wildcards, respectively. Next, we show how we can define multiple bounds for generic types.

## Unbounded Wildcards

For unknown types, we use the question mark as a type, allowing any type to be used in that context. For example, if I have a variable declared as `List<?>` (or an attribute or parameter), it could receive `List` objects with any valid type parameter, such as `String`, `Integer`, etc. Such unknown generic types are called **unbounded wildcards** (`<?>`), because they impose no type bound.

For example, we could have:

```java
List<?> l = new ArrayList<String>();
// or, for example
l = new LinkedList<Integer>();
```

Although the option of declaring variables this way may seem attractive, there are limitations. In such cases, we do not know the type of the objects in the list. Therefore, we cannot, for example, add elements to the list (except `null`, which is compatible with any reference type in Java), because there is no guarantee that the object being added has the same type as the list's type parameter.

Thus, if we tried to add an element to the list object (in this case, `l`), we would get a compile-time error:

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

Unbounded types are commonly used when we only want to read data, without modifying it. For example, we could have a method that receives a list and prints its elements without specifying the type of the list's elements:

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

Running the `main` method would show:

```text
1
2
3
A
B
C
```

Here we use printing as an example, but we could iterate over the objects, use them in *streams*, filter them with `instanceof`, obtain the list size, check whether a given object is contained, transform and copy them to a typed list, among other operations. What we cannot do is modify the list directly (using `add` or `set`, for example, except with `null`).

## Upper-Bounded Wildcards

**Upper-bounded wildcards** allow us to specify that only an object of a given type or one of its subtypes (obtained through subclassing or interface implementation) can be used as a type parameter. The notation `<? extends T>` is used to specify that the wildcard must be of type `T` or of a type that extends `T`.

For example, if I declare a list whose wildcard extends `Number`, I could assign objects of any of its subclasses (such as `Double` or `Integer`). If `Number` were a concrete class (it is abstract), we could also assign an object of the class itself. The following example shows precisely this:

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

As with unbounded wildcards, we cannot add elements to the list `l`, because we do not know exactly what the type of the list is. Thus, the first two calls to the `add` method produce compilation errors:

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

Although we know, by reading the code, that the object assigned to variable `l` is a list of integers, the compiler knows that `l` has an unknown type and therefore does not allow values to be added. When reading, the values are read as `Number`, which is the upper bound.

## Lower-Bounded Wildcards

**Lower-bounded wildcards** allow us to specify that only an object of a given type or one of its supertypes can be used as a type parameter. The notation `<? super T>` is used to specify that the wildcard must be of type `T` or of a superclass of `T`.

For example, if I declare a list whose wildcard has `Number` as a lower bound, I could assign objects of any of its superclasses (in the case of `Number`, only `Object`, since `Number` has no explicit superclass).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

It is permitted to add elements of the lower-bound type (in this case, `Number`) or any of its subtypes (such as `Double` or `Integer`, for example). The following is an example of a list whose wildcard has `Number` as its lower bound. In this case, we can instantiate an `ArrayList` of numbers (or of its superclass `Object`). And we can add elements of one of its subclasses (we cannot add an object of type `Number` because it is an abstract class, which cannot have direct instances). The example shows three element additions. The first two are allowed because the elements are subtypes of `Number` (`10` is an `Integer` and `1.0` is a `Double`). The third addition is not allowed, producing a compile-time error because `Object` is not a descendant of `Number`.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

If we created the `ArrayList` with `Object` as its type parameter, the third addition would still not be allowed at compile time, producing the same error (and the first two additions would remain allowed), because the type of the list is still unknown (we only know that it is `Number` or one of its supertypes).

## Multiple Bounds

In Java, a generic type can have **multiple bounds**, meaning that the type parameter can be restricted to accept only types that extend (or are) a specific class and that implement one or more interfaces. The syntax follows the form `<T extends Class & Interface1 & Interface2>`. If a class is used as a bound, it must be specified first, followed by the interfaces. If there is no class, only interfaces can be listed.

For example, the class `MultipleBounds` has a generic type `T` that extends the `Number` class and implements the `Comparable<T>` and `Serializable` interfaces:

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

In this example, `T` can only be `Number` or a type that inherits from `Number` and also implements `Comparable<T>` and `Serializable`. This is useful when we need multiple guarantees, such as access to superclass methods and contracts defined by several interfaces. This combination allows the code to be more flexible while remaining strongly typed, avoiding compile-time errors and ensuring that all required methods will be available for the generic type being used.

---

*This article is adapted from content in the book <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, by <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
