---
layout: post
title: "Cancellazione dei tipi e raw type in Java"
date: 2026-11-20
lang: it
translation_id: apagamento-tipos-crus-java
permalink: /it/type-erasure-and-raw-types-in-java/
share_text: >-
  La cancellazione sostiene la compatibilità; i raw type perdono il controllo degli elementi.
---

Java 5 ha introdotto i generici preservando la compatibilità con il codice precedente. Con la **cancellazione dei tipi** (*type erasure*), il compilatore controlla i parametri generici e li rimuove dalla rappresentazione eseguita dalla JVM. Li sostituisce con i loro limiti, di solito `Object` o il primo limite dichiarato.

Dopo la cancellazione, `Adapter<T>` assomiglia approssimativamente a una classe che usa `Object`:

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

Un client senza parametri di tipo avrebbe questa forma:

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

Questi frammenti **illustrano** il processo, senza trascrivere letteralmente il bytecode. Gli argomenti di tipo non sono disponibili a runtime nello stesso modo che durante la compilazione; alcune operazioni di riflessione risultano limitate.

## Raw type

Una lista parametrizzata verifica il tipo dei propri elementi:

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

Un *raw type* omette l'argomento di tipo sia nella dichiarazione sia nella costruzione:

```java
void main(){
    List names = new ArrayList();
}
```

Così si perde il controllo offerto da `List<String>` e la lista ammette una stringa e un intero:

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>` indica una lista di tipo **sconosciuto**, nella quale non si possono inserire elementi arbitrari, tranne `null`. Una `List` raw li accetta senza controllo del tipo. Nel codice nuovo, usate un argomento di tipo o un wildcard; riservate i raw type all'interazione con codice precedente.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
