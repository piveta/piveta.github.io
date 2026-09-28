---
layout: post
title: "Hello World - Traditionell vs. förenklad version"
date: 2026-08-22
lang: sv
translation_id: hello-world
permalink: /hello-world-sv/
---

Det är vanligt att börja studera ett programmeringsspråk genom att skriva ett program som kallas **Hello World** och som visar texten `Hello World!` på enhetens standardutmatning, vanligtvis skärmen. I Java kan vi skriva programmet så här:

```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```

I detta program har vi en klass som heter `Hello`. I objektorienterade system hjälper klasser till att modellera begrepp från den tillämpningsdomän som studeras. Klasser kapslar in både data och beteende som hör samman med ett visst begrepp.

Klassen `Hello` har en enda metod som heter `main`. Den tar emot en array av strängar som innehåller de kommandoradsargument som angavs när programmet kördes, om några sådana finns. I detta exempel används argumenten inte.

Metoden `main` är statisk, vilket innebär att den är en klassmetod och inte en instansmetod. Därför kan den anropas utan att ett objekt av klassen `Hello` skapas.

Inuti metoden `main` finns ett anrop till metoden `println`. Denna metod tillhör klassen `PrintStream` och skriver ut värdet som skickats som argument på skärmen, följt av en radavslutning.

Metoden `println` anropas via fältet `out` i klassen `System`. Fältet har typen `PrintStream` och ger åtkomst till systemets standardutmatning.

## Kompilering och körning

Java-program kompileras först till en mellanrepresentation som kallas **bytekod**, vilket säkerställer portabilitet. Bytekoden körs sedan av en Java Virtual Machine (JVM), som omvandlar den till maskinkod som är lämplig för den underliggande plattformen.

För att kompilera programmet måste det sparas i en fil som heter `Hello.java`. I Java har filer som innehåller publika typer normalt samma namn som typen.

Vi kan använda en integrerad utvecklingsmiljö (**IDE**) eller anropa kompilatorn direkt från kommandoraden, förutsatt att ett JDK är installerat.

Java-program skrivs normalt i en IDE, som erbjuder funktioner som förbättrar produktiviteten under utvecklingen, exempelvis navigering i källkod, refaktorering, statisk analys, kompilering, testning och felsökning.

Några av de mest populära IDE:erna för Java är:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

Vi kan också kompilera programmet direkt från kommandoraden med kompilatorn `javac`:

```text
    javac Hello.java
```

Kommandot tar `Hello.java` som indata och skapar filen `Hello.class`, som innehåller den kompilerade versionen av programmet.

Efter kompileringen kan vi köra programmet med kommandot `java`:

```text
    java Hello
```

Resultatet blir:

```text
    Hello World!
```

## Ett enklare tillvägagångssätt med Java 25+

Från och med Java 25 blev en funktion som hade utvecklats som *preview* sedan Java 21 permanent: **Compact Source Files and Instance Main Methods**. Den gör det möjligt att skriva små program med mindre standardkod genom att utelämna den explicita klassdeklarationen och förenkla metoden `main`.

Det tidigare programmet kan därför skrivas i Java 26 (den aktuella versionen) på följande sätt:

```java
    void main() {
        IO.println("Hello World!");
    }
```

I detta fall behöver vi inte deklarera klassen explicit eller skriva `public static void main(String[] args)`. Kompilatorn behandlar filen som om den implicit deklarerade en klass, och metoden `main` kan vara en instansmetod.

Vi kan också använda klassen `IO`, som tillhandahåller enkla in- och utmatningsoperationer för konsolen. I Java 26 tillhör `IO` paketet `java.lang` och är därför implicit tillgänglig. För att anropa dess metoder måste vi dock använda klassnamnet, som i `IO.println(...)`.

Eftersom funktionen inte längre är en *preview* behöver vi inga särskilda kompileringsalternativ. Programmet kan kompileras normalt:

```text
    javac Hello.java
```

och köras på samma sätt:

```text
    java Hello
```

Det är också möjligt att köra en källfil direkt med `java`-startprogrammet:

```text
    java Hello.java
```

I detta fall kompileras källkoden i minnet av startprogrammet självt innan körningen. Detta gör det möjligt att köra program direkt från källfiler utan att uttryckligen skapa en `.class`-fil.

Kompakta källfiler är särskilt intressanta för små exempel, utbildningsprogram, skript och experiment. När programmet växer och kräver en mer omfattande struktur kan vi naturligt återgå till den traditionella formen med explicita klass- och metoddeklarationer.

Processen som utförs av IDE:er är i huvudsak likadan. Utöver kompilering och körning erbjuder de funktioner för felsökning, testning, refaktorering, skapande och hantering av projekt, skapande av bibliotek, versionshantering och många andra uppgifter.

---

*Den här artikeln är en bearbetning av innehåll från boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
