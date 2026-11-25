---
layout: post
title: "Opérateurs en Java"
date: 2026-11-20
lang: fr
translation_id: operadores-java
permalink: /fr/operators-in-java/
share_text: >-
  Opérateurs en Java : exemples du livre en anglais.
---

Les opérateurs arithmétiques binaires comprennent `+`, `-`, `*`, `/` et `%`. Les opérateurs `++` et `--` modifient une variable d’une unité :

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

Dans `y = x++`, l’ancienne valeur est affectée avant l’incrémentation :

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Dans `y = ++x`, l’incrémentation précède l’affectation :

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

L’opérateur `=` affecte une valeur. On peut déclarer les variables :

```java
int age;
String name;
Double height;
```

Puis leur affecter des valeurs :

```java
age = 20;
name = "Mary";
height = 1.70;
```

Ou les initialiser directement :

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

Les opérateurs `+=`, `-=`, `*=`, `/=` et `%=` combinent opération et affectation :

```java
void main() {
    int a = 10;
    a += 10;
    IO.println("a = " + a);
    a -= 10;
    IO.println("a = " + a); 
    a *= 10;
    IO.println("a = " + a); 
    a /= 10;
    IO.println("a = " + a); 
    a %= 3;
    IO.println("a = " + a); 
}
```

La sortie est :

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

Les opérateurs relationnels `==`, `!=`, `>`, `>=`, `<` et `<=` produisent un booléen. Chaque `if` est indépendant :

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age == 10)
        IO.println("Age equals 10 years");
    if (age != 20)
        IO.println("Age differs from 20 years");
    if (age > 30)
        IO.println("Age is over 30 years");
    if (age <= 80)
        IO.println("Age is at most 80 years");
}
```

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
