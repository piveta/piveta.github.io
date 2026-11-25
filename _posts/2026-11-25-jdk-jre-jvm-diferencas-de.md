---
layout: post
title: "JDK, JRE und JVM: Was ist der Unterschied bei Java?"
date: 2026-11-25
lang: de
translation_id: jdk-jre-jvm-diferencas
permalink: /de/jdk-jre-jvm-unterschiede/
share_text: >-
  Erfahren Sie, welche Aufgaben JVM, JRE und JDK haben und mit welchen Befehlen Sie Ihre Java-Umgebung prüfen.
---

## JVM, JRE und JDK
Die **JVM** (Java Virtual Machine) führt Java-Bytecode aus. Sie lädt Klassen, prüft und verarbeitet Anweisungen und verwaltet Ressourcen wie den Arbeitsspeicher. Derselbe Bytecode kann auf verschiedenen Systemen laufen, sofern eine kompatible JVM vorhanden ist.

Die **JRE** (Java Runtime Environment) bezeichnet die Umgebung zum Ausführen von Java-Anwendungen, einschließlich JVM und Bibliotheken. Ob eigenständige JRE-Pakete verfügbar sind, hängt von Distribution und Version ab. Manche Anwendungen bringen ihre eigene Laufzeitumgebung mit.

Das **JDK** (Java Development Kit) umfasst die Laufzeitumgebung und Entwicklungswerkzeuge: den Compiler <code>javac</code>, den Starter <code>java</code> und weitere Werkzeuge zum Erstellen, Ausführen und Diagnostizieren von Anwendungen.

## Was sollte man zum Programmieren installieren?
Für die Java-Entwicklung installieren Sie ein zum Projekt passendes JDK. Die Distribution stellt JVM und benötigte Werkzeuge bereit. Oracle JDK und Eclipse Temurin sind Beispiele für Distributionen.

Prüfen Sie im Terminal:

~~~text
java --version
javac --version
~~~

Der erste Befehl zeigt die Version des Java-Starters, der zweite die Compiler-Version. Funktioniert <code>java</code>, aber <code>javac</code> wird nicht gefunden, prüfen Sie die JDK-Installation und ob dessen Verzeichnis <code>bin</code> im <code>PATH</code> liegt.

Unter Windows zeigen <code>where java</code> und <code>where javac</code>, welche ausführbare Datei verwendet wird. Unter macOS und Linux verwenden Sie <code>which java</code> und <code>which javac</code>.

## Vom Quellcode zur Ausführung
In der Datei <code>Hello.java</code> übersetzt der Compiler den Quellcode in Bytecode:

~~~text
javac Hello.java
java Hello
~~~

Der erste Befehl erzeugt <code>Hello.class</code>. Der zweite startet die JVM und führt die Klasse aus. Die Kompatibilität hängt sowohl von der Compiler-Version als auch von der Laufzeitversion ab.

## Quellen
- [Überblick über die Java-Plattform und JVM](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [Installationshandbuch für das JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
