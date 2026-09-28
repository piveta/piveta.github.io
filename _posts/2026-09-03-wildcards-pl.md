---
layout: post
title: "Wildcardy i ograniczenia w typach generycznych w Javie"
date: 2026-09-03
lang: pl
translation_id: wildcards-limites-java
permalink: /wildcardy-ograniczenia-typy-generyczne-java/
---

Oprócz konkretnych typów generycznych możemy używać **wildcardów**, aby wyrażać nieznane typy (`<?>`), ograniczać określony typ do podtypów danego typu (`<? extends Type>`) lub uwzględniać supertypy (za pomocą `<? super Type>`). W kolejnych sekcjach opisano odpowiednio wildcardy nieograniczone, z górnym ograniczeniem oraz z dolnym ograniczeniem. Następnie pokazujemy, jak definiować wiele ograniczeń dla typów generycznych.

## Wildcardy nieograniczone

Dla nieznanych typów używamy znaku zapytania jako typu, dzięki czemu w danym kontekście można użyć dowolnego typu. Na przykład zmienna zadeklarowana jako `List<?>` (lub atrybut albo parametr) może otrzymać obiekty `List` z dowolnym poprawnym parametrem typu, takim jak `String`, `Integer` itd. Takie nieznane typy generyczne nazywamy **wildcardami nieograniczonymi** (`<?>`), ponieważ nie nakładają żadnego ograniczenia typu.

Na przykład:

```java
List<?> l = new ArrayList<String>();
// lub na przykład
l = new LinkedList<Integer>();
```

Chociaż taki sposób deklarowania zmiennych może wydawać się atrakcyjny, ma ograniczenia. W takich przypadkach nie znamy typu obiektów znajdujących się na liście. Dlatego nie możemy na przykład dodawać elementów do listy (z wyjątkiem `null`, który jest zgodny z każdym typem referencyjnym w Javie), ponieważ nie ma gwarancji, że dodawany obiekt będzie miał ten sam typ co parametr typu listy.

Jeśli spróbujemy dodać element do listy (w tym przypadku `l`), otrzymamy błąd kompilacji:

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

Typy nieograniczone są często używane wtedy, gdy chcemy tylko odczytywać dane bez ich modyfikowania. Możemy na przykład mieć metodę, która przyjmuje listę i wypisuje jej elementy bez określania typu elementów listy:

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

Uruchomienie metody `main` wyświetli:

```text
1
2
3
A
B
C
```

Tutaj używamy wypisywania jako przykładu, ale możemy też iterować po obiektach, używać ich w *streams*, filtrować je za pomocą `instanceof`, pobierać rozmiar listy, sprawdzać, czy zawiera określony obiekt, przekształcać je i kopiować do typowanej listy oraz wykonywać inne operacje. Nie możemy natomiast bezpośrednio modyfikować listy (na przykład za pomocą `add` lub `set`, z wyjątkiem `null`).

## Wildcardy z górnym ograniczeniem

**Wildcardy z górnym ograniczeniem** pozwalają określić, że jako parametr typu może być używany tylko obiekt danego typu lub jednego z jego podtypów (uzyskanych przez dziedziczenie lub implementację interfejsu). Notacja `<? extends T>` określa, że wildcard musi być typu `T` lub typu rozszerzającego `T`.

Na przykład, jeśli zadeklaruję listę, której wildcard rozszerza `Number`, mogę przypisać jej obiekty dowolnej z jego podklas (takich jak `Double` lub `Integer`). Gdyby `Number` był klasą konkretną (jest abstrakcyjna), moglibyśmy również przypisać obiekt samej tej klasy. Poniższy przykład pokazuje ten przypadek:

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

Podobnie jak w przypadku wildcardów nieograniczonych, nie możemy dodawać elementów do listy `l`, ponieważ nie znamy dokładnie jej typu. Dlatego dwa pierwsze wywołania metody `add` powodują błędy kompilacji:

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

Chociaż czytając kod, wiemy, że obiekt przypisany do zmiennej `l` jest listą liczb całkowitych, kompilator wie tylko, że `l` ma nieznany typ, dlatego nie pozwala dodawać wartości. Podczas odczytu wartości są traktowane jako `Number`, czyli jako górne ograniczenie.

## Wildcardy z dolnym ograniczeniem

**Wildcardy z dolnym ograniczeniem** pozwalają określić, że jako parametr typu może być używany tylko obiekt danego typu lub jednego z jego supertypów. Notacja `<? super T>` określa, że wildcard musi być typu `T` lub jego nadklasy.

Na przykład, jeśli zadeklaruję listę, której wildcard ma `Number` jako dolne ograniczenie, mogę przypisać jej obiekty dowolnej z jego nadklas (w przypadku `Number` tylko `Object`, ponieważ `Number` nie ma jawnie określonej nadklasy).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

Można dodawać elementy typu dolnego ograniczenia (w tym przypadku `Number`) lub dowolnego z jego podtypów (takich jak `Double` lub `Integer`). Poniższy przykład pokazuje listę, której wildcard ma `Number` jako dolne ograniczenie. W tym przypadku możemy utworzyć `ArrayList` liczb (lub jego nadklasy `Object`). Możemy dodawać elementy jego podklas (nie możemy dodać obiektu typu `Number`, ponieważ jest to klasa abstrakcyjna i nie może mieć bezpośrednich instancji). Przykład pokazuje trzy dodania elementów. Pierwsze dwa są dozwolone, ponieważ elementy są podtypami `Number` (`10` jest typu `Integer`, a `1.0` typu `Double`). Trzecie dodanie nie jest dozwolone i powoduje błąd kompilacji, ponieważ `Object` nie jest potomkiem `Number`.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

Jeśli utworzylibyśmy `ArrayList` z `Object` jako parametrem typu, trzecie dodanie nadal nie byłoby dozwolone podczas kompilacji i powodowałoby ten sam błąd (pierwsze dwa pozostałyby dozwolone), ponieważ typ listy nadal jest nieznany (wiemy tylko, że jest to `Number` lub jeden z jego supertypów).

## Wiele ograniczeń

W Javie typ generyczny może mieć **wiele ograniczeń**, co oznacza, że parametr typu może być ograniczony do typów, które rozszerzają (lub są) określoną klasą i implementują jeden lub więcej interfejsów. Składnia ma postać `<T extends Class & Interface1 & Interface2>`. Jeśli jako ograniczenie używana jest klasa, musi zostać podana jako pierwsza, a następnie interfejsy. Jeśli nie ma klasy, można podać tylko interfejsy.

Na przykład klasa `MultipleBounds` ma typ generyczny `T`, który rozszerza klasę `Number` i implementuje interfejsy `Comparable<T>` oraz `Serializable`:

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

W tym przykładzie `T` może być tylko `Number` lub typem, który dziedziczy po `Number` i jednocześnie implementuje `Comparable<T>` oraz `Serializable`. Jest to przydatne, gdy potrzebujemy wielu gwarancji, takich jak dostęp do metod nadklasy oraz kontraktów zdefiniowanych przez wiele interfejsów. Takie połączenie pozwala zachować elastyczność kodu przy jednoczesnym silnym typowaniu, unikaniu błędów kompilacji i zapewnieniu dostępności wszystkich wymaganych metod dla używanego typu generycznego.

---

*Ten artykuł jest adaptacją treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
