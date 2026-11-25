---
layout: post
title: "Java in VS Code: How to Install and Configure the JDK"
date: 2026-11-25
lang: en
translation_id: java-no-vscode-configurar
permalink: /en/java-in-vs-code-setup/
share_text: >-
  Set up Java in Visual Studio Code, select a JDK, and run a first program.
---

## Install the JDK and Visual Studio Code
To program in **Java in VS Code**, install a JDK compatible with your project and install Visual Studio Code. In a terminal, check that the JDK is available:

~~~text
java --version
javac --version
~~~

If the commands are not found, check the JDK installation and <code>PATH</code>. Open a new terminal after changing environment variables.

## Install the Java extensions
In VS Code, open **Extensions**, search for **Extension Pack for Java**, and install the package published by Microsoft. It brings together language support, running, debugging, and other Java tools.

Another option is the Coding Pack for Java, available for Windows and macOS, which bundles VS Code, a JDK, and essential extensions.

## Configure the project JDK
Open the Command Palette with <code>Ctrl+Shift+P</code> on Windows or Linux, or <code>Cmd+Shift+P</code> on macOS. Run **Java: Configure Java Runtime** and check the JDK associated with the project.

The JDK selected for a project can differ from the one found in the terminal. If more than one version is installed, check both.

## Run a program
Open a folder in VS Code and create <code>Hello.java</code>:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

This uses compact source-file syntax and <code>IO.println</code>, available in Java 25 or later. Use **Run** beside <code>main</code> and check the terminal output. To debug, choose **Debug** and set a breakpoint.

If VS Code does not recognize the file, confirm that the folder is open, wait for the extensions to start, and check the JDK in **Java: Configure Java Runtime**.

## References
- [Getting started with Java in VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Java project management in VS Code](https://code.visualstudio.com/docs/java/java-project)
