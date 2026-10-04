---
layout: post
title: "Klasy wyjątków w Javie"
date: 2026-08-27
lang: pl
translation_id: classes-de-excecao
permalink: /klasy-wyjatkow-java-pl/
image: /images/descendentesThrowable.png
share_text: >-
  Throwable stanowi podstawę hierarchii wyjątków Javy, a jego bezpośrednimi podklasami są Exception i Error. Artykuł wyjaśnia wyjątki sprawdzane i niesprawdzane oraz rolę RuntimeException w tym podziale.
---
Podczas wykonywania programu mogą wystąpić sytuacje wymagające specjalnego przetwarzania. Mogą one reprezentować nietypowe lub błędne warunki, sytuacje, których programista nie przewidział, a nawet alternatywne ścieżki wykonania. Warunki te nazywamy **wyjątkami**.

W Javie wyjątki są reprezentowane przez obiekty należące do klasy `Throwable` lub jednej z jej podklas. Hierarchia wyjątków jest ważna dla zrozumienia, które wyjątki mogą być zgłaszane, przechwytywane i obsługiwane przez programy.

## Throwable

`Throwable` jest klasą bazową hierarchii wyjątków w Javie. Obiekty tej klasy przechowują informacje o konkretnym zdarzeniu i umożliwiają przekazanie tych informacji z miejsca wystąpienia wyjątku do kodu odpowiedzialnego za jego obsługę.

Tylko obiekty należące do `Throwable` lub jednej z jego podklas mogą być zgłaszane przez JVM lub przez programistę za pomocą `throw`. Podobnie klauzula `catch` może przechwytywać wyłącznie obiekty należące do tej hierarchii.

Do najważniejszych metod klasy `Throwable` należą `getMessage()`, która pozwala uzyskać komunikat związany z wyjątkiem, oraz `printStackTrace()`, która wyświetla ślad stosu wykonania do miejsca wystąpienia wyjątku.

Klasa `Throwable` ma dwie bezpośrednie podklasy: `Exception` i `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Hierarchia Throwable"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

Klasa `Error` reprezentuje poważne warunki, z których aplikacja na ogół nie jest w stanie się odzyskać. Są to sytuacje nietypowe, które normalnie nie powinny wystąpić podczas wykonywania programu.

Do ważnych podklas `Error` należą `AssertionError`, `IOError` i `VirtualMachineError`. Ta ostatnia ma między innymi podklasy `InternalError`, `OutOfMemoryError`, `StackOverflowError` i `UnknownError`.

Błędy mogą być zgłaszane przez samą JVM, często w wyniku warunków wykrytych przez system operacyjny lub środowisko uruchomieniowe. Mogą być również jawnie wywoływane przez programistę, na przykład za pomocą `assert` lub `throw`.

<img src="/images/exceptionsError.png"
     alt="Error i jego podklasy"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

Klasa `Exception` reprezentuje wyjątki, które w pewnych okolicznościach można obsłużyć i po których aplikacja może kontynuować działanie.

Jej podklasy obejmują `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException` i `RuntimeException`.

Podklasy `Exception`, które nie są podklasami `RuntimeException`, nazywamy **wyjątkami sprawdzanymi** (*checked exceptions*). Kompilator wymaga, aby program jawnie je uwzględnił. Można to zrobić, przechwytując wyjątek za pomocą klauzuli `catch` albo deklarując za pomocą `throws`, że metoda może go zgłosić.

<img src="/images/descendentesException.png"
     alt="Exception i jego podklasy"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

Wśród podklas `Exception` wyróżnia się `RuntimeException`. Ona oraz jej podklasy są nazywane **wyjątkami czasu wykonania** (*runtime exceptions*).

`RuntimeException` i jej podklasy są **wyjątkami niesprawdzanymi** (*unchecked exceptions*). Kompilator nie wymaga, aby były jawnie obsługiwane za pomocą `try`/`catch` ani deklarowane za pomocą `throws`.

Ten rodzaj wyjątku zazwyczaj reprezentuje błędy logiczne lub nieprawidłowe użycie programu. Typowe przykłady to:

- `ClassCastException`: występuje, gdy jawne rzutowanie typu jest niemożliwe.
- `IllegalArgumentException`: wskazuje, że metoda otrzymała argument uznany za nieprawidłowy lub nieodpowiedni.
- `IndexOutOfBoundsException`: występuje podczas próby uzyskania dostępu do nieistniejącej pozycji w strukturze indeksowanej.
- `NullPointerException`: występuje, gdy operacja jest wykonywana na referencji `null`.

Metoda, która może zgłosić `RuntimeException`, nie musi deklarować tej możliwości za pomocą `throws`. Oczywiście nadal można przechwytywać i obsługiwać te wyjątki za pomocą `try` i `catch`.

W praktyce wiele instancji `RuntimeException` wskazuje na problemy, którym można było zapobiec w samym programie. Gdy taki wyjątek wystąpi, zazwyczaj ważne jest zbadanie jego przyczyny i usunięcie problemu, zamiast po prostu przechwytywać wyjątek.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException i jego podklasy"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Wyjątki sprawdzane i niesprawdzane

Ważnym rozróżnieniem w hierarchii wyjątków Javy jest podział na **wyjątki sprawdzane** i **wyjątki niesprawdzane**.

`Throwable` oraz wszystkie jego podklasy, które nie są podklasami `RuntimeException` ani `Error`, nazywamy **wyjątkami sprawdzanymi**. `RuntimeException` i jej podklasy, a także `Error` i jego podklasy, nazywamy **wyjątkami niesprawdzanymi**.

Wyjątki sprawdzane muszą być obsługiwane lub jawnie deklarowane przez program. Oznacza to, że gdy metoda może zgłosić wyjątek sprawdzany, musi on zostać obsłużony przez klauzulę `catch` albo zadeklarowany w klauzuli `throws` tej metody.

Wyjątki niesprawdzane nie muszą natomiast być jawnie obsługiwane ani deklarowane. Kompilator nie wymaga przechwytywania ani deklarowania `RuntimeException`, `Error` ani ich podklas.

W uproszczeniu hierarchię można przedstawić następująco:

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

Taka organizacja pozwala na obsługę wyjątków na różnych poziomach hierarchii. Klauzula `catch` może na przykład przechwycić konkretny wyjątek lub jedną z jego klas nadrzędnych, zależnie od oczekiwanego zachowania.

Zrozumienie tej hierarchii jest podstawą zrozumienia mechanizmu obsługi wyjątków w Javie oraz podejmowania decyzji, które wyjątki należy obsługiwać, które propagować, a które reprezentują błędy wymagające naprawy w samym programie.

Ten artykuł jest adaptacją treści z książki <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, autorstwa <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.
