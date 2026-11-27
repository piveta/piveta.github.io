---
layout: post
title: "Java 循环"
date: 2026-11-20
lang: zh
translation_id: sentencas-repeticao-java
permalink: /zh/loops-in-java/
share_text: >-
  通过计数和求和示例理解 for、增强 for、while 和 do-while。
---

`for` 的头部包含初始化、条件和更新。此例输出 1 到 5。

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

另一例计算 `1/1 + 4/2 + 7/3 + … + 100/34` 的和，分子每次增加 3，分母每次增加 1。

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

结果为 `93.76358001910911`。`String.format` 可按照默认区域设置保留两位小数。

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

`Locale.US` 使用句点作为小数分隔符。

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

## 增强 for

对数组或 `Iterable` 的每个元素执行一次循环体。

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

接下来遍历姓名列表。

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

## while 和 do-while

`while` 在每次执行循环体前检查条件。

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

`do-while` 在循环体执行后检查条件，因此至少执行一次。

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

三个求和循环得到相同的结果。

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
