---
layout: post
title: "Grundlagen der objektorientierten Programmierung"
date: 2026-10-21
lang: de
translation_id: conceitos-basicos-poo-java
permalink: /grundlagen-objektorientierte-programmierung-de/
share_text: >-
  Einführung in die Grundlagen der objektorientierten Programmierung: Klassen, Objekte, Attribute, Methoden, Kapselung, Vererbung, Polymorphie und Beziehungen zwischen Klassen.
---

Die strukturierte Programmierung bietet Mechanismen, um die Konzepte eines Softwaresystems durch Datenstrukturen und die sie verarbeitenden Algorithmen zu modularisieren. Gängige strukturierte Programmiersprachen können unterschiedliche Datentypen und Variablen darstellen, um Eigenschaften und Merkmale der relevanten Konzepte auszudrücken. Verfahren und Funktionen modellieren die zugehörigen Operationen.

Bei der Wiederverwendung von Komponenten aus strukturierten Sprachen muss man jedoch die Beziehung zwischen den Daten — dargestellt durch Datenstrukturen, Datentypen und Variablen — und dem Verhalten — ausgedrückt durch Verfahren und Funktionen — ermitteln. Daher findet Wiederverwendung oft auf einer feingranularen Ebene statt und kann beträchtlichen Aufwand erfordern, etwa um herauszufinden, welche Verfahren und Funktionen zu welchen Datenstrukturen gehören. Wiederverwendbare Bibliotheken lassen sich zwar erstellen, doch die Beziehung zwischen Daten und Verhalten ist nicht explizit und nicht in einer einzigen Abstraktion zusammengefasst.

Die **objektorientierte Programmierung** (OOP) ist ein Programmierparadigma, das Konzepte einer Anwendungsdomäne durch abstrakte Datentypen namens Klassen darstellt. Diese Klassen modellieren sowohl die Eigenschaften und Merkmale der Konzepte als auch ihre Operationen. OOP erweitert die strukturierte Programmierung um Möglichkeiten, Klassen zu spezifizieren und zu kombinieren, um vollständige Computersysteme zu modellieren. Dabei soll eine größere Modularität und Wiederverwendung von Komponenten erreicht werden.

Heute gehört die objektorientierte Programmierung zu den am weitesten verbreiteten und akzeptierten Paradigmen der Softwareentwicklung. Viele moderne Sprachen unterstützen sie, darunter Java, C++, C#, Python, Kotlin, JavaScript, TypeScript, Swift und Ruby.

Eine **Klasse** ist ein Abstraktionsmechanismus zur Darstellung von Konzepten einer Anwendungsdomäne. In einer Bankdomäne gehören dazu beispielsweise Filialen, Konten, Kunden und Transaktionen. Wir könnten Klassen wie `Branch`, `Account`, `Customer` und `Transaction` definieren, um diese Konzepte abzubilden. Die Abbildung zeigt eine grafische Darstellung dieser Klassen.

<img src="/images/en/oopClasses.svg" alt="Die Klassen Branch, Account, Customer und Transaction." style="max-width: 300px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Klassen dienen als *Vorlagen*, um konkrete, manipulierbare Exemplare dieser Konzepte zu erzeugen. Solche Exemplare heißen **Objekte**. Ein Objekt ist eine **Instanz** einer Klasse; der Vorgang, Objekte zu erzeugen, heißt **Instanziierung**. Beispielsweise könnten wir Objekte für die Kunden *John*, *Peter* und *Mary* erzeugen, einschließlich ihrer persönlichen Daten und der für Kunden verfügbaren Funktionen.

<img src="/images/en/oopObjects.svg" alt="Die Objekte John, Peter und Mary sind Instanzen der Klasse Customer." style="max-width: 380px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Eine Klasse wird so definiert, dass sie Eigenschaften und Verhalten eines Konzepts darstellt. Die wichtigsten Mechanismen dafür sind Attribute und Methoden.

**Attribute** stellen Eigenschaften von Objekten einer Klasse dar. Zu den Attributen einer Klasse `Customer` könnten *name*, *age*, *address* und *marital status* gehören. Jede konkrete Kundeninstanz kann unterschiedliche Werte für diese Attribute haben. Ein Kundenobjekt könnte zum Beispiel folgende Werte besitzen: *name* $`=`$ John Smith, *age* $`=`$ 50, *address* $`=`$ 205 President Vargas Street und *marital status* $`=`$ married.

**Methoden** stellen Verhalten dar. Mögliche Methoden einer Klasse `Account` beziehen sich etwa auf das *Eröffnen*, *Schließen* oder *Ändern des Kontoinhabers*. Wird eine Methode **aufgerufen** (oder **invokiert**), wird die darin implementierte Operation ausgeführt. Klassen besitzen häufig spezielle Methoden zum Erzeugen (Instanziieren) von Objekten, sogenannte **Konstruktoren**, und zum Zerstören von Objekten, sogenannte **Destruktoren**.

Attribute und Methoden lassen sich außerdem in Instanz- und Klassenmitglieder unterteilen. **Instanzattribute und -methoden** werden am häufigsten verwendet und über Objekte der Klasse angesprochen. Sie beschreiben Eigenschaften und Operationen einzelner Instanzen. Instanzattribute einer Klasse `Account` wären etwa *bank*, *branch*, *account number* und *account holder*. Instanzmethoden führen Operationen für ein bestimmtes Konto aus, etwa *withdraw*, *transfer* und *deposit*. **Klassenattribute und -methoden** gehören hingegen zur Klasse selbst, nicht zu ihren Instanzen. Ein Klassenattribut könnte beispielsweise zählen, wie viele `Account`-Instanzen erzeugt wurden; eine Klassenmethode könnte diesen Wert zurückgeben.

Um den Zugriff auf Attribute und Methoden einzuschränken, bieten Klassen Mechanismen zur **Kapselung und Informationsverbergung**. Programmiersprachen stellen üblicherweise Sichtbarkeitsmodifizierer bereit, die festlegen, wer auf ein Attribut, eine Methode oder eine Klasse zugreifen darf.

Klassen abstrahieren und kapseln Konzepte aus der realen und der computerbasierten Welt. Diese Abstraktionen können durch Beziehungen kombiniert werden, damit Klassen gemeinsam die Anforderungen einer Anwendung erfüllen. Zu den wichtigsten Beziehungen zählen Vererbung, Assoziation, Aggregation, Komposition und Realisierung.

**Vererbung** ist ein Kompositionsmechanismus, mit dem Klassen die Schnittstelle und das Verhalten bestehender Klassen wiederverwenden und deren Funktionalität erweitern können. Eine Klasse, die eine andere erweitert, heißt **Unterklasse**; die erweiterte Klasse heißt **Oberklasse**. Üblicherweise wird die Erweiterung in der Unterklasse angegeben, etwa: `SubClass` erweitert `SuperClass`.

Abbildung 3 zeigt die Klassen `Shape`, `Rectangle`, `Triangle` und `Circle`. `Shape` ist die Oberklasse; `Rectangle`, `Triangle` und `Circle` sind ihre Unterklassen.

<img src="/images/en/oopInheritance.png" alt="Shape ist die Oberklasse von Rectangle, Triangle und Circle." style="max-width: 400px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Vererbungsmechanismen unterscheiden sich je nach Programmiersprache. Unterschiede betreffen häufig Sichtbarkeit und Mehrfachvererbung. In Sprachen wie C++ kann die **Sichtbarkeit der Vererbung** als **öffentlich** oder **privat** festgelegt werden. Betrachten wir eine Klasse `A` und eine Klasse `B`, die von `A` erbt. Dann ist `A` eine Oberklasse von `B` und `B` eine Unterklasse von `A`. Bei öffentlicher Vererbung ist `B` ein Subtyp von `A` und erbt sowohl deren Implementierung als auch ihre Schnittstelle. Überall dort, wo ein Objekt der Klasse `A` erwartet wird, kann daher ein Objekt der Klasse `B` (oder einer anderen Unterklasse von `A`) verwendet werden, denn jede Instanz von `B` gilt auch als Instanz von `A`. Dieses Prinzip heißt **Liskovsches Substitutionsprinzip**. Bei privater Vererbung ist `B` kein `A`; sie erbt lediglich die Implementierung von `A` und wird auf Basis von `A` implementiert. Das Liskovsche Substitutionsprinzip gilt hier nicht.

Vererbung kann außerdem **einfach oder mehrfach** sein. Bei einfacher Vererbung, wie sie Java und C# verwenden, darf eine Klasse nur eine Oberklasse haben. Bei Mehrfachvererbung, wie in C++, kann eine Klasse mehrere Oberklassen besitzen. Sprachdesigner sind sich nicht einig, ob die Vorteile der Mehrfachvererbung die damit verbundenen Probleme aufwiegen. Andere Sprachen bieten Alternativen wie virtuelle Vererbung auf Grundlage von Schnittstellen, *Traits* und *Mixins*.

Abbildung 4 zeigt Mehrfachvererbung. `Mammal` und `Bird` stehen für Tiere. `Horse`, `Dog` und `Bat` sind Unterklassen von `Mammal`; `Ostrich` und `Duck` sind Unterklassen von `Bird`. Zusätzlich wollen wir flugfähige Tiere klassifizieren. Dazu definieren wir `Flyer` für fliegende Objekte, die nicht unbedingt Tiere sein müssen. Mit Mehrfachvererbung können sowohl Objekte von `Duck` als auch von `Bat` zugleich fliegende Objekte sein, indem sie von `Flyer` erben.

<img src="/images/en/oopMultipleInheritance.png" alt="Mehrfachvererbung zwischen den Klassen Animal, Bird, Flyer und Mammal." style="max-width: 500px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Manche Klassen sind **abstrakt**. Wie **konkrete** Klassen stellen sie Eigenschaften und Verhalten einer Gruppe realer Objekte dar, können aber nicht direkt instanziiert werden. Im Mehrfachvererbungsbeispiel könnten `Mammal`, `Bird` und `Flyer` abstrakte Klassen sein, da es in der realen Welt nur Exemplare ihrer Unterklassen gibt, etwa Pferde, Hunde und Enten.

Neben Sichtbarkeit und Multiplizität ermöglicht Vererbung auch polymorphe Methoden. In der objektorientierten Programmierung ist **Polymorphie** die Fähigkeit einer Operation, sich je nach Klasse des aufrufenden Objekts unterschiedlich zu verhalten. Die wichtigsten Formen sind:

- **Ad-hoc-Polymorphie (oder Überladen)** tritt auf, wenn Methoden einer Klasse denselben Namen, aber unterschiedliche formale Parametertypen besitzen. Der Aufruf wählt eine Methode anhand des verwendeten Arguments aus.
- **Parametrische Polymorphie** entsteht, wenn eine Methode generisch definiert wird und an einen Typ gebunden ist, der erst später festgelegt wird, etwa bei der Deklaration einer Variablen oder der Instanziierung eines Objekts. In objektorientierten Sprachen heißen solche Typen generische Typen.
- **Subtyp-Polymorphie** entsteht, wenn Unterklassen Methoden einer Oberklasse überschreiben. Das aufrufende Objekt bestimmt, welche Methode ausgeführt wird. Üblicherweise erfolgt dies zur Laufzeit durch dynamische Bindung.

Neben Vererbung gibt es weitere Beziehungen, darunter Assoziation, Aggregation und Komposition. Im Allgemeinen unterscheiden sie sich durch den Grad der Kopplung ihrer Beteiligten:

- Bei einer **Assoziation** ist die Beziehung zwischen Objekten meist vorübergehend und kann zur Laufzeit leicht geändert werden. In einem Verkehrsszenario kann etwa eine Person als Fahrerin einem Fahrzeug zugeordnet sein. Ändert sich die Fahrerin, bestehen beide Objekte unabhängig voneinander weiter.
- Bei einer **Aggregation** ist die Beziehung stärker als bei einer Assoziation. Die aggregierten Objekte werden häufig zusammen mit dem aggregierenden Objekt erzeugt. Ein Auto kann beispielsweise vier Räder besitzen: Das Auto ist das aggregierende Objekt, die Räder sind die aggregierten Objekte. Die Beziehung kann zwar aufgelöst werden, aber ein Radwechsel ist aufwendiger und seltener als ein Fahrerwechsel.
- Bei einer **Komposition** ist die Beziehung noch stärker. Die zusammengesetzten Objekte sind Bestandteile eines größeren Objekts. So besteht etwa der Stoff eines Fahrzeugsitzes aus Fäden. Wenn die Fäden nicht mehr existieren, existiert auch der Sitz nicht mehr oder verliert zumindest seine Identität.

Diese Objektbeziehungen sind oft konzeptioneller Natur. Bei der Umsetzung in einer Programmiersprache verknüpfen wir Objekte zum Beispiel über Klassenattribute und weisen diesen zur Laufzeit Werte zu. Manchmal unterscheidet sich der Zeitpunkt der Objekterzeugung: Bei einer Komposition werden die Teile meist im Konstruktor des Ganzen erzeugt; bei einer Assoziation entstehen die Objekte üblicherweise unabhängig voneinander und werden bei Bedarf verknüpft.

Eine letzte Beziehung, die **Realisierung**, liegt vor, wenn eine Klasse erklärt, eine Schnittstelle zu implementieren. Eine **Schnittstelle** kann als abstrakte Klasse verstanden werden, deren Methoden alle abstrakt sind[^1]. Sie dient als Protokoll zwischen den Clients und den Implementierungen. Die Klasse (oder eine ihrer Unterklassen) muss die deklarierten Methoden implementieren. Dadurch können Clients Code schreiben, der der Schnittstelle entspricht, ohne wissen zu müssen, wie die implementierenden Klassen diese umsetzen.

[^1]: Seit Java 8 können Schnittstellen auch konkrete Methoden enthalten, sogenannte Standardmethoden, die mit dem Schlüsselwort `default` deklariert werden. Klassen, die eine Schnittstelle mit einer Standardmethode implementieren, müssen diese Methode nicht selbst implementieren, können es aber tun.

---

*Dieser Artikel adaptiert Inhalte aus dem Buch <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> von <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Verwandte Artikel

- [Klassen in Java](/klassen-in-java-de/)
- [Vererbung in Java](/vererbung-in-java-de/)
- [Polymorphie in Java](/polymorphie-in-java-de/)
- [Schnittstellen in Java](/schnittstellen-in-java-de/)
- [Links zu OOP und Java](/oop-java-links-de/)
- [Übungen zur objektorientierten Programmierung](/oop-uebungen-de/)
