---
layout: post
title: "Java i VS Code: installera och konfigurera JDK"
date: 2026-11-25
lang: sv
translation_id: java-no-vscode-configurar
permalink: /sv/java-i-vs-code-konfigurera/
share_text: >-
  Konfigurera Java i Visual Studio Code, välj ett JDK och kör ett första program.
---

## Installera JDK och Visual Studio Code
För att programmera **Java i VS Code** installerar du ett JDK som passar projektet och Visual Studio Code. Kontrollera i terminalen att JDK:t är tillgängligt:

~~~text
java --version
javac --version
~~~

Om kommandona saknas kontrollerar du JDK-installationen och <code>PATH</code>. Öppna en ny terminal efter att du har ändrat miljövariabler.

## Installera Java-tilläggen
Öppna **Extensions** i VS Code, sök efter **Extension Pack for Java** och installera paketet från Microsoft. Det samlar språkstöd, körning, felsökning och andra Java-verktyg.

Coding Pack for Java är ett alternativ för Windows och macOS som innehåller VS Code, JDK och viktiga tillägg.

## Konfigurera projektets JDK
Öppna kommandopaletten med <code>Ctrl+Shift+P</code> i Windows eller Linux, eller <code>Cmd+Shift+P</code> i macOS. Kör **Java: Configure Java Runtime** och kontrollera projektets JDK.

Projektets valda JDK kan skilja sig från det i terminalen. Kontrollera båda om flera versioner är installerade.

## Kör ett program
Öppna en mapp i VS Code och skapa <code>Hello.java</code>:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Exemplet använder kompakt källkodssyntax och <code>IO.println</code>, tillgängliga från Java 25. Välj **Run** vid <code>main</code> och kontrollera terminalutdata. För felsökning väljer du **Debug** och sätter en brytpunkt.

Om VS Code inte känner igen filen kontrollerar du att mappen är öppen, väntar tills tilläggen har startat och granskar JDK under **Java: Configure Java Runtime**.

## Referenser
- [Kom igång med Java i VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Java-projekthantering i VS Code](https://code.visualstudio.com/docs/java/java-project)
