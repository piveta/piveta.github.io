---
layout: post
title: "Typradering och råa typer i Java"
date: 2026-11-20
lang: sv
translation_id: apagamento-tipos-crus-java
permalink: /sv/type-erasure-and-raw-types-in-java/
share_text: >-
  Typradering bevarar kompatibiliteten; råa typer förlorar kontrollen av elementtyper.
---

Java 5 införde generiska typer och behöll kompatibiliteten med äldre kod. Genom **typradering** (*type erasure*) kontrollerar kompilatorn typparametrarna och tar sedan bort dem ur representationen som JVM kör. De ersätts av sina gränser, vanligen `Object` eller den första deklarerade gränsen.

Efter radering liknar `Adapter<T>` ungefär en klass som använder `Object`:

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

En klient utan typparametrar skulle se ut så här:

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

Kodstyckena **illustrerar** processen och är inte en bokstavlig återgivning av bytecode. Typargument finns inte tillgängliga under körning på samma sätt som vid kompilering, vilket begränsar viss reflektion.

## Råa typer

En parameteriserad lista kontrollerar elementens typ:

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

En *rå typ* utelämnar typargumentet både i deklarationen och vid konstruktionen:

```java
void main(){
    List names = new ArrayList();
}
```

Då förloras kontrollen som `List<String>` ger, så listan kan innehålla både en sträng och ett heltal:

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>` är en lista med **okänd typ**, där inga godtyckliga element utom `null` får läggas till. En rå `List` accepterar dem utan motsvarande kontroll. Använd en typparameter eller wildcard i ny kod och spara råa typer för samspel med äldre bibliotek.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
