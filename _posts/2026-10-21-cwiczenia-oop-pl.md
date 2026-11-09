---
layout: post
title: "Ćwiczenia z programowania obiektowego"
date: 2026-10-21
lang: pl
translation_id: exercicios-poo-java
permalink: /cwiczenia-oop-pl/
share_text: >-
  Ćwiczenia dotyczące pojęć OOP, polimorfizmu, dziedziczenia, klas abstrakcyjnych, generyków, Javy i kont bankowych.
---

1. Napisz samouczek wyjaśniający, jak przedstawić podstawowe pojęcia programowania obiektowego w wybranym języku innym niż Java.

2. Opisz polimorfizm, sposób jego działania i wpływ na programowanie systemowe, w tym zalety i wady. Podaj przykład.

3. Zdefiniuj nadpisywanie (*overriding*) i przeciążanie (*overloading*) metod w językach programowania obiektowego. Podaj przykłady.

4. Zdefiniuj dziedziczenie i opisz trzy sytuacje, w których byłoby odpowiednie. Dołącz przykład kodu.

5. Czym są klasy abstrakcyjne i do czego służą w językach obiektowych? Opisz co najmniej trzy sytuacje, w których byłyby odpowiednie.

6. Jakie zalety mają typy generyczne w systemach obiektowych i kiedy należy ich używać? Podaj co najmniej trzy przykłady sytuacji, w których ten mechanizm jest przydatny.

7. Rozważ poniższe stwierdzenia dotyczące programowania obiektowego:

   I. Metody definiują operacje w klasach.

   II. Klasy są abstrakcjami służącymi do reprezentowania pojęć ze świata rzeczywistego i świata komputerowego.

   III. Instancje klas są zwykle tworzone za pomocą konstruktorów, które tworzą obiekty określonej klasy.

   Wybierz poprawną odpowiedź:

   1. Tylko stwierdzenie I jest niepoprawne.
   2. Tylko stwierdzenie II jest niepoprawne.
   3. Tylko stwierdzenie III jest niepoprawne.
   4. Tylko stwierdzenia I i III są niepoprawne.
   5. Żadne stwierdzenie nie jest niepoprawne.

8. Wybierz poprawne stwierdzenie dotyczące dziedziczenia w Javie:

   1. Obiekt nadklasy można zawsze przypisać do zmiennej typu jednej z jej podklas bez błędu kompilacji.
   2. Dziedziczenie jest jedynym sposobem uzyskiwania dostępu do metod i pól spoza klasy.
   3. Nie można całkowicie zastąpić zachowania metody nadklasy; można je tylko rozszerzyć.
   4. Przeciążanie definiuje w nadklasie wiele metod o tych samych parametrach, aby podklasy mogły z nich korzystać.
   5. Podklasa dziedziczy wszystkie nieprywatne pola i metody nadklasy i może dodawać nowe pola oraz metody.

9. Utwórz klasy do zarządzania kontami bankowymi. Konta mogą być oszczędnościowe lub bieżące. Muszą umożliwiać:

   - Odczyt salda konta.
   - Zmianę salda konta.
   - Wypłatę pieniędzy z konta.
   - Wpłatę pieniędzy na konto.
   - Przelew na inne konto.
   - Blokowanie i odblokowywanie konta, np. przez `account1.block()` i `account1.unblock()`. Jeśli konto jest zablokowane, można tylko odczytać lub zmienić jego saldo.

10. Zaimplementuj w Javie grę *Saper* działającą w terminalu.

---

*Ten artykuł adaptuje treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kesslera Pivety</a>.*

## Powiązane artykuły

- [Podstawowe pojęcia programowania obiektowego](/oop-basics-java-pl/)
- [Klasy w Javie](/klasy-w-java-pl/)
- [Dziedziczenie w Javie](/dziedziczenie-w-java-pl/)
- [Polimorfizm w Javie](/polymorphism-in-java-pl/)
- [Interfejsy w Javie](/interfejsy-w-java-pl/)
- [Linki o OOP i Javie](/linki-oop-java-pl/)
