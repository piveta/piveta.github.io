---
layout: post
title: "Java w VS Code: instalacja i konfiguracja JDK"
date: 2026-11-25
lang: pl
translation_id: java-no-vscode-configurar
permalink: /pl/java-w-vs-code-konfiguracja/
share_text: >-
  Skonfiguruj Javę w Visual Studio Code, wybierz JDK i uruchom pierwszy program.
---

## Zainstaluj JDK i Visual Studio Code
Aby programować w **Javie w VS Code**, zainstaluj JDK zgodne z projektem oraz Visual Studio Code. Sprawdź w terminalu, czy JDK jest dostępne:

~~~text
java --version
javac --version
~~~

Jeśli poleceń nie znaleziono, sprawdź instalację JDK i zmienną <code>PATH</code>. Po zmianie zmiennych środowiskowych otwórz nowy terminal.

## Zainstaluj rozszerzenia Java
W VS Code otwórz **Extensions**, wyszukaj **Extension Pack for Java** i zainstaluj pakiet opublikowany przez Microsoft. Zawiera obsługę języka, uruchamianie, debugowanie i inne narzędzia Java.

Alternatywą jest Coding Pack for Java dla Windows i macOS, który obejmuje VS Code, JDK i podstawowe rozszerzenia.

## Skonfiguruj JDK projektu
Otwórz paletę poleceń skrótem <code>Ctrl+Shift+P</code> w Windows lub Linuksie albo <code>Cmd+Shift+P</code> w macOS. Uruchom **Java: Configure Java Runtime** i sprawdź JDK przypisane do projektu.

JDK projektu może różnić się od tego w terminalu. Przy kilku zainstalowanych wersjach sprawdź oba ustawienia.

## Uruchom program
Otwórz folder w VS Code i utwórz plik <code>Hello.java</code>:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Przykład wykorzystuje zwartą składnię pliku źródłowego i <code>IO.println</code>, dostępne od Javy 25. Wybierz **Run** obok <code>main</code> i sprawdź wynik w terminalu. Do debugowania wybierz **Debug** i ustaw punkt przerwania.

Jeśli VS Code nie rozpoznaje pliku, sprawdź, czy folder jest otwarty, poczekaj na uruchomienie rozszerzeń i zweryfikuj JDK w **Java: Configure Java Runtime**.

## Źródła
- [Pierwsze kroki z Javą w VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Zarządzanie projektami Java w VS Code](https://code.visualstudio.com/docs/java/java-project)
