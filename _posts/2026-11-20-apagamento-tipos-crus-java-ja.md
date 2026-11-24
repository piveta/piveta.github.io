---
layout: post
title: "Javaの型消去とraw型"
date: 2026-11-20
lang: ja
translation_id: apagamento-tipos-crus-java
permalink: /ja/type-erasure-and-raw-types-in-java/
share_text: >-
  型消去は旧コードとの互換性を支え、raw型では要素の型検査が失われます。
---

Java 5は旧コードとの互換性を保ちながらジェネリクスを導入しました。**型消去**（*type erasure*）では、コンパイラが型パラメータを検査してから、JVMが実行する表現からそれを取り除きます。代わりに境界型、通常は`Object`または最初に宣言された境界型を使います。

消去後の`Adapter<T>`は、おおむね`Object`を使う次のクラスに似ています。

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

型パラメータを書かないクライアントは次のようになります。

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

これらは処理を**説明するための近似例**であり、バイトコードの正確な転記ではありません。ジェネリック型の引数は実行時にはコンパイル時と同じ形で利用できず、一部のリフレクション操作に制約があります。

## raw型

型引数を指定したリストでは要素型が検査されます。

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

*raw型*では宣言と生成の双方から型引数を省きます。

```java
void main(){
    List names = new ArrayList();
}
```

これにより`List<String>`の検査が失われ、文字列と整数の両方を追加できてしまいます。

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>`は要素型が**不明なリスト**で、`null`以外の任意の要素を追加できません。一方、rawな`List`はその検査なしで要素を受け取ります。新しいコードでは型引数かワイルドカードを使い、raw型は主に旧ライブラリとの連携に限ります。

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
