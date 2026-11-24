---
layout: post
title: "Java의 제네릭 클래스와 메서드"
date: 2026-11-20
lang: ko
translation_id: classes-metodos-genericos-java
permalink: /ko/generic-classes-and-methods-in-java/
share_text: >-
  제네릭은 타입 안전성을 유지하면서 클래스와 메서드를 재사용하게 해 줍니다. Adapter<T>를 예로 살펴봅니다.
---

**매개변수 다형성**을 이용하면 클래스, 인터페이스, 레코드, 메서드가 사용 시 지정한 타입에 맞춰 동작합니다. Java 제네릭은 코드 재사용을 돕고 불필요한 형변환을 줄입니다. `List<String>`과 `List<Integer>`는 같은 인터페이스를 쓰지만, 컴파일러가 각 목록의 요소 타입을 검사합니다.

타입 매개변수가 없는 `Adapter`는 필드, 생성자, 메서드에 `Object`를 사용합니다.

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

모든 객체를 저장할 수 있지만, 특정 어댑터를 한 타입으로 제한할 수는 없습니다. `T`를 선언하면 같은 구현이 호출자가 선택한 타입을 사용합니다.

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

다음 클라이언트는 `Adapter<String>`을 만듭니다. 생성자와 `set`은 문자열을 받고 `get`은 문자열을 반환합니다. 출력은 `Test`, 이어서 `New Value`입니다.

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## 제네릭 메서드

메서드도 반환 타입 앞에 타입 매개변수를 선언할 수 있습니다. `print`는 컴파일 시 타입 검사를 유지하면서 서로 다른 타입의 목록을 받습니다.

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

타입 매개변수는 반환 타입도 결정합니다. `first`는 `List<T>`를 받아 `T`를 반환하므로, 정수 목록에서는 `Integer`, 이름 목록에서는 `String`을 반환합니다.

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

중간 변수는 타입을 분명히 보여 줍니다. 필요 없다면 표현식을 바로 사용할 수 있습니다.

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## 상한이 있는 타입 매개변수

`multiply`는 `Number` 또는 그 하위 타입의 목록을 받습니다. `<T extends Number>` 덕분에 각 요소에서 `doubleValue()`를 호출할 수 있습니다.

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

`Integer` 목록과 `Double` 목록을 모두 전달할 수 있습니다.

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

컴파일러는 호출마다 타입 매개변수를 검사하며 메서드 구현은 하나로 유지됩니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
