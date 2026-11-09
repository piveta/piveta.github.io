---
layout: post
title: "Polymorfism i Java"
date: 2026-10-21
lang: sv
translation_id: polimorfismo-em-java
permalink: /polymorfism-i-java-sv/
share_text: >-
  En introduktion till ad hoc-, parametrisk och subtypers polymorfism med Java-exempel.
---

Inom objektorienterad programmering är **polymorfism** en operations förmåga att bete sig olika beroende på det inblandade objektets klass. De viktigaste formerna är:

- **Ad hoc-polymorfism (eller överlagring)**: metoder med samma namn kan ha olika parametrar, och anropet väljer den version som passar argumenten.
- **Parametrisk polymorfism**: generiska klasser och metoder arbetar med typer som anges när de används.
- **Subtypspolymorfism**: en underklass kan överskugga en metod, och vilken implementation som körs beror på objektets konkreta klass.

Följande exempel visar dessa tre former i Java, med överlagring först. Klassen `Figure` har två överlagrade metoder som heter `resize`. Den första tar emot `percentage` av typen `Double`; den andra tar emot koordinaterna `x` och `y` av typen `Integer`.

```java
public class Figure {
    public void resize(Double percentage) {
        // Ändra storlek med en procentsats
    }
    public void resize(Integer x, Integer y) {
        // Ändra storlek utifrån koordinater
    }
}
```

Med **parametrisk polymorfism** kan vi skapa parametriserade typer med `<` och `>`. Klassen `ArrayList` har exempelvis typparametern `E`, som anger vilken typ av objekt listan kan lagra. Samma typparameter används som formell parameter till metoden `add`. Typen som `add` förväntar sig är alltså den typ som anges när `ArrayList` instansieras. Observera att klassen utökar `AbstractList` och implementerar bland annat gränssnitten `List`, `RandomAccess`, `Cloneable` och `Serializable` med samma typ `E`.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // Implementation av add
    }
    // Andra metoder och fält i klassen
}
```

Vi kan till exempel skapa en lista med strängar genom att ange typparametern `String` och lägga till element med `add`[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

I det här fallet förväntar sig kompilatorn att argumentet till `add` är en `String`. Ett objekt av en annan typ orsakar ett kompileringsfel. Om vi vill ha en lista med heltal kan vi ange en annan typ till `ArrayList`, här `Integer`:

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

För **subtypspolymorfism**, anta att klassen `Figure` har en metod `draw` som även kan anropas på objekt av klasserna `Triangle`, `Circle` och `Rectangle`. Var och en av dessa klasser överskuggar metoden för att implementera sitt eget ritbeteende. I följande kod anropar varje `draw`-anrop en annan implementation beroende på om objektet som tilldelats `figure` är `Circle`, `Triangle` eller `Rectangle`.

```java
Figure figure = new Circle(10);
// Anropar Circle:s draw-metod
figure.draw();
figure = new Triangle(20);
// Anropar Triangle:s draw-metod
figure.draw();
figure = new Rectangle(10, 20);
// Anropar Rectangle:s draw-metod
figure.draw();
```

[^8]: För att använda `ArrayList` behöver vi vanligtvis importera den med `import java.util.ArrayList;`. Kompakta källfiler kräver inga importer. I vanliga källfiler kan modulen `java.base` importeras med `import module java.base;`.

---

*Den här artikeln bygger på innehåll från boken <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> av <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Relaterade artiklar

- [Grundläggande begrepp inom objektorienterad programmering](/oop-basics-java-sv/)
- [Klasser i Java](/klasser-i-java-sv/)
- [Arv i Java](/arv-i-java-sv/)
- [Gränssnitt i Java](/interfaces-in-java-sv/)
- [Länkar om OOP och Java](/oop-java-links-sv/)
- [Övningar i objektorienterad programmering](/oop-exercises-sv/)
