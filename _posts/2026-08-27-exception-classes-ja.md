---
layout: post
title: "Javaの例外クラス"
date: 2026-08-27
lang: ja
translation_id: classes-de-excecao
permalink: /java-exception-classes-ja/
image: /images/descendentesThrowable.png
---
プログラムの実行中には、特別な処理を必要とする状況が発生することがあります。それらは、異常またはエラーの状態、プログラマが予期していなかった状況、あるいは別の実行フローを表すことがあります。このような状態を**例外**と呼びます。

Javaでは、例外は`Throwable`クラスまたはそのサブクラスのいずれかに属するオブジェクトとして表されます。例外の階層を理解することは、プログラムによってどの例外をスロー、捕捉、処理できるのかを理解するうえで重要です。

## Throwable

`Throwable`は、Javaの例外階層の基底クラスです。このクラスのオブジェクトは、ある特定の発生事象に関する情報を保持し、例外が発生した場所から、その処理を担当するコードへ情報を渡すことができます。

`Throwable`またはそのサブクラスに属するオブジェクトだけが、JVMまたはプログラマによって`throw`を使用してスローできます。同様に、`catch`節で捕捉できるのも、この階層に属するオブジェクトだけです。

`Throwable`の主なメソッドには、例外に関連付けられたメッセージを取得する`getMessage()`と、例外が発生した箇所までの実行スタックトレースを表示する`printStackTrace()`があります。

`Throwable`クラスには、`Exception`と`Error`という2つの直接のサブクラスがあります。

<img src="/images/descendentesThrowable.png"
     alt="Throwableの階層"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

`Error`クラスは、通常、アプリケーションが回復できない重大な状態を表します。これらは、プログラムの実行中には通常発生すべきではない異常な状況です。

`Error`の主なサブクラスには、`AssertionError`、`IOError`、`VirtualMachineError`があります。後者には、`InternalError`、`OutOfMemoryError`、`StackOverflowError`、`UnknownError`などのサブクラスがあります。

エラーはJVM自身によってスローされることがあり、オペレーティングシステムや実行環境によって検出された状態が原因となる場合があります。また、プログラマが`assert`や`throw`などを使用して明示的に発生させることもできます。

<img src="/images/exceptionsError.png"
     alt="Errorとそのサブクラス"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

`Exception`クラスは、特定の状況では処理することができ、アプリケーションがそこから回復できる例外を表します。

そのサブクラスには、`IOException`、`SQLException`、`ReflectiveOperationException`、`ClassNotFoundException`、`RuntimeException`があります。

`RuntimeException`のサブクラスではない`Exception`のサブクラスを**検査例外**（*checked exceptions*）と呼びます。コンパイラは、プログラムがこれらを明示的に扱うことを要求します。これは、`catch`節で例外を捕捉するか、`throws`を使用してメソッドがその例外をスローする可能性があることを宣言することで行えます。

<img src="/images/descendentesException.png"
     alt="Exceptionとそのサブクラス"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

`Exception`のサブクラスの中でも、`RuntimeException`は特に重要です。これとそのサブクラスを**実行時例外**（*runtime exceptions*）と呼びます。

`RuntimeException`とそのサブクラスは**非検査例外**（*unchecked exceptions*）です。コンパイラは、これらを`try`/`catch`で明示的に処理したり、`throws`で宣言したりすることを要求しません。

この種類の例外は、通常、論理エラーやプログラムの誤った使用を表します。一般的な例には次のものがあります。

- `ClassCastException`：明示的な型変換ができない場合に発生します。
- `IllegalArgumentException`：メソッドが無効または不適切と判断される引数を受け取ったことを示します。
- `IndexOutOfBoundsException`：インデックス付き構造の存在しない位置へアクセスしようとした場合に発生します。
- `NullPointerException`：`null`参照に対して操作を行った場合に発生します。

`RuntimeException`をスローする可能性のあるメソッドは、その可能性を`throws`で宣言する必要がありません。もちろん、これらの例外を`try`と`catch`で捕捉して処理することは可能です。

実際には、多くの`RuntimeException`インスタンスは、プログラム自体によって防ぐことができた問題を示しています。このような例外が発生した場合は、単に例外を捕捉するのではなく、その原因を調査して問題を修正することが通常重要です。

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeExceptionとそのサブクラス"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## 検査例外と非検査例外

Javaの例外階層における重要な区別の一つが、**検査例外**と**非検査例外**の違いです。

`Throwable`と、そのサブクラスのうち`RuntimeException`または`Error`のサブクラスではないものを**検査例外**と呼びます。`RuntimeException`とそのサブクラス、および`Error`とそのサブクラスは、**非検査例外**と呼びます。

検査例外は、プログラムによって処理するか、明示的に宣言する必要があります。つまり、検査例外をスローする可能性のあるメソッドは、その例外を`catch`節で処理するか、メソッドの`throws`節で宣言しなければなりません。

一方、非検査例外は明示的に処理または宣言する必要がありません。コンパイラは、`RuntimeException`、`Error`、またはそれらのサブクラスを捕捉または宣言することを要求しません。

簡略化すると、階層は次のように表せます。

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

この構成により、階層の異なるレベルで処理を行うことができます。たとえば、`catch`節では、目的とする動作に応じて、特定の例外またはそのスーパークラスのいずれかを捕捉できます。

この階層を理解することは、Javaの例外処理機構を理解し、どの例外を処理し、どの例外を伝播させ、どの例外をプログラム自体で修正すべきエラーとみなすかを判断するうえで基本となります。

この記事は、<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>（<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>著）の内容をもとにしています。
