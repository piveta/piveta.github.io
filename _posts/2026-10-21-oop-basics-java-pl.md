---
layout: post
title: "Podstawowe pojęcia programowania obiektowego"
date: 2026-10-21
lang: pl
translation_id: conceitos-basicos-poo-java
permalink: /oop-basics-java-pl/
share_text: >-
  Wprowadzenie do podstaw programowania obiektowego: klas, obiektów, atrybutów, metod, enkapsulacji, dziedziczenia, polimorfizmu i relacji między klasami.
---

Programowanie strukturalne udostępnia mechanizmy modularizacji pojęć w systemie oprogramowania za pomocą struktur danych i algorytmów, które je przetwarzają. Powszechnie używane języki strukturalne pozwalają reprezentować różne typy danych i zmienne, aby wyrażać właściwości oraz cechy rozważanych pojęć, a także procedury i funkcje modelujące powiązane operacje.

Przy ponownym wykorzystywaniu komponentów napisanych w językach strukturalnych trzeba jednak ustalić zależności między danymi (reprezentowanymi przez struktury, typy danych i zmienne) a zachowaniem (wyrażonym przez procedury i funkcje). Ponowne użycie odbywa się więc często na drobnym poziomie i może wymagać znacznego wysiłku, na przykład przy ustalaniu, które procedury i funkcje są powiązane z którymi strukturami danych. Można tworzyć biblioteki wielokrotnego użytku, ale związek między danymi a zachowaniem nie jest jawny ani skupiony w jednej abstrakcji.

**Programowanie obiektowe** (OOP) to paradygmat, który reprezentuje pojęcia z danej dziedziny za pomocą abstrakcyjnych typów danych zwanych klasami. Klasy modelują zarówno cechy i właściwości tych pojęć, jak i ich operacje. OOP rozszerza programowanie strukturalne o sposoby specyfikowania i łączenia klas w celu modelowania kompletnych systemów komputerowych, dążąc do większej modularności i ponownego wykorzystania komponentów.

Obecnie programowanie obiektowe jest jednym z najczęściej akceptowanych i stosowanych paradygmatów tworzenia oprogramowania. Obsługuje je wiele nowoczesnych języków, m.in. Java, C++, C#, Python, Kotlin, JavaScript, TypeScript, Swift i Ruby.

**Klasa** to mechanizm abstrakcji służący do reprezentowania pojęć z określonej dziedziny. W dziedzinie bankowości mogą to być na przykład oddziały, konta, klienci i transakcje. Możemy zdefiniować klasy `Branch`, `Account`, `Customer` i `Transaction`, aby je reprezentować. Rysunek przedstawia graficzną reprezentację tych klas.

<img src="/images/en/oopClasses.svg" alt="Klasy Branch, Account, Customer i Transaction." style="max-width: 300px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Klasy służą jako *szablony* do tworzenia konkretnych, możliwych do manipulowania przykładów tych pojęć. Takie przykłady nazywają się **obiektami**. Obiekt jest **instancją** klasy, a proces tworzenia obiektów to **instancjowanie**. Możemy na przykład utworzyć obiekty reprezentujące klientów *John*, *Peter* i *Mary*, wraz z ich danymi osobowymi oraz funkcjami dostępnymi dla klientów.

<img src="/images/en/oopObjects.svg" alt="Obiekty John, Peter i Mary są instancjami klasy Customer." style="max-width: 380px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Klasa jest definiowana tak, aby reprezentować właściwości, cechy i zachowanie danego pojęcia. Dwa główne mechanizmy to atrybuty i metody.

**Atrybuty** reprezentują cechy lub właściwości obiektów danej klasy. Atrybutami klasy `Customer` mogą być *name*, *age*, *address* i *marital status*. Każdy klient może mieć inne wartości tych atrybutów. Przykładowy obiekt klienta może mieć wartości: *name* $`=`$ John Smith, *age* $`=`$ 50, *address* $`=`$ 205 President Vargas Street i *marital status* $`=`$ married.

**Metody** reprezentują zachowanie. Możliwe metody klasy `Account` mogą odpowiadać operacjom *otwarcia*, *zamknięcia* lub *zmiany właściciela* konta. **Wywołanie** metody uruchamia zaimplementowaną w niej operację. Klasy często zawierają specjalne metody tworzące (instancjujące) obiekty, zwane **konstruktorami**, oraz metody niszczące obiekty, zwane **destruktorami**.

Atrybuty i metody dzielą się też na instancyjne i klasowe. Najczęściej używane **atrybuty i metody instancyjne** są dostępne przez obiekty klasy i reprezentują cechy oraz operacje poszczególnych instancji. Atrybutami instancyjnymi `Account` mogą być *bank*, *branch*, *account number* i *account holder*, a metodami instancyjnymi — *withdraw*, *transfer* i *deposit*. **Atrybuty i metody klasowe** należą natomiast do samej klasy, a nie do jej instancji. Atrybut klasowy może na przykład zliczać utworzone instancje `Account`, a metoda klasowa zwracać tę liczbę.

Aby ograniczyć dostęp do atrybutów i metod, klasy udostępniają mechanizmy **enkapsulacji i ukrywania informacji**. Języki programowania zwykle oferują modyfikatory widoczności określające, kto może uzyskać dostęp do danego atrybutu, metody lub klasy.

Klasy abstrakcyjnie przedstawiają i enkapsulują pojęcia ze świata rzeczywistego i świata komputerowego. Abstrakcje można łączyć za pomocą różnych relacji, aby klasy współpracowały przy spełnianiu wymagań aplikacji. Główne relacje między klasami to dziedziczenie, asocjacja, agregacja, kompozycja i realizacja.

**Dziedziczenie** to mechanizm kompozycji, który pozwala klasom ponownie wykorzystywać interfejs i zachowanie istniejących klas oraz rozszerzać ich funkcjonalność. Klasę rozszerzającą inną nazywa się **podklasą**, a klasę rozszerzaną — **nadklasą**. Rozszerzenie zwykle deklaruje się w podklasie, na przykład: `SubClass` rozszerza `SuperClass`.

Rysunek 3 przedstawia klasy `Shape`, `Rectangle`, `Triangle` i `Circle`. `Shape` jest nadklasą, a `Rectangle`, `Triangle` i `Circle` są jej podklasami.

<img src="/images/en/oopInheritance.png" alt="Shape jest nadklasą Rectangle, Triangle i Circle." style="max-width: 400px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Mechanizmy dziedziczenia różnią się między językami. Różnice dotyczą zwykle widoczności i liczby nadklas. Niektóre języki, takie jak C++, pozwalają określić dziedziczenie jako **publiczne** lub **prywatne**. Rozważmy klasę `A` i klasę `B`, która dziedziczy po `A`. `A` jest nadklasą `B`, a `B` podklasą `A`. Przy dziedziczeniu publicznym `B` jest podtypem `A` i dziedziczy zarówno implementację, jak i interfejs `A`. Wszędzie tam, gdzie oczekiwany jest obiekt `A`, można użyć obiektu `B` (lub innej podklasy `A`), ponieważ każda instancja `B` jest również instancją `A`. Zasadę tę nazywa się **zasadą podstawienia Liskov**. Przy dziedziczeniu prywatnym `B` nie jest `A`; dziedziczy tylko implementację `A` i jest zbudowana na jej podstawie. Zasada podstawienia Liskov nie ma tu zastosowania.

Dziedziczenie może być też **pojedyncze lub wielokrotne**. W dziedziczeniu pojedynczym, stosowanym przez Javę i C#, klasa może mieć tylko jedną nadklasę. W dziedziczeniu wielokrotnym, jak w C++, może mieć ich więcej. Projektanci języków nie są zgodni, czy korzyści z dziedziczenia wielokrotnego uzasadniają związane z nim problemy. Inne języki oferują alternatywy, takie jak dziedziczenie wirtualne oparte na interfejsach, *traits* i *mixins*.

Rysunek 4 pokazuje przykład dziedziczenia wielokrotnego. `Mammal` i `Bird` reprezentują zwierzęta. `Horse`, `Dog` i `Bat` są podklasami `Mammal`, a `Ostrich` i `Duck` — podklasami `Bird`. Chcemy też sklasyfikować zwierzęta potrafiące latać, więc tworzymy `Flyer`, klasę reprezentującą obiekty latające, które nie muszą być zwierzętami. Dzięki dziedziczeniu wielokrotnemu obiekty `Duck` i `Bat` mogą być również obiektami latającymi, dziedzicząc po `Flyer`.

<img src="/images/en/oopMultipleInheritance.png" alt="Dziedziczenie wielokrotne między klasami Animal, Bird, Flyer i Mammal." style="max-width: 500px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Niektóre klasy są **abstrakcyjne**. Podobnie jak klasy **konkretne**, reprezentują cechy i zachowanie zbioru rzeczywistych obiektów, ale nie można ich bezpośrednio instancjować. W przykładzie dziedziczenia wielokrotnego `Mammal`, `Bird` i `Flyer` mogłyby być klasami abstrakcyjnymi, ponieważ w świecie rzeczywistym występują tylko przykłady ich podklas, takie jak konie, psy i kaczki.

Oprócz widoczności i liczby nadklas dziedziczenie umożliwia tworzenie metod polimorficznych. W programowaniu obiektowym **polimorfizm** to zdolność operacji do różnego działania w zależności od klasy obiektu, który ją wywołuje. Główne formy to:

- **Polimorfizm ad hoc (lub przeciążanie)** zachodzi, gdy klasa ma metody o tej samej nazwie, lecz różnych typach parametrów formalnych. Użyty argument określa, która metoda zostanie wywołana.
- **Polimorfizm parametryczny** zachodzi, gdy metoda jest definiowana generycznie, a jej typ zostaje określony później, np. podczas deklaracji zmiennej lub instancjowania obiektu. W językach obiektowych takie typy nazywa się generycznymi.
- **Polimorfizm podtypów** zachodzi, gdy podklasy nadpisują metody nadklasy. Obiekt wywołujący metodę określa, która implementacja zostanie uruchomiona. Zwykle rozstrzyga się to w czasie wykonania za pomocą wiązania dynamicznego.

Oprócz dziedziczenia istnieją inne relacje, m.in. asocjacja, agregacja i kompozycja. Ogólnie różnią się stopniem powiązania między uczestnikami:

- W **asocjacji** relacja między obiektami jest zwykle tymczasowa i można ją łatwo zmienić w czasie wykonania. W systemie ruchu drogowego osoba może być powiązana z pojazdem jako kierowca. Po zmianie kierowcy oba obiekty nadal istnieją, nawet jeśli asocjacja zostanie usunięta.
- W **agregacji** relacja jest silniejsza niż w asocjacji. Obiekty agregowane często tworzy się wraz z obiektem agregującym. Samochód może mieć cztery koła: samochód jest obiektem agregującym, a koła — agregowanymi. Relację można usunąć, ale wymiana kół jest mniej typowa i bardziej pracochłonna niż zmiana kierowcy.
- W **kompozycji** relacja jest jeszcze silniejsza, ponieważ obiekty składowe są częścią większego obiektu. Na przykład tkanina siedzenia pojazdu jest złożona z nici. Gdy nici przestaną istnieć, siedzenie również przestanie istnieć lub utraci swoją tożsamość.

Relacje między obiektami są często pojęciowe. Przy odwzorowaniu ich w języku programowania obiekty można łączyć przez atrybuty klasy, przypisując im wartości w czasie wykonania. Różny może być moment tworzenia obiektów: w kompozycji obiekty składowe często tworzy się w konstruktorze całości, a w asocjacji obiekty powiązane zwykle powstają niezależnie i są łączone w razie potrzeby.

Ostatnia relacja, **realizacja**, występuje, gdy klasa deklaruje, że implementuje interfejs. **Interfejs** można traktować jako klasę abstrakcyjną, której wszystkie metody są abstrakcyjne[^1]. Służy on jako protokół między klientami a implementatorami. Klasa (lub jedna z jej podklas) musi zaimplementować zadeklarowane metody. Dzięki temu klienci mogą pisać kod zgodny z interfejsem bez zależności od sposobu jego implementacji.

[^1]: Od Javy 8 interfejsy mogą definiować także metody konkretne, zwane metodami domyślnymi, używając słowa kluczowego `default`. Klasy implementujące interfejs z metodą domyślną nie muszą jej implementować, ale mogą ją nadpisać.

---

*Ten artykuł adaptuje treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kesslera Pivety</a>.*

## Powiązane artykuły

- [Klasy w Javie](/klasy-w-java-pl/)
- [Dziedziczenie w Javie](/dziedziczenie-w-java-pl/)
- [Polimorfizm w Javie](/polymorphism-in-java-pl/)
- [Interfejsy w Javie](/interfejsy-w-java-pl/)
- [Linki o OOP i Javie](/linki-oop-java-pl/)
- [Ćwiczenia z programowania obiektowego](/oop-exercises-pl/)
