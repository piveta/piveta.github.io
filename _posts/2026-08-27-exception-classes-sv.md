---
layout: post
title: "Undantagsklasser i Java"
date: 2026-08-27
lang: sv
translation_id: classes-de-excecao
permalink: /undantagsklasser-java-sv/
image: /images/descendentesThrowable.png
share_text: >-
  I Javas undantagshierarki ligger Error och Exception under Throwable, medan RuntimeException hör till de okontrollerade undantagen. Artikeln förklarar skillnaden mellan kontrollerade och okontrollerade undantag.
---
Under körningen av ett program kan situationer uppstå som kräver särskild hantering. De kan representera onormala eller felaktiga tillstånd, situationer som programmeraren inte förutsåg eller till och med alternativa körningsflöden. Dessa tillstånd kallas **undantag**.

I Java representeras undantag av objekt som tillhör klassen `Throwable` eller någon av dess underklasser. Undantagshierarkin är viktig för att förstå vilka undantag som kan kastas, fångas och hanteras av program.

## Throwable

`Throwable` är basklassen i Javas undantagshierarki. Objekt av denna klass lagrar information om en viss händelse och gör det möjligt att överföra denna information från den punkt där undantaget uppstod till den kod som ansvarar för att hantera det.

Endast objekt som tillhör `Throwable` eller någon av dess underklasser kan kastas av JVM eller av programmeraren med `throw`. På samma sätt kan en `catch`-sats endast fånga objekt som tillhör denna hierarki.

Bland de viktigaste metoderna i `Throwable` finns `getMessage()`, som gör det möjligt att hämta meddelandet som hör till undantaget, och `printStackTrace()`, som visar körningsstacken fram till den punkt där undantaget uppstod.

Klassen `Throwable` har två direkta underklasser: `Exception` och `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Throwable-hierarkin"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

Klassen `Error` representerar allvarliga tillstånd som en applikation i allmänhet inte kan återhämta sig från. Det är onormala situationer som normalt inte bör inträffa under programmets körning.

Några viktiga underklasser till `Error` är `AssertionError`, `IOError` och `VirtualMachineError`. Den sistnämnda har bland annat underklasserna `InternalError`, `OutOfMemoryError`, `StackOverflowError` och `UnknownError`.

Fel kan kastas av JVM själv, ofta som en följd av tillstånd som upptäckts av operativsystemet eller körmiljön. De kan också uttryckligen skapas av programmeraren, till exempel med `assert` eller `throw`.

<img src="/images/exceptionsError.png"
     alt="Error och dess underklasser"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

Klassen `Exception` representerar undantag som under vissa omständigheter kan hanteras och som applikationen kan återhämta sig från.

Dess underklasser omfattar `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException` och `RuntimeException`.

De underklasser till `Exception` som inte är underklasser till `RuntimeException` kallas **kontrollerade undantag** (*checked exceptions*). Kompilatorn kräver att programmet uttryckligen tar hänsyn till dem. Detta kan göras genom att fånga undantaget med en `catch`-sats eller genom att med `throws` deklarera att metoden kan kasta det.

<img src="/images/descendentesException.png"
     alt="Exception och dess underklasser"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

Bland underklasserna till `Exception` utmärker sig `RuntimeException`. Den och dess underklasser kallas **körningsundantag** (*runtime exceptions*).

`RuntimeException` och dess underklasser är **okontrollerade undantag** (*unchecked exceptions*). Kompilatorn kräver inte att de uttryckligen hanteras med `try`/`catch` eller deklareras med `throws`.

Denna typ av undantag representerar vanligtvis logiska fel eller felaktig användning av ett program. Vanliga exempel är:

- `ClassCastException`: uppstår när en explicit typkonvertering inte är möjlig.
- `IllegalArgumentException`: anger att en metod har fått ett argument som anses ogiltigt eller olämpligt.
- `IndexOutOfBoundsException`: uppstår när ett försök görs att komma åt en position som inte finns i en indexerad struktur.
- `NullPointerException`: uppstår när en operation utförs på en `null`-referens.

En metod som kan kasta en `RuntimeException` behöver inte deklarera denna möjlighet med `throws`. Det är naturligtvis fortfarande möjligt att fånga och hantera dessa undantag med `try` och `catch`.

I praktiken indikerar många `RuntimeException`-instanser problem som hade kunnat förhindras av själva programmet. När ett sådant undantag uppstår är det vanligtvis viktigt att undersöka orsaken och åtgärda problemet i stället för att bara fånga undantaget.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException och dess underklasser"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Kontrollerade och okontrollerade undantag

En viktig skillnad i Javas undantagshierarki är mellan **kontrollerade** och **okontrollerade** undantag.

`Throwable` och alla dess underklasser som inte är underklasser till `RuntimeException` eller `Error` kallas **kontrollerade undantag**. `RuntimeException` och dess underklasser, liksom `Error` och dess underklasser, kallas **okontrollerade undantag**.

Kontrollerade undantag måste hanteras eller uttryckligen deklareras av programmet. Det innebär att när en metod kan kasta ett kontrollerat undantag måste det hanteras av en `catch`-sats eller deklareras i metodens `throws`-sats.

Okontrollerade undantag behöver däremot inte uttryckligen hanteras eller deklareras. Kompilatorn kräver inte att `RuntimeException`, `Error` eller deras underklasser fångas eller deklareras.

Förenklat kan hierarkin visas så här:

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

Denna organisation gör det möjligt att hantera undantag på olika nivåer i hierarkin. En `catch`-sats kan till exempel fånga ett specifikt undantag eller en av dess superklasser, beroende på önskat beteende.

Att förstå denna hierarki är grundläggande för att förstå Javas mekanism för undantagshantering och för att avgöra vilka undantag som ska hanteras, vilka som ska propageras och vilka som representerar fel som måste åtgärdas i själva programmet.

Denna artikel är anpassad från innehåll i boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.
