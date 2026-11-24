---
layout: post
title: "Typlöschung und Raw Types in Java"
date: 2026-11-20
lang: de
translation_id: apagamento-tipos-crus-java
permalink: /de/type-erasure-and-raw-types-in-java/
share_text: >-
  Typlöschung ermöglicht Kompatibilität mit altem Code; Raw Types verlieren die Prüfung der Elementtypen.
---

Java 5 führte Generics unter Wahrung der Abwärtskompatibilität ein. Bei der **Typlöschung** (*type erasure*) prüft der Compiler die Typparameter und entfernt sie anschließend aus der von der JVM ausgeführten Darstellung. An ihre Stelle treten die Schranken, meist `Object` oder die erste angegebene Schranke.

Nach der Löschung ähnelt `Adapter<T>` näherungsweise einer Klasse mit `Object`:

```java
public class Adapter{
    Object object;
    public Object get(){
        return object;
    }
    public void set(Object value){
        object = value;
    }
    public Adapter(Object initial){
        object = initial;
    }
}
```

Ein Client ohne Typparameter sähe so aus:

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

Diese Fragmente **veranschaulichen** den Vorgang und sind keine wörtliche Bytecode-Darstellung. Zur Laufzeit stehen generische Typargumente nicht in derselben Weise wie beim Kompilieren zur Verfügung; das schränkt bestimmte Reflexionsoperationen ein.

## Raw Types

Eine parametrisierte Liste prüft den Elementtyp:

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

Ein *Raw Type* lässt das Typargument sowohl bei der Deklaration als auch beim Erzeugen weg:

```java
void main(){
    List names = new ArrayList();
}
```

Damit entfällt die Prüfung von `List<String>`; die Liste kann Zeichenkette und Ganzzahl enthalten:

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>` ist eine Liste eines **unbekannten Typs**, der man außer `null` keine beliebigen Elemente hinzufügen kann. Eine rohe `List` nimmt Elemente ohne diese Prüfung an. Neuer Code sollte konkrete Typargumente oder Wildcards verwenden; Raw Types dienen vor allem der Zusammenarbeit mit altem Code.

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
