---
layout: post
title: "Java의 생성자"
date: 2026-11-24
lang: ko
translation_id: construtores-java
permalink: /ko/constructors-in-java/
share_text: "Java의 생성자"
---

생성자는 객체가 만들어질 때 그 상태를 초기화합니다. 책의 `Account` 클래스에서는 생성자가 초기 잔액을 받아 `setBalance`로 설정합니다. 첫 번째 코드에서는 나머지 필드와 메서드를 생략했습니다.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

`new Account(100.00)`으로 잔액이 100인 계좌를 만들고 50을 인출한 다음 100을 입금합니다. 출력되는 잔액은 `150.0`입니다.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

일반 클래스에 생성자 선언이 없으면 컴파일러가 기본 생성자를 제공합니다. `Account(Double value)`를 선언하면 이 암시적 생성자를 사용할 수 없습니다. `new Account()`도 지원하려면 인수가 없는 생성자를 명시적으로 선언하세요. 하위 클래스는 `Account`의 생성자를 상속하지 않지만 `super(value)`로 호출할 수 있습니다.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*참고 도서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

