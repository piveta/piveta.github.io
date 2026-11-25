---
layout: post
title: "JDK・JRE・JVMの違い：Javaでは何が違うのか"
date: 2026-11-25
lang: ja
translation_id: jdk-jre-jvm-diferencas
permalink: /ja/jdk-jre-jvm-differences/
share_text: >-
  JVM、JRE、JDKの役割と、Java環境を確認するコマンドを解説します。
---

## JVM、JRE、JDK
**JVM**（Java Virtual Machine）はJavaのバイトコードを実行します。クラスを読み込み、命令を検証・実行し、メモリーなどの資源を管理します。互換性のあるJVMがあれば、同じバイトコードを異なるシステムで実行できます。

**JRE**（Java Runtime Environment）は、JVMやライブラリーを含むJavaアプリケーションの実行環境を指します。単独のJREパッケージが提供されるかは、ディストリビューションとバージョンによって異なります。アプリケーションに実行環境が同梱される場合もあります。

**JDK**（Java Development Kit）は、実行環境と開発ツールをまとめたものです。コンパイラーの <code>javac</code>、起動コマンドの <code>java</code>、アプリケーションの作成・実行・診断に使うツールが含まれます。

## プログラミングには何をインストールする？
Javaの開発には、プロジェクトに適したJDKをインストールします。選んだディストリビューションがJVMと必要なツールを提供します。Oracle JDKとEclipse Temurinはその例です。

ターミナルで次のコマンドを確認します。

~~~text
java --version
javac --version
~~~

1つ目はJava起動コマンドのバージョン、2つ目はコンパイラーのバージョンを表示します。<code>java</code>は動作するのに<code>javac</code>が見つからない場合は、JDKのインストールと、<code>bin</code>ディレクトリーが<code>PATH</code>にあるかを確認してください。

Windowsでは<code>where java</code>と<code>where javac</code>、macOSとLinuxでは<code>which java</code>と<code>which javac</code>で使用中の実行ファイルを調べられます。

## ソースコードから実行まで
<code>Hello.java</code>をコンパイルして実行します。

~~~text
javac Hello.java
java Hello
~~~

1つ目は<code>Hello.class</code>を生成し、2つ目はJVMを起動してクラスを実行します。互換性はコンパイル時と実行時の両方のバージョンに左右されます。

## 参考資料
- [JavaプラットフォームとJVMの概要](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [JDKインストールガイド](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
