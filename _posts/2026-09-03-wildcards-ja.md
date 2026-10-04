---
layout: post
title: "Javaのジェネリック型におけるワイルドカードと境界"
date: 2026-09-03
lang: ja
translation_id: wildcards-limites-java
permalink: /java-generics-wildcards-bounds-ja/
share_text: >-
  Javaのジェネリクスでは、<?>が不明な型を表し、<? extends T>と<? super T>が上限と下限を指定します。型パラメータに複数の境界を設ける方法も取り上げます。
---

特定のジェネリック型に加えて、**ワイルドカード**を使用して未知の型（`<?>`）を表したり、指定した型をある型のサブタイプに制限したり（`<? extends Type>`）、スーパータイプを含めたり（`<? super Type>`）できます。以下では、それぞれ非境界ワイルドカード、上限付きワイルドカード、下限付きワイルドカードについて説明します。続いて、ジェネリック型に複数の境界を定義する方法を示します。

## 非境界ワイルドカード

未知の型には疑問符を型として使用し、そのコンテキストで任意の型を使用できるようにします。たとえば、変数を `List<?>`（または属性やパラメータ）として宣言すると、`String`、`Integer` など、任意の有効な型パラメータを持つ `List` オブジェクトを代入できます。このような未知のジェネリック型は**非境界ワイルドカード**（`<?>`）と呼ばれます。型に対する境界を設けないためです。

たとえば、次のようにできます。

```java
List<?> l = new ArrayList<String>();
// または、たとえば
l = new LinkedList<Integer>();
```

このような変数宣言は魅力的に見えるかもしれませんが、制限があります。この場合、リスト内のオブジェクトの型が分かりません。そのため、たとえばリストに要素を追加することはできません（Javaでは任意の参照型と互換性がある `null` を除く）。追加するオブジェクトがリストの型パラメータと同じ型である保証がないためです。

したがって、リスト（この場合は `l`）に要素を追加しようとすると、コンパイル時エラーになります。

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

非境界型は、データを変更せずに読み取りたい場合によく使用されます。たとえば、リストの要素の型を指定せずに、リストを受け取って要素を表示するメソッドを定義できます。

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

`main` メソッドを実行すると、次のように表示されます。

```text
1
2
3
A
B
C
```

ここでは表示を例にしていますが、オブジェクトを反復処理したり、*streams* で使用したり、`instanceof` でフィルタリングしたり、リストのサイズを取得したり、特定のオブジェクトが含まれているか確認したり、型付きリストに変換してコピーしたりすることもできます。一方、`add` や `set` などを使ってリストを直接変更することはできません（`null` を除く）。

## 上限付きワイルドカード

**上限付きワイルドカード**を使用すると、指定した型、またはそのサブタイプ（継承またはインターフェースの実装によって得られるもの）のオブジェクトだけを型パラメータとして使用できることを指定できます。`<? extends T>` という記法は、ワイルドカードが型 `T` または `T` を継承する型でなければならないことを示します。

たとえば、ワイルドカードが `Number` を extends するリストを宣言すると、`Double` や `Integer` など、その任意のサブクラスのオブジェクトを代入できます。`Number` が具象クラスだった場合（実際には抽象クラスです）、クラス自身のオブジェクトも代入できます。次の例はこれを示しています。

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

非境界ワイルドカードの場合と同様に、リストの正確な型が分からないため、リスト `l` に要素を追加することはできません。そのため、最初の2つの `add` 呼び出しはコンパイルエラーになります。

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

コードを読めば、変数 `l` に代入されているオブジェクトが整数のリストであることは分かります。しかしコンパイラは、`l` の型が未知であることしか分からないため、値の追加を許可しません。読み出す場合、値は上限である `Number` として扱われます。

## 下限付きワイルドカード

**下限付きワイルドカード**を使用すると、指定した型、またはそのスーパータイプのオブジェクトだけを型パラメータとして使用できることを指定できます。`<? super T>` という記法は、ワイルドカードが型 `T` または `T` のスーパークラスでなければならないことを示します。

たとえば、ワイルドカードの下限が `Number` であるリストを宣言すると、そのスーパー クラス（`Number` の場合は明示的なスーパークラスを持たないため `Object` のみ）のオブジェクトを代入できます。

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

下限の型（この場合は `Number`）またはそのサブタイプ（たとえば `Double` や `Integer`）の要素を追加できます。次の例は、`Number` を下限とするワイルドカードを持つリストです。この場合、数値の `ArrayList`（またはそのスーパー クラスである `Object`）をインスタンス化できます。そのサブクラスの要素を追加できます（`Number` は抽象クラスで直接のインスタンスを持てないため、型 `Number` のオブジェクトを直接作成して追加することはできません）。例には3つの要素追加があります。最初の2つは `Number` のサブタイプなので許可されます（`10` は `Integer`、`1.0` は `Double`）。3つ目は許可されず、`Object` は `Number` の子孫ではないためコンパイル時エラーになります。

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

`Object` を型パラメータとして `ArrayList` を生成した場合でも、3つ目の追加はコンパイル時に許可されず、同じエラーになります（最初の2つは引き続き許可されます）。リストの型は依然として未知であり、`Number` またはそのスーパータイプのいずれかであることしか分からないためです。

## 複数の境界

Javaでは、ジェネリック型に**複数の境界**を指定できます。これは、型パラメータを特定のクラスを継承する（またはそのクラス自体である）型、および1つ以上のインターフェースを実装する型に制限できることを意味します。構文は `<T extends Class & Interface1 & Interface2>` の形式です。クラスを境界として使用する場合は、最初にクラスを指定し、その後にインターフェースを指定します。クラスがない場合は、インターフェースだけを列挙できます。

たとえば、`MultipleBounds` クラスのジェネリック型 `T` は、`Number` クラスを継承し、`Comparable<T>` と `Serializable` インターフェースを実装します。

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

この例では、`T` は `Number` または `Number` を継承し、さらに `Comparable<T>` と `Serializable` を実装する型に限られます。これは、スーパークラスのメソッドへのアクセスや、複数のインターフェースによって定義された契約など、複数の保証が必要な場合に有用です。この組み合わせにより、強い型付けを維持しながらコードを柔軟にし、コンパイル時エラーを避け、使用するジェネリック型に必要なすべてのメソッドが利用できることを保証できます。

---

*この記事は、<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>（<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a> 著）の内容をもとにしています。*
