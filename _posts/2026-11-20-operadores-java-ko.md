---
layout: post
title: "Java의 연산자"
date: 2026-11-20
lang: ko
translation_id: operadores-java
permalink: /ko/operators-in-java/
share_text: >-
  산술, 대입, 비교 연산자를 책의 예제로 살펴봅니다.
---

## 산술 연산자

`+`, `-`, `*`, `/`, `%`는 각각 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지입니다. 연산자 우선순위는 식의 묶임을 결정합니다. `++`와 `--`는 변수를 1만큼 변경합니다.

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

`y = x++`는 먼저 이전 값인 10을 `y`에 대입합니다. 그 후 `x`가 11이 됩니다.

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

`y = ++x`는 먼저 증가시킵니다. 두 변수의 값은 모두 11이 됩니다.

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

`+`, `-`, `~`, `!`도 단항 연산자로 쓸 수 있습니다.

## 대입 연산자

`=`는 오른쪽 식의 값을 왼쪽 변수에 대입합니다.

```java
int age;
String name;
Double height;
```

선언 이후에 값을 대입할 수 있습니다.

```java
age = 20;
name = "Mary";
height = 1.70;
```

선언과 함께 초기화할 수도 있습니다.

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

## 복합 대입

`+=`, `-=`, `*=`, `/=`, `%=`는 연산과 대입을 함께 수행합니다.

```java
void main() {
    int a = 10;
    a += 10;
    IO.println("a = " + a);
    a -= 10;
    IO.println("a = " + a); 
    a *= 10;
    IO.println("a = " + a); 
    a /= 10;
    IO.println("a = " + a); 
    a %= 3;
    IO.println("a = " + a); 
}
```

다음 순서로 값이 출력됩니다.

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

복합 대입에서는 왼쪽 식을 한 번만 평가하며 그 타입도 고려합니다. 시프트와 비트 연산에도 복합 대입이 있습니다.

## 비교 연산자

`==`, `!=`, `>`, `>=`, `<`, `<=`는 불리언 값을 반환합니다.

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age == 10)
        IO.println("Age equals 10 years");
    if (age != 20)
        IO.println("Age differs from 20 years");
    if (age > 30)
        IO.println("Age is over 30 years");
    if (age <= 80)
        IO.println("Age is at most 80 years");
}
```

10을 입력하면 세 조건이 참입니다. 각 `if`를 독립적으로 검사하며 `Integer.parseInt`는 입력을 정수로 변환합니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
