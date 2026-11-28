---
layout: post
title: "Java 콘솔에서 읽고 쓰기"
date: 2026-11-20
lang: ko
translation_id: leitura-escrita-java
permalink: /ko/reading-and-writing-on-the-java-console/
share_text: >-
  IO, Scanner, readln으로 값을 입력하고 출력합니다.
---

Java 25의 `IO`는 출력에 `print`와 `println`을, 입력에 `readln`을 제공합니다. 정적 임포트를 하면 클래스 이름 없이 호출할 수 있습니다.

## 값 출력하기

`print`는 줄을 바꾸지 않고 `println`은 줄을 끝냅니다.

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

10과 20을 더한 결과가 한 줄에 표시됩니다.

## Scanner로 읽기

`nextLine()`은 한 줄을 읽고 `nextInt()`는 정수를 읽습니다. 주소를 읽기 전에 `nextLine()`을 한 번 더 호출해 남은 줄바꿈을 소비합니다.

```java
import java.util.Scanner;
void main(){
    var s = new Scanner(System.in);
    IO.println("Name: ");
    var name = s.nextLine(); 
    IO.println("Age: ");
    var age = s.nextInt(); 
    s.nextLine(); // Consumes the line break
    IO.println("Address: ");
    var address = s.nextLine(); 
    IO.println("Entered data:");
    IO.println("Name: " + name + ", Age: " + age);
    IO.println("Address: " + address);
}
```

## IO.readln으로 읽기

`readln`은 입력 안내문을 표시하고 `String`을 반환합니다. `Integer.parseInt`는 나이를 정수로 변환합니다.

```java
import static java.lang.IO.*; 
void main(){
    var name = readln("Name: ");
    var age = Integer.parseInt(readln("Age: ")); 
    var address = readln("Address: ");
    println("Entered data:");
    println("Name: " + name + ", Age: " + age);
    println("Address: " + address);
}
```

정수로 변환할 수 없는 입력은 `NumberFormatException`을 일으킵니다. 이 예제에서는 예외 처리를 생략했습니다. 콘솔은 학습에 적합하며 실제 프로그램에서는 폼이나 그래픽 인터페이스도 사용합니다.

한 줄 주석은 `//`으로 시작하고 여러 줄 주석은 `/*`과 `*/` 사이에 씁니다.

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

간결한 소스 파일 예제에는 프리뷰 기능을 활성화해야 할 수 있습니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
