---
layout: post
title: "Java의 반복문"
date: 2026-11-20
lang: ko
translation_id: sentencas-repeticao-java
permalink: /ko/loops-in-java/
share_text: >-
  for, 향상된 for, while, do-while의 예제입니다.
---

`for`의 머리에는 초기화, 조건, 갱신을 작성합니다. 이 예제는 1부터 5까지 출력합니다.

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

다음 예제는 `1/1 + 4/2 + 7/3 + … + 100/34`의 합을 구합니다. 분자는 3씩, 분모는 1씩 증가합니다.

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

합은 `93.76358001910911`입니다. `String.format`으로 기본 로캘에 맞춰 소수점 이하 두 자리까지 표시할 수 있습니다.

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

`Locale.US`는 소수 구분 기호로 마침표를 씁니다.

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

## 향상된 for

배열이나 `Iterable`의 각 요소에 대해 본문을 한 번씩 실행합니다.

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

다음 예제는 이름 리스트를 순회합니다.

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

## while과 do-while

`while`은 본문을 실행하기 전에 조건을 확인합니다.

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

`do-while`은 본문을 실행한 뒤 조건을 확인하므로 적어도 한 번은 실행됩니다.

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

세 반복문으로 계산한 합은 모두 같습니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
