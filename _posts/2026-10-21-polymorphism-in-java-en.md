---
layout: post
title: "Polymorphism in Java"
date: 2026-10-21
lang: en
translation_id: polimorfismo-em-java
permalink: /en/polymorphism-in-java/
share_text: >-
  An introduction to ad hoc, parametric, and subtype polymorphism, with Java examples.
---

In object-oriented programming, **polymorphism** is the ability of an operation to behave differently depending on the class of the object involved. The main forms are:

- **Ad hoc polymorphism (or overloading)**: methods with the same name can have different parameters, and a call selects the compatible version based on its arguments;
- **Parametric polymorphism**: generic classes and methods work with types that are specified when they are used;
- **Subtype polymorphism**: a subclass can override a method, and the implementation that runs depends on the concrete class of the object.

The following examples show these three forms in Java, starting with overloading. The `Figure` class has two overloaded methods named `resize`. The first receives a `percentage` of type `Double`; the second receives two coordinates, `x` and `y`, of type `Integer`.

```java
public class Figure {
    public void resize(Double percentage) {
        // Resize by percentage
    }
    public void resize(Integer x, Integer y) {
        // Resize by coordinates
    }
}
```

For **parametric polymorphism**, we can create parameterized types using `<` and `>`. For example, the `ArrayList` class has a type parameter `E` that specifies the type of objects the list can store. This type parameter is also used as the formal parameter of the `add` method. Thus, the type expected by `add` is the same one used when instantiating `ArrayList`. Note that it extends `AbstractList` and implements the `List` interface, both using the same type `E`, as well as other interfaces.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // Implementation of add
    }
    // Other methods and fields of the class
}
```

For example, we can create a list of strings with the type parameter `String` and insert elements by calling `add`[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

In this case, the compiler expects the argument passed to `add` to be a `String`. Passing an object of another type causes a compile-time error. If we wanted a list of integers, we could pass a different type to `ArrayList`, in this case `Integer`:

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

For **subtype polymorphism**, suppose the `Figure` class has a `draw` method that can also be called on objects of the `Triangle`, `Circle`, and `Rectangle` classes. Suppose that each of these classes overrides the method to implement its own drawing behavior. In the following code, each call to `draw` invokes a different implementation according to the class of the object assigned to `figure`: `Circle`, `Triangle`, or `Rectangle`.

```java
Figure figure = new Circle(10);
// Calls Circle's draw method
figure.draw();
figure = new Triangle(20);
// Calls Triangle's draw method
figure.draw();
figure = new Rectangle(10, 20);
// Calls Rectangle's draw method
figure.draw();
```

[^8]: To use `ArrayList`, we usually need to import it with `import java.util.ArrayList;`. Imports are not required in compact source files. In regular source files, the `java.base` module can be imported with `import module java.base;`.

---

*This article is adapted from content in <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, a book by <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Related articles

- [Basic Object-Oriented Programming Concepts](/en/basic-oop-concepts/)
- [Classes in Java](/en/classes-in-java/)
- [Inheritance in Java](/en/inheritance-in-java/)
- [Interfaces in Java](/en/interfaces-in-java/)
- [OOP and Java Links](/en/oop-java-links/)
- [Object-Oriented Programming Exercises](/en/object-oriented-programming-exercises/)
