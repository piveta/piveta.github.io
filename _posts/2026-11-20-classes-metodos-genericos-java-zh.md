---
layout: post
title: "Java 中的泛型类与泛型方法"
date: 2026-11-20
lang: zh
translation_id: classes-metodos-genericos-java
permalink: /zh/generic-classes-and-methods-in-java/
share_text: >-
  泛型让类和方法在保持类型安全的同时复用；以 Adapter<T> 为例。
---

**参数多态**让类、接口、记录或方法按照使用时指定的类型工作。Java 泛型促进代码复用，并减少不必要的类型转换。`List<String>` 和 `List<Integer>` 使用相同的接口，但编译器会分别检查各自的元素类型。

没有类型参数时，`Adapter` 的字段、构造方法和普通方法都使用 `Object`：

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

它能存放任何对象，却无法限制某个适配器只使用一种类型。声明 `T` 后，同一实现便使用调用者选定的类型：

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

下面的客户端创建 `Adapter<String>`。构造方法和 `set` 接受字符串，`get` 返回字符串。程序依次输出 `Test` 和 `New Value`：

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## 泛型方法

方法也可以在返回类型之前声明类型参数。`print` 接受元素类型不同的列表，同时保留编译期类型检查：

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

类型参数还可以决定返回类型。`first` 接收 `List<T>` 并返回 `T`：整数列表对应 `Integer`，姓名列表对应 `String`。

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

中间变量让类型更清楚；不需要时也可以直接使用表达式：

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## 有上界的类型参数

`multiply` 接受 `Number` 或其子类型的列表。`<T extends Number>` 使方法能够对每个元素调用 `doubleValue()`：

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

既可以传入 `Integer` 列表，也可以传入 `Double` 列表：

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

编译器在每次调用时检查类型参数，而方法仍只有一份实现。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
