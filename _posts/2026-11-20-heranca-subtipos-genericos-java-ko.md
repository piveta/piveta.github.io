---
layout: post
title: "Java 제네릭의 상속과 하위 타입"
date: 2026-11-24
lang: ko
translation_id: heranca-subtipos-genericos-java
permalink: /ko/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car>는 List<Vehicle>이 아닙니다. 불변성과 extends·super를 이용한 읽기·쓰기를 설명합니다.
---

Java 제네릭 타입은 기본적으로 **불변**입니다. `Car`가 `Vehicle`을 상속해도 `List<Car>`는 `List<Vehicle>`의 하위 타입이 아닙니다. `extends`와 `super` 와일드카드는 타입을 사용하는 자리에서 다른 관계를 표현합니다.

## 불변성

예제에서 `Car`와 `Motorcycle`은 `Vehicle`을 상속합니다.

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

자동차 목록을 `List<Vehicle>` 변수에 대입할 수 없습니다. 다음 대입은 **컴파일 오류**를 일으킵니다.

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

이 규칙은 타입 안전성을 보장합니다. 대입이 허용된다면 실제로 자동차 목록인 객체에 `vehicles`를 통해 오토바이를 추가할 수 있습니다. 다음 코드는 **가정상의 예**이며 실행 가능한 프로그램이 아닙니다.

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## 공변적 사용: `extends`

차량이나 그 하위 타입을 **읽기** 위해 메서드는 `List<? extends Vehicle>`을 받을 수 있습니다. 읽은 요소는 적어도 `Vehicle`입니다.

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

`List<Vehicle>`, `List<Car>`, `List<Motorcycle>`을 전달할 수 있습니다. 실제 목록의 타입을 모르므로 `Car`를 추가할 수는 없습니다.

## 반공변적 사용: `super`

자동차를 **추가**하려면 메서드는 `Car` 또는 상위 타입의 목록을 받을 수 있습니다.

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

`List<Car>`, `List<Vehicle>`, `List<Object>`이 가능합니다. 읽을 때 정적으로 보장되는 타입은 `Object`뿐입니다. 여기서 공변성과 반공변성은 **와일드카드 사용 방식**을 가리키며 `List<T>` 선언 자체는 불변입니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
