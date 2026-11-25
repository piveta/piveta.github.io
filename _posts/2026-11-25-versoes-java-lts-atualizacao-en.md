---
layout: post
title: "Java Versions: LTS, Updates, and How to Check Your Version"
date: 2026-11-25
lang: en
translation_id: versoes-java-lts-atualizacao
permalink: /en/java-versions-lts-updates/
share_text: >-
  Learn how Java releases work, what LTS means, and how to check and update a JDK.
---

## Check your Java version
Run these commands in a terminal:

~~~text
java --version
javac --version
~~~

The first identifies the Java launcher used to start applications. The second identifies the compiler. With multiple JDKs installed, the executable found on <code>PATH</code> may differ from the one configured in an IDE.

## Java releases and LTS
Java feature releases follow a six-month cadence. An **LTS** (*long-term support*) release receives long-term support from certain vendors. The duration, price, and terms depend on the distribution and provider.

In Oracle's support roadmap, Java 8, 11, 17, 21, and 25 are LTS releases. Oracle plans a new LTS release every two years. Check the current roadmap and provider policy before choosing a production version.

Your choice also depends on libraries, tools, and application requirements. An LTS release offers a longer support horizon, while intermediate releases provide newer features sooner.

## Where to find Java releases and JEPs
Oracle maintains an [index of JDK release notes](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html), linking releases and updates. The notes describe changes, fixes, and added or removed features. For example, the [JDK 27 release notes](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) describe its changes and point to related JEPs.

A **JEP** (JDK Enhancement Proposal) documents a proposed JDK improvement, its goals, design, and status. Some features first appear as *preview* or *incubator* features and may change before becoming permanent.

To follow language evolution, see [Java language changes by release](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html), which lists features and related JEPs, and the [language changes summary](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html), which helps compare permanent and preview features.

## Update Java
1. Check the current version with <code>java --version</code> and <code>javac --version</code>.
2. Confirm what the project, dependencies, and production environment support.
3. Download an update from your current distribution or choose a compatible one.
4. Install the JDK and adjust <code>PATH</code>, <code>JAVA_HOME</code>, and IDE settings if needed.
5. Open a new terminal, verify the versions, and run the application tests.

A same-line update and a major-version migration are different decisions. Before changing major versions, review release notes and test the application and dependencies.

On Windows, <code>where.exe java</code> and <code>where.exe javac</code> show the executables found. On macOS or Linux, use <code>which java</code> and <code>which javac</code>.

## References
- [Oracle Java SE support roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [Oracle JDK licensing FAQs](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
