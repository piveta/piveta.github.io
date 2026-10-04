---
layout: post
title: "Hello World - Versione tradizionale vs. versione semplificata"
date: 2026-08-22
lang: it
translation_id: hello-world
permalink: /hello-world-it/
share_text: >-
  L’esempio mette a confronto la classe Java con main e la forma di avvio semplificata introdotta da Java 25+. In entrambi i casi, il programma mostra lo stesso messaggio Hello World.
---

È consuetudine iniziare lo studio di un linguaggio di programmazione scrivendo un programma chiamato **Hello World**, che visualizza il testo `Hello World!` sull’output standard del dispositivo, generalmente lo schermo. In Java, possiamo scrivere questo programma come segue:

```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```

In questo programma abbiamo una classe denominata `Hello`. Nei sistemi orientati agli oggetti, le classi aiutano a modellare i concetti del dominio applicativo studiato. Le classi incapsulano sia i dati sia il comportamento associati a un determinato concetto.

La classe `Hello` ha un solo metodo, chiamato `main`, che riceve un array di stringhe contenente gli argomenti della riga di comando forniti durante l’esecuzione del programma, se presenti. In questo esempio, tali argomenti non vengono utilizzati.

Il metodo `main` è statico, il che significa che è un metodo di classe e non un metodo di istanza. Pertanto, può essere chiamato senza creare un oggetto della classe `Hello`.

All’interno del metodo `main` viene effettuata una chiamata al metodo `println`. Questo metodo appartiene alla classe `PrintStream` e stampa sullo schermo il valore passato come argomento, seguito da un terminatore di riga.

Il metodo `println` viene chiamato tramite il campo `out` della classe `System`. Questo campo è di tipo `PrintStream` e fornisce accesso all’output standard del sistema.

## Compilazione ed esecuzione

I programmi Java vengono prima compilati in una rappresentazione intermedia chiamata **bytecode**, che garantisce la portabilità. Questi bytecode vengono successivamente eseguiti da una Java Virtual Machine (JVM), che li converte in codice macchina adatto alla piattaforma sottostante.

Per compilare il programma, è necessario salvarlo in un file denominato `Hello.java`. In Java, i file che contengono tipi pubblici hanno normalmente lo stesso nome del tipo.

Possiamo utilizzare un ambiente di sviluppo integrato (**IDE**) oppure invocare direttamente il compilatore dalla riga di comando, purché sia installato un JDK.

I programmi Java vengono normalmente scritti in un IDE, che offre funzionalità che migliorano la produttività durante lo sviluppo, come la navigazione nel codice sorgente, il refactoring, l’analisi statica, la compilazione, i test e il debugging.

Alcuni degli IDE più popolari per Java sono:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

Possiamo anche compilare direttamente il programma dalla riga di comando usando il compilatore `javac`:

```text
    javac Hello.java
```

Il comando riceve `Hello.java` come input e produce il file `Hello.class`, che contiene la versione compilata del programma.

Dopo la compilazione, possiamo eseguire il programma usando il comando `java`:

```text
    java Hello
```

L’output sarà:

```text
    Hello World!
```

## Un approccio più semplice con Java 25+

A partire da Java 25, una funzionalità sviluppata come *preview* a partire da Java 21 è diventata definitiva: **Compact Source Files and Instance Main Methods**. Consente di scrivere piccoli programmi con meno codice standard, omettendo la dichiarazione esplicita della classe e semplificando il metodo `main`.

Pertanto, il programma precedente può ora essere scritto in Java 26 (la versione attuale) come segue:

```java
    void main() {
        IO.println("Hello World!");
    }
```

In questo caso, non è necessario dichiarare esplicitamente la classe né scrivere `public static void main(String[] args)`. Il compilatore considera il file come se dichiarasse implicitamente una classe e il metodo `main` può essere un metodo di istanza.

Possiamo anche utilizzare la classe `IO`, che fornisce semplici operazioni di input e output sulla console. In Java 26, `IO` appartiene al package `java.lang` ed è quindi disponibile implicitamente. Per chiamare i suoi metodi, tuttavia, dobbiamo utilizzare il nome della classe, come in `IO.println(...)`.

Poiché questa funzionalità non è più in stato di *preview*, non sono necessarie opzioni speciali di compilazione. Il programma può essere compilato normalmente:

```text
    javac Hello.java
```

ed eseguito nello stesso modo:

```text
    java Hello
```

È inoltre possibile eseguire direttamente un file sorgente utilizzando il launcher `java`:

```text
    java Hello.java
```

In questo caso, il codice sorgente viene compilato in memoria dal launcher stesso prima dell’esecuzione. Questo meccanismo consente di eseguire programmi direttamente dai file sorgente senza produrre esplicitamente un file `.class`.

L’uso dei file sorgente compatti è particolarmente interessante per piccoli esempi, programmi didattici, script e sperimentazioni. Quando il programma cresce e richiede una struttura più elaborata, possiamo naturalmente tornare alla forma tradizionale, con dichiarazioni esplicite di classi e metodi.

Il processo eseguito dagli IDE è essenzialmente simile. Oltre alla compilazione e all’esecuzione, essi forniscono funzionalità per il debugging, i test, il refactoring, la creazione e la gestione dei progetti, la creazione di librerie, la gestione delle versioni e molte altre attività.

---

*Questo articolo è un adattamento di contenuti del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, di <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
