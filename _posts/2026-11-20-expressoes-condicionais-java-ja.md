---
layout: post
title: "Javaの式と条件文"
date: 2026-11-20
lang: ja
translation_id: expressoes-condicionais-java
permalink: /ja/expressions-and-conditional-statements-in-java/
share_text: >-
  式、ブロック、if、else、三項演算子、switch。
---

## 式と文

式を評価すると値が得られます。リテラル、変数、演算子、メソッド呼び出し、オブジェクト生成などを含められます。次の断片は単独では完全なプログラムになりません。

```text
x + 2 * 1
c.getBalance()
i = 20
```

文は実行の単位です。メソッド呼び出し、代入、インクリメントなどを文にできます。この例には別途宣言と`Account`クラスが必要です。

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

波括弧で文をブロックにまとめます。例では整数を読み取り、条件が成立した場合に二つのメッセージを表示します。

```java
void main() {
    int x = Integer.parseInt(
            IO.readln("Enter an integer: "));
    if (x < 10) {  
        IO.println("X is less than 10."); 
        IO.println("Initialize X with another value."); 
    }
}
```

## 条件文

`if`は真偽式が真の場合に文を実行します。

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else`は条件が偽の場合の動作を指定します。

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

波括弧を使うと、各分岐に複数の文を書けます。

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
    }
    else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

`if`を入れ子にして、成人かどうかを確認した後に優先アクセスの条件を調べます。

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
        if (age >= 65)
            IO.println("Priority access granted");
    } else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

三項演算子は条件に応じて二つの値のどちらかを選びます。

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age: "));
    // The ternary operator has this syntax: 
		// (expr) ? true : false
    String message = ((age >= 18) ? "At least" : "Under") + 
                 " 18 years old";
    IO.println(message);
}
```

## switchによる分岐

従来の`switch`文では、該当するケースに入り、`break`で抜けます。`default`はほかの値を扱います。

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message;
    switch (age) {
        case 0: case 1: case 2: case 3: case 4: case 5:
            message = "Very young";
            break;
        case 18:
            message = "Reaching adulthood";
            break;
        case 65:
            message = "Entering senior years";
            break;
        default:
            message = "No special case";
            break;
        }
        IO.println(message);
}
```

矢印を使う`switch`式は値を返します。同じケースの複数の値はコンマで区切れます。

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message = switch (age) {
        case 0, 1, 2, 3, 4, 5 -> "Very young";
        case 18 -> "Reaching adulthood";
        case 65 -> "Entering senior years";
        default -> "No special case";
    };
    IO.println(message);
}
```

パターンマッチングでは`when`ガードで型パターンに条件を追加できます。例では`Integer`、`String`、`null`、その他を区別します。

```java
private static String age(Object ageObject) {
    return switch (ageObject) {
        case Integer i when i >= 65 -> 
            "[Integer] Adult: " + i + 
            "\nPriority access granted.";
        case Integer i when i >= 18 -> 
            "[Integer] Adult: " + i + 
             "\nAccess granted.";
        case Integer i -> "[Integer] Minor: " + 
                i + "\nAccess denied.";
        case String s -> 
            "[String] Age provided as text: " + s;
        case null -> "[null] Age not provided";
        default -> "Unexpected data type: " + 
                ageObject.getClass().getName();
    };
}
```

メインプログラムは四つの値でこのメソッドを呼び出します。

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

出力は以下のとおりです。

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

最後の例には`switch`のパターンマッチングに対応したJavaが必要です。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
