---
layout: post
title: "Java의 변수와 타입"
date: 2026-11-24
lang: ko
translation_id: variaveis-tipos-java
permalink: /ko/variables-and-types-in-java/
share_text: >-
  지역 변수와 var, 기본형과 참조형을 살펴봅니다.
---

지역 변수에는 이름, 타입, 스코프가 있습니다. Java는 지역 변수에 기본값을 넣지 않으므로 사용하기 전에 값을 대입해야 합니다.

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

선언에 리스트 타입이 있으면 컴파일러는 `<>`의 타입 인수를 추론합니다.

```java
ArrayList<Double> list = new ArrayList<>();
```

`var`를 쓰면 필수 초기화 식에서 타입을 추론합니다. 여기서는 생성자 호출에 `Double`을 지정합니다.

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Java는 대소문자를 구분합니다. 관례상 클래스와 인터페이스는 대문자로, 변수와 메서드는 소문자로 시작하며 상수에는 대문자와 밑줄을 사용합니다.

## 기본형

`byte`, `short`, `int`, `long`, `float`, `double`, `boolean`, `char`가 기본형입니다.

```java
void main() {
    byte b;
    short s;
    int x, y, z;
    long l;
    float f;
    double d;
    boolean test;
    char c;
}
```

리터럴로 직접 초기화할 수 있습니다. 접미사 `L`은 `long`, `f`는 `float`를 나타냅니다.

```java
void main() {
    byte b = 10;
    short s = 20;
    int x = 10, y = 20, z = 30;
    long l = 100L;
    float f = 12.3f;
    double d = 20.45;
    boolean test = true;
    char c = 'a';
}
```

정수 리터럴은 `0b`로 이진수, `0x`로 십육진수를 나타낼 수도 있습니다.

## 참조형

클래스, 인터페이스, 열거형, 레코드, 배열은 참조형입니다. 문자열 리터럴은 큰따옴표로 묶습니다.

```java
void main() {
    String s = "This is a string...";
}
```

래퍼 클래스는 기본형 값을 객체로 표현합니다. 이 장의 다른 예제에서는 컬렉션 API도 자주 사용합니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
