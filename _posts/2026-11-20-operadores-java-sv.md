---
layout: post
title: "Operatorer i Java"
date: 2026-11-20
lang: sv
translation_id: operadores-java
permalink: /sv/operators-in-java/
share_text: >-
  Aritmetiska operatorer, tilldelningar och jämförelser med exempel från boken.
---

## Aritmetiska operatorer

`+`, `-`, `*`, `/` och `%` står för addition, subtraktion, multiplikation, division och rest. Prioriteten styr hur uttrycken grupperas. `++` och `--` ändrar variabeln med ett.

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

I `y = x++` får `y` det gamla värdet 10. Sedan blir `x` 11.

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

I `y = ++x` sker ökningen först. Båda variablerna får värdet 11.

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Andra unära operatorer är `+`, `-`, `~` och `!`.

## Tilldelning

`=` tilldelar värdet av uttrycket till höger till variabeln till vänster.

```java
int age;
String name;
Double height;
```

Tilldelningen kan göras efter deklarationen.

```java
age = 20;
name = "Mary";
height = 1.70;
```

Variabeln kan också initieras i deklarationen.

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

## Sammansatt tilldelning

`+=`, `-=`, `*=`, `/=` och `%=` kombinerar en operation med en tilldelning.

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

Programmet visar värdena i följande ordning.

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

Vid sammansatt tilldelning utvärderas uttrycket till vänster en gång och dess typ beaktas. Det finns också sammansatta operatorer för skift och bitoperationer.

## Jämförelser

`==`, `!=`, `>`, `>=`, `<` och `<=` ger ett booleskt värde.

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

Vid indata 10 är tre villkor sanna eftersom varje `if` prövas separat. `Integer.parseInt` omvandlar texten till ett heltal.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
