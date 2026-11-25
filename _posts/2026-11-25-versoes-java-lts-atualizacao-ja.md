---
layout: post
title: "Javaのバージョン：LTS、更新、バージョン確認"
date: 2026-11-25
lang: ja
translation_id: versoes-java-lts-atualizacao
permalink: /ja/java-versions-lts-updates/
share_text: >-
  Javaのリリースサイクル、LTSの意味、JDKの確認と更新方法を説明します。
---

## Javaのバージョンを確認
ターミナルで次のコマンドを実行します。

~~~text
java --version
javac --version
~~~

1つ目はアプリケーションを起動するJavaランチャー、2つ目はコンパイラーのバージョンを示します。複数のJDKをインストールしている場合、<code>PATH</code>で見つかる実行ファイルとIDEで設定したものが異なる場合があります。

## JavaのリリースとLTS
Javaは6か月ごとに機能リリースを行います。**LTS**（長期サポート）版は、一部のベンダーから長期サポートを受けます。サポート期間、価格、条件はディストリビューションとベンダーによって異なります。

Oracleのサポートロードマップでは、Java 8、11、17、21、25がLTSです。Oracleは2年ごとに新しいLTS版を予定しています。本番用のバージョンを決める前に、最新のロードマップとベンダーの方針を確認してください。

選択はライブラリー、ツール、アプリケーション要件にも左右されます。LTSは長いサポート期間を得やすく、中間リリースは新機能を早く利用できます。

## リリースとJEPを調べる
Oracleの[JDKリリースノート一覧](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html)には、各リリースと更新へのリンクがあります。ノートには変更、修正、追加・削除された機能が記載されます。[JDK 27のリリースノート](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html)では新機能と関連JEPを確認できます。

**JEP**（JDK Enhancement Proposal）はJDKの改善案、目的、設計、状態を記録します。機能によっては最初に*preview*や*incubator*として提供され、正式機能になる前に変更されることがあります。

[バージョンごとのJava言語変更](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html)と[言語変更の概要](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html)で、正式機能とプレビュー機能を比較できます。

## Javaを更新する
1. <code>java --version</code>と<code>javac --version</code>で現在のバージョンを確認します。
2. プロジェクト、依存ライブラリー、本番環境の対応状況を調べます。
3. 使用中のディストリビューションから更新を取得するか、互換性のあるものを選びます。
4. JDKをインストールし、必要なら<code>PATH</code>、<code>JAVA_HOME</code>、IDEを設定します。
5. 新しいターミナルでバージョンを確認し、アプリケーションのテストを実行します。

同じ系列の更新とメジャーバージョン移行は別の判断です。移行前にリリースノートを読み、アプリケーションと依存関係をテストします。

Windowsでは<code>where.exe java</code>と<code>where.exe javac</code>、macOSとLinuxでは<code>which java</code>と<code>which javac</code>で実行ファイルを確認できます。

## 参考資料
- [Oracle Java SEサポートロードマップ](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [Oracle JDKライセンスFAQ](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
