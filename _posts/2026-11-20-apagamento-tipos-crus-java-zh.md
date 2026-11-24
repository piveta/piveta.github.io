---
layout: post
title: "Java 的类型擦除与原始类型"
date: 2026-11-20
lang: zh
translation_id: apagamento-tipos-crus-java
permalink: /zh/type-erasure-and-raw-types-in-java/
share_text: >-
  类型擦除维持旧代码兼容性；原始类型失去元素类型检查。
---

Java 5 在兼容旧代码的前提下引入泛型。通过**类型擦除**（*type erasure*），编译器先检查泛型类型参数，再从 JVM 执行的表示中移除它们，并以其边界类型代替，通常是 `Object` 或声明的第一个边界。

擦除后，`Adapter<T>` 大致类似一个使用 `Object` 的类：

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

不写类型参数的客户端可表示为：

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

这些代码只是对擦除过程的**说明**，不是字节码的逐字转写。运行时无法以编译时相同的方式获取泛型类型实参，因此某些反射操作受到限制。

## 原始类型

指定类型实参的列表会检查元素类型：

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

*原始类型*在声明和构造时都省略类型实参：

```java
void main(){
    List names = new ArrayList();
}
```

这样就失去 `List<String>` 提供的检查，列表可以同时加入字符串和整数：

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>` 表示元素类型**未知**的列表，除了 `null`，不能随意添加元素。原始 `List` 则不做这种类型检查。新代码应使用类型实参或通配符，原始类型主要用于与旧库交互。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
