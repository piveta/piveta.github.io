---
layout: post
title: "Wildcard e limiti nei tipi generici in Java"
date: 2026-09-03
lang: it
translation_id: wildcards-limites-java
permalink: /wildcard-limiti-tipi-generici-java/
share_text: >-
  Nei generics Java, <?> indica un tipo sconosciuto, mentre <? extends T> e <? super T> definiscono limiti superiore e inferiore. I wildcard rendono più flessibile il modo in cui i tipi generici accettano sottotipi e supertipi.
---

Oltre ai tipi generici specifici, possiamo usare le **wildcard** per esprimere tipi sconosciuti (`<?>`), limitare il tipo specificato a includere sottotipi di un determinato tipo (`<? extends Type>`) oppure includere supertipi (usando `<? super Type>`). Le sezioni seguenti descrivono rispettivamente wildcard non limitate, con limite superiore e con limite inferiore. Successivamente mostriamo come definire limiti multipli per i tipi generici.

## Wildcard non limitate

Per i tipi sconosciuti, usiamo il punto interrogativo come tipo, consentendo di utilizzare qualsiasi tipo in quel contesto. Ad esempio, se una variabile è dichiarata come `List<?>` (oppure è un attributo o un parametro), può ricevere oggetti `List` con qualsiasi parametro di tipo valido, come `String`, `Integer`, ecc. Questi tipi generici sconosciuti sono chiamati **wildcard non limitate** (`<?>`), perché non impongono alcun limite di tipo.

Ad esempio:

```java
List<?> l = new ArrayList<String>();
// oppure, per esempio
l = new LinkedList<Integer>();
```

Sebbene questa modalità di dichiarazione delle variabili possa sembrare interessante, presenta delle limitazioni. In questi casi non conosciamo il tipo degli oggetti presenti nella lista. Pertanto, non possiamo, ad esempio, aggiungere elementi alla lista (eccetto `null`, che è compatibile con qualsiasi tipo riferimento in Java), perché non vi è alcuna garanzia che l'oggetto aggiunto abbia lo stesso tipo del parametro di tipo della lista.

Se provassimo ad aggiungere un elemento alla lista (in questo caso `l`), otterremmo quindi un errore in fase di compilazione:

```java
void main(){
    List<?> l = new ArrayList<String>();
    // Compilation error: 
    //    "The method add(capture#2-of ?) in the type 
    //     List<capture#2-of ?> is not applicable 
    //     for the arguments (String)"
    l.add("Maria");
}
```

I tipi non limitati sono comunemente usati quando vogliamo soltanto leggere i dati, senza modificarli. Ad esempio, potremmo avere un metodo che riceve una lista e ne stampa gli elementi senza specificare il tipo degli elementi della lista:

```java
public void print(List<?> list) {
    for (Object obj : list)
        IO.println(obj);
}
void main(){
    print(List.of(1, 2, 3));
    print(List.of("A", "B", "C"));
}
```

L'esecuzione del metodo `main` mostrerebbe:

```text
1
2
3
A
B
C
```

Qui usiamo la stampa come esempio, ma potremmo iterare sugli oggetti, usarli negli *stream*, filtrarli con `instanceof`, ottenere la dimensione della lista, verificare se un determinato oggetto è contenuto, trasformarli e copiarli in una lista tipizzata, tra le altre operazioni. Ciò che non possiamo fare è modificare direttamente la lista (usando `add` o `set`, ad esempio, eccetto `null`).

## Wildcard con limite superiore

Le **wildcard con limite superiore** permettono di specificare che solo un oggetto di un determinato tipo o di uno dei suoi sottotipi (ottenuti tramite ereditarietà o implementazione di un'interfaccia) può essere usato come parametro di tipo. La notazione `<? extends T>` specifica che la wildcard deve essere del tipo `T` o di un tipo che estende `T`.

Ad esempio, se dichiaro una lista la cui wildcard estende `Number`, posso assegnarle oggetti di una qualsiasi delle sue sottoclassi (come `Double` o `Integer`). Se `Number` fosse una classe concreta (è astratta), potremmo anche assegnare un oggetto della classe stessa. Il seguente esempio mostra esattamente questo caso:

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

Come per le wildcard non limitate, non possiamo aggiungere elementi alla lista `l`, perché non conosciamo esattamente il tipo della lista. Pertanto, le prime due chiamate al metodo `add` producono errori di compilazione:

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

Sebbene leggendo il codice sappiamo che l'oggetto assegnato alla variabile `l` è una lista di interi, il compilatore sa che `l` ha un tipo sconosciuto e quindi non consente di aggiungere valori. In lettura, i valori vengono letti come `Number`, che rappresenta il limite superiore.

## Wildcard con limite inferiore

Le **wildcard con limite inferiore** permettono di specificare che solo un oggetto di un determinato tipo o di uno dei suoi supertipi può essere usato come parametro di tipo. La notazione `<? super T>` specifica che la wildcard deve essere del tipo `T` o di una sua superclasse.

Ad esempio, se dichiaro una lista la cui wildcard ha `Number` come limite inferiore, posso assegnarle oggetti di una qualsiasi delle sue superclassi (nel caso di `Number`, solo `Object`, poiché `Number` non ha una superclasse esplicita).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

È consentito aggiungere elementi del tipo del limite inferiore (in questo caso `Number`) o di uno dei suoi sottotipi (come `Double` o `Integer`, ad esempio). L'esempio seguente mostra una lista la cui wildcard ha `Number` come limite inferiore. In questo caso possiamo istanziare una `ArrayList` di numeri (o della sua superclasse `Object`). Possiamo aggiungere elementi di una delle sue sottoclassi (non possiamo aggiungere un oggetto di tipo `Number` perché è una classe astratta, che non può avere istanze dirette). L'esempio mostra tre inserimenti. I primi due sono consentiti perché gli elementi sono sottotipi di `Number` (`10` è un `Integer` e `1.0` è un `Double`). Il terzo inserimento non è consentito e produce un errore di compilazione perché `Object` non è un discendente di `Number`.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

Se creassimo l'`ArrayList` con `Object` come parametro di tipo, il terzo inserimento continuerebbe a non essere consentito in fase di compilazione, producendo lo stesso errore (e i primi due inserimenti rimarrebbero consentiti), perché il tipo della lista è ancora sconosciuto (sappiamo solo che è `Number` o uno dei suoi supertipi).

## Limiti multipli

In Java, un tipo generico può avere **limiti multipli**, il che significa che il parametro di tipo può essere ristretto ai tipi che estendono (o sono) una classe specifica e che implementano una o più interfacce. La sintassi segue la forma `<T extends Class & Interface1 & Interface2>`. Se viene usata una classe come limite, deve essere specificata per prima, seguita dalle interfacce. Se non c'è una classe, è possibile elencare solo interfacce.

Ad esempio, la classe `MultipleBounds` ha un tipo generico `T` che estende la classe `Number` e implementa le interfacce `Comparable<T>` e `Serializable`:

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

In questo esempio, `T` può essere `Number` o un tipo che eredita da `Number` e implementa anche `Comparable<T>` e `Serializable`. Questo è utile quando abbiamo bisogno di più garanzie, ad esempio l'accesso ai metodi della superclasse e ai contratti definiti da diverse interfacce. Questa combinazione rende il codice più flessibile pur mantenendo la tipizzazione forte, evitando errori in fase di compilazione e garantendo che tutti i metodi richiesti siano disponibili per il tipo generico utilizzato.

---

*Questo articolo è adattato dai contenuti del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, di <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
