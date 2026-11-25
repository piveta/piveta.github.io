---
layout: post
title: "Java und das JDK unter Windows installieren"
date: 2026-11-25
lang: de
translation_id: como-instalar-java-jdk-windows
permalink: /de/java-jdk-windows-installieren/
share_text: >-
  Laden Sie ein JDK für Windows herunter, installieren Sie es und prüfen Sie es mit java und javac.
---

## Eine Java-Distribution auswählen
Laden Sie zum Programmieren unter Windows ein **JDK** herunter, das zu Ihrem Projekt passt. Oracle JDK und Eclipse Temurin sind verfügbare Distributionen. Für langfristigen Support kann eine LTS-Version sinnvoll sein. Prüfen Sie die Projektanforderungen und die Bedingungen der Distribution.

Kontrollieren Sie in den Windows-Einstellungen Systemtyp und Prozessorarchitektur. Wählen Sie auf der Downloadseite das passende Paket, etwa x64 oder AArch64, sowie den Windows-Installer.

## JDK herunterladen und installieren
Für Eclipse Temurin gehen Sie so vor:

1. Öffnen Sie die [Adoptium-Downloadseite](https://adoptium.net/temurin/releases/).
2. Wählen Sie Java-Version, Windows, Architektur und das Paket **JDK**.
3. Laden Sie den MSI-Installer herunter und starten Sie ihn.
4. Prüfen Sie, ob Java zum <code>PATH</code> hinzugefügt wird. Benötigt ein anderes Werkzeug <code>JAVA_HOME</code>, wählen Sie auch diese Option.
5. Schließen Sie die Installation ab und öffnen Sie ein neues Terminal.

Im Temurin-Installer ist das Hinzufügen zu <code>PATH</code> eine Standardoption; <code>JAVA_HOME</code> ist zusätzlich.

## Installation prüfen
Führen Sie in PowerShell oder der Eingabeaufforderung Folgendes aus:

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

Die ersten beiden Befehle zeigen Java- und Compiler-Versionen. Die anderen zeigen Programme im <code>PATH</code>. Wird ein Befehl nicht gefunden, öffnen Sie ein neues Terminal und prüfen die Umgebungsvariablen. Bei einer unerwarteten Version prüfen Sie die Reihenfolge der Verzeichnisse in <code>PATH</code>.

Speichern Sie dies als <code>Hello.java</code>, um die Kompilierung zu testen:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Das Beispiel nutzt kompakte Quelldatei-Syntax und <code>IO.println</code>, verfügbar ab Java 25. Führen Sie aus:

~~~text
javac Hello.java
java Hello
~~~

Die Ausgabe lautet <code>Hello World!</code>. Vor Java 25 verwenden Sie die vom JDK unterstützte Programmform.

## Quellen
- [Eclipse-Temurin-MSI-Installer](https://adoptium.net/installation/windows/)
- [Oracle-JDK-Installation](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
