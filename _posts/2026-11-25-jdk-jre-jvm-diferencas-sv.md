---
layout: post
title: "JDK, JRE och JVM: vad är skillnaden i Java?"
date: 2026-11-25
lang: sv
translation_id: jdk-jre-jvm-diferencas
permalink: /sv/skillnader-jdk-jre-jvm/
share_text: >-
  Lär dig vad JVM, JRE och JDK gör och vilka kommandon som kontrollerar Java-miljön.
---

## JVM, JRE och JDK
**JVM** (Java Virtual Machine) kör Java-bytecode. Den läser in klasser, verifierar och kör instruktioner samt hanterar resurser som minne. Samma bytecode kan köras på olika system när en kompatibel JVM finns.

**JRE** (Java Runtime Environment) betecknar miljön som behövs för att köra Java-program, inklusive JVM och bibliotek. Om fristående JRE-paket finns beror på distribution och version. Vissa program innehåller en egen körmiljö.

**JDK** (Java Development Kit) samlar körmiljön och utvecklingsverktyg, bland annat kompilatorn <code>javac</code>, startprogrammet <code>java</code> och verktyg för att skapa, köra och felsöka program.

## Vad ska du installera för att programmera?
Installera ett JDK som passar projektet. Distributionen tillhandahåller JVM och de verktyg som behövs. Oracle JDK och Eclipse Temurin är exempel på distributioner.

Kontrollera kommandona i en terminal:

~~~text
java --version
javac --version
~~~

Det första visar versionen på Java-startprogrammet, det andra kompilatorns version. Om <code>java</code> fungerar men <code>javac</code> saknas, kontrollera JDK-installationen och att dess katalog <code>bin</code> finns i <code>PATH</code>.

I Windows visar <code>where java</code> och <code>where javac</code> vilken körbar fil som används. I macOS och Linux använder du <code>which java</code> och <code>which javac</code>.

## Från källkod till körning
I filen <code>Hello.java</code> omvandlar kompilatorn källkoden till bytecode:

~~~text
javac Hello.java
java Hello
~~~

Det första kommandot skapar <code>Hello.class</code>. Det andra startar JVM och kör klassen. Kompatibiliteten beror på versionerna som kompilerar respektive kör programmet.

## Referenser
- [Översikt över Java-plattformen och JVM](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [Installationsguide för JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
