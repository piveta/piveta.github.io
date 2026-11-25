---
layout: post
title: "Installera Java och JDK i Windows"
date: 2026-11-25
lang: sv
translation_id: como-instalar-java-jdk-windows
permalink: /sv/installera-java-jdk-windows/
share_text: >-
  Hämta och installera ett JDK i Windows och kontrollera installationen med java och javac.
---

## Välj en Java-distribution
För Java-utveckling i Windows hämtar du ett **JDK** som passar projektet. Oracle JDK och Eclipse Temurin är tillgängliga. En LTS-version kan passa projekt som behöver långsiktigt stöd. Kontrollera projektkrav och distributionsvillkor.

Kontrollera systemtyp och processorarkitektur i Windows-inställningarna. Välj rätt paket, till exempel x64 eller AArch64, och Windows-installationsprogrammet.

## Hämta och installera JDK
Så här installerar du Eclipse Temurin:

1. Öppna [Adoptiums nedladdningssida](https://adoptium.net/temurin/releases/).
2. Välj Java-version, Windows, arkitektur och paketet **JDK**.
3. Hämta och kör MSI-installationsprogrammet.
4. Kontrollera om Java ska läggas till i <code>PATH</code>. Om ett verktyg behöver <code>JAVA_HOME</code>, välj även det alternativet.
5. Slutför installationen och öppna en ny terminal.

I Temurin är det standard att lägga till Java i <code>PATH</code>; <code>JAVA_HOME</code> är ett extra val.

## Kontrollera installationen
Kör i PowerShell eller Kommandotolken:

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

De två första visar Java- och kompilatorversionerna. De andra visar program som hittas i <code>PATH</code>. Om ett kommando saknas öppnar du en ny terminal och granskar miljövariablerna. Om fel version visas kontrollerar du katalogordningen i <code>PATH</code>.

Spara koden som <code>Hello.java</code> för att testa kompileringen:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Exemplet använder kompakt källkodssyntax och <code>IO.println</code>, tillgängliga från Java 25. Kör:

~~~text
javac Hello.java
java Hello
~~~

Utdata är <code>Hello World!</code>. Före Java 25 använder du den programform som ditt JDK stöder.

## Referenser
- [Eclipse Temurin MSI-installationsprogram](https://adoptium.net/installation/windows/)
- [Installation av Oracle JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
