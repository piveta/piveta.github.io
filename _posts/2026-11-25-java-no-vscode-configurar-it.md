---
layout: post
title: "Java in VS Code: installare e configurare il JDK"
date: 2026-11-25
lang: it
translation_id: java-no-vscode-configurar
permalink: /it/java-in-vs-code-configurare/
share_text: >-
  Configura Java in Visual Studio Code, scegli un JDK ed esegui il primo programma.
---

## Installa il JDK e Visual Studio Code
Per programmare in **Java con VS Code**, installa un JDK compatibile con il progetto e Visual Studio Code. Verifica nel terminale che il JDK sia accessibile:

~~~text
java --version
javac --version
~~~

Se i comandi non vengono trovati, controlla l’installazione del JDK e il <code>PATH</code>. Dopo aver modificato le variabili d’ambiente, apri un nuovo terminale.

## Installa le estensioni Java
In VS Code, apri **Extensions**, cerca **Extension Pack for Java** e installa il pacchetto pubblicato da Microsoft. Include supporto al linguaggio, esecuzione, debug e altri strumenti Java.

Un’alternativa è Coding Pack for Java, disponibile per Windows e macOS, che include VS Code, un JDK e le estensioni essenziali.

## Configura il JDK del progetto
Apri la Command Palette con <code>Ctrl+Shift+P</code> su Windows o Linux, oppure <code>Cmd+Shift+P</code> su macOS. Avvia **Java: Configure Java Runtime** e controlla il JDK associato al progetto.

Il JDK del progetto può essere diverso da quello disponibile nel terminale. Se hai più versioni installate, verifica entrambe.

## Esegui un programma
Apri una cartella in VS Code e crea <code>Hello.java</code>:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

L’esempio usa la dichiarazione compatta e <code>IO.println</code>, disponibili da Java 25. Seleziona **Run** accanto a <code>main</code> e controlla l’output nel terminale. Per il debug, scegli **Debug** e imposta un breakpoint.

Se VS Code non riconosce il file, verifica che la cartella sia aperta, attendi l’avvio delle estensioni e controlla il JDK in **Java: Configure Java Runtime**.

## Riferimenti
- [Introduzione a Java in VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Gestione dei progetti Java in VS Code](https://code.visualstudio.com/docs/java/java-project)
