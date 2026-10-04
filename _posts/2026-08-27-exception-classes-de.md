---
layout: post
title: "Ausnahmeklassen in Java"
date: 2026-08-27
lang: de
translation_id: classes-de-excecao
permalink: /exception-classes-de/
image: /images/descendentesThrowable.png
share_text: >-
  Throwable bildet die Wurzel der Java-Ausnahmenhierarchie und hat Exception und Error als direkte Unterklassen. Der Beitrag erläutert geprüfte und ungeprüfte Ausnahmen sowie die Rolle von RuntimeException bei dieser Unterscheidung.
---
Während der Ausführung eines Programms können Situationen auftreten, die eine besondere Behandlung erfordern. Sie können abnormale oder fehlerhafte Bedingungen, vom Programmierer nicht vorhergesehene Situationen oder sogar alternative Ausführungsabläufe darstellen. Diese Bedingungen werden **Ausnahmen** genannt.

In Java werden Ausnahmen durch Objekte dargestellt, die zur Klasse `Throwable` oder zu einer ihrer Unterklassen gehören. Die Ausnahmehierarchie ist wichtig, um zu verstehen, welche Ausnahmen von Programmen ausgelöst, abgefangen und behandelt werden können.

## Throwable

`Throwable` ist die Basisklasse der Ausnahmehierarchie in Java. Objekte dieser Klasse speichern Informationen über ein bestimmtes Ereignis und ermöglichen es, diese Informationen von der Stelle, an der die Ausnahme aufgetreten ist, an den für ihre Behandlung verantwortlichen Code zu übertragen.

Nur Objekte, die zu `Throwable` oder einer ihrer Unterklassen gehören, können von der JVM oder vom Programmierer mit `throw` ausgelöst werden. Ebenso kann eine `catch`-Klausel nur Objekte dieser Hierarchie abfangen.

Zu den wichtigsten Methoden von `Throwable` gehören `getMessage()`, mit der die mit der Ausnahme verbundene Nachricht abgerufen werden kann, und `printStackTrace()`, die den Ausführungs-Stacktrace bis zu der Stelle anzeigt, an der die Ausnahme aufgetreten ist.

Die Klasse `Throwable` besitzt zwei direkte Unterklassen: `Exception` und `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Throwable-Hierarchie"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

Die Klasse `Error` repräsentiert schwerwiegende Bedingungen, von denen sich eine Anwendung im Allgemeinen nicht erholen kann. Dies sind abnormale Situationen, die während der Programmausführung normalerweise nicht auftreten sollten.

Zu den wichtigen Unterklassen von `Error` gehören `AssertionError`, `IOError` und `VirtualMachineError`. Letztere besitzt unter anderem die Unterklassen `InternalError`, `OutOfMemoryError`, `StackOverflowError` und `UnknownError`.

Fehler können von der JVM selbst ausgelöst werden, häufig als Folge von Bedingungen, die vom Betriebssystem oder von der Laufzeitumgebung erkannt wurden. Sie können auch explizit vom Programmierer erzeugt werden, beispielsweise durch `assert` oder `throw`.

<img src="/images/exceptionsError.png"
     alt="Error und seine Unterklassen"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

Die Klasse `Exception` repräsentiert Ausnahmen, die unter bestimmten Umständen behandelt werden können und von denen sich die Anwendung erholen kann.

Zu ihren Unterklassen gehören `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException` und `RuntimeException`.

Die `Exception`-Unterklassen, die keine Unterklassen von `RuntimeException` sind, werden **geprüfte Ausnahmen** (*checked exceptions*) genannt. Der Compiler verlangt, dass sie vom Programm ausdrücklich berücksichtigt werden. Dies kann geschehen, indem die Ausnahme mit einer `catch`-Klausel abgefangen wird oder indem mit `throws` deklariert wird, dass die Methode sie auslösen kann.

<img src="/images/descendentesException.png"
     alt="Exception und ihre Unterklassen"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

Unter den Unterklassen von `Exception` nimmt `RuntimeException` eine besondere Stellung ein. Sie und ihre Unterklassen werden **Laufzeitausnahmen** (*runtime exceptions*) genannt.

`RuntimeException` und ihre Unterklassen sind **ungeprüfte Ausnahmen** (*unchecked exceptions*). Der Compiler verlangt nicht, dass sie ausdrücklich mit `try`/`catch` behandelt oder mit `throws` deklariert werden.

Diese Art von Ausnahme repräsentiert häufig logische Fehler oder eine fehlerhafte Verwendung eines Programms. Häufige Beispiele sind:

- `ClassCastException`: tritt auf, wenn eine explizite Typumwandlung nicht möglich ist.
- `IllegalArgumentException`: zeigt an, dass eine Methode ein als ungültig oder ungeeignet betrachtetes Argument erhalten hat.
- `IndexOutOfBoundsException`: tritt auf, wenn versucht wird, auf eine nicht vorhandene Position in einer indizierten Struktur zuzugreifen.
- `NullPointerException`: tritt auf, wenn eine Operation mit einer `null`-Referenz ausgeführt wird.

Eine Methode, die eine `RuntimeException` auslösen kann, muss diese Möglichkeit nicht mit `throws` deklarieren. Natürlich ist es weiterhin möglich, diese Ausnahmen mit `try` und `catch` abzufangen und zu behandeln.

In der Praxis weisen viele `RuntimeException`-Instanzen auf Probleme hin, die vom Programm selbst hätten verhindert werden können. Wenn eine solche Ausnahme auftritt, ist es normalerweise wichtig, ihre Ursache zu untersuchen und das Problem zu beheben, anstatt die Ausnahme einfach abzufangen.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException und ihre Unterklassen"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Geprüfte und ungeprüfte Ausnahmen

Eine wichtige Unterscheidung in der Java-Ausnahmehierarchie besteht zwischen **geprüften** und **ungeprüften** Ausnahmen.

`Throwable` und alle seine Unterklassen, die keine Unterklassen von `RuntimeException` oder `Error` sind, werden **geprüfte Ausnahmen** genannt. `RuntimeException` und ihre Unterklassen sowie `Error` und seine Unterklassen werden **ungeprüfte Ausnahmen** genannt.

Geprüfte Ausnahmen müssen vom Programm behandelt oder ausdrücklich deklariert werden. Das bedeutet, dass eine Methode, die eine geprüfte Ausnahme auslösen kann, sie entweder mit einer `catch`-Klausel behandeln oder in ihrer `throws`-Klausel deklarieren muss.

Ungeprüfte Ausnahmen müssen dagegen nicht ausdrücklich behandelt oder deklariert werden. Der Compiler verlangt nicht, dass `RuntimeException`, `Error` oder ihre Unterklassen abgefangen oder deklariert werden.

In vereinfachter Form lässt sich die Hierarchie wie folgt darstellen:

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

Diese Organisation ermöglicht eine Behandlung auf unterschiedlichen Ebenen der Hierarchie. Eine `catch`-Klausel kann beispielsweise eine bestimmte Ausnahme oder eine ihrer Oberklassen abfangen, abhängig vom gewünschten Verhalten.

Das Verständnis dieser Hierarchie ist grundlegend für das Verständnis des Ausnahmebehandlungsmechanismus von Java und für die Entscheidung, welche Ausnahmen behandelt, welche weitergereicht und welche als Fehler betrachtet werden sollten, die im Programm selbst behoben werden müssen.

Dieser Artikel ist aus Inhalten des Buches <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> von <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a> adaptiert.
