---
layout: post
title: "Javaの継承"
date: 2026-10-21
lang: ja
translation_id: heranca-em-java
permalink: /inheritance-in-java-ja/
share_text: >-
  Javaの継承、メソッドのオーバーライド、サブタイプ変換、抽象クラスを紹介します。
---

**継承**は、既存クラスのインターフェースと振る舞いを再利用し、その機能を拡張するための合成メカニズムです。継承によって別のクラスを拡張するクラスを**サブクラス**、拡張されるクラスを**スーパークラス**と呼びます。

Javaのクラスは単一継承をサポートします（インターフェースでは多重継承が可能です）。サブクラスはスーパークラスのサブタイプです。継承はサブクラスで`extends`キーワードを使って宣言します（`Class extends SuperClass`）。スーパークラスが明示されていないクラスは、Javaのクラス階層のルートである`Object`のサブクラスになります。

次の`CheckingAccount`クラスを考えてみましょう。これは`Account`を拡張し、フィールド、その読み書きメソッド、コンストラクターを追加します。`Account`には引数なしのコンストラクターがないため、`CheckingAccount`のコンストラクターは`super`を使ってスーパークラスのコンストラクターを呼び出します。

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

サブクラスには、スーパークラスで宣言された振る舞いを拡張または置き換える**オーバーライドされたメソッド**がよくあります。ここでは、`CheckingAccount`が同じシグネチャ[^6]を持つメソッドを宣言し、`Account`の`withdraw`をオーバーライドしています。まず`super`でスーパークラスのメソッドを呼び出し、次に`deductFee`で取引額の1%を残高から差し引きます。

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // その他のコンストラクター、フィールド、メソッド
}
```

たとえば、`CheckingAccount`の初期残高が100.00で、50.00を引き出すと、0.50の手数料が差し引かれ、残高は49.50になります。

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

リスコフの置換原則に従えば、スーパークラスのオブジェクトが期待される場所にサブクラスのオブジェクトを代入できます。すべての`CheckingAccount`インスタンスは`Account`インスタンスでもあります。逆は常に成り立つわけではなく、`Account`は`SavingsAccount`かもしれません。この場合は明示的な型変換（*キャスト*）が必要です。

次の例では、`checkingAccount`は`CheckingAccount`型で、そのクラスのインスタンスを参照します。`Account`型の変数`account`には同じオブジェクトが代入されます。この代入に変換は必要ありません。逆方向の代入には明示的なキャストが必要です。

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // CheckingAccountはAccountである
checkingAccount = (CheckingAccount) account; // 有効な明示的キャスト
```

`SavingsAccount`も`Account`のサブクラスだとします。次の例で`account`は`CheckingAccount`を参照しています。このオブジェクトは`SavingsAccount`ではないため、`SavingsAccount`へのキャストは実行時に失敗します。

```java
Account account = new CheckingAccount(100.00);
// 次の明示的キャストは実行時に失敗する
SavingsAccount savingsAccount = (SavingsAccount) account;
```

現代のIDEは明らかに誤った変換を警告しますが、事前に結果が分からない場合もあります。たとえば、メソッドの引数が分かるのは呼び出し時です。誤ったキャストは`ClassCastException`型の実行時例外を引き起こすことがあります[^7]。

`Account`には`CheckingAccount`、`SavingsAccount`、場合によっては`InvestmentAccount`など複数のサブタイプがあるため、抽象クラスにして、そのサブクラスだけをインスタンス化できるようにできます。

```java
public abstract class Account {
    // すべての口座種別に共通するフィールドとメソッド
}
```

`Account`を直接インスタンス化することはできません。前の例のように、サブクラスのコンストラクターを使います。

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: Javaのメソッドシグネチャは、名前、型パラメーター（あれば）、仮パラメーターで構成されます。[Java言語仕様](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2)を参照してください。

[^7]: [ClassCastException APIドキュメント](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html)を参照してください。

---

*この記事は、<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a>著『<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>』の内容をもとにしています。*

## 関連記事

- [オブジェクト指向プログラミングの基本概念](/oop-basics-java-ja/)
- [Javaのクラス](/classes-in-java-ja/)
- [Javaのポリモーフィズム](/polymorphism-in-java-ja/)
- [Javaのインターフェース](/interfaces-in-java-ja/)
- [OOPとJavaのリンク集](/oop-java-links-ja/)
- [オブジェクト指向プログラミングの演習](/oop-exercises-ja/)
