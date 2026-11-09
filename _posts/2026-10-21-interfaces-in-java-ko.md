---
layout: post
title: "Java의 인터페이스"
date: 2026-10-21
lang: ko
translation_id: interfaces-em-java
permalink: /interfaces-in-java-ko/
share_text: >-
  Java 인터페이스가 계약을 정의하고 클래스가 이를 구현하는 방법을 알아봅니다.
---

Java의 인터페이스는 클래스와 비슷한 방식으로 정의합니다. 일반적으로 구현이 없는 메서드를 선언하지만, Java는 미리 정의된 구현을 갖는 기본 메서드(*default methods*)도 지원합니다. 인터페이스를 구현하는 클래스는 기본 메서드를 재정의할지 선택할 수 있습니다.

인터페이스는 `interface` 키워드로 선언하며 다른 인터페이스를 확장할 수 있습니다. 인터페이스에는 다중 상속이 허용됩니다. 예를 들어 Java의 `List` 인터페이스는 `Collection`과 `Iterable`을 확장합니다.

다음 예제는 `AccountOperations`라는 인터페이스를 선언합니다. 이를 구현하는 클래스는 적어도 `withdraw`와 `transfer` 메서드를 제공해야 합니다.

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

`Account`가 `AccountOperations`를 구현하면 하위 클래스는 메서드를 상속하고 인터페이스 계약도 충족합니다. 여기서는 구체 클래스 `Account`가 `withdraw`와 `transfer`를 구현하므로 하위 클래스에서 다시 구현할 필요가 없습니다.

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // withdraw의 구체적 구현
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // transfer의 구체적 구현
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

또 다른 방법은 `withdraw`, `deposit`, `transfer`의 구현을 `AccountOperations` 인터페이스의 `default` 메서드로 옮기는 것입니다. 인터페이스에는 `getBalance`와 `setBalance`도 선언해야 합니다.

```java
public interface AccountOperations {
    public Double getBalance();
    public void setBalance(Double balance);
    public default void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public default void transfer(AccountOperations destination,
                                 Double amount) {
        destination.deposit(amount);
        this.withdraw(amount);
    }
    public default void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
}
```

간소화된 `Account` 클래스는 다음과 같습니다.

```java
public class Account implements AccountOperations {
    private Double balance;

    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

인터페이스를 `Account`와 분리하면 클래스가 잔액을 저장하고 관리하는 방식에 더 많은 유연성을 줄 수 있습니다. 예를 들어 Java 컬렉션 프레임워크에는 목록이 수행할 수 있는 작업을 정의하는 `List` 인터페이스가 있습니다. `ArrayList`와 `LinkedList` 같은 구체 구현은 서로 다른 저장 및 접근 전략을 사용합니다. 전자는 배열을, 후자는 이중 연결 리스트를 사용합니다.

---

*이 글은 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a>의 저서 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>의 내용을 바탕으로 작성했습니다.*

## 관련 글

- [객체 지향 프로그래밍의 기본 개념](/oop-basics-java-ko/)
- [Java의 클래스](/classes-in-java-ko/)
- [Java의 상속](/inheritance-in-java-ko/)
- [Java의 다형성](/polymorphism-in-java-ko/)
- [OOP와 Java 링크](/oop-java-links-ko/)
- [객체 지향 프로그래밍 연습 문제](/oop-exercises-ko/)
