---
layout: post
title: "Java의 타입 소거와 원시 타입"
date: 2026-11-20
lang: ko
translation_id: apagamento-tipos-crus-java
permalink: /ko/type-erasure-and-raw-types-in-java/
share_text: >-
  타입 소거는 기존 코드와의 호환성을 유지하고, 원시 타입은 요소의 타입 검사를 잃습니다.
---

Java 5는 이전 코드와 호환성을 유지하며 제네릭을 도입했습니다. **타입 소거**(*type erasure*) 과정에서 컴파일러는 제네릭 타입 매개변수를 검사한 뒤 JVM이 실행할 표현에서는 제거합니다. 매개변수는 보통 `Object` 또는 첫 번째로 선언한 상한으로 대체됩니다.

소거 후 `Adapter<T>`는 대략 `Object`를 쓰는 다음 클래스와 비슷합니다.

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

타입 매개변수를 쓰지 않는 클라이언트는 다음과 같습니다.

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

이 코드는 과정을 **설명하기 위한 근사 예**이지 바이트코드를 그대로 옮긴 것이 아닙니다. 제네릭 타입 인자는 실행 시 컴파일 때와 같은 방식으로 이용할 수 없어 일부 리플렉션 작업에 제약이 생깁니다.

## 원시 타입

타입 인자를 지정한 목록은 요소 타입을 검사합니다.

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

*원시 타입*은 선언과 생성 양쪽에서 타입 인자를 생략합니다.

```java
void main(){
    List names = new ArrayList();
}
```

그 결과 `List<String>`의 검사가 사라져 문자열과 정수를 모두 추가할 수 있습니다.

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>`는 요소 타입을 **알 수 없는 목록**으로, `null`을 제외한 임의의 요소를 추가할 수 없습니다. 반면 원시 `List`는 그런 검사 없이 요소를 받습니다. 새 코드에서는 타입 인자나 와일드카드를 쓰고 원시 타입은 주로 기존 라이브러리와 연동할 때 사용합니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
