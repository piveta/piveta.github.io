---
layout: post
title: "Java 泛型中的继承与子类型"
date: 2026-11-24
lang: zh
translation_id: heranca-subtipos-genericos-java
permalink: /zh/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car> 不是 List<Vehicle>；理解不变性以及 extends 和 super 对读写的作用。
---

Java 泛型默认具有**不变性**。即使 `Car` 继承 `Vehicle`，`List<Car>` 也不是 `List<Vehicle>` 的子类型。`extends` 与 `super` 通配符可以在使用类型的位置表达其他关系。

## 不变性

例子中，`Car` 和 `Motorcycle` 都继承 `Vehicle`：

```java
public class Vehicle {
    public void move() {
        IO.println("Vehicle moving");
    }
}

public class Car extends Vehicle {
    public void honk() {
        IO.println("Horn sounded");
    }
}

public class Motorcycle extends Vehicle {
    public void doWheelie() {
        IO.println("Motorcycle doing a wheelie");
    }
}
```

不能把汽车列表赋给 `List<Vehicle>` 变量。下面的赋值会产生**编译错误**：

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

这条规则维护类型安全。假如赋值被允许，就能通过 `vehicles` 把摩托车加入实际上的汽车列表。以下片段只是**假设性示例**，不是有效程序：

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## 协变式使用：`extends`

要**读取**车辆或其子类型，可以让方法接收 `List<? extends Vehicle>`。读出的每个元素至少是 `Vehicle`：

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

该方法接受 `List<Vehicle>`、`List<Car>` 和 `List<Motorcycle>`，但不能添加 `Car`，因为列表的具体类型未知。

## 逆变式使用：`super`

要**添加**汽车，方法可以接收 `Car` 或其超类型的列表：

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

`List<Car>`、`List<Vehicle>` 和 `List<Object>` 都可以传入。读取时静态保证的类型只有 `Object`。这里的协变与逆变描述的是**通配符的使用方式**，`List<T>` 的声明仍是不变的。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
