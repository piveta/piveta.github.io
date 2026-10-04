---
layout: post
title: "Java의 예외 클래스"
date: 2026-08-27
lang: ko
translation_id: classes-de-excecao
permalink: /java-exception-classes-ko/
image: /images/descendentesThrowable.png
share_text: >-
  Java 예외 계층은 Throwable에서 시작해 Error와 Exception으로 나뉘며, RuntimeException은 비검사 예외에 속합니다. 이 글에서는 검사 예외와 비검사 예외의 차이를 살펴봅니다.
---
프로그램을 실행하는 동안 특별한 처리가 필요한 상황이 발생할 수 있습니다. 이러한 상황은 비정상적이거나 오류가 있는 상태, 프로그래머가 예상하지 못한 상황, 또는 다른 실행 흐름을 나타낼 수 있습니다. 이러한 상태를 **예외(exception)**라고 합니다.

Java에서 예외는 `Throwable` 클래스 또는 그 하위 클래스에 속하는 객체로 표현됩니다. 예외 계층 구조를 이해하는 것은 프로그램에서 어떤 예외를 발생시키고, 포착하고, 처리할 수 있는지 이해하는 데 중요합니다.

## Throwable

`Throwable`은 Java 예외 계층 구조의 기본 클래스입니다. 이 클래스의 객체는 특정 발생 상황에 대한 정보를 저장하며, 예외가 발생한 지점에서 그 처리를 담당하는 코드로 이 정보를 전달할 수 있습니다.

`Throwable` 또는 그 하위 클래스에 속하는 객체만 JVM이나 프로그래머가 `throw`를 사용하여 발생시킬 수 있습니다. 마찬가지로 `catch` 절도 이 계층 구조에 속하는 객체만 포착할 수 있습니다.

`Throwable`의 주요 메서드로는 예외와 연결된 메시지를 가져오는 `getMessage()`와 예외가 발생한 지점까지의 실행 스택 추적을 표시하는 `printStackTrace()`가 있습니다.

`Throwable` 클래스에는 `Exception`과 `Error`라는 두 개의 직접적인 하위 클래스가 있습니다.

<img src="/images/descendentesThrowable.png"
     alt="Throwable 계층 구조"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

`Error` 클래스는 일반적으로 애플리케이션이 복구할 수 없는 심각한 상태를 나타냅니다. 이러한 상황은 프로그램 실행 중에 일반적으로 발생해서는 안 되는 비정상적인 상황입니다.

`Error`의 주요 하위 클래스로는 `AssertionError`, `IOError`, `VirtualMachineError`가 있습니다. 후자에는 `InternalError`, `OutOfMemoryError`, `StackOverflowError`, `UnknownError` 등의 하위 클래스가 있습니다.

오류는 JVM 자체에서 발생시킬 수 있으며, 운영 체제나 실행 환경에서 감지한 조건의 결과인 경우가 많습니다. 또한 프로그래머가 `assert`나 `throw` 등을 사용하여 명시적으로 발생시킬 수도 있습니다.

<img src="/images/exceptionsError.png"
     alt="Error와 그 하위 클래스"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

`Exception` 클래스는 특정 상황에서 처리할 수 있고 애플리케이션이 복구할 수 있는 예외를 나타냅니다.

하위 클래스에는 `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException`, `RuntimeException` 등이 있습니다.

`RuntimeException`의 하위 클래스가 아닌 `Exception`의 하위 클래스를 **검사 예외(checked exception)**라고 합니다. 컴파일러는 프로그램이 이러한 예외를 명시적으로 처리하도록 요구합니다. 이는 `catch` 절로 예외를 포착하거나 `throws`를 사용하여 메서드가 해당 예외를 발생시킬 수 있음을 선언하는 방식으로 수행할 수 있습니다.

<img src="/images/descendentesException.png"
     alt="Exception과 그 하위 클래스"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

`Exception`의 하위 클래스 중에서 `RuntimeException`이 특히 중요합니다. 이 클래스와 그 하위 클래스를 **런타임 예외(runtime exception)**라고 합니다.

`RuntimeException`과 그 하위 클래스는 **비검사 예외(unchecked exception)**입니다. 컴파일러는 이러한 예외를 `try`/`catch`로 명시적으로 처리하거나 `throws`로 선언하도록 요구하지 않습니다.

이러한 유형의 예외는 일반적으로 논리적 오류나 프로그램의 잘못된 사용을 나타냅니다. 일반적인 예는 다음과 같습니다.

- `ClassCastException`: 명시적인 형 변환이 불가능할 때 발생합니다.
- `IllegalArgumentException`: 메서드가 유효하지 않거나 부적절하다고 판단되는 인자를 받았음을 나타냅니다.
- `IndexOutOfBoundsException`: 인덱스로 접근하는 구조에서 존재하지 않는 위치에 접근하려 할 때 발생합니다.
- `NullPointerException`: `null` 참조에 대해 연산을 수행할 때 발생합니다.

`RuntimeException`을 발생시킬 수 있는 메서드는 이러한 가능성을 `throws`로 선언할 필요가 없습니다. 물론 이러한 예외를 `try`와 `catch`로 포착하고 처리할 수는 있습니다.

실제로 많은 `RuntimeException` 인스턴스는 프로그램 자체에서 예방할 수 있었던 문제를 나타냅니다. 이러한 예외가 발생하면 단순히 예외를 포착하기보다는 원인을 조사하고 문제를 수정하는 것이 일반적으로 중요합니다.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException과 그 하위 클래스"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## 검사 예외와 비검사 예외

Java의 예외 계층 구조에서 중요한 구분은 **검사 예외**와 **비검사 예외**의 차이입니다.

`Throwable`과 그 하위 클래스 중 `RuntimeException` 또는 `Error`의 하위 클래스가 아닌 것들을 **검사 예외**라고 합니다. `RuntimeException`과 그 하위 클래스, 그리고 `Error`와 그 하위 클래스는 **비검사 예외**라고 합니다.

검사 예외는 프로그램에서 처리하거나 명시적으로 선언해야 합니다. 즉, 검사 예외를 발생시킬 수 있는 메서드는 해당 예외를 `catch` 절에서 처리하거나 메서드의 `throws` 절에 선언해야 합니다.

반면 비검사 예외는 명시적으로 처리하거나 선언할 필요가 없습니다. 컴파일러는 `RuntimeException`, `Error` 또는 그 하위 클래스를 포착하거나 선언하도록 요구하지 않습니다.

단순화하면 계층 구조는 다음과 같이 나타낼 수 있습니다.

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

이러한 구조를 통해 계층 구조의 서로 다른 수준에서 예외를 처리할 수 있습니다. 예를 들어 원하는 동작에 따라 `catch` 절에서 특정 예외 또는 그 상위 클래스 중 하나를 포착할 수 있습니다.

이 계층 구조를 이해하는 것은 Java의 예외 처리 메커니즘을 이해하고, 어떤 예외를 처리해야 하는지, 어떤 예외를 전파해야 하는지, 어떤 예외가 프로그램 자체에서 수정해야 할 오류를 나타내는지를 결정하는 데 기본적입니다.

이 글은 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>의 내용을 바탕으로 작성되었으며, 저자는 <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>입니다.
