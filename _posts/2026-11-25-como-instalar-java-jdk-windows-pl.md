---
layout: post
title: "Jak zainstalować Javę i JDK w systemie Windows"
date: 2026-11-25
lang: pl
translation_id: como-instalar-java-jdk-windows
permalink: /pl/instalacja-java-jdk-windows/
share_text: >-
  Pobierz i zainstaluj JDK w Windows, a następnie sprawdź je poleceniami java i javac.
---

## Wybierz dystrybucję Javy
Do programowania w Javie w Windows pobierz **JDK** zgodne z projektem. Dostępne są między innymi Oracle JDK i Eclipse Temurin. W projektach wymagających długiego wsparcia można rozważyć wersję LTS. Sprawdź wymagania i warunki dystrybucji.

W Ustawieniach Windows sprawdź typ systemu i architekturę procesora. Wybierz pakiet, na przykład x64 lub AArch64, oraz instalator Windows.

## Pobierz i zainstaluj JDK
Instalacja Eclipse Temurin:

1. Otwórz [stronę pobierania Adoptium](https://adoptium.net/temurin/releases/).
2. Wybierz wersję Javy, Windows, architekturę i pakiet **JDK**.
3. Pobierz i uruchom instalator MSI.
4. Sprawdź, czy Java zostanie dodana do <code>PATH</code>. Jeśli inne narzędzie wymaga <code>JAVA_HOME</code>, zaznacz też tę opcję.
5. Zakończ instalację i otwórz nowy terminal.

W Temurin dodanie do <code>PATH</code> jest standardową opcją, a ustawienie <code>JAVA_HOME</code> dodatkową.

## Sprawdź instalację
W PowerShellu lub wierszu polecenia uruchom:

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

Dwa pierwsze polecenia pokazują wersje Javy i kompilatora. Pozostałe wskazują pliki w <code>PATH</code>. Jeśli polecenia nie znaleziono, otwórz nowy terminal i sprawdź zmienne środowiskowe. Przy innej wersji sprawdź kolejność katalogów w <code>PATH</code>.

Zapisz kod jako <code>Hello.java</code>, aby przetestować kompilację:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Przykład używa zwartej składni pliku źródłowego i <code>IO.println</code>, dostępnych od Javy 25. Uruchom:

~~~text
javac Hello.java
java Hello
~~~

Wynik to <code>Hello World!</code>. W starszych wersjach użyj formy programu obsługiwanej przez zainstalowane JDK.

## Źródła
- [Instalator MSI Eclipse Temurin](https://adoptium.net/installation/windows/)
- [Instalacja Oracle JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
