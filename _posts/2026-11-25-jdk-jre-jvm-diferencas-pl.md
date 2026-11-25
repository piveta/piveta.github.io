---
layout: post
title: "JDK, JRE i JVM: czym się różnią w Javie?"
date: 2026-11-25
lang: pl
translation_id: jdk-jre-jvm-diferencas
permalink: /pl/roznice-jdk-jre-jvm/
share_text: >-
  Poznaj role JVM, JRE i JDK oraz polecenia sprawdzające środowisko Java.
---

## JVM, JRE i JDK
**JVM** (Java Virtual Machine) wykonuje bajtkod Javy. Ładuje klasy, weryfikuje i wykonuje instrukcje oraz zarządza zasobami, takimi jak pamięć. Ten sam bajtkod może działać na różnych systemach, jeśli dostępna jest zgodna JVM.

**JRE** (Java Runtime Environment) oznacza środowisko potrzebne do uruchamiania aplikacji Java, w tym JVM i biblioteki. Dostępność samodzielnych pakietów JRE zależy od dystrybucji i wersji. Niektóre aplikacje dołączają własne środowisko uruchomieniowe.

**JDK** (Java Development Kit) obejmuje środowisko uruchomieniowe i narzędzia programistyczne: kompilator <code>javac</code>, launcher <code>java</code> oraz narzędzia do tworzenia, uruchamiania i diagnozowania aplikacji.

## Co zainstalować do programowania?
Do programowania w Javie zainstaluj JDK odpowiednie dla projektu. Wybrana dystrybucja zapewnia JVM i potrzebne narzędzia. Oracle JDK i Eclipse Temurin to przykłady dystrybucji.

W terminalu sprawdź polecenia:

~~~text
java --version
javac --version
~~~

Pierwsze pokazuje wersję launchera Java, a drugie kompilatora. Jeśli <code>java</code> działa, ale <code>javac</code> nie zostaje znalezione, sprawdź instalację JDK i obecność katalogu <code>bin</code> w <code>PATH</code>.

W Windows polecenia <code>where java</code> i <code>where javac</code> wskazują używany plik wykonywalny. W macOS i Linuksie użyj <code>which java</code> i <code>which javac</code>.

## Od kodu źródłowego do uruchomienia
W pliku <code>Hello.java</code> kompilator zamienia kod źródłowy na bajtkod:

~~~text
javac Hello.java
java Hello
~~~

Pierwsze polecenie tworzy <code>Hello.class</code>. Drugie uruchamia JVM, aby wykonać klasę. Zgodność zależy od wersji kompilatora i wersji użytej do uruchomienia.

## Źródła
- [Przegląd platformy Java i JVM](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [Przewodnik instalacji JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
