---
layout: post
title: "Java 제네릭 연습 문제"
date: 2026-11-20
lang: ko
translation_id: exercicios-tipos-genericos-java
permalink: /ko/java-generics-exercises/
share_text: >-
  제네릭 메서드, 와일드카드, 상속, Optional<T>, Box<T>에 관한 열 가지 문제입니다.
---

다음 문제는 **Orientação a Objetos com Java**의 제네릭 장을 바탕으로 합니다. 코드 구조는 책을 따르며 식별자, 주석, 메시지는 영어로 유지합니다.

1. Java 컬렉션 프레임워크의 주요 인터페이스를 조사하고, 제네릭이 클래스를 수정하지 않고 자료구조를 재사용하게 하는 방식을 설명하세요.
2. 두 `Comparable` 객체를 받아 더 큰 것을 반환하는 정적 제네릭 메서드 `max`를 작성하세요.
3. 임의 타입의 목록을 받아 출력하는 정적 메서드를 와일드카드로 작성하세요.
4. 숫자 목록을 합산하는 정적 메서드를 만들고 `extends`로 `Number` 목록만 받도록 하세요.
5. 다음 클래스 계층을 살펴보세요.

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   다음 메서드는 악기 또는 그 하위 클래스의 목록을 받습니다.

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   `Guitar`와 `Flute` 목록을 전달하세요. 이후 메서드 안에서 악기를 추가해 보고 컴파일 오류를 확인하세요.
6. `Number`이면서 `Comparable`인 요소의 목록을 받아 최댓값을 반환하는 제네릭 메서드를 구현하세요.
7. 다음 메서드들을 구현하고 `Car`, `Motorcycle`, `Vehicle` 목록으로 시험하세요.

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

8. `List<String>`만 식별하는 `boolean checkList(Object obj)`를 만들어 보세요. Java에서 직접 가능한지 조사하고 `List<?>` 또는 `List<Object>`를 쓰는 대안을 제시하세요.
9. `Optional<T>`를 조사하고 값이 있으면 출력하고 없으면 *empty*를 출력하는 `printOptional(Optional<T> opt)`를 만드세요. `Optional<String>`과 `Optional<Integer>`로 시험하세요.
10. 한 요소를 보관하는 `Box<T>`를 만드세요. `store(T item)`은 `null`을 거부하고, `get()`은 값을 반환하며, `compare(Box<T> b1, Box<T> b2)`는 `compareTo`로 비교합니다. 상속 관계가 있는 서로 다른 타입의 상자를 비교하는 `compareWithInheritance`도 `<? extends T>` 또는 `<? super T>`로 구현하고 시험하세요.

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

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
