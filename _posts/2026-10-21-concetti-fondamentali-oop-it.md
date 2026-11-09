---
layout: post
title: "Concetti fondamentali della programmazione orientata agli oggetti"
date: 2026-10-21
lang: it
translation_id: conceitos-basicos-poo-java
permalink: /concetti-fondamentali-oop-it/
share_text: >-
  Introduzione ai concetti fondamentali della programmazione orientata agli oggetti: classi, oggetti, attributi, metodi, incapsulamento, ereditarietà, polimorfismo e relazioni tra classi.
---

La programmazione strutturata offre meccanismi per modularizzare i concetti coinvolti in un sistema software tramite strutture dati e algoritmi che le manipolano. I linguaggi strutturati più usati permettono di rappresentare diversi tipi di dati e variabili per esprimere proprietà e caratteristiche dei concetti in questione, nonché procedure e funzioni per modellarne le operazioni.

Quando vogliamo riutilizzare componenti scritti con linguaggi strutturati, però, dobbiamo individuare la relazione tra i dati — rappresentati da strutture dati, tipi e variabili — e il comportamento — espresso da procedure e funzioni. Di conseguenza, il riuso avviene spesso a grana fine e può richiedere un notevole sforzo, per esempio per capire quali procedure e funzioni corrispondono a quali strutture dati. È possibile creare librerie riutilizzabili, ma la relazione tra dati e comportamento non è esplicita né concentrata in un’unica astrazione.

La **programmazione orientata agli oggetti** (OOP) è un paradigma che rappresenta i concetti di un determinato dominio applicativo tramite tipi di dati astratti chiamati classi. Le classi modellano sia le caratteristiche e le proprietà di tali concetti sia le relative operazioni. L’OOP estende la programmazione strutturata fornendo gli strumenti per specificare e comporre classi, così da modellare sistemi computazionali completi e ottenere maggiore modularità e riuso dei componenti.

Oggi la programmazione orientata agli oggetti è uno dei paradigmi più accettati e usati nello sviluppo software. Molti linguaggi moderni la supportano, tra cui Java, C++, C#, Python, Kotlin, JavaScript, TypeScript, Swift e Ruby.

Una **classe** è un meccanismo di astrazione usato per rappresentare concetti di un dominio applicativo. In un dominio bancario, per esempio, i concetti possono riguardare filiali, conti, clienti e transazioni. Potremmo definire classi come `Branch`, `Account`, `Customer` e `Transaction` per rappresentarli. La figura mostra una rappresentazione grafica di queste classi.

<img src="/images/en/oopClasses.svg" alt="Le classi Branch, Account, Customer e Transaction." style="max-width: 300px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Le classi fungono da *modelli* per creare esemplari concreti e manipolabili di questi concetti. Tali esemplari si chiamano **oggetti**. Un oggetto è un’**istanza** di una classe, e il processo di creazione di oggetti si chiama **istanziazione**. Potremmo, per esempio, creare oggetti che rappresentano i clienti *John*, *Peter* e *Mary*, con le rispettive informazioni personali e le funzionalità disponibili per i clienti.

<img src="/images/en/oopObjects.svg" alt="Gli oggetti John, Peter e Mary sono istanze della classe Customer." style="max-width: 380px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Una classe viene definita per rappresentare le proprietà, le caratteristiche e il comportamento di un concetto. I due meccanismi principali sono gli attributi e i metodi.

Gli **attributi** rappresentano le caratteristiche o le proprietà degli oggetti di una classe. Tra gli attributi di `Customer` potrebbero esserci *name*, *age*, *address* e *marital status*. Ogni cliente può avere valori diversi per questi attributi. Un oggetto che rappresenta un cliente potrebbe, per esempio, avere *name* $`=`$ John Smith, *age* $`=`$ 50, *address* $`=`$ 205 President Vargas Street e *marital status* $`=`$ married.

I **metodi** rappresentano il comportamento. Alcuni metodi di `Account` potrebbero riguardare le operazioni di *apertura*, *chiusura* o *cambio del titolare* di un conto. L’**invocazione** o la **chiamata** di un metodo esegue l’operazione implementata dal metodo stesso. Le classi hanno spesso metodi speciali per creare (istanziare) oggetti, chiamati **costruttori**, e per distruggerli, chiamati **distruttori**.

Attributi e metodi si dividono inoltre in due categorie: di istanza e di classe. Gli **attributi e metodi di istanza** sono i più comuni e si accedono tramite gli oggetti della classe. Rappresentano caratteristiche e operazioni associate alle singole istanze. Alcuni attributi di istanza di `Account` potrebbero essere *bank*, *branch*, *account number* e *account holder*; alcuni metodi di istanza potrebbero essere *withdraw*, *transfer* e *deposit*. Gli **attributi e metodi di classe**, invece, appartengono alla classe stessa e non alle sue istanze. Per esempio, un attributo di classe potrebbe contare quante istanze di `Account` sono state create e un metodo di classe potrebbe restituire quel numero.

Per limitare l’accesso ad attributi e metodi, le classi offrono meccanismi di **incapsulamento e occultamento dell’informazione**. I linguaggi di programmazione forniscono comunemente modificatori di visibilità che specificano chi può accedere a un attributo, metodo o classe.

Le classi sono meccanismi di astrazione che rappresentano e incapsulano concetti del mondo reale e del mondo computazionale. Le astrazioni possono essere combinate tramite relazioni affinché le classi collaborino al soddisfacimento dei requisiti di un’applicazione. Tra le principali relazioni tra classi figurano ereditarietà, associazione, aggregazione, composizione e realizzazione.

L’**ereditarietà** è un meccanismo di composizione che consente alle classi di riutilizzare l’interfaccia e il comportamento di classi esistenti estendendone le funzionalità. Una classe che ne estende un’altra è detta **sottoclasse**; la classe estesa è la **superclasse**. Di solito, l’estensione viene dichiarata nella sottoclasse, per esempio: `SubClass` estende `SuperClass`.

La figura 3 mostra le classi `Shape`, `Rectangle`, `Triangle` e `Circle`. `Shape` è la superclasse e `Rectangle`, `Triangle` e `Circle` sono le sue sottoclassi.

<img src="/images/en/oopInheritance.png" alt="Shape è la superclasse di Rectangle, Triangle e Circle." style="max-width: 400px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

I meccanismi di ereditarietà variano tra i linguaggi. Le differenze riguardano spesso visibilità e molteplicità. Alcuni linguaggi, come C++, permettono di specificare l’ereditarietà come **pubblica** o **privata**. Consideriamo una classe `A` e una classe `B` che eredita da `A`. In tal caso `A` è la superclasse di `B`, e `B` è la sottoclasse di `A`. Con l’ereditarietà pubblica, `B` è un sottotipo di `A` ed eredita sia l’implementazione sia l’interfaccia di `A`. Ovunque sia richiesto un oggetto `A`, si può usare un oggetto `B` (o un’altra sottoclasse di `A`), poiché ogni istanza di `B` è considerata anche un’istanza di `A`. Questo principio si chiama **principio di sostituzione di Liskov**. Con l’ereditarietà privata, `B` non è un `A`: eredita soltanto l’implementazione di `A` e viene realizzata in termini di `A`. In questo caso il principio di sostituzione di Liskov non si applica.

L’ereditarietà può anche essere **singola o multipla**. Nell’ereditarietà singola, usata da Java e C#, una classe può avere una sola superclasse. Con l’ereditarietà multipla, adottata per esempio da C++, una classe può avere più superclassi. I progettisti dei linguaggi non concordano sul fatto che i vantaggi dell’ereditarietà multipla giustifichino i problemi che può causare. Altri linguaggi offrono alternative, come l’ereditarietà virtuale basata su interfacce, i *trait* e i *mixin*.

La figura 4 mostra un esempio di ereditarietà multipla. `Mammal` e `Bird` rappresentano animali. `Horse`, `Dog` e `Bat` sono sottoclassi di `Mammal`, mentre `Ostrich` e `Duck` sono sottoclassi di `Bird`. Vogliamo anche classificare gli animali capaci di volare, quindi creiamo `Flyer`, una classe che rappresenta oggetti volanti non necessariamente animali. Con l’ereditarietà multipla, gli oggetti `Duck` e `Bat` possono essere anche oggetti volanti perché ereditano da `Flyer`.

<img src="/images/en/oopMultipleInheritance.png" alt="Ereditarietà multipla tra le classi Animal, Bird, Flyer e Mammal." style="max-width: 500px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Alcune classi sono **astratte**. Come le classi **concrete**, rappresentano le caratteristiche e il comportamento di un insieme di oggetti del mondo reale, ma non possono essere istanziate direttamente. Nell’esempio di ereditarietà multipla, `Mammal`, `Bird` e `Flyer` potrebbero essere astratte, perché nel mondo reale esistono solo esemplari delle sottoclassi, come cavalli, cani e anatre.

Oltre a visibilità e molteplicità, l’ereditarietà permette di creare metodi polimorfici. Nella programmazione orientata agli oggetti, il **polimorfismo** è la capacità di un’operazione di comportarsi in modo diverso secondo la classe dell’oggetto che la invoca. Le forme principali sono:

- Il **polimorfismo ad hoc (o overload)** si verifica quando una classe ha metodi con lo stesso nome ma tipi di parametri formali diversi. L’argomento usato determina quale metodo viene invocato.
- Il **polimorfismo parametrico** si verifica quando un metodo viene definito in modo generico e associato a un tipo specificato solo in seguito, per esempio quando si dichiara una variabile o si istanzia un oggetto. Nei linguaggi orientati agli oggetti questi sono detti tipi generici.
- Il **polimorfismo di sottotipo** si verifica quando una sottoclasse ridefinisce metodi di una superclasse. L’oggetto che invoca il metodo determina quale implementazione viene eseguita. La scelta avviene normalmente durante l’esecuzione tramite binding dinamico.

Oltre all’ereditarietà ci sono altre relazioni, tra cui associazione, aggregazione e composizione. In generale, differiscono per il grado di accoppiamento tra i partecipanti:

- Nell’**associazione**, il rapporto tra oggetti è spesso temporaneo e può essere modificato facilmente a runtime. In un sistema di traffico, per esempio, una persona può essere associata a un veicolo nel ruolo di conducente. Se il conducente cambia, entrambi gli oggetti continuano a esistere anche se l’associazione viene rimossa.
- Nell’**aggregazione**, il rapporto è più forte che nell’associazione. Gli oggetti aggregati vengono spesso creati insieme all’oggetto aggregatore. Un’automobile può avere quattro ruote: l’auto è l’oggetto aggregatore e le ruote sono gli oggetti aggregati. Il rapporto può essere sciolto, ma sostituire le ruote è meno comune e più impegnativo che cambiare conducente.
- Nella **composizione**, il rapporto è ancora più forte: gli oggetti composti sono parti di un oggetto più grande. Per esempio, il tessuto del sedile di un veicolo è fatto di fili. Se i fili cessano di esistere, anche il sedile cessa di esistere o perde la propria identità.

Queste relazioni tra oggetti sono spesso concettuali. Quando le si mappa in un linguaggio di programmazione, si possono associare, aggregare o comporre oggetti tramite attributi di classe, assegnando loro valori a runtime. Può cambiare il momento in cui gli oggetti vengono creati: in una composizione, quelli componenti vengono spesso creati nel costruttore dell’insieme; in un’associazione, gli oggetti correlati vengono solitamente creati in modo indipendente e collegati quando serve.

Un’ultima relazione, la **realizzazione**, si verifica quando una classe dichiara di implementare un’interfaccia. Un’**interfaccia** può essere vista come una classe astratta con tutti i metodi astratti[^1]. Funge da protocollo tra i client e chi la implementa. La classe (o una sua sottoclasse) deve implementare i metodi dichiarati dall’interfaccia. I client possono quindi scrivere codice conforme all’interfaccia senza dipendere da come le classi la implementano.

[^1]: Da Java 8, le interfacce possono anche definire metodi concreti chiamati metodi predefiniti, usando la parola chiave `default`. Le classi che implementano un’interfaccia con un metodo predefinito non sono obbligate a implementarlo, ma possono farlo.

---

*Questo articolo adatta contenuti del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> di <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articoli correlati

- [Classi in Java](/classi-java-it/)
- [Ereditarietà in Java](/ereditarieta-java-it/)
- [Polimorfismo in Java](/polimorfismo-java-it/)
- [Interfacce in Java](/interfacce-java-it/)
- [Link su OOP e Java](/link-oop-java-it/)
- [Esercizi di programmazione orientata agli oggetti](/esercizi-oop-it/)
