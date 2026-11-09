---
layout: post
title: "Polymorphie in Java"
date: 2026-10-21
lang: de
translation_id: polimorfismo-em-java
permalink: /polymorphie-in-java-de/
share_text: >-
  Einführung in Ad-hoc-, parametrische und Subtyp-Polymorphie mit Java-Beispielen.
---

In der objektorientierten Programmierung bezeichnet **Polymorphie** die Fähigkeit einer Operation, sich je nach Klasse des beteiligten Objekts unterschiedlich zu verhalten. Die wichtigsten Formen sind:

- **Ad-hoc-Polymorphie (oder Überladen)**: Methoden mit demselben Namen können unterschiedliche Parameter haben. Ein Aufruf wählt anhand der Argumente die passende Variante aus.
- **Parametrische Polymorphie**: Generische Klassen und Methoden arbeiten mit Typen, die bei ihrer Verwendung festgelegt werden.
- **Subtyp-Polymorphie**: Eine Unterklasse kann eine Methode überschreiben. Welche Implementierung ausgeführt wird, hängt von der konkreten Klasse des Objekts ab.

Die folgenden Beispiele zeigen diese drei Formen in Java, beginnend mit dem Überladen. Die Klasse `Figure` besitzt zwei überladene Methoden namens `resize`. Die erste erhält einen `percentage` vom Typ `Double`; die zweite zwei Koordinaten `x` und `y` vom Typ `Integer`.

```java
public class Figure {
    public void resize(Double percentage) {
        // Größe prozentual ändern
    }
    public void resize(Integer x, Integer y) {
        // Größe anhand der Koordinaten ändern
    }
}
```

Für **parametrische Polymorphie** können wir parametrisierte Typen mit `<` und `>` erstellen. Die Klasse `ArrayList` hat beispielsweise einen Typparameter `E`, der den Typ der Objekte festlegt, welche die Liste speichern kann. Dieser Typparameter wird auch als formaler Parameter der Methode `add` verwendet. Der von `add` erwartete Typ ist somit derselbe, der bei der Instanziierung von `ArrayList` angegeben wird. Beachte, dass `ArrayList` `AbstractList` erweitert und unter anderem `List`, `RandomAccess`, `Cloneable` sowie `Serializable` implementiert, jeweils mit demselben Typ `E`.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // Implementierung von add
    }
    // Weitere Methoden und Felder der Klasse
}
```

Zum Beispiel können wir eine Liste von Zeichenketten mit dem Typparameter `String` erstellen und durch Aufruf von `add` Elemente einfügen[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

In diesem Fall erwartet der Compiler, dass das an `add` übergebene Argument ein `String` ist. Ein Objekt eines anderen Typs führt zu einem Kompilierungsfehler. Für eine Liste ganzer Zahlen können wir `ArrayList` einen anderen Typ übergeben, hier `Integer`:

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

Für **Subtyp-Polymorphie** nehmen wir an, dass die Klasse `Figure` eine Methode `draw` besitzt, die auch auf Objekten der Klassen `Triangle`, `Circle` und `Rectangle` aufgerufen werden kann. Jede dieser Klassen überschreibt die Methode, um ihr eigenes Zeichenverhalten zu implementieren. Im folgenden Code ruft jeder Aufruf von `draw` eine andere Implementierung auf, je nachdem, welches Objekt (`Circle`, `Triangle` oder `Rectangle`) der Variablen `figure` zugewiesen ist.

```java
Figure figure = new Circle(10);
// Ruft die draw-Methode von Circle auf
figure.draw();
figure = new Triangle(20);
// Ruft die draw-Methode von Triangle auf
figure.draw();
figure = new Rectangle(10, 20);
// Ruft die draw-Methode von Rectangle auf
figure.draw();
```

[^8]: Für `ArrayList` wird üblicherweise `import java.util.ArrayList;` benötigt. In kompakten Quelldateien sind keine Imports nötig. In regulären Quelldateien kann das Modul `java.base` mit `import module java.base;` importiert werden.

---

*Dieser Artikel adaptiert Inhalte aus dem Buch <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> von <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Verwandte Artikel

- [Grundlagen der objektorientierten Programmierung](/grundlagen-objektorientierte-programmierung-de/)
- [Klassen in Java](/klassen-in-java-de/)
- [Vererbung in Java](/vererbung-in-java-de/)
- [Schnittstellen in Java](/schnittstellen-in-java-de/)
- [Links zu OOP und Java](/oop-java-links-de/)
- [Übungen zur objektorientierten Programmierung](/oop-uebungen-de/)
