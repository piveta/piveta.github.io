---
layout: post
title: "Javaジェネリクスの演習"
date: 2026-11-20
lang: ja
translation_id: exercicios-tipos-genericos-java
permalink: /ja/java-generics-exercises/
share_text: >-
  ジェネリックメソッド、ワイルドカード、継承、Optional<T>、Box<T>に関する10問。
---

以下は**Orientação a Objetos com Java**のジェネリクス章に基づく演習です。コードの構造は本に従い、識別子、コメント、メッセージは英語にしています。

1. Javaコレクションフレームワークの主なインターフェースを調べ、ジェネリクスがクラスを変更せずにデータ構造の再利用を可能にする仕組みを説明してください。
2. 二つの`Comparable`オブジェクトを受け取り大きい方を返す静的ジェネリックメソッド`max`を作成してください。
3. 任意の型のリストを受け取り表示する静的メソッドを、ワイルドカードを使って作成してください。
4. 数値リストを合計する静的メソッドを作成し、`extends`で`Number`のリストに限定してください。
5. 次のクラス階層を考えてください。

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   次のメソッドは楽器またはそのサブクラスのリストを受け取ります。

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   `Guitar`と`Flute`のリストを渡してください。次にメソッド内で楽器の追加を試み、コンパイルエラーを確認してください。
6. `Number`かつ`Comparable`である要素のリストを受け取り、最大値を返すジェネリックメソッドを実装してください。
7. 次の三つのメソッドを実装し、`Car`、`Motorcycle`、`Vehicle`のリストで試してください。

   ```java
   void printInvariant(List<Vehicle> list){
       // Implement
   }
   void printCovariant(List<? extends Vehicle> list){
       // Implement
   }
   void printContravariant(List<? super Vehicle> list){
       // Implement
   }
   ```

8. `List<String>`だけを判定する`boolean checkList(Object obj)`を試作してください。Javaで直接できるか調べ、`List<?>`または`List<Object>`を使う代案を示してください。
9. `Optional<T>`を調べ、値または*empty*を表示する`printOptional(Optional<T> opt)`を作ってください。`Optional<String>`と`Optional<Integer>`で試してください。
10. 一つの要素を保持する`Box<T>`を作成してください。`store(T item)`は`null`を拒否し、`get()`は値を返し、`compare(Box<T> b1, Box<T> b2)`は`compareTo`で比較します。継承関係のある異なる型の箱を比較する`compareWithInheritance`も`<? extends T>`または`<? super T>`で作り、次を試してください。

    ```java
     Box<Integer> box1 = new Box<>();
     Box<Integer> box2 = new Box<>();
     box1.store(10);
     box2.store(5);
     boolean result = Box.compare(box1, box2); // true

     Box<Double> box3 = new Box<>();
     Box<Integer> box4 = new Box<>();
     box3.store(7.5);
     box4.store(5);
     boolean result2 = Box.compareWithInheritance(box3,
        box4); // true
    ```

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
