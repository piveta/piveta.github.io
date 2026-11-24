---
layout: post
title: "Javaのコンストラクタ"
date: 2026-11-24
lang: ja
translation_id: construtores-java
permalink: /ja/constructors-in-java/
share_text: "Javaのコンストラクタ"
---

コンストラクタはオブジェクトの生成時にその状態を初期化します。本書の `Account` クラスでは、初期残高を受け取り、`setBalance` で設定します。最初のコード例では、ほかのフィールドとメソッドを省略しています。

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

`new Account(100.00)` で残高100の口座を作り、50を引き出して100を預け入れます。表示される残高は `150.0` です。

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

通常のクラスでコンストラクタを一つも宣言しないと、コンパイラがデフォルトコンストラクタを用意します。`Account(Double value)` を宣言すると、この暗黙のコンストラクタは使えなくなります。`new Account()` も使うには、引数なしのコンストラクタを明示的に宣言します。サブクラスは `Account` のコンストラクタを継承しませんが、`super(value)` で呼び出せます。

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*出典 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

