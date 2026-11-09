---
layout: post
title: "Java의 클래스"
date: 2026-10-21
lang: ko
translation_id: classes-em-java
permalink: /classes-in-java-ko/
share_text: >-
  Java에서 클래스, 필드, 메서드, 생성자, 캡슐화를 정의하는 방법을 알아봅니다.
---

Java는 클래스, 필드, 메서드, 상속, 인터페이스, 다형성, 캡슐화 등 객체 지향 프로그래밍의 주요 개념을 지원합니다.

## 클래스, 필드, 메서드

Java에서는 `class` 키워드와 이름, 필드와 메서드를 정의할 수 있는 본문으로 클래스를 선언합니다. 다른 선택적 구성 요소는 뒤에서 설명합니다. `Account`라는 클래스를 생각해 봅시다. 다른 클래스에서 접근할 수 있도록 `public`으로 선언할 수 있습니다.

```java
public class Account {
    // 클래스 본문
}
```

클래스 본문에 필드와 메서드를 추가할 수 있습니다. 다음 예제에서는 `Double` 형식의 `balance` 필드[^2]와 `withdraw` 메서드를 추가합니다. 이 메서드는 값을 반환하지 않으며(`void`), `Double` 형식의 `amount`라는 형식 매개변수를 받습니다. 메서드는 인수로 전달된 금액을 잔액에서 뺍니다.

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // 또는 balance -= amount;
    }
}
```

마찬가지로 계좌 잔액을 늘리는 `deposit` 메서드를 추가할 수 있습니다.

```java
public class Account {
    // balance와 withdraw는 생략
    public void deposit(Double amount) {
        balance = balance + amount; // 또는 balance += amount;
    }
}
```

계좌에서 여러 작업을 수행하는 클라이언트를 생각해 봅시다. 먼저 생성자를 호출해 `Account` 객체를 만들고, 그 참조를 `account`라는 변수에 할당합니다. 그런 다음 잔액을 100.00으로 설정하고, 50.00을 인출하고, 100.00을 입금한 뒤 잔액을 출력합니다.

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

출력은 다음과 같습니다.

```text
Balance: 150.0
```

`withdraw`와 `deposit`은 인스턴스 메서드이므로 호출하려면 `Account` 객체가 필요합니다. 최신 Java 버전에서는 이 예제처럼 `main`도 정적 메서드나 인스턴스 메서드가 될 수 있습니다[^3].

앞의 예제는 `Account`의 필드와 메서드를 사용하는 클라이언트를 보여 줍니다. 클라이언트는 암시적으로 선언된 이름 없는 클래스 안에 있습니다. 그러나 `balance`에 직접 접근하므로 클래스 사이의 결합도가 높아집니다. 이는 일반적으로 바람직하지 않습니다[^4]. 대안으로 `balance` 접근을 캡슐화하여 전용 메서드로 읽고 쓰게 할 수 있습니다. 그러면 결합도를 낮추고 읽기 및 쓰기 작업을 계속 제공하는 한 잔액의 내부 표현을 나중에 변경할 수도 있습니다. 필드의 가시성을 낮춰 클래스 내부에서만 접근할 수 있도록 하는 것도 좋은 방법입니다.

Java의 가시성에는 패키지 전용(기본값), `private`, `public`, `protected`가 있습니다. 이 수준에 따라 어떤 클래스가 필드나 메서드에 접근할 수 있는지가 결정됩니다. 패키지 전용을 제외한 각 수준에는 키워드가 있습니다.

다음 코드는 캡슐화를 개선하고 클래스의 내부 상태를 클라이언트로부터 숨깁니다. 공개 읽기 및 쓰기 메서드(`getBalance`와 `setBalance`)를 추가하고, `balance`의 가시성을 `private`으로 바꾸며, 이 메서드로 잔액을 갱신합니다. `this` 참조는 `balance` 필드와 이름이 같은 메서드 매개변수를 구분합니다. `this.balance`는 매개변수가 아니라 필드를 가리킵니다.

```java
public class Account {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
}
```

클라이언트도 변경하여 setter 메서드로 잔액을 수정합니다.

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

생성자를 명시적으로 선언하지 않으면 Java 클래스에는 매개변수가 없는 기본 생성자가 있습니다. 클라이언트가 클래스를 더 쉽게 사용할 수 있도록 다른 생성자를 정의할 수 있습니다. 예를 들어 이 `Account` 생성자는 초기 금액을 받아 잔액으로 설정합니다. 상위 클래스의 생성자를 호출해야 한다면 `super`를 사용할 수 있습니다.

```java
public class Account {
    // Account의 필드와 메서드
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

이제 `Account`에는 인수가 없는 기본 생성자가 없으므로 클라이언트는 새 생성자를 사용하고 초기 잔액을 제공해야 합니다[^5].

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java에는 소멸자 메서드가 없습니다. 더 이상 참조되지 않는 객체는 가비지 컬렉터가 자동으로 회수합니다.

[^2]: 간단한 설명을 위해 여기서는 `Double`을 사용합니다. 금액은 일반적으로 부동 소수점 변수에 저장하지 않고 `long` 같은 정수 형식이나 `BigDecimal`을 사용합니다.

[^3]: [JEP 512](https://openjdk.org/jeps/512)를 참조하세요.

[^4]: 여기서 “클래스들”은 `Account`와 `main`을 포함하는 암시적 이름 없는 클래스를 가리킵니다.

[^5]: 생성자를 정의하면 클래스에는 더 이상 기본 생성자가 없습니다. 필요한 경우 인수가 없는 생성자를 별도로 정의할 수 있습니다.

---

*이 글은 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a>의 저서 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>의 내용을 바탕으로 작성했습니다.*

## 관련 글

- [객체 지향 프로그래밍의 기본 개념](/oop-basics-java-ko/)
- [Java의 상속](/inheritance-in-java-ko/)
- [Java의 다형성](/polymorphism-in-java-ko/)
- [Java의 인터페이스](/interfaces-in-java-ko/)
- [OOP와 Java 링크](/oop-java-links-ko/)
- [객체 지향 프로그래밍 연습 문제](/oop-exercises-ko/)
