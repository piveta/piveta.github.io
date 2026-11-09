---
layout: post
title: "Övningar i objektorienterad programmering"
date: 2026-10-21
lang: sv
translation_id: exercicios-poo-java
permalink: /oop-ovningar-sv/
share_text: >-
  Övningar om OOP-begrepp, polymorfism, arv, abstrakta klasser, generiska typer, Java och bankkonton.
---

1. Skriv en handledning som förklarar hur de grundläggande begreppen inom objektorienterad programmering kan representeras i ett valfritt språk förutom Java.

2. Beskriv polymorfism, hur den uppstår och hur den påverkar systemprogrammering, inklusive fördelar och nackdelar. Ge ett exempel.

3. Definiera metodöverskuggning (*overriding*) och metodöverlagring (*overloading*) i objektorienterade programmeringsspråk. Ge exempel.

4. Definiera arv och beskriv tre situationer där det skulle vara lämpligt. Ta med ett kodexempel.

5. Vad är abstrakta klasser och vad används de till i objektorienterade programmeringsspråk? Beskriv minst tre situationer där de skulle vara lämpliga.

6. Vilka fördelar har generiska typer i objektorienterade system och när bör de användas? Ge minst tre exempel på situationer där mekanismen är användbar.

7. Tänk på följande påståenden om objektorienterad programmering:

   I. Metoder definierar operationer i klasser.

   II. Klasser är abstraktioner som används för att representera begrepp från den verkliga och den datorbaserade världen.

   III. Klassinstanser skapas vanligtvis med konstruktorer, som skapar objekt av en viss klass.

   Välj det rätta alternativet:

   1. Endast påstående I är felaktigt.
   2. Endast påstående II är felaktigt.
   3. Endast påstående III är felaktigt.
   4. Endast påståendena I och III är felaktiga.
   5. Inget av påståendena är felaktigt.

8. Välj det rätta påståendet om arv i Java:

   1. Ett objekt av en superklass kan alltid tilldelas en variabel vars typ är en av dess underklasser utan kompileringsfel.
   2. Arv är det enda sättet att komma åt metoder och fält utanför en klass.
   3. Det går inte att helt ersätta beteendet hos en superklassmetod; det kan bara utökas.
   4. Överlagring definierar flera metoder med samma parametrar i en superklass så att dess underklasser kan använda dem.
   5. En underklass ärver alla icke-privata fält och metoder från sin superklass och kan lägga till nya fält och metoder.

9. Skapa klasser för att hantera bankkonton. Konton kan vara sparkonton eller lönekonton. Det ska gå att:

   - Läsa ett kontos saldo.
   - Ändra ett kontos saldo.
   - Ta ut pengar från ett konto.
   - Sätta in pengar på ett konto.
   - Överföra pengar till ett annat konto.
   - Spärra och låsa upp ett konto, till exempel med `account1.block()` och `account1.unblock()`. Om ett konto är spärrat får bara saldot läsas eller ändras.

10. Implementera spelet *Minesweeper* i Java för terminalen.

---

*Den här artikeln bygger på innehåll från boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Relaterade artiklar

- [Grundläggande begrepp inom objektorienterad programmering](/oop-basics-java-sv/)
- [Klasser i Java](/klasser-i-java-sv/)
- [Arv i Java](/arv-i-java-sv/)
- [Polymorfism i Java](/polymorfism-i-java-sv/)
- [Gränssnitt i Java](/granssnitt-i-java-sv/)
- [Länkar om OOP och Java](/lankar-oop-java-sv/)
