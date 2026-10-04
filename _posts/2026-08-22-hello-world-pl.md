---
layout: post
title: "Hello World - Wersja tradycyjna i uproszczona"
date: 2026-08-22
lang: pl
translation_id: hello-world
permalink: /hello-world-pl/
share_text: >-
  Przykład zestawia tradycyjną klasę Java z metodą main z uproszczonym sposobem uruchamiania dostępnym od Javy 25. Oba warianty wyświetlają ten sam komunikat Hello World.
---

Naukę języka programowania zwykle rozpoczyna się od napisania programu o nazwie **Hello World**, który wyświetla tekst `Hello World!` na standardowym wyjściu urządzenia, zazwyczaj na ekranie. W Javie możemy napisać ten program następująco:

```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```

W tym programie mamy klasę o nazwie `Hello`. W systemach obiektowych klasy pomagają modelować pojęcia z badanego obszaru zastosowania. Klasy hermetyzują zarówno dane, jak i zachowanie związane z określonym pojęciem.

Klasa `Hello` ma jedną metodę o nazwie `main`, która otrzymuje tablicę łańcuchów znaków zawierającą argumenty wiersza poleceń przekazane podczas uruchamiania programu, jeśli takie istnieją. W tym przykładzie argumenty te nie są używane.

Metoda `main` jest statyczna, co oznacza, że jest metodą klasy, a nie metodą instancji. Dlatego można ją wywołać bez tworzenia obiektu klasy `Hello`.

Wewnątrz metody `main` znajduje się wywołanie metody `println`. Metoda ta należy do klasy `PrintStream` i wyświetla na ekranie wartość przekazaną jako argument, a następnie terminator wiersza.

Metoda `println` jest wywoływana za pośrednictwem pola `out` klasy `System`. Pole to ma typ `PrintStream` i zapewnia dostęp do standardowego wyjścia systemu.

## Kompilacja i wykonanie

Programy Java są najpierw kompilowane do pośredniej reprezentacji zwanej **bajtkodem**, co zapewnia przenośność. Następnie bajtkod jest wykonywany przez Java Virtual Machine (JVM), która przekształca go w kod maszynowy odpowiedni dla danej platformy.

Aby skompilować program, należy zapisać go w pliku o nazwie `Hello.java`. W Javie pliki zawierające typy publiczne mają zwykle taką samą nazwę jak typ.

Możemy użyć zintegrowanego środowiska programistycznego (**IDE**) albo wywołać kompilator bezpośrednio z wiersza poleceń, pod warunkiem że zainstalowany jest JDK.

Programy Java są zwykle pisane w IDE, które zapewnia funkcje zwiększające produktywność podczas programowania, takie jak nawigacja po kodzie źródłowym, refaktoryzacja, analiza statyczna, kompilacja, testowanie i debugowanie.

Niektóre z najpopularniejszych IDE dla Javy to:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

Program możemy również skompilować bezpośrednio z wiersza poleceń za pomocą kompilatora `javac`:

```text
    javac Hello.java
```

Polecenie przyjmuje `Hello.java` jako dane wejściowe i tworzy plik `Hello.class`, zawierający skompilowaną wersję programu.

Po kompilacji możemy uruchomić program za pomocą polecenia `java`:

```text
    java Hello
```

Wynik będzie następujący:

```text
    Hello World!
```

## Prostsze podejście w Javie 25+

Od Javy 25 funkcja rozwijana jako *preview* od Javy 21 stała się częścią języka: **Compact Source Files and Instance Main Methods**. Pozwala ona pisać małe programy z mniejszą ilością kodu pomocniczego poprzez pominięcie jawnej deklaracji klasy i uproszczenie metody `main`.

Poprzedni program można więc teraz zapisać w Javie 26 (obecnej wersji) następująco:

```java
    void main() {
        IO.println("Hello World!");
    }
```

W tym przypadku nie musimy jawnie deklarować klasy ani pisać `public static void main(String[] args)`. Kompilator traktuje plik jako taki, który niejawnie deklaruje klasę, a metoda `main` może być metodą instancji.

Możemy również użyć klasy `IO`, która udostępnia proste operacje wejścia i wyjścia konsoli. W Javie 26 `IO` należy do pakietu `java.lang`, więc jest dostępna niejawnie. Aby wywołać jej metody, musimy jednak użyć nazwy klasy, jak w `IO.println(...)`.

Ponieważ funkcja ta nie jest już w fazie *preview*, nie potrzebujemy żadnych specjalnych opcji kompilacji. Program można skompilować normalnie:

```text
    javac Hello.java
```

i uruchomić w ten sam sposób:

```text
    java Hello
```

Możliwe jest również bezpośrednie uruchomienie pliku źródłowego za pomocą programu uruchamiającego `java`:

```text
    java Hello.java
```

W tym przypadku kod źródłowy jest kompilowany w pamięci przez sam program uruchamiający przed wykonaniem. Mechanizm ten pozwala uruchamiać programy bezpośrednio z plików źródłowych bez jawnego tworzenia pliku `.class`.

Kompaktowe pliki źródłowe są szczególnie interesujące w przypadku małych przykładów, programów edukacyjnych, skryptów i eksperymentów. Gdy program rośnie i wymaga bardziej rozbudowanej struktury, możemy naturalnie powrócić do tradycyjnej formy z jawnymi deklaracjami klas i metod.

Proces wykonywany przez IDE jest zasadniczo podobny. Oprócz kompilacji i uruchamiania zapewniają one funkcje debugowania, testowania, refaktoryzacji, tworzenia i zarządzania projektami, tworzenia bibliotek, zarządzania wersjami i wiele innych.

---

*Ten artykuł jest adaptacją treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
