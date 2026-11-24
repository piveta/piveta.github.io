---
layout: post
title: "Javaのジェネリッククラスとメソッド"
date: 2026-11-24
lang: ja
translation_id: classes-metodos-genericos-java
permalink: /ja/generic-classes-and-methods-in-java/
share_text: >-
  ジェネリクスによって型安全性を保ちながらクラスとメソッドを再利用できます。Adapter<T>を例に説明します。
---

**パラメトリック多相**では、クラス、インターフェース、レコード、メソッドが使用時に指定された型に対応します。Javaのジェネリクスはコードの再利用を助け、不要なキャストを減らします。`List<String>`と`List<Integer>`は同じインターフェースを使いますが、コンパイラはそれぞれの要素型を検査します。

型パラメータのない`Adapter`は、フィールド、コンストラクタ、メソッドで`Object`を使用します。

```java
public class Adapter{
    Object object;
    public Object get(){
        return object;
    }
    public void set(Object value){
        object = value;
    }
    public Adapter(Object initial){
       object = initial;
    }
}
```

任意のオブジェクトを保持できますが、個々のアダプターを特定の型に制限できません。`T`を宣言すると、同じ実装が呼び出し側の選んだ型を扱います。

```java
public class Adapter<T>{
    T object;
    public T get(){
        return object;
    }
    public void set(T value){
        object = value;
    }
    public Adapter(T initial){
        object = initial;
    }
}
```

次のクライアントは`Adapter<String>`を作ります。コンストラクタと`set`は文字列を受け取り、`get`は文字列を返します。出力は`Test`、続いて`New Value`です。

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## ジェネリックメソッド

メソッドも戻り値の型の前に型パラメータを宣言できます。`print`は、コンパイラによる型検査を維持しながら、異なる要素型のリストを受け取ります。

```java
public static <T> void print(List<T> list){
    for (T element : list)
        IO.println(element);
}
void main(){
    List<Integer> integers = List.of(1, 2, 3, 4);
    List<String> names = List.of("Mary", "John", "Carol");
    print(integers);
    print(names);
}
```

型パラメータは戻り値の型も決められます。`first`は`List<T>`を受け取り`T`を返すため、整数のリストなら`Integer`、名前のリストなら`String`になります。

```java
public static <T> T first(List<T> list) {
    return list.isEmpty() ? null : list.get(0);
}
void main(){
    List<Integer> integers = List.of(1, 2, 3, 4);
    List<String> names = List.of("Mary", "John", "Carol");
    Integer integer = first(integers);
    String name = first(names);
    IO.println(integer);
    IO.println(name);
}
```

中間変数は型を明確にします。必要なければ式を直接使えます。

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## 境界のある型パラメータ

`multiply`は`Number`またはそのサブタイプのリストを受け取ります。`<T extends Number>`により、各要素で`doubleValue()`を呼べます。

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

`Integer`のリストも`Double`のリストも渡せます。

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

コンパイラは呼び出しごとに型パラメータを検査しますが、メソッドの実装は一つです。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
