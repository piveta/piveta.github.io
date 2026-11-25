---
layout: post
title: "Wersje Javy: LTS, aktualizacje i sprawdzanie wersji"
date: 2026-11-25
lang: pl
translation_id: versoes-java-lts-atualizacao
permalink: /pl/wersje-java-lts-aktualizacje/
share_text: >-
  Poznaj cykl wydań Javy, znaczenie LTS oraz sposób sprawdzania i aktualizowania JDK.
---

## Sprawdź wersję Javy
Uruchom w terminalu:

~~~text
java --version
javac --version
~~~

Pierwsze polecenie wskazuje launcher Java uruchamiający aplikacje, drugie — kompilator. Przy wielu zainstalowanych JDK plik znaleziony w <code>PATH</code> może różnić się od wersji skonfigurowanej w IDE.

## Wersje Javy i LTS
Java publikuje wydania funkcyjne co sześć miesięcy. Wersja **LTS** (*long-term support*) otrzymuje długoterminowe wsparcie od wybranych dostawców. Czas, cena i warunki wsparcia zależą od dystrybucji i dostawcy.

Według harmonogramu wsparcia Oracle wersje Java 8, 11, 17, 21 i 25 są LTS. Oracle planuje nowe LTS co dwa lata. Przed wyborem wersji produkcyjnej sprawdź aktualny harmonogram i politykę dostawcy.

Wybór zależy także od bibliotek, narzędzi i wymagań aplikacji. LTS daje dłuższy horyzont wsparcia, a wydania pośrednie szybciej udostępniają nowe funkcje.

## Gdzie szukać wersji i JEP
Oracle prowadzi [indeks informacji o wydaniach JDK](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html), z odnośnikami do wersji i aktualizacji. Notatki opisują zmiany, poprawki oraz dodane lub usunięte funkcje. [Informacje o JDK 27](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) przedstawiają nowości i powiązane JEP.

**JEP** (*JDK Enhancement Proposal*) dokumentuje propozycję ulepszenia JDK, jej cele, projekt i status. Niektóre funkcje pojawiają się najpierw jako *preview* lub *incubator* i mogą się zmienić przed utrwaleniem.

[Zmiany języka Java według wydań](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html) oraz [podsumowanie zmian](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html) pomagają porównać funkcje stałe i zapoznawcze.

## Aktualizowanie Javy
1. Sprawdź wersję poleceniami <code>java --version</code> i <code>javac --version</code>.
2. Ustal, które wersje obsługują projekt, zależności i produkcja.
3. Pobierz aktualizację używanej dystrybucji lub wybierz zgodną.
4. Zainstaluj JDK i w razie potrzeby dostosuj <code>PATH</code>, <code>JAVA_HOME</code> i IDE.
5. Otwórz nowy terminal, sprawdź wersje i uruchom testy aplikacji.

Aktualizacja w ramach tej samej linii i migracja do głównej wersji to różne decyzje. Przed migracją przeczytaj informacje o wydaniu i przetestuj aplikację oraz zależności.

W Windows użyj <code>where.exe java</code> i <code>where.exe javac</code>, a w macOS i Linuksie <code>which java</code> oraz <code>which javac</code>.

## Źródła
- [Harmonogram wsparcia Oracle Java SE](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [FAQ licencyjne Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
