---
layout: post
title: "How to Install Java and the JDK on Windows"
date: 2026-11-25
lang: en
translation_id: como-instalar-java-jdk-windows
permalink: /en/how-to-install-java-jdk-windows/
share_text: >-
  Learn how to download and install a JDK on Windows and verify it with java and javac.
---

## Choose a Java distribution
To program in Java on Windows, download a **JDK** compatible with your project. Oracle JDK and Eclipse Temurin are available distributions. An LTS release may suit projects that need long-term support. Check the project requirements and the distribution terms.

In Windows Settings, check your system type and processor architecture. On the download page, select the matching package, such as x64 or AArch64, and the Windows installer.

## Download and install the JDK
For Eclipse Temurin:

1. Open the [Adoptium downloads page](https://adoptium.net/temurin/releases/).
2. Select the Java version, Windows, your architecture, and the **JDK** package.
3. Download and run the MSI installer.
4. Check whether Java should be added to <code>PATH</code>. If another tool requires <code>JAVA_HOME</code>, select that option too.
5. Finish setup and open a new terminal.

In the Temurin installer, adding Java to <code>PATH</code> is a standard option; setting <code>JAVA_HOME</code> is additional.

## Verify the installation
In PowerShell or Command Prompt, run:

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

The first two print the Java and compiler versions. The others show executables found on <code>PATH</code>. If a command is not found, open a new terminal and check the environment variables. If an unexpected version appears, inspect the directory order in <code>PATH</code>.

Save this as <code>Hello.java</code> to test compilation:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

This uses compact source-file syntax and <code>IO.println</code>, available starting with Java 25. Run:

~~~text
javac Hello.java
java Hello
~~~

The output is <code>Hello World!</code>. Before Java 25, use the program form supported by your JDK.

## References
- [Eclipse Temurin MSI installer](https://adoptium.net/installation/windows/)
- [Oracle JDK installation](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
