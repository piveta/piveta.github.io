---
layout: post
title: "Java-Versionen: LTS, Updates und Versionsprüfung"
date: 2026-11-25
lang: de
translation_id: versoes-java-lts-atualizacao
permalink: /de/java-versionen-lts-updates/
share_text: >-
  Erfahren Sie mehr über Java-Releases, die Bedeutung von LTS und das Prüfen und Aktualisieren eines JDK.
---

## Java-Version prüfen
Führen Sie diese Befehle im Terminal aus:

~~~text
java --version
javac --version
~~~

Der erste zeigt den Java-Starter für Anwendungen, der zweite den Compiler. Sind mehrere JDKs installiert, kann das über <code>PATH</code> gefundene Programm von der IDE-Konfiguration abweichen.

## Java-Versionen und LTS
Java veröffentlicht Funktionsversionen im Abstand von sechs Monaten. Eine **LTS**-Version (*long-term support*) erhält von bestimmten Anbietern langfristigen Support. Dauer, Kosten und Bedingungen hängen von Distribution und Anbieter ab.

In Oracles Support-Roadmap sind Java 8, 11, 17, 21 und 25 LTS-Versionen. Oracle plant alle zwei Jahre eine neue LTS-Version. Prüfen Sie vor einer Produktionsentscheidung die aktuelle Roadmap und die Richtlinien des Anbieters.

Die Wahl hängt auch von Bibliotheken, Werkzeugen und Anforderungen der Anwendung ab. Eine LTS-Version bietet einen längeren Supportzeitraum; Zwischenversionen bringen neue Funktionen früher.

## Java-Versionen und JEPs finden
Oracle führt einen [Index der JDK-Release-Notes](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html) mit Links zu Releases und Updates. Die Notes beschreiben Änderungen, Fehlerkorrekturen sowie neue oder entfernte Funktionen. Die [Release-Notes für JDK 27](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) erläutern Neuerungen und verweisen auf zugehörige JEPs.

Eine **JEP** (*JDK Enhancement Proposal*) dokumentiert einen Vorschlag zur Verbesserung des JDK mit Zielen, Entwurf und Status. Manche Funktionen erscheinen zunächst als *Preview* oder *Incubator* und können sich vor der endgültigen Einführung ändern.

Die [Änderungen der Java-Sprache pro Release](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html) verknüpfen Funktionen mit ihren JEPs. Die [Zusammenfassung der Sprachänderungen](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html) erleichtert den Vergleich dauerhafter und vorläufiger Funktionen.

## Java aktualisieren
1. Prüfen Sie die Version mit <code>java --version</code> und <code>javac --version</code>.
2. Klären Sie die Unterstützung durch Projekt, Abhängigkeiten und Produktionsumgebung.
3. Laden Sie ein Update Ihrer Distribution herunter oder wählen Sie eine kompatible Distribution.
4. Installieren Sie das JDK und passen Sie bei Bedarf <code>PATH</code>, <code>JAVA_HOME</code> und IDE an.
5. Öffnen Sie ein neues Terminal, prüfen Sie die Versionen und führen Sie die Anwendungstests aus.

Ein Update innerhalb derselben Versionslinie ist etwas anderes als eine Migration auf eine Hauptversion. Prüfen Sie vorher die Release-Notes und testen Sie Anwendung und Abhängigkeiten.

Unter Windows zeigen <code>where.exe java</code> und <code>where.exe javac</code> die gefundenen Programme. Unter macOS und Linux verwenden Sie <code>which java</code> und <code>which javac</code>.

## Quellen
- [Oracle Java SE Support-Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [Oracle-JDK-Lizenz-FAQ](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
