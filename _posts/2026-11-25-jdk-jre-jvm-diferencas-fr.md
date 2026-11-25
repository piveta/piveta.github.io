---
layout: post
title: "JDK, JRE et JVM : quelle différence en Java ?"
date: 2026-11-25
lang: fr
translation_id: jdk-jre-jvm-diferencas
permalink: /fr/differences-jdk-jre-jvm/
share_text: >-
  Comprenez les rôles de la JVM, du JRE et du JDK, et découvrez les commandes qui vérifient l’environnement Java.
---

## JVM, JRE et JDK
La **JVM** (Java Virtual Machine) exécute le bytecode Java. Elle charge les classes, vérifie et exécute les instructions, et gère des ressources comme la mémoire. Le même bytecode peut fonctionner sur différents systèmes lorsqu’une JVM compatible est disponible.

Le **JRE** (Java Runtime Environment) désigne l’environnement nécessaire à l’exécution des applications Java, avec la JVM et les bibliothèques. La disponibilité de paquets JRE autonomes dépend de la distribution et de sa version. Certaines applications intègrent leur propre environnement d’exécution.

Le **JDK** (Java Development Kit) réunit l’environnement d’exécution et les outils de développement, notamment le compilateur <code>javac</code>, le lanceur <code>java</code> et d’autres outils pour créer, exécuter et diagnostiquer des applications.

## Que faut-il installer pour programmer ?
Pour développer en Java, installez un JDK adapté au projet. La distribution fournit la JVM et les outils nécessaires. Oracle JDK et Eclipse Temurin sont des exemples de distributions.

Dans un terminal, vérifiez les commandes :

~~~text
java --version
javac --version
~~~

La première affiche la version du lanceur Java ; la seconde, celle du compilateur. Si <code>java</code> fonctionne mais que <code>javac</code> est introuvable, vérifiez l’installation du JDK et la présence de son dossier <code>bin</code> dans le <code>PATH</code>.

Sous Windows, <code>where java</code> et <code>where javac</code> indiquent l’exécutable utilisé. Sous macOS et Linux, utilisez <code>which java</code> et <code>which javac</code>.

## Du code source à l’exécution
Dans <code>Hello.java</code>, le compilateur transforme le code source en bytecode :

~~~text
javac Hello.java
java Hello
~~~

La première commande crée <code>Hello.class</code>. La deuxième démarre la JVM pour exécuter la classe. La compatibilité dépend des versions utilisées pour compiler et exécuter.

## Références
- [Présentation de la plateforme Java et de la JVM](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [Guide d’installation du JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
