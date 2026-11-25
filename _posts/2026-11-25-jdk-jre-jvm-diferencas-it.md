---
layout: post
title: "JDK, JRE e JVM: qual è la differenza in Java?"
date: 2026-11-25
lang: it
translation_id: jdk-jre-jvm-diferencas
permalink: /it/differenze-jdk-jre-jvm/
share_text: >-
  Scopri i ruoli di JVM, JRE e JDK e i comandi per verificare l’ambiente Java.
---

## JVM, JRE e JDK
La **JVM** (Java Virtual Machine) esegue il bytecode Java. Carica le classi, verifica ed esegue le istruzioni e gestisce risorse come la memoria. Lo stesso bytecode può funzionare su sistemi diversi quando è disponibile una JVM compatibile.

Il **JRE** (Java Runtime Environment) indica l’ambiente necessario per eseguire applicazioni Java, inclusi JVM e librerie. La disponibilità di pacchetti JRE autonomi dipende dalla distribuzione e dalla versione. Alcune applicazioni includono il proprio ambiente di esecuzione.

Il **JDK** (Java Development Kit) comprende l’ambiente di esecuzione e gli strumenti di sviluppo: il compilatore <code>javac</code>, il launcher <code>java</code> e altri strumenti per creare, eseguire e diagnosticare applicazioni.

## Cosa installare per programmare?
Per sviluppare in Java, installa un JDK adatto al progetto. La distribuzione fornisce la JVM e gli strumenti necessari. Oracle JDK ed Eclipse Temurin sono esempi di distribuzioni.

Nel terminale, verifica questi comandi:

~~~text
java --version
javac --version
~~~

Il primo mostra la versione del launcher Java, il secondo quella del compilatore. Se <code>java</code> funziona ma <code>javac</code> non viene trovato, verifica che il JDK sia installato e che la cartella <code>bin</code> sia nel <code>PATH</code>.

Su Windows, <code>where java</code> e <code>where javac</code> aiutano a identificare l’eseguibile in uso. Su macOS e Linux, usa <code>which java</code> e <code>which javac</code>.

## Dal codice sorgente all’esecuzione
Nel file <code>Hello.java</code>, il compilatore trasforma il codice sorgente in bytecode:

~~~text
javac Hello.java
java Hello
~~~

Il primo comando genera <code>Hello.class</code>. Il secondo avvia la JVM per eseguire la classe. La compatibilità dipende dalla versione usata per compilare e da quella usata per eseguire.

## Riferimenti
- [Panoramica della piattaforma Java e della JVM](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [Guida all’installazione del JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
