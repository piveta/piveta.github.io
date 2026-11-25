---
layout: post
title: "WindowsにJavaとJDKをインストールする方法"
date: 2026-11-25
lang: ja
translation_id: como-instalar-java-jdk-windows
permalink: /ja/install-java-jdk-windows/
share_text: >-
  WindowsでJDKをダウンロード・インストールし、javaとjavacで確認する方法を紹介します。
---

## Javaディストリビューションを選ぶ
WindowsでJavaを開発するには、プロジェクトに合う**JDK**をダウンロードします。Oracle JDKやEclipse Temurinがあります。長期サポートが必要なプロジェクトではLTS版が候補になります。要件と利用条件を確認してください。

Windowsの設定でシステムの種類とプロセッサーのアーキテクチャを確認します。ダウンロードページではx64やAArch64など適切なパッケージとWindows用インストーラーを選びます。

## JDKをダウンロードしてインストール
Eclipse Temurinの場合：

1. [Adoptiumのダウンロードページ](https://adoptium.net/temurin/releases/)を開きます。
2. Javaのバージョン、Windows、アーキテクチャ、**JDK**パッケージを選びます。
3. MSIインストーラーをダウンロードして実行します。
4. Javaを<code>PATH</code>に追加するか確認します。他のツールが<code>JAVA_HOME</code>を必要とする場合は、その設定も選択します。
5. インストールを完了し、新しいターミナルを開きます。

Temurinでは<code>PATH</code>への追加が標準設定で、<code>JAVA_HOME</code>は追加設定です。

## インストールを確認
PowerShellまたはコマンドプロンプトで実行します。

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

最初の2つはJavaとコンパイラーのバージョンを表示し、後の2つは<code>PATH</code>上の実行ファイルを示します。コマンドが見つからない場合は新しいターミナルを開いて環境変数を確認します。別のバージョンなら<code>PATH</code>内の順序を確認します。

コンパイルを試すには、次を<code>Hello.java</code>として保存します。

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Java 25から使えるコンパクトソース形式と<code>IO.println</code>を使用しています。次を実行します。

~~~text
javac Hello.java
java Hello
~~~

出力は<code>Hello World!</code>です。Java 25より前では、インストール済みJDKが対応する形式を使います。

## 参考資料
- [Eclipse Temurin MSIインストーラー](https://adoptium.net/installation/windows/)
- [Oracle JDKのインストール](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
