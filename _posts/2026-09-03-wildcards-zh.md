---
layout: post
title: "Java 泛型类型中的通配符与边界"
date: 2026-09-03
lang: zh
translation_id: wildcards-limites-java
permalink: /java-generics-wildcards-bounds-zh/
share_text: >-
  在Java泛型中，<?>表示未知类型，<? extends T>和<? super T>分别指定上界和下界。文章还展示了如何为类型参数设置多个边界。
---

除了具体的泛型类型之外，我们还可以使用**通配符**来表示未知类型（`<?>`），将指定类型限制为某个给定类型的子类型（`<? extends Type>`），或者包含超类型（使用 `<? super Type>`）。下面分别介绍无界通配符、上界通配符和下界通配符。随后，我们将说明如何为泛型类型定义多个边界。

## 无界通配符

对于未知类型，我们使用问号作为类型，使任意类型都可以用于该上下文。例如，如果一个变量声明为 `List<?>`（或者一个属性或参数采用这种类型），它可以接收具有任意有效类型参数的 `List` 对象，例如 `String`、`Integer` 等。这种未知的泛型类型称为**无界通配符**（`<?>`），因为它不施加任何类型边界。

例如：

```java
List<?> l = new ArrayList<String>();
// 或者，例如
l = new LinkedList<Integer>();
```

这种变量声明方式看起来可能很有吸引力，但存在限制。在这种情况下，我们不知道列表中对象的类型。因此，例如不能向列表中添加元素（`null` 除外，因为它与 Java 中的任何引用类型兼容），因为无法保证要添加的对象与列表的类型参数具有相同的类型。

因此，如果尝试向列表对象（这里是 `l`）添加元素，就会产生编译时错误：

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

无界类型通常用于只读取数据而不修改数据的场景。例如，我们可以定义一个接收列表并打印其元素的方法，而不指定列表元素的类型：

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

运行 `main` 方法将显示：

```text
1
2
3
A
B
C
```

这里以打印为例，但我们还可以遍历对象、在 *streams* 中使用它们、使用 `instanceof` 进行过滤、获取列表大小、检查是否包含某个对象，以及将其转换并复制到类型化列表中，等等。不能做的是直接修改列表（例如使用 `add` 或 `set`，`null` 除外）。

## 上界通配符

**上界通配符**允许我们指定，只能使用给定类型或其子类型（通过继承或实现接口得到的类型）作为类型参数。记法 `<? extends T>` 表示通配符必须是类型 `T` 或继承 `T` 的某个类型。

例如，如果声明一个通配符上界为 `Number` 的列表，就可以为其赋值任意子类的对象，例如 `Double` 或 `Integer`。如果 `Number` 是具体类（实际上它是抽象类），也可以赋值该类本身的对象。下面的例子正是如此：

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

与无界通配符一样，我们不能向列表 `l` 中添加元素，因为不知道列表的确切类型。因此，前两个 `add` 调用都会产生编译错误：

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

虽然通过代码可以知道赋给变量 `l` 的对象实际上是一个整数列表，但编译器只知道 `l` 的类型是未知的，因此不允许添加值。读取时，值会被视为 `Number`，因为它是上界。

## 下界通配符

**下界通配符**允许我们指定，只能使用给定类型或其超类型作为类型参数。记法 `<? super T>` 表示通配符必须是类型 `T` 或 `T` 的某个超类。

例如，如果声明一个以下界 `Number` 为边界的列表，就可以为其赋值其任意超类的对象（对于 `Number`，只有 `Object`，因为 `Number` 没有显式声明的超类）。

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

允许添加下界类型（这里是 `Number`）或其任何子类型（例如 `Double` 或 `Integer`）的元素。下面是一个以下界 `Number` 为边界的列表示例。在这种情况下，可以实例化元素类型为 `Number`（或其超类 `Object`）的 `ArrayList`。可以添加其子类的元素（不能添加 `Number` 类型的对象，因为它是抽象类，不能直接创建其实例）。示例中进行了三次添加。前两次是允许的，因为元素是 `Number` 的子类型（`10` 是 `Integer`，`1.0` 是 `Double`）。第三次添加不允许，因为 `Object` 不是 `Number` 的后代，因此会产生编译时错误。

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

如果使用 `Object` 作为类型参数创建 `ArrayList`，第三次添加在编译时仍然不允许，并产生相同的错误（前两次添加仍然允许），因为列表的类型仍然未知（我们只知道它是 `Number` 或其某个超类型）。

## 多重边界

在 Java 中，泛型类型可以具有**多个边界**，这意味着可以将类型参数限制为某个特定类的子类（或该类本身），并且同时实现一个或多个接口。语法形式为 `<T extends Class & Interface1 & Interface2>`。如果使用类作为边界，必须先指定类，然后再指定接口。如果没有类，则只能列出接口。

例如，`MultipleBounds` 类的泛型类型 `T` 扩展 `Number` 类，并实现 `Comparable<T>` 和 `Serializable` 接口：

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

在这个例子中，`T` 只能是 `Number` 或者继承 `Number` 并同时实现 `Comparable<T>` 和 `Serializable` 的类型。当我们需要多个保证时，这种方式很有用，例如需要访问超类方法以及由多个接口定义的契约。这种组合可以在保持强类型的同时提高代码的灵活性，避免编译时错误，并确保使用的泛型类型提供所需的全部方法。

---

*本文改编自 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> 一书的内容，作者为 <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>。*
