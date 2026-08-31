---
layout: post
title: "Hello World - Traditional vs. Simplified Version"
date: 2026-08-22
lang: en
translation_id: hello-world
permalink: /en/hello-world/
---

It is customary to begin studying a programming language by writing a program called **Hello World**, which displays the text `Hello World!` on the standard output of the device, usually the screen. In Java, we can write this program as follows:
```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```
In this program, we have a class named `Hello`. Classes in object-oriented systems help model concepts from the application domain being studied. Classes encapsulate both the data and the behavior associated with a particular concept.

The `Hello` class has a single method, called `main`, which receives an array of character strings containing the command-line arguments provided when the program is executed, if any. In this example, these arguments are not used.

The `main` method is static, which means that it is a class method rather than an instance method. Therefore, it can be called without creating an object of the `Hello` class.

Inside the `main` method, there is a call to the `println` method. This method belongs to the `PrintStream` class and prints the value passed as an argument to the screen, followed by a line terminator.

The `println` method is called through the `out` field of the `System` class. This field has type `PrintStream` and provides access to the system's standard output.

## Compilation and execution

Java programs are first compiled into an intermediate representation called **bytecode**, which ensures portability. These bytecodes are subsequently executed by a Java Virtual Machine (JVM), which converts them into machine code suitable for the underlying platform.

To compile the program, it must be stored in a file named `Hello.java`. In Java, files containing public types normally have the same name as the type.

We can use an integrated development environment (**IDE**) or invoke the compiler directly from the command line, provided that a JDK is installed.

Java programs are normally written in an IDE, which provides features that improve productivity during development, such as source-code navigation, refactoring, static analysis, compilation, testing, and debugging.

Some of the most popular IDEs for Java are:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

We can also compile the program directly from the command line using the `javac` compiler:

```text
    javac Hello.java
```
The command takes `Hello.java` as input and produces the `Hello.class` file, which contains the compiled version of the program.

After compilation, we can execute the program using the `java` command:

```text
    java Hello
```

The output will be:

```text
    Hello World!
```

## A simpler approach with Java 25+

Starting with Java 25, a feature that had been developed as *preview* since Java 21 became permanent: **Compact Source Files and Instance Main Methods**. It allows small programs to be written with less boilerplate by omitting the explicit class declaration and simplifying the `main` method.

Thus, the previous program can be written now in Java 26 (the current version) as:

```java
    void main() {
        IO.println("Hello World!");
    }
```

In this case, we do not need to explicitly declare the class or write `public static void main(String[] args)`. The compiler treats the file as implicitly declaring a class, and the `main` method can be an instance method.

We can also use the `IO` class, which provides simple console input and output operations. In Java 26, `IO` belongs to the `java.lang` package and is therefore implicitly available. To call its methods, however, we need to use the class name, as in `IO.println(...)`.

Since this feature is no longer in *preview* status, we do not need to use any special compilation options. The program can be compiled normally:

```text
    javac Hello.java
```

and executed in the same way:

```text
    java Hello
```

It is also possible to execute a source file directly using the `java` launcher:

```text
    java Hello.java
```

In this case, the source code is compiled in memory by the launcher itself before execution. This mechanism allows programs to be executed directly from source files without explicitly producing a `.class` file.

The use of compact source files is particularly interesting for small examples, learning programs, scripts, and experiments. As the program grows and requires a more elaborate structure, we can naturally return to the traditional form, with explicit class and method declarations.

The process performed by IDEs is essentially similar. In addition to compilation and execution, they provide features for debugging, testing, refactoring, project creation and management, library creation, version management, and many other tasks.

---

*This article is adapted from content in the book <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, by <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
