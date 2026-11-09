---
layout: post
title: "Grundläggande begrepp inom objektorienterad programmering"
date: 2026-10-21
lang: sv
translation_id: conceitos-basicos-poo-java
permalink: /oop-basics-java-sv/
share_text: >-
  En introduktion till grunderna i objektorienterad programmering: klasser, objekt, attribut, metoder, inkapsling, arv, polymorfism och relationer mellan klasser.
---

Strukturerad programmering erbjuder mekanismer för att modularisera begreppen i ett programvarusystem med hjälp av datastrukturer och algoritmerna som hanterar dem. Vanliga strukturerade språk kan representera olika datatyper och variabler för att uttrycka egenskaper och kännetecken hos begreppen, samt procedurer och funktioner för att modellera deras operationer.

När vi vill återanvända komponenter som skrivits i strukturerade språk måste vi dock identifiera sambandet mellan data — som representeras av datastrukturer, datatyper och variabler — och beteende — som uttrycks genom procedurer och funktioner. Därför sker återanvändning ofta på en finfördelad nivå och kan kräva en betydande arbetsinsats, exempelvis för att avgöra vilka procedurer och funktioner som hör ihop med vilka datastrukturer. Det går att skapa återanvändbara bibliotek, men sambandet mellan data och beteende är inte uttryckligt eller samlat i en enda abstraktion.

**Objektorienterad programmering** (OOP) är ett paradigm som representerar begrepp från en viss tillämpningsdomän med abstrakta datatyper som kallas klasser. Klasserna modellerar både begreppens egenskaper och kännetecken samt deras operationer. OOP utökar strukturerad programmering genom att erbjuda sätt att specificera och komponera klasser för att modellera kompletta datorsystem, med målet att öka modulariteten och återanvändningen av komponenter.

I dag är objektorienterad programmering ett av de mest accepterade och använda paradigmen inom programvaruutveckling. Många moderna språk stöder det, bland annat Java, C++, C#, Python, Kotlin, JavaScript, TypeScript, Swift och Ruby.

En **klass** är en abstraktionsmekanism som används för att representera begrepp inom en viss tillämpningsdomän. I en bankdomän kan begreppen till exempel vara filialer, konton, kunder och transaktioner. Vi kan definiera klasserna `Branch`, `Account`, `Customer` och `Transaction` för att representera dem. Figuren visar en grafisk representation av klasserna.

<img src="/images/en/oopClasses.svg" alt="Klasserna Branch, Account, Customer och Transaction." style="max-width: 300px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Klasser fungerar som *mallar* för att skapa konkreta och hanterbara exempel på begreppen. Sådana exempel kallas **objekt**. Ett objekt är en **instans** av en klass, och processen att skapa objekt kallas **instansiering**. Vi kan till exempel skapa objekt som representerar kunderna *John*, *Peter* och *Mary*, med deras personuppgifter och de funktioner som är tillgängliga för kunder.

<img src="/images/en/oopObjects.svg" alt="Objekten John, Peter och Mary är instanser av klassen Customer." style="max-width: 380px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

En klass definieras för att representera egenskaper, kännetecken och beteende hos ett begrepp. De två huvudsakliga mekanismerna för detta är attribut och metoder.

**Attribut** representerar kännetecken eller egenskaper hos objekt i en klass. Attribut i klassen `Customer` kan till exempel vara *name*, *age*, *address* och *marital status*. Varje kund kan ha olika värden för attributen. Ett kundobjekt kan till exempel ha värdena *name* $`=`$ John Smith, *age* $`=`$ 50, *address* $`=`$ 205 President Vargas Street och *marital status* $`=`$ married.

**Metoder** representerar beteende. Möjliga metoder i klassen `Account` kan motsvara operationerna att *öppna*, *avsluta* eller *byta kontohavare* för ett konto. Att **anropa** en metod utför den operation som metoden implementerar. Klasser har ofta särskilda metoder för att skapa (instansiera) objekt, så kallade **konstruktorer**, och för att förstöra objekt, så kallade **destruktorer**.

Attribut och metoder delas också in i instansmedlemmar och klassmedlemmar. De vanligaste **instansattributen och instansmetoderna** nås via klassens objekt och beskriver egenskaper och operationer för enskilda instanser. Instansattribut i `Account` kan vara *bank*, *branch*, *account number* och *account holder*, medan instansmetoder kan vara *withdraw*, *transfer* och *deposit*. **Klassattribut och klassmetoder** hör däremot till klassen själv och inte till dess instanser. Ett klassattribut kan till exempel räkna antalet skapade `Account`-instanser, och en klassmetod kan hämta det antalet.

För att begränsa åtkomsten till attribut och metoder erbjuder klasser mekanismer för **inkapsling och informationsdöljning**. Programmeringsspråk tillhandahåller vanligtvis synlighetsmodifierare som anger vem som får komma åt ett visst attribut, en metod eller en klass.

Klasser abstraherar och kapslar in begrepp från den verkliga och den datorbaserade världen. Abstraktionerna kan kombineras genom relationer så att klasser samarbetar för att uppfylla en applikations krav. De viktigaste relationerna mellan klasser är arv, association, aggregation, komposition och realisering.

**Arv** är en kompositionsmekanism som gör det möjligt för klasser att återanvända gränssnitt och beteende från befintliga klasser och utöka deras funktioner. En klass som utökar en annan kallas **underklass**, och den utökade klassen kallas **superklass**. Utökningen deklareras vanligtvis i underklassen, till exempel: `SubClass` utökar `SuperClass`.

Figur 3 visar klasserna `Shape`, `Rectangle`, `Triangle` och `Circle`. `Shape` är superklassen och `Rectangle`, `Triangle` och `Circle` är dess underklasser.

<img src="/images/en/oopInheritance.png" alt="Shape är superklass till Rectangle, Triangle och Circle." style="max-width: 400px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Arvsmekanismer varierar mellan programmeringsspråk. Skillnaderna gäller ofta synlighet och antal superklasser. Vissa språk, som C++, gör det möjligt att ange **publikt** eller **privat** arv. Anta att klassen `B` ärver från klassen `A`. Då är `A` superklass till `B`, och `B` underklass till `A`. Vid publikt arv är `B` en subtyp till `A` och ärver både dess implementation och dess gränssnitt. Där ett `A`-objekt förväntas kan därför ett `B`-objekt (eller ett objekt från en annan underklass till `A`) användas, eftersom varje `B`-instans även räknas som en `A`-instans. Denna princip kallas **Liskovs substitutionsprincip**. Vid privat arv är `B` inte ett `A`; den ärver bara `A`:s implementation och byggs med `A` som grund. Liskovs substitutionsprincip gäller inte i det fallet.

Arv kan också vara **enkelt eller multipelt**. Vid enkelarv, som används av Java och C#, kan en klass bara ha en superklass. Vid multipelt arv, som i C++, kan en klass ha flera superklasser. Språkkonstruktörer är oense om fördelarna med multipelt arv väger upp problemen det kan medföra. Andra språk erbjuder alternativ som virtuellt arv baserat på gränssnitt, *traits* och *mixins*.

Figur 4 visar multipelt arv. `Mammal` och `Bird` representerar djur. `Horse`, `Dog` och `Bat` är underklasser till `Mammal`, medan `Ostrich` och `Duck` är underklasser till `Bird`. Vi vill också klassificera djur som kan flyga och skapar därför `Flyer`, en klass för flygande objekt som inte nödvändigtvis är djur. Med multipelt arv kan både `Duck`- och `Bat`-objekt också vara flygande objekt genom att ärva från `Flyer`.

<img src="/images/en/oopMultipleInheritance.png" alt="Multipelt arv mellan klasserna Animal, Bird, Flyer och Mammal." style="max-width: 500px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Vissa klasser är **abstrakta**. Precis som **konkreta** klasser representerar de egenskaper och beteende hos en grupp verkliga objekt, men de kan inte instansieras direkt. I exemplet med multipelt arv kan `Mammal`, `Bird` och `Flyer` vara abstrakta klasser eftersom det i verkligheten bara finns exempel på deras underklasser, till exempel hästar, hundar och ankor.

Utöver synlighet och antal superklasser möjliggör arv polymorfa metoder. Inom objektorienterad programmering är **polymorfism** en operations förmåga att bete sig olika beroende på klassen hos objektet som anropar den. De viktigaste formerna är:

- **Ad hoc-polymorfism (eller överlagring)** uppstår när en klass har metoder med samma namn men olika typer på de formella parametrarna. Argumentet avgör vilken metod som anropas.
- **Parametrisk polymorfism** uppstår när en metod definieras generiskt och kopplas till en typ som anges senare, till exempel när en variabel deklareras eller ett objekt instansieras. I objektorienterade språk kallas dessa generiska typer.
- **Subtypspolymorfism** uppstår när underklasser överskuggar metoder från en superklass. Objektet som anropar metoden avgör vilken implementation som körs. Det bestäms vanligtvis vid körning genom dynamisk bindning.

Utöver arv finns andra relationer, bland annat association, aggregation och komposition. I allmänhet skiljer de sig åt genom kopplingsgraden mellan deltagarna:

- Vid en **association** är relationen mellan objekt vanligtvis tillfällig och enkel att ändra vid körning. I ett trafiksystem kan en person exempelvis vara associerad med ett visst fordon i rollen som förare. Om föraren byts ut finns båda objekten kvar även om associationen tas bort.
- Vid en **aggregation** är relationen starkare än en association. De aggregerade objekten skapas ofta samtidigt som det aggregerande objektet. En bil kan till exempel ha fyra hjul: bilen är det aggregerande objektet och hjulen är de aggregerade objekten. Relationen kan tas bort, men det är mindre vanligt och mer omständligt att byta hjul än att byta förare.
- Vid en **komposition** är relationen ännu starkare, eftersom de sammansatta objekten är delar av ett större objekt. Tyget i ett fordonssäte består exempelvis av trådar. Om trådarna upphör att finnas upphör även sätet att finnas eller förlorar åtminstone sin identitet.

Relationerna mellan objekt är ofta konceptuella. När de mappas till ett programmeringsspråk kan objekt associeras, aggregeras eller komponeras via klassattribut, som tilldelas värden vid körning. Tidpunkten då objekten skapas kan variera: i en komposition skapas delarna ofta i konstruktorn för helheten, medan associerade objekt vanligtvis skapas oberoende av varandra och kopplas ihop vid behov.

En sista relation, **realisering**, uppstår när en klass deklarerar att den implementerar ett gränssnitt. Ett **gränssnitt** kan ses som en abstrakt klass där alla metoder är abstrakta[^1]. Det fungerar som ett protokoll mellan klienter och implementerare. Klassen (eller en av dess underklasser) måste implementera metoderna som deklareras i gränssnittet. Klienter kan därmed skriva kod som följer gränssnittet utan att vara beroende av hur klasserna implementerar det.

[^1]: Sedan Java 8 kan gränssnitt även definiera konkreta metoder, så kallade standardmetoder, med nyckelordet `default`. Klasser som implementerar ett gränssnitt med en standardmetod behöver inte implementera den själva, men kan göra det.

---

*Den här artikeln bygger på innehåll från boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Relaterade artiklar

- [Klasser i Java](/klasser-i-java-sv/)
- [Arv i Java](/arv-i-java-sv/)
- [Polymorfism i Java](/polymorfism-i-java-sv/)
- [Gränssnitt i Java](/granssnitt-i-java-sv/)
- [Länkar om OOP och Java](/lankar-oop-java-sv/)
- [Övningar i objektorienterad programmering](/oop-exercises-sv/)
