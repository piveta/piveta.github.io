---
layout: post
title: "Les classes d’exceptions en Java"
date: 2026-08-27
lang: fr
translation_id: classes-de-excecao
permalink: /classes-exceptions-java-fr/
image: /images/descendentesThrowable.png
share_text: >-
  Dans la hiérarchie Java, Throwable se divise notamment en Error et Exception, tandis que RuntimeException relève des exceptions non vérifiées. L’article explique ce qui distingue les exceptions vérifiées des non vérifiées.
---
Pendant l’exécution d’un programme, des situations peuvent survenir et nécessiter un traitement particulier. Elles peuvent représenter des conditions anormales ou erronées, des situations qui n’avaient pas été prévues par le programmeur ou même des flux d’exécution alternatifs. Ces conditions sont appelées **exceptions**.

En Java, les exceptions sont représentées par des objets appartenant à la classe `Throwable` ou à l’une de ses sous-classes. La hiérarchie des exceptions est importante pour comprendre quelles exceptions peuvent être levées, interceptées et traitées par les programmes.

## Throwable

`Throwable` est la classe de base de la hiérarchie des exceptions en Java. Les objets de cette classe stockent des informations sur un événement particulier et permettent de transférer ces informations du point où l’exception s’est produite vers le code responsable de son traitement.

Seuls les objets appartenant à `Throwable` ou à l’une de ses sous-classes peuvent être levés par la JVM ou par le programmeur à l’aide de `throw`. De même, une clause `catch` ne peut intercepter que des objets appartenant à cette hiérarchie.

Parmi les principales méthodes de `Throwable` figurent `getMessage()`, qui permet d’obtenir le message associé à l’exception, et `printStackTrace()`, qui affiche la trace de la pile d’exécution jusqu’au point où l’exception s’est produite.

La classe `Throwable` possède deux sous-classes directes : `Exception` et `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Hiérarchie de Throwable"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

La classe `Error` représente des conditions graves dont une application ne peut généralement pas se remettre. Il s’agit de situations anormales qui ne devraient normalement pas se produire pendant l’exécution du programme.

Parmi les sous-classes importantes de `Error` figurent `AssertionError`, `IOError` et `VirtualMachineError`. Cette dernière possède notamment les sous-classes `InternalError`, `OutOfMemoryError`, `StackOverflowError` et `UnknownError`.

Les erreurs peuvent être levées par la JVM elle-même, souvent à la suite de conditions détectées par le système d’exploitation ou l’environnement d’exécution. Elles peuvent également être produites explicitement par le programmeur, par exemple au moyen de `assert` ou de `throw`.

<img src="/images/exceptionsError.png"
     alt="Error et ses sous-classes"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

La classe `Exception` représente des exceptions qui, dans certaines circonstances, peuvent être traitées et dont l’application peut se remettre.

Ses sous-classes comprennent `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException` et `RuntimeException`.

Les sous-classes de `Exception` qui ne sont pas des sous-classes de `RuntimeException` sont appelées **exceptions vérifiées** (*checked exceptions*). Le compilateur exige qu’elles soient explicitement prises en compte par le programme. Cela peut être fait en interceptant l’exception avec une clause `catch` ou en déclarant, avec `throws`, que la méthode peut la lever.

<img src="/images/descendentesException.png"
     alt="Exception et ses sous-classes"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

Parmi les sous-classes de `Exception`, `RuntimeException` se distingue. Elle et ses sous-classes sont appelées **exceptions d’exécution** (*runtime exceptions*).

`RuntimeException` et ses sous-classes sont des **exceptions non vérifiées** (*unchecked exceptions*). Le compilateur n’exige pas qu’elles soient explicitement traitées avec `try`/`catch` ou déclarées avec `throws`.

Ce type d’exception représente généralement des erreurs logiques ou une utilisation incorrecte d’un programme. Parmi les exemples courants figurent :

- `ClassCastException` : se produit lorsqu’une conversion de type explicite n’est pas possible.
- `IllegalArgumentException` : indique qu’une méthode a reçu un argument considéré comme invalide ou inapproprié.
- `IndexOutOfBoundsException` : se produit lorsqu’une tentative est faite pour accéder à une position inexistante dans une structure indexée.
- `NullPointerException` : se produit lorsqu’une opération est effectuée sur une référence `null`.

Une méthode susceptible de lever une `RuntimeException` n’a pas besoin de déclarer cette possibilité avec `throws`. Il reste naturellement possible d’intercepter et de traiter ces exceptions avec `try` et `catch`.

En pratique, de nombreuses instances de `RuntimeException` indiquent des problèmes qui auraient pu être évités par le programme lui-même. Lorsqu’une telle exception se produit, il est généralement important d’en rechercher la cause et de corriger le problème plutôt que de simplement intercepter l’exception.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException et ses sous-classes"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exceptions vérifiées et non vérifiées

Une distinction importante dans la hiérarchie des exceptions Java est celle entre les **exceptions vérifiées** et les **exceptions non vérifiées**.

`Throwable` et toutes ses sous-classes qui ne sont pas des sous-classes de `RuntimeException` ou de `Error` sont appelées **exceptions vérifiées**. `RuntimeException` et ses sous-classes, ainsi que `Error` et ses sous-classes, sont appelées **exceptions non vérifiées**.

Les exceptions vérifiées doivent être traitées ou déclarées explicitement par le programme. Cela signifie que lorsqu’une méthode peut lever une exception vérifiée, celle-ci doit être traitée par une clause `catch` ou déclarée dans la clause `throws` de la méthode.

Les exceptions non vérifiées, en revanche, n’ont pas besoin d’être explicitement traitées ou déclarées. Le compilateur n’exige pas que `RuntimeException`, `Error` ou leurs sous-classes soient interceptées ou déclarées.

Sous une forme simplifiée, la hiérarchie peut être représentée ainsi :

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

Cette organisation permet d’effectuer le traitement à différents niveaux de la hiérarchie. Une clause `catch` peut, par exemple, intercepter une exception particulière ou l’une de ses superclasses, selon le comportement souhaité.

Comprendre cette hiérarchie est fondamental pour comprendre le mécanisme de gestion des exceptions de Java et pour décider quelles exceptions doivent être traitées, lesquelles doivent être propagées et lesquelles représentent des erreurs qui doivent être corrigées dans le programme lui-même.

Cet article est adapté du contenu du livre <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, d’<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.
