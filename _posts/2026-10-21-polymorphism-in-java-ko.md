---
layout: post
title: "Java의 다형성"
date: 2026-10-21
lang: ko
translation_id: polimorfismo-em-java
permalink: /polymorphism-in-java-ko/
share_text: >-
  Java 예제로 애드혹, 매개변수형, 하위 타입 다형성을 소개합니다.
---

객체 지향 프로그래밍에서 **다형성**은 관련 객체의 클래스에 따라 연산이 다르게 동작할 수 있는 능력입니다. 주요 형태는 다음과 같습니다.

- **애드혹 다형성(오버로딩)**: 같은 이름의 메서드가 다른 매개변수를 가질 수 있으며, 인수에 맞는 버전이 선택됩니다.
- **매개변수형 다형성**: 제네릭 클래스와 메서드가 사용 시점에 지정되는 타입을 처리합니다.
- **하위 타입 다형성**: 하위 클래스가 메서드를 재정의할 수 있고, 실행되는 구현은 객체의 구체 클래스에 따라 달라집니다.

다음 예제는 Java에서 세 가지 형태를 보여 주며, 오버로딩부터 시작합니다. `Figure` 클래스에는 `resize`라는 이름의 오버로드된 메서드가 두 개 있습니다. 첫 번째는 `Double` 타입의 `percentage`를 받고, 두 번째는 `Integer` 타입의 좌표 `x`, `y`를 받습니다.

```java
public class Figure {
    public void resize(Double percentage) {
        // 백분율로 크기 변경
    }
    public void resize(Integer x, Integer y) {
        // 좌표로 크기 변경
    }
}
```

**매개변수형 다형성**에서는 `<`와 `>`를 사용해 매개변수화된 타입을 만들 수 있습니다. 예를 들어 `ArrayList` 클래스에는 목록에 저장할 수 있는 객체의 타입을 지정하는 `E` 타입 매개변수가 있습니다. 이 타입 매개변수는 `add` 메서드의 형식 매개변수로도 사용됩니다. 따라서 `add`가 기대하는 타입은 `ArrayList`를 인스턴스화할 때 지정하는 타입과 같습니다. `ArrayList`는 `AbstractList`를 확장하고, 같은 `E` 타입으로 `List`, `RandomAccess`, `Cloneable`, `Serializable` 등의 인터페이스를 구현합니다.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // add의 구현
    }
    // 클래스의 다른 메서드와 필드
}
```

예를 들어 타입 매개변수 `String`을 사용해 문자열 목록을 만들고 `add`를 호출해 요소를 넣을 수 있습니다[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

이 경우 컴파일러는 `add`에 전달되는 인수가 `String`이기를 기대합니다. 다른 타입의 객체를 전달하면 컴파일 오류가 발생합니다. 정수 목록이 필요하다면 `ArrayList`에 다른 타입인 `Integer`를 전달할 수 있습니다.

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

**하위 타입 다형성**의 경우, `Figure` 클래스에 `Triangle`, `Circle`, `Rectangle` 클래스의 객체에서도 호출할 수 있는 `draw` 메서드가 있다고 합시다. 각 클래스는 고유한 그리기 동작을 구현하도록 메서드를 재정의합니다. 다음 코드에서는 `figure`에 할당된 객체가 `Circle`, `Triangle`, `Rectangle` 중 무엇인지에 따라 각 `draw` 호출이 서로 다른 구현을 실행합니다.

```java
Figure figure = new Circle(10);
// Circle의 draw 메서드를 호출
figure.draw();
figure = new Triangle(20);
// Triangle의 draw 메서드를 호출
figure.draw();
figure = new Rectangle(10, 20);
// Rectangle의 draw 메서드를 호출
figure.draw();
```

[^8]: `ArrayList`를 사용하려면 일반적으로 `import java.util.ArrayList;`로 가져와야 합니다. 간결한 소스 파일에서는 import가 필요하지 않습니다. 일반 소스 파일에서는 `import module java.base;`로 `java.base` 모듈을 가져올 수 있습니다.

---

*이 글은 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a>의 저서 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>의 내용을 바탕으로 작성했습니다.*

## 관련 글

- [객체 지향 프로그래밍의 기본 개념](/oop-basics-java-ko/)
- [Java의 클래스](/classes-in-java-ko/)
- [Java의 상속](/inheritance-in-java-ko/)
- [Java의 인터페이스](/interfaces-in-java-ko/)
- [OOP와 Java 링크](/oop-java-links-ko/)
- [객체 지향 프로그래밍 연습 문제](/oop-exercises-ko/)
