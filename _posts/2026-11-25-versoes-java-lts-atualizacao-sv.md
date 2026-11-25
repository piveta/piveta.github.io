---
layout: post
title: "Java-versioner: LTS, uppdateringar och versionskontroll"
date: 2026-11-25
lang: sv
translation_id: versoes-java-lts-atualizacao
permalink: /sv/java-versioner-lts-uppdateringar/
share_text: >-
  Lär dig hur Java-versioner släpps, vad LTS betyder och hur du kontrollerar och uppdaterar ett JDK.
---

## Kontrollera Java-versionen
Kör följande kommandon i terminalen:

~~~text
java --version
javac --version
~~~

Det första visar Java-startprogrammet som används för att starta program, det andra kompilatorn. Om flera JDK-versioner är installerade kan programmet i <code>PATH</code> skilja sig från det som IDE:n använder.

## Java-versioner och LTS
Java får funktionsversioner var sjätte månad. En **LTS**-version (*long-term support*) får långsiktigt stöd från vissa leverantörer. Stödets längd, pris och villkor beror på distribution och leverantör.

I Oracles supportplan är Java 8, 11, 17, 21 och 25 LTS-versioner. Oracle planerar en ny LTS vartannat år. Kontrollera den aktuella planen och leverantörens policy innan du väljer produktionsversion.

Valet beror också på bibliotek, verktyg och programmets krav. LTS ger en längre supportperiod, medan mellanversioner ger tidigare tillgång till nya funktioner.

## Hitta versioner och JEP
Oracle har ett [index över JDK-versionernas information](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html) med länkar till releaser och uppdateringar. Informationen beskriver ändringar, rättningar och nya eller borttagna funktioner. [Informationen om JDK 27](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) tar upp nyheter och länkar till relaterade JEP.

En **JEP** (*JDK Enhancement Proposal*) beskriver ett föreslaget JDK-förbättringsarbete, dess mål, utformning och status. Vissa funktioner kommer först som *preview* eller *incubator* och kan ändras innan de blir permanenta.

Se [Java-språkändringar per version](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html) och [sammanfattningen av språkändringar](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html) för att jämföra permanenta funktioner med förhandsversioner.

## Uppdatera Java
1. Kontrollera versionen med <code>java --version</code> och <code>javac --version</code>.
2. Ta reda på vilka versioner projektet, beroenden och produktionen stöder.
3. Hämta en uppdatering från din distribution eller välj en kompatibel.
4. Installera JDK och justera vid behov <code>PATH</code>, <code>JAVA_HOME</code> och IDE:n.
5. Öppna en ny terminal, kontrollera versionerna och kör programmets tester.

En uppdatering inom samma versionsserie och en migrering till en ny huvudversion är olika beslut. Läs versionsinformationen och testa programmet och beroendena före en migrering.

I Windows visar <code>where.exe java</code> och <code>where.exe javac</code> hittade program. I macOS och Linux använder du <code>which java</code> och <code>which javac</code>.

## Referenser
- [Oracles supportplan för Java SE](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [Vanliga frågor om Oracle JDK-licenser](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
