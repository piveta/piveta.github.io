---
layout: post
title: "Le classi delle eccezioni in Java"
date: 2026-08-27
lang: it
translation_id: classes-de-excecao
permalink: /classi-eccezioni-java-it/
image: /images/descendentesThrowable.png
---
Durante l’esecuzione di un programma possono verificarsi situazioni che richiedono una gestione particolare. Possono rappresentare condizioni anomale o errate, situazioni non previste dal programmatore o persino flussi di esecuzione alternativi. Queste condizioni sono chiamate **eccezioni**.

In Java, le eccezioni sono rappresentate da oggetti appartenenti alla classe `Throwable` o a una delle sue sottoclassi. La gerarchia delle eccezioni è importante per comprendere quali eccezioni possono essere lanciate, intercettate e gestite dai programmi.

## Throwable

`Throwable` è la classe base della gerarchia delle eccezioni in Java. Gli oggetti di questa classe memorizzano informazioni relative a un determinato evento e permettono di trasferire tali informazioni dal punto in cui si è verificata l’eccezione al codice responsabile della sua gestione.

Solo gli oggetti appartenenti a `Throwable` o a una delle sue sottoclassi possono essere lanciati dalla JVM o dal programmatore mediante `throw`. Allo stesso modo, una clausola `catch` può intercettare solo oggetti appartenenti a questa gerarchia.

Tra i principali metodi di `Throwable` ci sono `getMessage()`, che permette di ottenere il messaggio associato all’eccezione, e `printStackTrace()`, che visualizza lo stack trace dell’esecuzione fino al punto in cui si è verificata l’eccezione.

La classe `Throwable` ha due sottoclassi dirette: `Exception` e `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Gerarchia di Throwable"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

La classe `Error` rappresenta condizioni gravi dalle quali un’applicazione generalmente non può recuperare. Si tratta di situazioni anomale che normalmente non dovrebbero verificarsi durante l’esecuzione del programma.

Tra le sottoclassi importanti di `Error` ci sono `AssertionError`, `IOError` e `VirtualMachineError`. Quest’ultima ha, tra le altre, le sottoclassi `InternalError`, `OutOfMemoryError`, `StackOverflowError` e `UnknownError`.

Gli errori possono essere lanciati dalla JVM stessa, spesso come conseguenza di condizioni rilevate dal sistema operativo o dall’ambiente di esecuzione. Possono anche essere prodotti esplicitamente dal programmatore, per esempio tramite `assert` o `throw`.

<img src="/images/exceptionsError.png"
     alt="Error e le sue sottoclassi"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

La classe `Exception` rappresenta eccezioni che, in determinate circostanze, possono essere gestite e dalle quali l’applicazione può recuperare.

Le sue sottoclassi includono `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException` e `RuntimeException`.

Le sottoclassi di `Exception` che non sono sottoclassi di `RuntimeException` sono chiamate **eccezioni controllate** (*checked exceptions*). Il compilatore richiede che siano esplicitamente considerate dal programma. Questo può essere fatto intercettando l’eccezione con una clausola `catch` oppure dichiarando, tramite `throws`, che il metodo può lanciarla.

<img src="/images/descendentesException.png"
     alt="Exception e le sue sottoclassi"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

Tra le sottoclassi di `Exception`, `RuntimeException` occupa una posizione particolare. Essa e le sue sottoclassi sono chiamate **eccezioni a runtime** (*runtime exceptions*).

`RuntimeException` e le sue sottoclassi sono **eccezioni non controllate** (*unchecked exceptions*). Il compilatore non richiede che siano gestite esplicitamente con `try`/`catch` o dichiarate con `throws`.

Questo tipo di eccezione rappresenta generalmente errori logici o un uso scorretto del programma. Alcuni esempi comuni sono:

- `ClassCastException`: si verifica quando una conversione esplicita di tipo non è possibile.
- `IllegalArgumentException`: indica che un metodo ha ricevuto un argomento considerato non valido o inappropriato.
- `IndexOutOfBoundsException`: si verifica quando si tenta di accedere a una posizione inesistente in una struttura indicizzata.
- `NullPointerException`: si verifica quando viene eseguita un’operazione su un riferimento `null`.

Un metodo che può lanciare una `RuntimeException` non deve dichiarare questa possibilità con `throws`. Naturalmente, è comunque possibile intercettare e gestire queste eccezioni con `try` e `catch`.

In pratica, molte istanze di `RuntimeException` indicano problemi che avrebbero potuto essere evitati dal programma stesso. Quando se ne verifica una, è generalmente importante individuarne la causa e correggere il problema anziché limitarsi a intercettare l’eccezione.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException e le sue sottoclassi"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Eccezioni controllate e non controllate

Una distinzione importante nella gerarchia delle eccezioni di Java è quella tra **eccezioni controllate** ed **eccezioni non controllate**.

`Throwable` e tutte le sue sottoclassi che non sono sottoclassi di `RuntimeException` o `Error` sono chiamate **eccezioni controllate**. `RuntimeException` e le sue sottoclassi, così come `Error` e le sue sottoclassi, sono chiamate **eccezioni non controllate**.

Le eccezioni controllate devono essere gestite o dichiarate esplicitamente dal programma. Ciò significa che, quando un metodo può lanciare un’eccezione controllata, questa deve essere gestita da una clausola `catch` oppure dichiarata nella clausola `throws` del metodo.

Le eccezioni non controllate, invece, non devono essere gestite o dichiarate esplicitamente. Il compilatore non richiede che `RuntimeException`, `Error` o le loro sottoclassi vengano intercettate o dichiarate.

In forma semplificata, la gerarchia può essere visualizzata come segue:

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

Questa organizzazione permette di effettuare la gestione a diversi livelli della gerarchia. Una clausola `catch` può, per esempio, intercettare un’eccezione specifica o una delle sue superclassi, a seconda del comportamento desiderato.

Comprendere questa gerarchia è fondamentale per comprendere il meccanismo di gestione delle eccezioni di Java e per decidere quali eccezioni devono essere gestite, quali devono essere propagate e quali rappresentano errori che devono essere corretti nel programma stesso.

Questo articolo è adattato da contenuti del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, di <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.
