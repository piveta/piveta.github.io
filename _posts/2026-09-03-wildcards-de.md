---
layout: post
title: "Wildcards und Grenzen bei generischen Typen in Java"
date: 2026-09-03
lang: de
translation_id: wildcards-limites-java
permalink: /wildcards-und-grenzen-generische-typen-java/
share_text: >-
  In Java-Generics steht <?> für einen unbekannten Typ; <? extends T> und <? super T> legen obere beziehungsweise untere Grenzen fest. Der Beitrag zeigt, wie diese Wildcards generische Typen flexibel beschränken.
---

Neben spezifischen generischen Typen können wir **Wildcards** verwenden, um unbekannte Typen (`<?>`) auszudrücken, den angegebenen Typ auf Untertypen eines bestimmten Typs zu beschränken (`<? extends Type>`) oder Supertypen einzubeziehen (mit `<? super Type>`). In den folgenden Abschnitten beschreiben wir unbeschränkte, obergrenzenbeschränkte und untergrenzenbeschränkte Wildcards. Anschließend zeigen wir, wie wir mehrere Grenzen für generische Typen definieren können.

## Unbeschränkte Wildcards

Für unbekannte Typen verwenden wir das Fragezeichen als Typ, sodass jeder Typ in diesem Kontext verwendet werden kann. Wenn beispielsweise eine Variable als `List<?>` (oder ein Attribut oder Parameter) deklariert ist, kann sie `List`-Objekte mit jedem gültigen Typparameter aufnehmen, etwa `String`, `Integer` usw. Solche unbekannten generischen Typen werden **unbeschränkte Wildcards** (`<?>`) genannt, da sie keine Typgrenze vorgeben.

Zum Beispiel:

```java
List<?> l = new ArrayList<String>();
// oder beispielsweise
l = new LinkedList<Integer>();
```

Obwohl diese Art der Variablendeklaration attraktiv erscheinen mag, gibt es Einschränkungen. In solchen Fällen kennen wir den Typ der Objekte in der Liste nicht. Daher können wir beispielsweise keine Elemente zur Liste hinzufügen (außer `null`, das mit jedem Referenztyp in Java kompatibel ist), da nicht garantiert ist, dass das hinzuzufügende Objekt denselben Typ wie der Typparameter der Liste hat.

Wenn wir versuchen, ein Element zur Liste (in diesem Fall `l`) hinzuzufügen, erhalten wir daher einen Fehler zur Compile-Zeit:

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

Unbeschränkte Typen werden häufig verwendet, wenn wir Daten nur lesen und nicht verändern möchten. Wir könnten beispielsweise eine Methode definieren, die eine Liste entgegennimmt und ihre Elemente ausgibt, ohne den Typ der Listenelemente anzugeben:

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

Die Ausführung der Methode `main` würde Folgendes anzeigen:

```text
1
2
3
A
B
C
```

Hier verwenden wir die Ausgabe als Beispiel, aber wir könnten die Objekte auch durchlaufen, in *Streams* verwenden, mit `instanceof` filtern, die Größe der Liste ermitteln, prüfen, ob ein bestimmtes Objekt enthalten ist, sie in eine typisierte Liste transformieren und kopieren und vieles mehr. Was wir nicht tun können, ist die Liste direkt zu verändern (beispielsweise mit `add` oder `set`, außer mit `null`).

## Wildcards mit Obergrenze

**Wildcards mit Obergrenze** erlauben anzugeben, dass nur ein Objekt eines bestimmten Typs oder eines seiner Untertypen (durch Vererbung oder Implementierung eines Interfaces) als Typparameter verwendet werden kann. Die Notation `<? extends T>` gibt an, dass die Wildcard den Typ `T` oder einen Typ haben muss, der von `T` erbt.

Wenn wir beispielsweise eine Liste deklarieren, deren Wildcard `Number` erweitert, können wir Objekte beliebiger Unterklassen zuweisen (etwa `Double` oder `Integer`). Wäre `Number` eine konkrete Klasse (sie ist abstrakt), könnten wir auch ein Objekt dieser Klasse selbst zuweisen. Das folgende Beispiel zeigt dies:

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

Wie bei unbeschränkten Wildcards können wir keine Elemente zur Liste `l` hinzufügen, da wir den genauen Typ der Liste nicht kennen. Daher erzeugen die ersten beiden Aufrufe von `add` Compile-Fehler:

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

Obwohl wir beim Lesen des Codes wissen, dass das der Variablen `l` zugewiesene Objekt eine Liste von Ganzzahlen ist, weiß der Compiler nur, dass `l` einen unbekannten Typ hat, und erlaubt daher das Hinzufügen von Werten nicht. Beim Lesen werden die Werte als `Number` gelesen, da dies die Obergrenze ist.

## Wildcards mit Untergrenze

**Wildcards mit Untergrenze** erlauben anzugeben, dass nur ein Objekt eines bestimmten Typs oder eines seiner Supertypen als Typparameter verwendet werden kann. Die Notation `<? super T>` gibt an, dass die Wildcard den Typ `T` oder eine Oberklasse von `T` haben muss.

Wenn wir beispielsweise eine Liste deklarieren, deren Wildcard `Number` als Untergrenze hat, können wir Objekte beliebiger Oberklassen zuweisen (im Fall von `Number` nur `Object`, da `Number` keine explizite Oberklasse hat).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

Es ist erlaubt, Elemente des Typs der Untergrenze (`Number`) oder eines seiner Untertypen hinzuzufügen (beispielsweise `Double` oder `Integer`). Das folgende Beispiel zeigt eine Liste, deren Wildcard `Number` als Untergrenze hat. In diesem Fall können wir eine `ArrayList` von Zahlen (oder ihrer Oberklasse `Object`) instanziieren. Wir können Elemente einer ihrer Unterklassen hinzufügen (ein Objekt vom Typ `Number` selbst können wir nicht hinzufügen, da es eine abstrakte Klasse ist und keine direkten Instanzen haben kann). Das Beispiel zeigt drei Elemente. Die ersten beiden sind erlaubt, weil sie Untertypen von `Number` sind (`10` ist ein `Integer` und `1.0` ein `Double`). Das dritte Hinzufügen ist nicht erlaubt und führt zu einem Compile-Fehler, weil `Object` kein Nachkomme von `Number` ist.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

Wenn wir die `ArrayList` mit `Object` als Typparameter erzeugen würden, wäre das dritte Hinzufügen zur Compile-Zeit weiterhin nicht erlaubt und würde denselben Fehler erzeugen (die ersten beiden Hinzufügungen blieben erlaubt), weil der Typ der Liste weiterhin unbekannt ist (wir wissen nur, dass er `Number` oder einer seiner Supertypen entspricht).

## Mehrere Grenzen

In Java kann ein generischer Typ **mehrere Grenzen** haben. Das bedeutet, dass der Typparameter nur Typen akzeptieren darf, die eine bestimmte Klasse erweitern (oder diese selbst sind) und ein oder mehrere Interfaces implementieren. Die Syntax hat die Form `<T extends Class & Interface1 & Interface2>`. Wenn eine Klasse als Grenze verwendet wird, muss sie zuerst angegeben werden, gefolgt von den Interfaces. Wenn keine Klasse verwendet wird, können nur Interfaces aufgelistet werden.

Beispielsweise besitzt die Klasse `MultipleBounds` den generischen Typ `T`, der die Klasse `Number` erweitert und die Interfaces `Comparable<T>` und `Serializable` implementiert:

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

In diesem Beispiel kann `T` nur `Number` oder ein Typ sein, der von `Number` erbt und außerdem `Comparable<T>` und `Serializable` implementiert. Dies ist nützlich, wenn wir mehrere Garantien benötigen, beispielsweise Zugriff auf Methoden der Oberklasse und Verträge, die durch mehrere Interfaces definiert werden. Diese Kombination macht den Code flexibler und bleibt dabei typsicher, wodurch Compile-Fehler vermieden und sichergestellt wird, dass alle für den verwendeten generischen Typ erforderlichen Methoden verfügbar sind.

---

*Dieser Artikel ist aus Inhalten des Buches <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> von <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a> adaptiert.*
