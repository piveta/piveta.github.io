---
layout: post
title: "Javaのインターフェース"
date: 2026-10-21
lang: ja
translation_id: interfaces-em-java
permalink: /interfaces-in-java-ja/
share_text: >-
  Javaのインターフェースが契約を定義し、クラスがそれを実装する方法を学びます。
---

Javaのインターフェースはクラスと似た方法で定義します。通常、実装を持たないメソッドを宣言しますが、Javaはあらかじめ実装を持つデフォルトメソッドもサポートしています。インターフェースを実装するクラスは、デフォルトメソッドをオーバーライドするかどうかを選べます。

インターフェースは`interface`キーワードで宣言し、他のインターフェースを拡張できます。インターフェースでは多重継承が可能です。たとえば、Javaの`List`インターフェースは`Collection`と`Iterable`を拡張します。

次の例では、`AccountOperations`というインターフェースを宣言しています。これを実装するクラスは、少なくとも`withdraw`と`transfer`メソッドを提供する必要があります。

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

`Account`が`AccountOperations`を実装すると、そのサブクラスはメソッドを継承し、インターフェースの契約も満たします。ここでは具体クラス`Account`が`withdraw`と`transfer`を実装しているため、サブクラスで再実装する必要はありません。

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // withdrawの具体的な実装
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // transferの具体的な実装
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

別の方法として、`withdraw`、`deposit`、`transfer`の実装を`default`メソッドとして`AccountOperations`インターフェースに移すこともできます。このインターフェースでは`getBalance`と`setBalance`も宣言する必要があります。

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

簡略化した`Account`クラスは次のようになります。

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

インターフェースを`Account`から分離すると、クラスが残高を格納・管理する方法に柔軟性を持たせることができます。たとえば、Java Collections Frameworkの`List`インターフェースは、リストで実行できる操作を定義しています。`ArrayList`や`LinkedList`などの具体クラスは、異なる格納・アクセス方式を使います。前者は配列を、後者は双方向連結リストを使用します。

---

*この記事は、<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a>著『<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>』の内容をもとにしています。*

## 関連記事

- [オブジェクト指向プログラミングの基本概念](/oop-basics-java-ja/)
- [Javaのクラス](/classes-in-java-ja/)
- [Javaの継承](/inheritance-in-java-ja/)
- [Javaのポリモーフィズム](/polymorphism-in-java-ja/)
- [OOPとJavaのリンク集](/oop-java-links-ja/)
- [オブジェクト指向プログラミングの演習](/oop-exercises-ja/)
