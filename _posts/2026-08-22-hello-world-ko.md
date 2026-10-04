---
layout: post
title: "Hello World - 전통적인 버전과 간소화된 버전"
date: 2026-08-22
lang: ko
translation_id: hello-world
permalink: /hello-world-ko/
share_text: >-
  전통적인 Java Hello World 프로그램의 클래스와 main 메서드, 컴파일과 실행 과정을 살펴봅니다. 이어서 Java 25부터 사용할 수 있는 간결한 소스 파일과 인스턴스 main 메서드를 소개합니다.
---

프로그래밍 언어를 공부할 때 일반적으로 **Hello World**라는 프로그램을 작성하는 것부터 시작합니다. 이 프로그램은 장치의 표준 출력, 일반적으로 화면에 `Hello World!`라는 텍스트를 표시합니다. Java에서는 다음과 같이 작성할 수 있습니다.

```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```

이 프로그램에는 `Hello`라는 이름의 클래스가 있습니다. 객체 지향 시스템에서 클래스는 연구 대상인 애플리케이션 도메인의 개념을 모델링하는 데 사용됩니다. 클래스는 특정 개념과 관련된 데이터와 동작을 모두 캡슐화합니다.

`Hello` 클래스에는 `main`이라는 하나의 메서드가 있습니다. 이 메서드는 프로그램 실행 시 제공된 명령줄 인자를 담은 문자열 배열을 받으며, 인자가 없는 경우도 있습니다. 이 예제에서는 이러한 인자를 사용하지 않습니다.

`main` 메서드는 static입니다. 즉, 인스턴스 메서드가 아니라 클래스 메서드입니다. 따라서 `Hello` 클래스의 객체를 생성하지 않고 호출할 수 있습니다.

`main` 메서드 내부에서는 `println` 메서드를 호출합니다. 이 메서드는 `PrintStream` 클래스에 속하며 인자로 전달된 값을 화면에 출력한 다음 줄 종결자를 출력합니다.

`println` 메서드는 `System` 클래스의 `out` 필드를 통해 호출됩니다. 이 필드의 타입은 `PrintStream`이며 시스템의 표준 출력에 접근할 수 있게 합니다.

## 컴파일과 실행

Java 프로그램은 먼저 **바이트코드**라는 중간 표현으로 컴파일되므로 이식성을 확보할 수 있습니다. 이후 이 바이트코드는 Java Virtual Machine(JVM)에 의해 실행되며, 기반 플랫폼에 적합한 기계어 코드로 변환됩니다.

프로그램을 컴파일하려면 `Hello.java`라는 파일에 저장해야 합니다. Java에서는 public 타입을 포함하는 파일은 일반적으로 해당 타입과 같은 이름을 가집니다.

통합 개발 환경(**IDE**)을 사용하거나 JDK가 설치되어 있다면 명령줄에서 컴파일러를 직접 호출할 수 있습니다.

Java 프로그램은 일반적으로 IDE에서 작성합니다. IDE는 소스 코드 탐색, 리팩터링, 정적 분석, 컴파일, 테스트, 디버깅 등 개발 생산성을 높이는 기능을 제공합니다.

Java에서 널리 사용되는 IDE는 다음과 같습니다.

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

`javac` 컴파일러를 사용하여 명령줄에서 직접 프로그램을 컴파일할 수도 있습니다.

```text
    javac Hello.java
```

이 명령은 `Hello.java`를 입력으로 받아 컴파일된 프로그램이 들어 있는 `Hello.class` 파일을 생성합니다.

컴파일한 후에는 `java` 명령을 사용하여 프로그램을 실행할 수 있습니다.

```text
    java Hello
```

출력은 다음과 같습니다.

```text
    Hello World!
```

## Java 25+의 더 간단한 방법

Java 25부터 Java 21 이후 *preview*로 개발되어 온 **Compact Source Files and Instance Main Methods** 기능이 정식 기능이 되었습니다. 이 기능을 사용하면 명시적인 클래스 선언을 생략하고 `main` 메서드를 간소화하여 적은 상용구 코드로 작은 프로그램을 작성할 수 있습니다.

따라서 앞의 프로그램은 현재 버전인 Java 26에서 다음과 같이 작성할 수 있습니다.

```java
    void main() {
        IO.println("Hello World!");
    }
```

이 경우 클래스를 명시적으로 선언하거나 `public static void main(String[] args)`를 작성할 필요가 없습니다. 컴파일러는 파일이 암묵적으로 클래스를 선언하는 것으로 처리하며, `main` 메서드는 인스턴스 메서드가 될 수 있습니다.

또한 간단한 콘솔 입출력 기능을 제공하는 `IO` 클래스도 사용할 수 있습니다. Java 26에서 `IO`는 `java.lang` 패키지에 속하므로 암묵적으로 사용할 수 있습니다. 그러나 해당 메서드를 호출하려면 `IO.println(...)`과 같이 클래스 이름을 사용해야 합니다.

이 기능은 더 이상 *preview* 상태가 아니므로 특별한 컴파일 옵션이 필요하지 않습니다. 프로그램은 일반적인 방법으로 컴파일할 수 있습니다.

```text
    javac Hello.java
```

그리고 같은 방식으로 실행할 수 있습니다.

```text
    java Hello
```

`java` 런처를 사용하여 소스 파일을 직접 실행하는 것도 가능합니다.

```text
    java Hello.java
```

이 경우 실행 전에 런처 자체가 소스 코드를 메모리에서 컴파일합니다. 이를 통해 명시적으로 `.class` 파일을 생성하지 않고도 소스 파일에서 직접 프로그램을 실행할 수 있습니다.

컴팩트 소스 파일은 작은 예제, 학습 프로그램, 스크립트 및 실험에 특히 유용합니다. 프로그램이 커지고 더 정교한 구조가 필요해지면 명시적인 클래스와 메서드 선언을 사용하는 전통적인 형태로 자연스럽게 돌아갈 수 있습니다.

IDE가 수행하는 과정도 본질적으로 유사합니다. 컴파일과 실행 외에도 디버깅, 테스트, 리팩터링, 프로젝트 생성 및 관리, 라이브러리 생성, 버전 관리 등 다양한 기능을 제공합니다.

---

*이 글은 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>의 내용을 바탕으로 작성되었으며, 저자는 <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>입니다.*
