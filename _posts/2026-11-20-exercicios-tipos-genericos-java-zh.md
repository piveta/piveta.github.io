---
layout: post
title: "Java 泛型练习"
date: 2026-11-20
lang: zh
translation_id: exercicios-tipos-genericos-java
permalink: /zh/java-generics-exercises/
share_text: >-
  十道关于泛型方法、通配符、继承、Optional<T> 和 Box<T> 的练习。
---

以下练习根据 **Orientação a Objetos com Java** 的泛型章节编写。代码结构遵循原书，标识符、注释和输出消息保留英语版本。

1. 研究 Java 集合框架的主要接口，说明泛型如何让数据结构在不修改类的情况下复用。
2. 创建静态泛型方法 `max`，接收两个 `Comparable` 对象并返回较大的一个。
3. 创建静态方法，用通配符接收并输出任意元素类型的列表。
4. 创建求数值列表之和的方法，用 `extends` 将其限制为 `Number` 列表。
5. 考虑以下类层次结构：

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   下面的方法接收乐器或其子类的列表：

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   分别传入 `Guitar` 和 `Flute` 的列表。然后尝试在方法内部添加乐器，观察编译错误。
6. 实现泛型方法，接收同时属于 `Number` 和 `Comparable` 的元素列表，并返回最大元素。
7. 实现下面三个方法，并用 `Car`、`Motorcycle` 和 `Vehicle` 的列表测试：

   ```java
   void printInvariant(List<Vehicle> list){
       // Implement
   }
   void printCovariant(List<? extends Vehicle> list){
       // Implement
   }
   void printContravariant(List<? super Vehicle> list){
       // Implement
   }
   ```

8. 尝试实现 `boolean checkList(Object obj)`，使其仅识别 `List<String>`。研究 Java 是否能直接做到，并提出使用 `List<?>` 或 `List<Object>` 的替代方案。
9. 研究 `Optional<T>`，实现 `printOptional(Optional<T> opt)` 来输出值或 *empty*。用 `Optional<String>` 和 `Optional<Integer>` 测试。
10. 创建存储单个元素的 `Box<T>`。`store(T item)` 应拒绝 `null`，`get()` 返回元素，`compare(Box<T> b1, Box<T> b2)` 使用 `compareTo` 比较。再用 `<? extends T>` 或 `<? super T>` 实现比较具有继承关系的不同类型盒子的 `compareWithInheritance`，并测试：

    ```java
     Box<Integer> box1 = new Box<>();
     Box<Integer> box2 = new Box<>();
     box1.store(10);
     box2.store(5);
     boolean result = Box.compare(box1, box2); // true

     Box<Double> box3 = new Box<>();
     Box<Integer> box4 = new Box<>();
     box3.store(7.5);
     box4.store(5);
     boolean result2 = Box.compareWithInheritance(box3,
        box4); // true
    ```

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
