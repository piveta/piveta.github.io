---
layout: post
title: "Javaのクラス"
date: 2026-10-21
lang: ja
translation_id: classes-em-java
permalink: /classes-in-java-ja/
share_text: >-
  Javaでクラス、フィールド、メソッド、コンストラクター、カプセル化を定義する方法を学びます。
---

Javaは、クラス、フィールド、メソッド、継承、インターフェース、ポリモーフィズム、カプセル化など、オブジェクト指向プログラミングの主要な概念をサポートしています。

## クラス、フィールド、メソッド

Javaでは、`class`キーワード、名前、フィールドやメソッドを定義する本体を使ってクラスを宣言します。その他の省略可能な要素については後で説明します。`Account`というクラスを考えてみましょう。他のクラスからアクセスできるように、`public`にできます。

```java
public class Account {
    // クラス本体
}
```

クラス本体にはフィールドとメソッドを追加できます。次の例では、`Double`型の`balance`フィールド[^2]と、`withdraw`メソッドを追加します。このメソッドは値を返さず（`void`）、`Double`型の`amount`という仮引数を受け取ります。メソッドは、引数として渡された金額を残高から差し引きます。

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // または balance -= amount;
    }
}
```

同様に、口座残高を増やす`deposit`メソッドも追加できます。

```java
public class Account {
    // balanceとwithdrawは省略
    public void deposit(Double amount) {
        balance = balance + amount; // または balance += amount;
    }
}
```

口座に対して操作を行うクライアントを考えます。まず、コンストラクターを呼び出して`Account`オブジェクトを作成し、その参照を`account`という変数に代入します。次に残高を100.00に設定し、50.00を引き出し、100.00を預け入れて、残高を出力します。

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

出力は次のとおりです。

```text
Balance: 150.0
```

`withdraw`と`deposit`はインスタンスメソッドなので、呼び出すには`Account`オブジェクトが必要です。最近のJavaでは、この例のように`main`も静的メソッドまたはインスタンスメソッドにできます[^3]。

前の例では、クライアントが`Account`のフィールドとメソッドを使っています。クライアントは暗黙的に宣言された名前のないクラスにあります。しかし、`balance`に直接アクセスしており、クラス間の結合が強くなります。これは通常望ましくありません[^4]。代わりに、`balance`へのアクセスをカプセル化し、専用メソッドを通して読み書きできます。これにより結合を弱め、読み書きの操作を維持したまま、残高の内部表現を後で変更できます。また、フィールドの可視性を下げ、クラス内からのみアクセスできるようにするのがよい方法です。

Javaには、パッケージプライベート（デフォルト）、`private`、`public`、`protected`の可視性があります。これらのレベルによって、どのクラスがフィールドやメソッドにアクセスできるかが決まります。パッケージプライベート以外のレベルにはキーワードがあります。

次のコードではカプセル化を改善し、内部状態をクライアントから隠します。公開の読み書きメソッド（`getBalance`と`setBalance`）を追加し、`balance`を`private`にして、これらのメソッドを通じて残高を更新します。`this`参照は、フィールド`balance`と同名のメソッド引数を区別します。`this.balance`は引数ではなくフィールドを指します。

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

クライアントも変更し、setterメソッドを通じて残高を更新します。

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

コンストラクターが明示的に宣言されていない場合、Javaクラスには引数なしのデフォルトコンストラクターがあります。クライアントがクラスを使いやすいように、他のコンストラクターを定義できます。たとえば、この`Account`コンストラクターは初期金額を受け取り、それを残高に設定します。スーパークラスのコンストラクターを呼び出す必要がある場合は、`super`を使います。

```java
public class Account {
    // Accountのフィールドとメソッド
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

`Account`には引数なしのデフォルトコンストラクターがなくなったため、クライアントは新しいコンストラクターを使い、初期残高を渡す必要があります[^5]。

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Javaにはデストラクターメソッドがありません。参照されなくなったオブジェクトは、ガベージコレクターによって自動的に回収されます。

[^2]: ここでは簡潔さのために`Double`を使用しています。金額は通常、浮動小数点型ではなく、`long`のような整数型や`BigDecimal`に格納します。

[^3]: [JEP 512](https://openjdk.org/jeps/512)を参照してください。

[^4]: ここでの「クラス」は`Account`と、`main`を含む暗黙的に宣言された名前のないクラスを指します。

[^5]: コンストラクターを定義すると、そのクラスにはデフォルトコンストラクターがなくなります。必要に応じて引数なしのコンストラクターを別途定義できます。

---

*この記事は、<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a>著『<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>』の内容をもとにしています。*

## 関連記事

- [オブジェクト指向プログラミングの基本概念](/oop-basics-java-ja/)
- [Javaの継承](/inheritance-in-java-ja/)
- [Javaのポリモーフィズム](/polymorphism-in-java-ja/)
- [Javaのインターフェース](/interfaces-in-java-ja/)
- [OOPとJavaのリンク集](/oop-java-links-ja/)
- [オブジェクト指向プログラミングの演習](/oop-exercises-ja/)
