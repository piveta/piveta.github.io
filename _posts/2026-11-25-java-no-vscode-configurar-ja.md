---
layout: post
title: "VS CodeでJavaを使う：JDKのインストールと設定"
date: 2026-11-25
lang: ja
translation_id: java-no-vscode-configurar
permalink: /ja/java-vscode-setup/
share_text: >-
  Visual Studio CodeでJavaを設定し、JDKを選択して最初のプログラムを実行します。
---

## JDKとVisual Studio Codeをインストール
**VS CodeでJava**を開発するには、プロジェクトに合うJDKとVisual Studio Codeをインストールします。ターミナルでJDKを確認します。

~~~text
java --version
javac --version
~~~

コマンドが見つからない場合はJDKのインストールと<code>PATH</code>を確認してください。環境変数を変更した後は新しいターミナルを開きます。

## Java拡張機能をインストール
VS Codeの**Extensions**を開き、**Extension Pack for Java**を検索してMicrosoftのパッケージをインストールします。言語サポート、実行、デバッグなどのJavaツールがまとめられています。

WindowsとmacOSでは、VS Code、JDK、主要な拡張機能をまとめたCoding Pack for Javaも利用できます。

## プロジェクトのJDKを設定
WindowsとLinuxでは<code>Ctrl+Shift+P</code>、macOSでは<code>Cmd+Shift+P</code>でコマンドパレットを開きます。**Java: Configure Java Runtime**を実行し、プロジェクトに割り当てられたJDKを確認します。

プロジェクトのJDKとターミナルのJDKは異なることがあります。複数のバージョンがある場合は両方確認してください。

## プログラムを実行
VS Codeでフォルダーを開き、<code>Hello.java</code>を作成します。

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Java 25以降で利用できるコンパクトソース形式と<code>IO.println</code>を使います。<code>main</code>の横にある**Run**を選び、ターミナルの出力を確認します。デバッグでは**Debug**を選択してブレークポイントを設定します。

ファイルが認識されない場合は、フォルダーが開いていること、拡張機能の起動が完了したこと、**Java: Configure Java Runtime**のJDK設定を確認します。

## 参考資料
- [VS CodeでJavaを始める](https://code.visualstudio.com/docs/java/java-tutorial)
- [VS CodeでのJavaプロジェクト管理](https://code.visualstudio.com/docs/java/java-project)
