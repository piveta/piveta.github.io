---
layout: post
title: "Javaジェネリクスにおける継承とサブタイプ"
date: 2026-11-24
lang: ja
translation_id: heranca-subtipos-genericos-java
permalink: /ja/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car>はList<Vehicle>ではありません。不変性とextends・superによる読み書きを説明します。
---

Javaのジェネリック型は基本的に**不変**です。`Car`が`Vehicle`を継承していても、`List<Car>`は`List<Vehicle>`のサブタイプではありません。`extends`と`super`のワイルドカードは、型を使用する場面で別の関係を表します。

## 不変性

例では`Car`と`Motorcycle`が`Vehicle`を継承します。

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

車のリストを`List<Vehicle>`型の変数に代入することはできません。次の代入は**コンパイルエラー**になります。

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

この規則は型安全性を守ります。もし代入できれば、実際には車のリストであるものに`vehicles`経由でバイクを追加できてしまいます。次の断片は**仮定上のコード**で、実行可能な例ではありません。

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## 共変的な使用：`extends`

車両やそのサブタイプを**読み取る**メソッドは`List<? extends Vehicle>`を受け取れます。読み取った要素は少なくとも`Vehicle`です。

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

`List<Vehicle>`、`List<Car>`、`List<Motorcycle>`を渡せます。ただし実際のリスト型が不明なため、`Car`を追加できません。

## 反変的な使用：`super`

車を**追加する**メソッドは、`Car`またはそのスーパータイプのリストを受け取れます。

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

`List<Car>`、`List<Vehicle>`、`List<Object>`が使えます。読み取る場合に保証される型は`Object`だけです。ここでの共変性・反変性は**ワイルドカードを使う箇所**の性質であり、`List<T>`の宣言自体は不変です。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
