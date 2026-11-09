---
layout: post
title: "Javaのポリモーフィズム"
date: 2026-10-21
lang: ja
translation_id: polimorfismo-em-java
permalink: /polymorphism-in-java-ja/
share_text: >-
  Javaの例を使って、アドホック、パラメトリック、サブタイプのポリモーフィズムを紹介します。
---

オブジェクト指向プログラミングにおける**ポリモーフィズム**とは、関係するオブジェクトのクラスに応じて、操作が異なる振る舞いをする能力です。主な形式は次のとおりです。

- **アドホックポリモーフィズム（オーバーロード）**：同じ名前のメソッドに異なるパラメーターを指定でき、引数に応じて適切なメソッドが選択されます。
- **パラメトリックポリモーフィズム**：ジェネリッククラスやメソッドが、使用時に指定される型を扱います。
- **サブタイプポリモーフィズム**：サブクラスがメソッドをオーバーライドでき、実行される実装はオブジェクトの具体的なクラスに応じて決まります。

次の例では、オーバーロードから始めて、Javaで3つの形式を示します。`Figure`クラスには`resize`という名前のオーバーロードされたメソッドが2つあります。1つ目は`Double`型の`percentage`を受け取り、2つ目は`Integer`型の座標`x`と`y`を受け取ります。

```java
public class Figure {
    public void resize(Double percentage) {
        // 割合に応じてサイズを変更
    }
    public void resize(Integer x, Integer y) {
        // 座標に応じてサイズを変更
    }
}
```

**パラメトリックポリモーフィズム**では、`<`と`>`を使ってパラメーター化された型を作成できます。たとえば`ArrayList`クラスには、リストが格納できるオブジェクトの型を指定する型パラメーター`E`があります。この型パラメーターは`add`メソッドの仮パラメーターにも使われます。したがって、`add`が期待する型は、`ArrayList`をインスタンス化するときに指定した型と同じです。`ArrayList`は`AbstractList`を拡張し、同じ`E`型を使って`List`、`RandomAccess`、`Cloneable`、`Serializable`などのインターフェースを実装しています。

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // addの実装
    }
    // その他のメソッドとフィールド
}
```

たとえば、型パラメーターに`String`を指定して文字列のリストを作成し、`add`を呼び出して要素を追加できます[^8]。

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

この場合、コンパイラーは`add`に渡す引数が`String`であることを期待します。他の型のオブジェクトを渡すとコンパイルエラーになります。整数のリストが必要なら、`ArrayList`に別の型、ここでは`Integer`を指定します。

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

**サブタイプポリモーフィズム**について、`Figure`クラスに`draw`メソッドがあり、`Triangle`、`Circle`、`Rectangle`クラスのオブジェクトにも呼び出せるとします。それぞれのクラスが独自の描画動作を実装するために、このメソッドをオーバーライドします。次のコードでは、`figure`に代入されたオブジェクトが`Circle`、`Triangle`、`Rectangle`のどれであるかに応じて、`draw`の各呼び出しが異なる実装を実行します。

```java
Figure figure = new Circle(10);
// Circleのdrawメソッドを呼び出す
figure.draw();
figure = new Triangle(20);
// Triangleのdrawメソッドを呼び出す
figure.draw();
figure = new Rectangle(10, 20);
// Rectangleのdrawメソッドを呼び出す
figure.draw();
```

[^8]: `ArrayList`を使うには通常、`import java.util.ArrayList;`でインポートします。コンパクトソースファイルではインポートは不要です。通常のソースファイルでは、`import module java.base;`で`java.base`モジュールをインポートできます。

---

*この記事は、<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Eduardo Kessler Piveta</a>著『<a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>』の内容をもとにしています。*

## 関連記事

- [オブジェクト指向プログラミングの基本概念](/oop-basics-java-ja/)
- [Javaのクラス](/classes-in-java-ja/)
- [Javaの継承](/inheritance-in-java-ja/)
- [Javaのインターフェース](/interfaces-in-java-ja/)
- [OOPとJavaのリンク集](/oop-java-links-ja/)
- [オブジェクト指向プログラミングの演習](/oop-exercises-ja/)
