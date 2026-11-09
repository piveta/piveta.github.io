---
layout: post
title: "Java 中的多态"
date: 2026-10-21
lang: zh
translation_id: polimorfismo-em-java
permalink: /polymorphism-in-java-zh/
share_text: >-
  通过 Java 示例介绍特设多态、参数化多态和子类型多态。
---

在面向对象编程中，**多态**是指一个操作能够根据相关对象的类表现出不同的行为。主要形式包括：

- **特设多态（或重载）**：同名方法可以具有不同参数，调用时会根据实参选择兼容的方法版本。
- **参数化多态**：泛型类和泛型方法可以处理在使用时指定的类型。
- **子类型多态**：子类可以重写方法，实际执行的实现取决于对象的具体类。

下面的示例展示 Java 中的三种形式，先从重载开始。`Figure` 类有两个重载的 `resize` 方法。第一个接收 `Double` 类型的 `percentage`；第二个接收 `Integer` 类型的坐标 `x` 和 `y`。

```java
public class Figure {
    public void resize(Double percentage) {
        // 按百分比调整大小
    }
    public void resize(Integer x, Integer y) {
        // 根据坐标调整大小
    }
}
```

对于**参数化多态**，我们可以用 `<` 和 `>` 创建参数化类型。例如，`ArrayList` 类有一个 `E` 类型参数，用来指定列表可以存储的对象类型。这个类型参数也用作 `add` 方法的形式参数。因此，`add` 所期望的类型与实例化 `ArrayList` 时指定的类型相同。请注意，`ArrayList` 扩展 `AbstractList`，并使用相同的 `E` 类型实现 `List`、`RandomAccess`、`Cloneable`、`Serializable` 等接口。

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // add 的实现
    }
    // 类的其他方法和字段
}
```

例如，我们可以使用 `String` 类型参数创建字符串列表，并调用 `add` 添加元素[^8]。

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

此时，编译器要求传递给 `add` 的参数是 `String`。传入其他类型的对象会导致编译错误。如果需要整数列表，可以为 `ArrayList` 指定另一种类型，即 `Integer`：

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

对于**子类型多态**，假设 `Figure` 类有一个 `draw` 方法，也可以在 `Triangle`、`Circle` 和 `Rectangle` 类的对象上调用。每个类都会重写该方法，实现自己的绘制行为。在下面的代码中，`figure` 被赋予 `Circle`、`Triangle` 或 `Rectangle` 对象；每次调用 `draw` 都会根据对象的类执行不同的实现。

```java
Figure figure = new Circle(10);
// 调用 Circle 的 draw 方法
figure.draw();
figure = new Triangle(20);
// 调用 Triangle 的 draw 方法
figure.draw();
figure = new Rectangle(10, 20);
// 调用 Rectangle 的 draw 方法
figure.draw();
```

[^8]: 通常需要使用 `import java.util.ArrayList;` 导入 `ArrayList`。紧凑源文件不需要导入语句。在常规源文件中，可以通过 `import module java.base;` 导入 `java.base` 模块。

---

*本文改编自 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a> 所著《<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>》中的内容。*

## 相关文章

- [面向对象编程的基本概念](/oop-basics-java-zh/)
- [Java 中的类](/classes-in-java-zh/)
- [Java 中的继承](/inheritance-in-java-zh/)
- [Java 中的接口](/interfaces-in-java-zh/)
- [OOP 与 Java 链接](/oop-java-links-zh/)
- [面向对象编程练习](/oop-exercises-zh/)
