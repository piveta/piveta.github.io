---
layout: post
title: "Hello World - Traditionelle vs. vereinfachte Version"
date: 2026-08-22
lang: de
translation_id: hello-world
permalink: /hello-world-de/
share_text: >-
  Der Beitrag führt durch ein klassisches Java-Hello-World-Programm mit Klasse und main, einschließlich Kompilierung und Ausführung. Anschließend zeigt er kompakte Quelldateien und Instanz-main-Methoden, die ab Java 25 verfügbar sind.
---

Beim Erlernen einer Programmiersprache beginnt man üblicherweise mit einem Programm namens **Hello World**, das den Text `Hello World!` auf der Standardausgabe des Geräts, normalerweise dem Bildschirm, ausgibt. In Java können wir dieses Programm wie folgt schreiben:

```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```

In diesem Programm haben wir eine Klasse namens `Hello`. Klassen in objektorientierten Systemen helfen dabei, Konzepte aus dem untersuchten Anwendungsbereich zu modellieren. Klassen kapseln sowohl die Daten als auch das Verhalten, die mit einem bestimmten Konzept verbunden sind.

Die Klasse `Hello` besitzt eine einzige Methode namens `main`, die ein Array von Zeichenketten mit den beim Ausführen des Programms übergebenen Kommandozeilenargumenten erhält, sofern vorhanden. In diesem Beispiel werden diese Argumente nicht verwendet.

Die Methode `main` ist statisch, was bedeutet, dass sie eine Klassenmethode und keine Instanzmethode ist. Daher kann sie aufgerufen werden, ohne ein Objekt der Klasse `Hello` zu erzeugen.

Innerhalb der Methode `main` erfolgt ein Aufruf der Methode `println`. Diese Methode gehört zur Klasse `PrintStream` und gibt den als Argument übergebenen Wert auf dem Bildschirm aus, gefolgt von einem Zeilenabschluss.

Die Methode `println` wird über das Feld `out` der Klasse `System` aufgerufen. Dieses Feld hat den Typ `PrintStream` und ermöglicht den Zugriff auf die Standardausgabe des Systems.

## Kompilierung und Ausführung

Java-Programme werden zunächst in eine Zwischenrepräsentation namens **Bytecode** kompiliert, die die Portabilität gewährleistet. Diese Bytecodes werden anschließend von einer Java Virtual Machine (JVM) ausgeführt, die sie in für die zugrunde liegende Plattform geeigneten Maschinencode umwandelt.

Um das Programm zu kompilieren, muss es in einer Datei namens `Hello.java` gespeichert werden. In Java haben Dateien, die öffentliche Typen enthalten, normalerweise denselben Namen wie der Typ.

Wir können eine integrierte Entwicklungsumgebung (**IDE**) verwenden oder den Compiler direkt über die Kommandozeile aufrufen, sofern ein JDK installiert ist.

Java-Programme werden normalerweise in einer IDE geschrieben. Sie bietet Funktionen, die die Produktivität während der Entwicklung erhöhen, beispielsweise Quellcode-Navigation, Refactoring, statische Analyse, Kompilierung, Tests und Debugging.

Einige der beliebtesten IDEs für Java sind:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

Wir können das Programm auch direkt über die Kommandozeile mit dem Compiler `javac` kompilieren:

```text
    javac Hello.java
```

Der Befehl nimmt `Hello.java` als Eingabe und erzeugt die Datei `Hello.class`, die die kompilierte Version des Programms enthält.

Nach der Kompilierung können wir das Programm mit dem Befehl `java` ausführen:

```text
    java Hello
```

Die Ausgabe lautet:

```text
    Hello World!
```

## Ein einfacherer Ansatz mit Java 25+

Ab Java 25 wurde eine Funktion, die seit Java 21 als *Preview* entwickelt worden war, endgültig Bestandteil der Sprache: **Compact Source Files and Instance Main Methods**. Sie ermöglicht es, kleine Programme mit weniger Boilerplate zu schreiben, indem die explizite Klassendeklaration weggelassen und die `main`-Methode vereinfacht wird.

Daher kann das vorherige Programm in Java 26 (der aktuellen Version) nun wie folgt geschrieben werden:

```java
    void main() {
        IO.println("Hello World!");
    }
```

In diesem Fall müssen wir weder die Klasse explizit deklarieren noch `public static void main(String[] args)` schreiben. Der Compiler behandelt die Datei so, als würde sie implizit eine Klasse deklarieren, und die `main`-Methode kann eine Instanzmethode sein.

Wir können auch die `IO`-Klasse verwenden, die einfache Konsolen-Ein- und Ausgabeoperationen bereitstellt. In Java 26 gehört `IO` zum Paket `java.lang` und ist daher implizit verfügbar. Um ihre Methoden aufzurufen, müssen wir jedoch den Klassennamen verwenden, wie bei `IO.println(...)`.

Da diese Funktion nicht mehr den Status *Preview* besitzt, benötigen wir keine besonderen Kompilierungsoptionen. Das Programm kann normal kompiliert werden:

```text
    javac Hello.java
```

und auf dieselbe Weise ausgeführt werden:

```text
    java Hello
```

Es ist auch möglich, eine Quelldatei direkt mit dem `java`-Launcher auszuführen:

```text
    java Hello.java
```

In diesem Fall wird der Quellcode vom Launcher vor der Ausführung im Speicher kompiliert. Dadurch können Programme direkt aus Quelldateien ausgeführt werden, ohne explizit eine `.class`-Datei zu erzeugen.

Die Verwendung kompakter Quelldateien ist besonders für kleine Beispiele, Lernprogramme, Skripte und Experimente interessant. Wenn das Programm wächst und eine umfangreichere Struktur benötigt, können wir natürlich zur traditionellen Form mit expliziten Klassen- und Methodendeklarationen zurückkehren.

Der von IDEs ausgeführte Prozess ist im Wesentlichen ähnlich. Neben Kompilierung und Ausführung bieten sie Funktionen zum Debuggen, Testen, Refactoring, Erstellen und Verwalten von Projekten, Erstellen von Bibliotheken, Versionsverwaltung und viele weitere Aufgaben.

---

*Dieser Artikel ist eine Adaption von Inhalten aus dem Buch <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> von <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
