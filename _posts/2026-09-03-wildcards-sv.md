---
layout: post
title: "Wildcards och begränsningar i generiska typer i Java"
date: 2026-09-03
lang: sv
translation_id: wildcards-limites-java
permalink: /wildcards-begransningar-generiska-typer-java/
---

Utöver specifika generiska typer kan vi använda **wildcards** för att uttrycka okända typer (`<?>`), begränsa den angivna typen till undertyper av en viss typ (`<? extends Type>`) eller inkludera supertyper (med `<? super Type>`). Följande avsnitt beskriver obegränsade wildcards, wildcards med övre begränsning och wildcards med nedre begränsning. Därefter visar vi hur vi kan definiera flera begränsningar för generiska typer.

## Obegränsade wildcards

För okända typer använder vi frågetecknet som typ, vilket gör att vilken typ som helst kan användas i det sammanhanget. Om en variabel till exempel deklareras som `List<?>` (eller är ett attribut eller en parameter), kan den tilldelas `List`-objekt med vilken giltig typparameter som helst, till exempel `String`, `Integer` osv. Sådana okända generiska typer kallas **obegränsade wildcards** (`<?>`), eftersom de inte anger någon typbegränsning.

Till exempel:

```java
List<?> l = new ArrayList<String>();
// eller till exempel
l = new LinkedList<Integer>();
```

Även om detta sätt att deklarera variabler kan verka attraktivt finns det begränsningar. I sådana fall känner vi inte till typen på objekten i listan. Därför kan vi till exempel inte lägga till element i listan (förutom `null`, som är kompatibelt med alla referenstyper i Java), eftersom det inte finns någon garanti för att objektet som läggs till har samma typ som listans typparameter.

Om vi försöker lägga till ett element i listobjektet (i detta fall `l`) får vi därför ett kompileringsfel:

```java
void main(){
    List<?> l = new ArrayList<String>();
    // Compilation error: 
    //    "The method add(capture#2-of ?) in the type 
    //     List<capture#2-of ?> is not applicable 
    //     for the arguments (String)"
    l.add("Maria");
}
```

Obegränsade typer används ofta när vi bara vill läsa data utan att ändra den. Vi kan till exempel ha en metod som tar emot en lista och skriver ut dess element utan att ange typen på listans element:

```java
public void print(List<?> list) {
    for (Object obj : list)
        IO.println(obj);
}
void main(){
    print(List.of(1, 2, 3));
    print(List.of("A", "B", "C"));
}
```

När `main` körs visas:

```text
1
2
3
A
B
C
```

Här använder vi utskrift som exempel, men vi kan också iterera över objekten, använda dem i *streams*, filtrera dem med `instanceof`, hämta listans storlek, kontrollera om ett visst objekt finns i listan, omvandla och kopiera dem till en typad lista och utföra andra operationer. Det vi inte kan göra är att direkt ändra listan (till exempel med `add` eller `set`, förutom med `null`).

## Wildcards med övre begränsning

**Wildcards med övre begränsning** gör det möjligt att ange att endast ett objekt av en viss typ eller en av dess undertyper (genom arv eller implementation av ett interface) kan användas som typparameter. Notationen `<? extends T>` anger att wildcarden måste vara av typen `T` eller en typ som utökar `T`.

Om jag till exempel deklarerar en lista vars wildcard utökar `Number`, kan jag tilldela objekt av vilken som helst av dess subklasser (till exempel `Double` eller `Integer`). Om `Number` vore en konkret klass (den är abstrakt), skulle vi också kunna tilldela ett objekt av själva klassen. Följande exempel visar detta:

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

Precis som med obegränsade wildcards kan vi inte lägga till element i listan `l`, eftersom vi inte känner till listans exakta typ. Därför ger de två första anropen till `add` kompileringsfel:

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

Även om vi genom att läsa koden vet att objektet som tilldelats variabeln `l` är en lista med heltal, vet kompilatorn att `l` har en okänd typ och tillåter därför inte att värden läggs till. Vid läsning behandlas värdena som `Number`, vilket är den övre begränsningen.

## Wildcards med nedre begränsning

**Wildcards med nedre begränsning** gör det möjligt att ange att endast ett objekt av en viss typ eller en av dess supertyper kan användas som typparameter. Notationen `<? super T>` anger att wildcarden måste vara av typen `T` eller en superklass till `T`.

Om jag till exempel deklarerar en lista vars wildcard har `Number` som nedre begränsning kan jag tilldela objekt av någon av dess superklasser (i fallet `Number` endast `Object`, eftersom `Number` inte har någon uttrycklig superklass).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

Det är tillåtet att lägga till element av typen för den nedre begränsningen (i detta fall `Number`) eller någon av dess undertyper (till exempel `Double` eller `Integer`). Följande exempel visar en lista vars wildcard har `Number` som nedre begränsning. I detta fall kan vi skapa en `ArrayList` av tal (eller av dess superklass `Object`). Vi kan lägga till element av dess subklasser (vi kan inte lägga till ett objekt av typen `Number`, eftersom det är en abstrakt klass som inte kan ha direkta instanser). Exemplet visar tre tillägg. De två första är tillåtna eftersom elementen är undertyper av `Number` (`10` är en `Integer` och `1.0` är en `Double`). Det tredje tillägget är inte tillåtet och ger ett kompileringsfel eftersom `Object` inte är en ättling till `Number`.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

Om vi skapade `ArrayList` med `Object` som typparameter skulle det tredje tillägget fortfarande inte vara tillåtet vid kompilering och ge samma fel (de två första tilläggen skulle fortfarande vara tillåtna), eftersom listans typ fortfarande är okänd (vi vet bara att den är `Number` eller en av dess supertyper).

## Flera begränsningar

I Java kan en generisk typ ha **flera begränsningar**, vilket innebär att typparametern kan begränsas till typer som utökar (eller är) en viss klass och som implementerar ett eller flera interface. Syntaxen följer formen `<T extends Class & Interface1 & Interface2>`. Om en klass används som begränsning måste den anges först, följd av interfacen. Om ingen klass används kan endast interface listas.

Till exempel har klassen `MultipleBounds` en generisk typ `T` som utökar klassen `Number` och implementerar interfacen `Comparable<T>` och `Serializable`:

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

I detta exempel kan `T` endast vara `Number` eller en typ som ärver från `Number` och dessutom implementerar `Comparable<T>` och `Serializable`. Detta är användbart när vi behöver flera garantier, till exempel tillgång till superklassens metoder och kontrakt som definieras av flera interface. Kombinationen gör koden mer flexibel samtidigt som den förblir starkt typad, undviker kompileringsfel och säkerställer att alla nödvändiga metoder finns tillgängliga för den använda generiska typen.

---

*Den här artikeln är baserad på innehåll från boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
