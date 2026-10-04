---
layout: post
title: "Java 제네릭 타입의 와일드카드와 경계"
date: 2026-09-03
lang: ko
translation_id: wildcards-limites-java
permalink: /java-generics-wildcards-bounds-ko/
share_text: >-
  Java 제네릭에서 <?>는 알 수 없는 타입을 나타내고, <? extends T>와 <? super T>는 상한과 하한을 지정합니다. 와일드카드는 제네릭 타입이 허용하는 범위를 유연하게 표현합니다.
---

구체적인 제네릭 타입 외에도 **와일드카드**를 사용하여 알 수 없는 타입(`<?>`)을 표현하거나, 지정된 타입을 특정 타입의 하위 타입으로 제한하거나(`<? extends Type>`), 상위 타입을 포함하도록 할 수 있습니다(`<? super Type>` 사용). 다음 절에서는 순서대로 비한정 와일드카드, 상한 와일드카드, 하한 와일드카드를 설명합니다. 이어서 제네릭 타입에 여러 경계를 정의하는 방법을 살펴봅니다.

## 비한정 와일드카드

알 수 없는 타입에는 물음표를 타입으로 사용하여 해당 문맥에서 어떤 타입이든 사용할 수 있도록 합니다. 예를 들어 변수를 `List<?>`(또는 필드나 매개변수)로 선언하면 `String`, `Integer` 등 유효한 모든 타입 매개변수를 가진 `List` 객체를 할당할 수 있습니다. 이러한 알 수 없는 제네릭 타입을 **비한정 와일드카드**(`<?>`)라고 하는데, 타입에 대한 경계를 지정하지 않기 때문입니다.

예를 들어 다음과 같이 작성할 수 있습니다.

```java
List<?> l = new ArrayList<String>();
// 또는 예를 들어
l = new LinkedList<Integer>();
```

이러한 방식의 변수 선언은 매력적으로 보일 수 있지만 제한이 있습니다. 이 경우 리스트에 있는 객체의 타입을 알 수 없습니다. 따라서 리스트에 요소를 추가할 수 없습니다(`null`은 Java의 모든 참조 타입과 호환되므로 예외입니다). 추가하려는 객체가 리스트의 타입 매개변수와 같은 타입이라는 보장이 없기 때문입니다.

따라서 리스트 객체(이 경우 `l`)에 요소를 추가하려고 하면 컴파일 시 오류가 발생합니다.

```java
void main(){
    List<?> l = new ArrayList<String>();
    // Compilation error: 
    //    "The method add(capture#2-of ?) in the type 
    //     List<capture#2-of ?> is not applicable 
    //     for the arguments (String)"
    l.add("Maria");
}
```

비한정 타입은 데이터를 수정하지 않고 읽기만 하려는 경우에 흔히 사용됩니다. 예를 들어 리스트의 요소 타입을 지정하지 않고 리스트를 받아 요소를 출력하는 메서드를 만들 수 있습니다.

```java
public void print(List<?> list) {
    for (Object obj : list)
        IO.println(obj);
}
void main(){
    print(List.of(1, 2, 3));
    print(List.of("A", "B", "C"));
}
```

`main` 메서드를 실행하면 다음과 같이 출력됩니다.

```text
1
2
3
A
B
C
```

여기서는 출력을 예로 들었지만, 객체를 순회하거나 *streams*에서 사용하거나 `instanceof`로 필터링하거나 리스트의 크기를 얻거나 특정 객체가 포함되어 있는지 확인하거나 타입이 지정된 리스트로 변환하여 복사하는 등의 작업도 할 수 있습니다. 반면 `add`나 `set` 등을 사용하여 리스트를 직접 수정할 수는 없습니다(`null`은 예외입니다).

## 상한 와일드카드

**상한 와일드카드**를 사용하면 특정 타입 또는 그 하위 타입(상속이나 인터페이스 구현을 통해 얻어진 타입)의 객체만 타입 매개변수로 사용할 수 있도록 지정할 수 있습니다. `<? extends T>` 표기법은 와일드카드가 타입 `T` 또는 `T`를 상속하는 타입이어야 함을 나타냅니다.

예를 들어 와일드카드가 `Number`를 상한으로 하는 리스트를 선언하면 `Double`이나 `Integer`와 같은 하위 클래스의 객체를 할당할 수 있습니다. `Number`가 구체 클래스였다면(실제로는 추상 클래스입니다) 해당 클래스 자체의 객체도 할당할 수 있습니다. 다음 예가 이를 보여줍니다.

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

비한정 와일드카드와 마찬가지로 리스트의 정확한 타입을 알 수 없기 때문에 `l`에 요소를 추가할 수 없습니다. 따라서 처음 두 `add` 호출은 컴파일 오류를 발생시킵니다.

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

코드를 읽으면 변수 `l`에 할당된 객체가 정수 리스트라는 것을 알 수 있지만, 컴파일러는 `l`의 타입이 알려지지 않았다는 것만 알기 때문에 값을 추가하도록 허용하지 않습니다. 값을 읽을 때는 상한인 `Number`로 읽습니다.

## 하한 와일드카드

**하한 와일드카드**를 사용하면 특정 타입 또는 그 상위 타입의 객체만 타입 매개변수로 사용할 수 있도록 지정할 수 있습니다. `<? super T>` 표기법은 와일드카드가 타입 `T` 또는 `T`의 슈퍼클래스여야 함을 나타냅니다.

예를 들어 와일드카드의 하한이 `Number`인 리스트를 선언하면 그 슈퍼클래스 중 하나의 객체를 할당할 수 있습니다(`Number`의 경우 명시적인 슈퍼클래스가 없으므로 `Object`만 해당).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

하한 타입(이 경우 `Number`) 또는 그 하위 타입(예: `Double`, `Integer`)의 요소를 추가할 수 있습니다. 다음은 `Number`를 하한으로 갖는 와일드카드 리스트의 예입니다. 이 경우 숫자의 `ArrayList`(또는 그 상위 클래스인 `Object`)를 인스턴스화할 수 있습니다. 그 하위 클래스의 요소를 추가할 수 있습니다(`Number`는 추상 클래스이므로 직접 인스턴스를 만들 수 없기 때문에 `Number` 타입의 객체를 직접 추가할 수는 없습니다). 예제에는 세 번의 요소 추가가 있습니다. 처음 두 개는 `Number`의 하위 타입이므로 허용됩니다(`10`은 `Integer`, `1.0`은 `Double`). 세 번째 추가는 `Object`가 `Number`의 자손이 아니므로 허용되지 않으며 컴파일 시 오류가 발생합니다.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

`Object`를 타입 매개변수로 사용하여 `ArrayList`를 생성하더라도 세 번째 추가는 컴파일 시 허용되지 않고 동일한 오류가 발생합니다(처음 두 추가는 계속 허용됩니다). 리스트의 타입은 여전히 알 수 없으며 `Number` 또는 그 상위 타입 중 하나라는 것만 알 수 있기 때문입니다.

## 여러 경계

Java에서는 제네릭 타입에 **여러 경계**를 지정할 수 있습니다. 즉, 타입 매개변수를 특정 클래스를 상속하거나(또는 그 클래스 자체이면서) 하나 이상의 인터페이스를 구현하는 타입으로 제한할 수 있습니다. 문법은 `<T extends Class & Interface1 & Interface2>` 형식을 따릅니다. 클래스를 경계로 사용하는 경우에는 클래스를 먼저 지정하고 그 뒤에 인터페이스를 지정해야 합니다. 클래스가 없다면 인터페이스만 나열할 수 있습니다.

예를 들어 `MultipleBounds` 클래스의 제네릭 타입 `T`는 `Number` 클래스를 상속하고 `Comparable<T>` 및 `Serializable` 인터페이스를 구현합니다.

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

이 예에서 `T`는 `Number`이거나 `Number`를 상속하면서 `Comparable<T>`와 `Serializable`도 구현하는 타입만 될 수 있습니다. 이는 상위 클래스의 메서드에 대한 접근이나 여러 인터페이스가 정의하는 계약과 같이 여러 보장이 필요할 때 유용합니다. 이러한 조합은 강한 타입 검사를 유지하면서 코드를 더 유연하게 만들고 컴파일 시 오류를 방지하며, 사용되는 제네릭 타입에 필요한 모든 메서드를 사용할 수 있도록 합니다.

---

*이 글은 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> 책의 내용을 바탕으로 작성되었으며, 저자는 <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>입니다.*
