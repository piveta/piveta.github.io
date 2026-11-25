---
layout: post
title: "JDK, JRE, and JVM: What Is the Difference in Java?"
date: 2026-11-25
lang: en
translation_id: jdk-jre-jvm-diferencas
permalink: /en/jdk-jre-jvm-differences/
share_text: >-
  Understand the roles of the JVM, JRE, and JDK, and learn which commands check your Java environment.
---

## JVM, JRE, and JDK
The **JVM** (Java Virtual Machine) executes Java bytecode. It loads classes, verifies and runs instructions, and manages resources such as memory. The same bytecode can run on different systems when a compatible JVM is available.

The **JRE** (Java Runtime Environment) describes the environment needed to run Java applications, including the JVM and libraries. Whether a standalone JRE package is available depends on the distribution and version. Some applications bundle their own runtime.

The **JDK** (Java Development Kit) includes the runtime environment and development tools: the compiler <code>javac</code>, the launcher <code>java</code>, and other tools for building, running, and diagnosing applications.

## What should you install to program?
To develop in Java, install a JDK that suits your project. The distribution provides the JVM and the required tools. Oracle JDK and Eclipse Temurin are examples of distributions.

In a terminal, check these commands:

~~~text
java --version
javac --version
~~~

The first prints the Java launcher version; the second prints the compiler version. If <code>java</code> works but <code>javac</code> is not found, check that a JDK is installed and that its <code>bin</code> directory is on <code>PATH</code>.

On Windows, <code>where java</code> and <code>where javac</code> help identify the executable in use. On macOS and Linux, use <code>which java</code> and <code>which javac</code>.

## From source code to execution
In a file named <code>Hello.java</code>, the compiler turns source code into bytecode:

~~~text
javac Hello.java
java Hello
~~~

The first command creates <code>Hello.class</code>. The second starts the JVM to run the class. Compatibility depends on both the version used to compile and the one used to run the program.

## References
- [Java platform and JVM overview](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [JDK installation guide](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
