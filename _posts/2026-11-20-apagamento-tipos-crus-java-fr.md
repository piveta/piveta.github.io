---
layout: post
title: "Effacement des types et types bruts en Java"
date: 2026-11-20
lang: fr
translation_id: apagamento-tipos-crus-java
permalink: /fr/type-erasure-and-raw-types-in-java/
share_text: >-
  L'effacement préserve la compatibilité ; les types bruts perdent les vérifications des éléments.
---

Java 5 a introduit les génériques en préservant la compatibilité avec les programmes antérieurs. Par **effacement des types** (*type erasure*), le compilateur vérifie les paramètres puis les retire de la représentation exécutée par la JVM. Il les remplace par leurs bornes, en général `Object` ou la première borne déclarée.

Après effacement, `Adapter<T>` ressemble approximativement à une classe utilisant `Object` :

```java
public class Adapter{
    Object object;
    public Object get(){
        return object;
    }
    public void set(Object value){
        object = value;
    }
    public Adapter(Object initial){
        object = initial;
    }
}
```

Un client sans paramètres de type prendrait cette forme :

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

Ces fragments **illustrent** le procédé, sans transcrire littéralement le bytecode. Les arguments de type ne sont plus accessibles à l'exécution comme ils l'étaient à la compilation, ce qui limite certaines opérations de réflexion.

## Types bruts

Une liste paramétrée vérifie le type de ses éléments :

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

Un *type brut* omet l'argument de type à la déclaration comme à la construction :

```java
void main(){
    List names = new ArrayList();
}
```

On perd ainsi la vérification offerte par `List<String>` ; la liste accepte une chaîne et un entier :

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>` est une liste d'un type **inconnu** dans laquelle on ne peut ajouter d'éléments arbitraires, hormis `null`. Une `List` brute accepte des éléments sans cette vérification. Dans un nouveau programme, préférez un argument de type ou un joker ; réservez les types bruts à l'interopérabilité avec du code ancien.

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
