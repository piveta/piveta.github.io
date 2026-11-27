---
layout: post
title: "Javaのループ"
date: 2026-11-20
lang: ja
translation_id: sentencas-repeticao-java
permalink: /ja/loops-in-java/
share_text: >-
  for、拡張for、while、do-whileの例。
---

`for`のヘッダーには初期化、条件、更新を書きます。この例は1から5までを表示します。

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

次の例では`1/1 + 4/2 + 7/3 + … + 100/34`を合計します。分子を3ずつ、分母を1ずつ増やします。

```java
void main(){
    double sum = 0.0;
    for (int numerator = 1, denominator = 1; 
         numerator <= 100;
         numerator += 3, denominator++)
        sum += (double) numerator / denominator;
    IO.println("Sum: " + sum);
}
```

合計は`93.76358001910911`です。`String.format`は既定のロケールで小数点以下2桁に整形できます。

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

`Locale.US`を指定すると小数点にピリオドを使います。

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

## 拡張for

配列または`Iterable`の各要素について本体を1回実行します。

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

次の例は名前のリストを走査します。

```java
void main() {
    // Creates a list of people's names
    var people = new ArrayList<String>();
    people.add("Mary");
    people.add("Peter");
    people.add("Paul");
    // Iterates over the collection, displaying names
    for (var p : people)
        IO.println("Person's name: " + p);
}
```

## whileとdo-while

`while`は本体を実行する前に条件を確認します。

```java
void main() {
    int numerator = 1, denominator = 1;
    var sum = 0.0;
    while (numerator <= 100) {
        sum += (double) numerator / denominator;
        numerator += 3;
        denominator++;
    }
    IO.println("Sum: " + sum);
}
```

`do-while`は本体の実行後に条件を確認するため、本体が少なくとも1回は実行されます。

```java
void main() {
    int numerator = 1, denominator = 1;
    var sum = 0.0;
    do {
        sum += (double) numerator / denominator;
        numerator += 3;
        denominator++;
    } while (numerator <= 100);
    IO.println("Sum: " + sum);
}
```

三つのループで計算した合計は同じ値になります。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
