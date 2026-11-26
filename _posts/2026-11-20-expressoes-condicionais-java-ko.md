---
layout: post
title: "Java의 표현식과 조건문"
date: 2026-11-20
lang: ko
translation_id: expressoes-condicionais-java
permalink: /ko/expressions-and-conditional-statements-in-java/
share_text: >-
  표현식, 블록, if, else, 삼항 연산자, switch를 다룹니다.
---

## 표현식과 문장

표현식을 평가하면 값이 나옵니다. 리터럴, 변수, 연산자, 메서드 호출, 객체 생성 등이 포함될 수 있습니다. 다음 코드는 일부만 보여 줍니다.

```text
x + 2 * 1
c.getBalance()
i = 20
```

문장은 실행 단위입니다. 메서드 호출, 대입, 증가 연산은 세미콜론을 붙여 문장으로 사용할 수 있습니다. 이 예에는 별도 선언과 `Account` 클래스가 필요합니다.

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

중괄호는 여러 문장을 블록으로 묶습니다. 이 프로그램은 정수를 읽고 조건이 참일 때 메시지 두 개를 출력합니다.

```java
void main() {
    int x = Integer.parseInt(
            IO.readln("Enter an integer: "));
    if (x < 10) {  
        IO.println("X is less than 10."); 
        IO.println("Initialize X with another value."); 
    }
}
```

## 조건문

`if`는 불리언 조건이 참일 때 해당 문장을 실행합니다.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else`는 조건이 거짓일 때 할 일을 지정합니다.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

중괄호를 쓰면 각 분기에 여러 문장을 넣을 수 있습니다.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
    }
    else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

성인 여부를 검사한 뒤 중첩 `if`로 우선 이용 조건을 확인합니다.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
        if (age >= 65)
            IO.println("Priority access granted");
    } else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

삼항 연산자는 조건에 따라 두 값 중 하나를 선택합니다.

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age: "));
    // The ternary operator has this syntax: 
		// (expr) ? true : false
    String message = ((age >= 18) ? "At least" : "Under") + 
                 " 18 years old";
    IO.println(message);
}
```

## switch로 분기하기

기존 `switch` 문은 일치하는 경우를 선택합니다. `break`는 그 분기를 끝내고 `default`는 나머지 값을 처리합니다.

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message;
    switch (age) {
        case 0: case 1: case 2: case 3: case 4: case 5:
            message = "Very young";
            break;
        case 18:
            message = "Reaching adulthood";
            break;
        case 65:
            message = "Entering senior years";
            break;
        default:
            message = "No special case";
            break;
        }
        IO.println(message);
}
```

화살표를 사용하는 `switch` 표현식은 값을 반환합니다. 같은 분기의 여러 값은 쉼표로 구분합니다.

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message = switch (age) {
        case 0, 1, 2, 3, 4, 5 -> "Very young";
        case 18 -> "Reaching adulthood";
        case 65 -> "Entering senior years";
        default -> "No special case";
    };
    IO.println(message);
}
```

패턴 매칭에서는 `when` 가드로 타입에 추가 조건을 붙일 수 있습니다. 예제는 `Integer`, `String`, `null`, 기타 값을 구분합니다.

```java
private static String age(Object ageObject) {
    return switch (ageObject) {
        case Integer i when i >= 65 -> 
            "[Integer] Adult: " + i + 
            "\nPriority access granted.";
        case Integer i when i >= 18 -> 
            "[Integer] Adult: " + i + 
             "\nAccess granted.";
        case Integer i -> "[Integer] Minor: " + 
                i + "\nAccess denied.";
        case String s -> 
            "[String] Age provided as text: " + s;
        case null -> "[null] Age not provided";
        default -> "Unexpected data type: " + 
                ageObject.getClass().getName();
    };
}
```

프로그램은 서로 다른 네 값으로 메서드를 호출합니다.

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

출력은 다음과 같습니다.

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

마지막 예제에는 `switch` 패턴 매칭을 지원하는 Java 버전이 필요합니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
