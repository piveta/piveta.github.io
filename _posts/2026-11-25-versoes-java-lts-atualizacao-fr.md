---
layout: post
title: "Versions de Java : LTS, mises à jour et vérification"
date: 2026-11-25
lang: fr
translation_id: versoes-java-lts-atualizacao
permalink: /fr/versions-java-lts-mises-a-jour/
share_text: >-
  Découvrez le rythme des versions Java, la signification de LTS et comment vérifier et mettre à jour un JDK.
---

## Vérifier la version de Java
Exécutez ces commandes dans un terminal :

~~~text
java --version
javac --version
~~~

La première identifie le lanceur Java utilisé pour démarrer les applications ; la seconde, le compilateur. Avec plusieurs JDK installés, l’exécutable trouvé dans le <code>PATH</code> peut différer de celui configuré dans l’IDE.

## Versions Java et LTS
Java publie des versions fonctionnelles tous les six mois. Une version **LTS** (*long-term support*) bénéficie d’un support à long terme de certains fournisseurs. La durée, le prix et les conditions dépendent de la distribution et du fournisseur.

Dans la feuille de route Oracle, Java 8, 11, 17, 21 et 25 sont des versions LTS. Oracle prévoit une nouvelle LTS tous les deux ans. Consultez la feuille de route et la politique du fournisseur avant de choisir une version de production.

Le choix dépend aussi des bibliothèques, des outils et des exigences de l’application. Une LTS offre un horizon de support plus long ; les versions intermédiaires donnent accès plus tôt aux nouveautés.

## Consulter les versions et les JEP
Oracle tient un [index des notes de version du JDK](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html), avec des liens vers les versions et leurs mises à jour. Les notes décrivent les changements, corrections et fonctionnalités ajoutées ou supprimées. Les [notes du JDK 27](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) présentent les nouveautés et leurs JEP.

Une **JEP** (*JDK Enhancement Proposal*) décrit une proposition d’évolution du JDK, ses objectifs, sa conception et son état. Certaines fonctions apparaissent d’abord en *preview* ou en *incubator* et peuvent évoluer avant de devenir permanentes.

Consultez les [changements du langage Java par version](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html) et le [résumé des changements](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html) pour comparer fonctions définitives et préliminaires.

## Mettre Java à jour
1. Identifiez la version avec <code>java --version</code> et <code>javac --version</code>.
2. Vérifiez la compatibilité du projet, de ses dépendances et de la production.
3. Téléchargez une mise à jour de votre distribution ou choisissez-en une compatible.
4. Installez le JDK et ajustez si nécessaire <code>PATH</code>, <code>JAVA_HOME</code> et l’IDE.
5. Ouvrez un nouveau terminal, vérifiez les versions et lancez les tests de l’application.

Une mise à jour dans la même ligne et une migration de version majeure sont deux décisions différentes. Avant une migration, lisez les notes et testez l’application et ses dépendances.

Sous Windows, <code>where.exe java</code> et <code>where.exe javac</code> affichent les exécutables trouvés. Sous macOS et Linux, utilisez <code>which java</code> et <code>which javac</code>.

## Références
- [Feuille de route Oracle Java SE](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [FAQ des licences Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
