---
layout: post
title: "Polimorfizm w Javie"
date: 2026-10-21
lang: pl
translation_id: polimorfismo-em-java
permalink: /polymorphism-in-java-pl/
share_text: >-
  Wprowadzenie do polimorfizmu ad hoc, parametrycznego i podtypów z przykładami w Javie.
---

W programowaniu obiektowym **polimorfizm** oznacza zdolność operacji do różnego działania w zależności od klasy obiektu. Główne formy to:

- **Polimorfizm ad hoc (lub przeciążanie)**: metody o tej samej nazwie mogą przyjmować różne parametry, a wywołanie wybiera wersję pasującą do argumentów.
- **Polimorfizm parametryczny**: klasy i metody generyczne działają z typami określanymi w chwili użycia.
- **Polimorfizm podtypów**: podklasa może nadpisać metodę, a wykonywana implementacja zależy od konkretnej klasy obiektu.

Poniższe przykłady pokazują te trzy formy w Javie, zaczynając od przeciążania. Klasa `Figure` ma dwie przeciążone metody o nazwie `resize`. Pierwsza przyjmuje `percentage` typu `Double`, a druga współrzędne `x` i `y` typu `Integer`.

```java
public class Figure {
    public void resize(Double percentage) {
        // Zmiana rozmiaru o wartość procentową
    }
    public void resize(Integer x, Integer y) {
        // Zmiana rozmiaru według współrzędnych
    }
}
```

W **polimorfizmie parametrycznym** typy parametryzowane tworzy się za pomocą `<` i `>`. Klasa `ArrayList` ma na przykład parametr typu `E`, który określa typ obiektów przechowywanych na liście. Ten parametr jest również parametrem formalnym metody `add`. Typ oczekiwany przez `add` jest więc taki sam jak typ podany przy tworzeniu `ArrayList`. Zwróć uwagę, że klasa rozszerza `AbstractList` i implementuje między innymi interfejsy `List`, `RandomAccess`, `Cloneable` i `Serializable`, używając tego samego typu `E`.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // Implementacja add
    }
    // Inne metody i pola klasy
}
```

Możemy na przykład utworzyć listę tekstów z parametrem typu `String` i dodawać elementy za pomocą `add`[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

W tym przypadku kompilator oczekuje, że argument przekazany do `add` będzie typu `String`. Przekazanie obiektu innego typu powoduje błąd kompilacji. Jeśli chcemy listę liczb całkowitych, możemy podać `ArrayList` inny typ, w tym przypadku `Integer`:

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

W **polimorfizmie podtypów** załóżmy, że klasa `Figure` ma metodę `draw`, którą można wywoływać także na obiektach klas `Triangle`, `Circle` i `Rectangle`. Każda z tych klas nadpisuje metodę, aby zaimplementować własny sposób rysowania. W poniższym kodzie każde wywołanie `draw` uruchamia inną implementację, zależnie od tego, czy do `figure` przypisano `Circle`, `Triangle`, czy `Rectangle`.

```java
Figure figure = new Circle(10);
// Wywołuje draw z klasy Circle
figure.draw();
figure = new Triangle(20);
// Wywołuje draw z klasy Triangle
figure.draw();
figure = new Rectangle(10, 20);
// Wywołuje draw z klasy Rectangle
figure.draw();
```

[^8]: Aby używać `ArrayList`, zwykle trzeba ją zaimportować przez `import java.util.ArrayList;`. Importy nie są potrzebne w kompaktowych plikach źródłowych. W zwykłych plikach można zaimportować moduł `java.base` za pomocą `import module java.base;`.

---

*Ten artykuł adaptuje treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kesslera Pivety</a>.*

## Powiązane artykuły

- [Podstawowe pojęcia programowania obiektowego](/oop-basics-java-pl/)
- [Klasy w Javie](/klasy-w-java-pl/)
- [Dziedziczenie w Javie](/dziedziczenie-w-java-pl/)
- [Interfejsy w Javie](/interfaces-in-java-pl/)
- [Linki o OOP i Javie](/oop-java-links-pl/)
- [Ćwiczenia z programowania obiektowego](/oop-exercises-pl/)
