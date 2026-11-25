---
layout: post
title: "Versioni di Java: LTS, aggiornamenti e come verificare la versione"
date: 2026-11-25
lang: it
translation_id: versoes-java-lts-atualizacao
permalink: /it/versioni-java-lts-aggiornamenti/
share_text: >-
  Scopri il ciclo delle versioni Java, il significato di LTS e come verificare e aggiornare un JDK.
---

## Verifica la versione di Java
Esegui questi comandi nel terminale:

~~~text
java --version
javac --version
~~~

Il primo identifica il launcher Java usato per avviare le applicazioni; il secondo il compilatore. Con più JDK installati, l’eseguibile trovato nel <code>PATH</code> può essere diverso da quello configurato nell’IDE.

## Versioni Java e LTS
Java pubblica versioni con nuove funzionalità ogni sei mesi. Una versione **LTS** (*long-term support*) riceve supporto a lungo termine da determinati fornitori. Durata, prezzo e condizioni dipendono dalla distribuzione e dal provider.

Nella roadmap di Oracle, Java 8, 11, 17, 21 e 25 sono versioni LTS. Oracle prevede una nuova LTS ogni due anni. Prima di scegliere la versione per la produzione, consulta la roadmap aggiornata e la politica del provider.

La scelta dipende anche da librerie, strumenti e requisiti dell’applicazione. Una LTS offre un orizzonte di supporto più lungo; le versioni intermedie offrono prima le novità.

## Dove consultare versioni e JEP
Oracle mantiene un [indice delle note di rilascio del JDK](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html), con collegamenti ai rilasci e agli aggiornamenti. Le note descrivono modifiche, correzioni e funzionalità introdotte o rimosse. Le [note del JDK 27](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) illustrano le novità e rimandano alle JEP correlate.

Una **JEP** (*JDK Enhancement Proposal*) documenta una proposta di miglioramento del JDK, con obiettivi, soluzione e stato. Alcune funzionalità vengono introdotte come *preview* o *incubator* e possono cambiare prima di diventare definitive.

Consulta le [modifiche al linguaggio Java per versione](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html) e il [riepilogo delle modifiche](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html) per confrontare funzionalità definitive e in anteprima.

## Aggiorna Java
1. Identifica la versione con <code>java --version</code> e <code>javac --version</code>.
2. Controlla cosa supportano progetto, dipendenze e ambiente di produzione.
3. Scarica un aggiornamento della distribuzione usata oppure scegline una compatibile.
4. Installa il JDK e, se necessario, modifica <code>PATH</code>, <code>JAVA_HOME</code> e le impostazioni dell’IDE.
5. Apri un nuovo terminale, verifica le versioni ed esegui i test dell’applicazione.

Aggiornare all’interno della stessa linea e migrare a una versione principale sono decisioni diverse. Prima della migrazione, leggi le note e prova applicazione e dipendenze.

Su Windows, <code>where.exe java</code> e <code>where.exe javac</code> mostrano gli eseguibili trovati. Su macOS o Linux, usa <code>which java</code> e <code>which javac</code>.

## Riferimenti
- [Roadmap di supporto Oracle Java SE](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [FAQ sulle licenze Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
