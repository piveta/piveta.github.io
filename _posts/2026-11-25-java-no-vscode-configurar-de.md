---
layout: post
title: "Java in VS Code: JDK installieren und konfigurieren"
date: 2026-11-25
lang: de
translation_id: java-no-vscode-configurar
permalink: /de/java-in-vs-code-einrichten/
share_text: >-
  Richten Sie Java in Visual Studio Code ein, wählen Sie ein JDK und führen Sie ein erstes Programm aus.
---

## JDK und Visual Studio Code installieren
Für **Java in VS Code** installieren Sie ein zum Projekt passendes JDK sowie Visual Studio Code. Prüfen Sie im Terminal, ob das JDK verfügbar ist:

~~~text
java --version
javac --version
~~~

Werden die Befehle nicht gefunden, prüfen Sie JDK-Installation und <code>PATH</code>. Öffnen Sie nach Änderungen an Umgebungsvariablen ein neues Terminal.

## Java-Erweiterungen installieren
Öffnen Sie in VS Code **Extensions**, suchen Sie nach **Extension Pack for Java** und installieren Sie das von Microsoft veröffentlichte Paket. Es bündelt Sprachunterstützung, Ausführung, Debugging und weitere Java-Werkzeuge.

Alternativ gibt es das Coding Pack for Java für Windows und macOS mit VS Code, JDK und wichtigen Erweiterungen.

## Projekt-JDK konfigurieren
Öffnen Sie die Befehlspalette mit <code>Ctrl+Shift+P</code> unter Windows oder Linux beziehungsweise <code>Cmd+Shift+P</code> unter macOS. Starten Sie **Java: Configure Java Runtime** und prüfen Sie das dem Projekt zugeordnete JDK.

Das Projekt-JDK kann vom JDK im Terminal abweichen. Wenn mehrere Versionen installiert sind, prüfen Sie beide.

## Programm ausführen
Öffnen Sie einen Ordner in VS Code und erstellen Sie <code>Hello.java</code>:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Das Beispiel nutzt kompakte Quelldatei-Syntax und <code>IO.println</code>, verfügbar ab Java 25. Wählen Sie **Run** neben <code>main</code> und prüfen Sie die Terminalausgabe. Zum Debuggen wählen Sie **Debug** und setzen einen Haltepunkt.

Erkennt VS Code die Datei nicht, prüfen Sie, ob der Ordner geöffnet ist, warten Sie den Start der Erweiterungen ab und kontrollieren Sie das JDK unter **Java: Configure Java Runtime**.

## Quellen
- [Erste Schritte mit Java in VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Java-Projektverwaltung in VS Code](https://code.visualstudio.com/docs/java/java-project)
