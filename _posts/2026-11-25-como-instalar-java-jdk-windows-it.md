---
layout: post
title: "Come installare Java e il JDK su Windows"
date: 2026-11-25
lang: it
translation_id: como-instalar-java-jdk-windows
permalink: /it/installare-java-jdk-windows/
share_text: >-
  Scarica e installa un JDK su Windows, poi verifica l’installazione con java e javac.
---

## Scegli una distribuzione Java
Per programmare in Java su Windows, scarica un **JDK** compatibile con il progetto. Oracle JDK ed Eclipse Temurin sono distribuzioni disponibili. Una versione LTS può essere adatta ai progetti che richiedono supporto a lungo termine. Controlla i requisiti e le condizioni della distribuzione.

Nelle Impostazioni di Windows verifica il tipo di sistema e l’architettura del processore. Scegli il pacchetto corretto, per esempio x64 o AArch64, e l’installer per Windows.

## Scarica e installa il JDK
Per Eclipse Temurin:

1. Apri la [pagina di download di Adoptium](https://adoptium.net/temurin/releases/).
2. Seleziona versione Java, Windows, architettura e pacchetto **JDK**.
3. Scarica ed esegui l’installer MSI.
4. Controlla se Java verrà aggiunto a <code>PATH</code>. Se un altro strumento richiede <code>JAVA_HOME</code>, seleziona anche questa opzione.
5. Completa l’installazione e apri un nuovo terminale.

In Temurin, aggiungere Java a <code>PATH</code> è un’opzione standard; impostare <code>JAVA_HOME</code> è un’opzione aggiuntiva.

## Verifica l’installazione
In PowerShell o nel Prompt dei comandi esegui:

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

I primi due comandi mostrano le versioni di Java e del compilatore. Gli altri indicano gli eseguibili trovati in <code>PATH</code>. Se un comando non viene trovato, apri un nuovo terminale e verifica le variabili d’ambiente. Se compare una versione diversa, controlla l’ordine delle cartelle in <code>PATH</code>.

Salva il codice come <code>Hello.java</code> per provare la compilazione:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

L’esempio usa la dichiarazione compatta e <code>IO.println</code>, disponibili da Java 25. Esegui:

~~~text
javac Hello.java
java Hello
~~~

L’output è <code>Hello World!</code>. Prima di Java 25, usa la forma di programma supportata dal JDK installato.

## Riferimenti
- [Installer MSI di Eclipse Temurin](https://adoptium.net/installation/windows/)
- [Installazione Oracle JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
