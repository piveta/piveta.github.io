---
layout: post
title: "Java의 상속"
date: 2026-10-21
lang: ko
translation_id: heranca-em-java
permalink: /inheritance-in-java-ko/
share_text: >-
  Java의 상속, 메서드 재정의, 하위 타입 변환, 추상 클래스를 소개합니다.
---

**상속**은 기존 클래스의 인터페이스와 동작을 재사용하면서 기능을 확장할 수 있게 하는 합성 메커니즘입니다. 다른 클래스를 상속해 확장하는 클래스를 **하위 클래스**, 확장되는 클래스를 **상위 클래스**라고 합니다.

Java는 클래스의 단일 상속을 허용합니다(인터페이스는 다중 상속이 가능합니다). 하위 클래스는 상위 클래스의 하위 타입입니다. 하위 클래스에서 `extends` 키워드로 상속을 선언합니다. 예: `Class extends SuperClass`. 상위 클래스가 명시적으로 선언되지 않은 클래스는 Java 클래스 계층의 루트인 `Object`의 하위 클래스가 됩니다.

다음 `CheckingAccount` 클래스를 살펴봅시다. 이 클래스는 `Account`를 확장하고 필드, 필드를 읽고 쓰는 메서드, 생성자를 추가합니다. `Account`에 인수가 없는 생성자가 없으므로 `CheckingAccount` 생성자는 `super`를 사용해 상위 클래스의 생성자를 호출합니다.

```java
public class CheckingAccount extends Account {
    private Double dailyWithdrawalLimit;
    public Double getDailyWithdrawalLimit() {
        return dailyWithdrawalLimit;
    }
    public void setDailyWithdrawalLimit(Double dailyWithdrawalLimit) {
        this.dailyWithdrawalLimit = dailyWithdrawalLimit;
    }
    public CheckingAccount(Double amount) {
        super(amount);
    }
}
```

하위 클래스에는 상위 클래스에서 선언된 동작을 확장하거나 대체하는 **재정의된 메서드**가 흔히 있습니다. 여기서 `CheckingAccount`는 같은 시그니처[^6]의 메서드를 선언하여 `Account`의 `withdraw`를 재정의합니다. 먼저 `super`로 상위 클래스의 메서드를 호출한 다음, `deductFee`를 통해 거래 금액의 1%를 잔액에서 차감합니다.

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // 다른 생성자, 필드, 메서드
}
```

예를 들어 `CheckingAccount`의 초기 잔액이 100.00일 때 50.00을 인출하면 0.50의 수수료가 부과되어 잔액은 49.50이 됩니다.

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

리스코프 치환 원칙에 따라 상위 클래스 객체가 필요한 곳에 하위 클래스 객체를 할당할 수 있습니다. 모든 `CheckingAccount` 인스턴스는 `Account` 인스턴스이기도 합니다. 반대는 항상 참이 아닙니다. 예를 들어 `Account`는 `SavingsAccount`일 수 있습니다. 이런 경우 명시적 형 변환(*캐스트*)이 필요합니다.

다음 예제에서 `checkingAccount`는 `CheckingAccount` 타입이며 해당 클래스의 인스턴스를 참조합니다. `Account` 타입의 `account` 변수에는 같은 객체가 할당됩니다. 이 할당에는 변환이 필요하지 않습니다. 반대 방향의 할당에는 명시적 캐스트가 필요합니다.

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // CheckingAccount는 Account이다.
checkingAccount = (CheckingAccount) account; // 유효한 명시적 캐스트
```

`SavingsAccount`도 `Account`의 하위 클래스라고 가정해 봅시다. 다음 예제에서 `account`는 `CheckingAccount`를 참조합니다. 객체가 `SavingsAccount`가 아니므로 `SavingsAccount`로 캐스팅하면 실행 중 실패합니다.

```java
Account account = new CheckingAccount(100.00);
// 다음 명시적 캐스트는 실행 중 실패합니다.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

최신 IDE는 명백히 잘못된 변환에 경고를 표시하지만, 결과를 미리 알 수 없는 경우도 있습니다. 예를 들어 메서드의 인수는 메서드가 호출될 때에야 알 수 있습니다. 잘못된 캐스트는 `ClassCastException` 형식의 런타임 예외를 일으킬 수 있습니다[^7].

`Account`에는 `CheckingAccount`, `SavingsAccount`, 그리고 경우에 따라 `InvestmentAccount` 같은 여러 하위 타입이 있을 수 있습니다. 하위 클래스의 인스턴스만 만들 수 있도록 `Account`를 추상 클래스로 만들 수 있습니다.

```java
public abstract class Account {
    // 모든 계좌 유형에 공통인 필드와 메서드
}
```

이제 `Account`를 직접 인스턴스화할 수 없습니다. 앞선 예제처럼 하위 클래스의 생성자를 사용해야 합니다.

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: Java에서 메서드 시그니처는 이름, 타입 매개변수(있는 경우), 형식 매개변수로 구성됩니다. [Java 언어 명세](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2)를 참조하세요.

[^7]: [ClassCastException API 문서](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html)를 참조하세요.

---

*이 글은 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a>의 저서 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>의 내용을 바탕으로 작성했습니다.*

## 관련 글

- [객체 지향 프로그래밍의 기본 개념](/oop-basics-java-ko/)
- [Java의 클래스](/classes-in-java-ko/)
- [Java의 다형성](/polymorphism-in-java-ko/)
- [Java의 인터페이스](/interfaces-in-java-ko/)
- [OOP와 Java 링크](/oop-java-links-ko/)
- [객체 지향 프로그래밍 연습 문제](/oop-exercises-ko/)
