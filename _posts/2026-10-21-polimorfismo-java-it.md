---
layout: post
title: "Polimorfismo in Java"
date: 2026-10-21
lang: it
translation_id: polimorfismo-em-java
permalink: /polimorfismo-java-it/
share_text: >-
  Introduzione al polimorfismo ad hoc, parametrico e di sottotipo, con esempi in Java.
---

Nella programmazione orientata agli oggetti, il **polimorfismo** è la capacità di un’operazione di comportarsi in modo diverso in base alla classe dell’oggetto coinvolto. Le forme principali sono:

- **Polimorfismo ad hoc (o overload)**: metodi con lo stesso nome possono avere parametri diversi; la chiamata sceglie la versione compatibile in base agli argomenti.
- **Polimorfismo parametrico**: classi e metodi generici lavorano con tipi specificati al momento dell’utilizzo.
- **Polimorfismo di sottotipo**: una sottoclasse può ridefinire un metodo e l’implementazione eseguita dipende dalla classe concreta dell’oggetto.

Gli esempi seguenti mostrano le tre forme in Java, iniziando dall’overload. La classe `Figure` ha due metodi omonimi `resize`. Il primo riceve un `percentage` di tipo `Double`; il secondo riceve le coordinate `x` e `y` di tipo `Integer`.

```java
public class Figure {
    public void resize(Double percentage) {
        // Ridimensionamento in base alla percentuale
    }
    public void resize(Integer x, Integer y) {
        // Ridimensionamento in base alle coordinate
    }
}
```

Per il **polimorfismo parametrico**, possiamo creare tipi parametrizzati usando `<` e `>`. La classe `ArrayList`, per esempio, ha un parametro di tipo `E` che specifica il tipo di oggetti memorizzabili nell’elenco. Lo stesso parametro è usato come parametro formale del metodo `add`. Il tipo atteso da `add` è quindi quello indicato quando si crea l’`ArrayList`. Si noti che `ArrayList` estende `AbstractList` e implementa, tra le altre, le interfacce `List`, `RandomAccess`, `Cloneable` e `Serializable`, usando lo stesso tipo `E`.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // Implementazione di add
    }
    // Altri metodi e campi della classe
}
```

Per esempio, possiamo creare un elenco di stringhe con il parametro di tipo `String` e inserirvi elementi chiamando `add`[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

In questo caso, il compilatore si aspetta che l’argomento passato a `add` sia un `String`. Passare un oggetto di un altro tipo provoca un errore di compilazione. Per un elenco di interi, possiamo passare ad `ArrayList` un altro tipo, in questo caso `Integer`:

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

Per il **polimorfismo di sottotipo**, supponiamo che `Figure` abbia un metodo `draw`, invocabile anche su oggetti delle classi `Triangle`, `Circle` e `Rectangle`. Ciascuna di queste classi ridefinisce il metodo per realizzare il proprio comportamento di disegno. Nel codice seguente, ogni chiamata a `draw` invoca un’implementazione diversa in base alla classe dell’oggetto assegnato a `figure`: `Circle`, `Triangle` o `Rectangle`.

```java
Figure figure = new Circle(10);
// Invoca il metodo draw di Circle
figure.draw();
figure = new Triangle(20);
// Invoca il metodo draw di Triangle
figure.draw();
figure = new Rectangle(10, 20);
// Invoca il metodo draw di Rectangle
figure.draw();
```

[^8]: Per usare `ArrayList`, normalmente occorre importarla con `import java.util.ArrayList;`. I file sorgente compatti non richiedono import. Nei file sorgente regolari, è possibile importare il modulo `java.base` con `import module java.base;`.

---

*Questo articolo adatta contenuti del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> di <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articoli correlati

- [Concetti fondamentali della programmazione orientata agli oggetti](/concetti-fondamentali-oop-it/)
- [Classi in Java](/classi-java-it/)
- [Ereditarietà in Java](/ereditarieta-java-it/)
- [Interfacce in Java](/interfacce-java-it/)
- [Link su OOP e Java](/link-oop-java-it/)
- [Esercizi di programmazione orientata agli oggetti](/esercizi-oop-it/)
