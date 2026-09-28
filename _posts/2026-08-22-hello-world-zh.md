---
layout: post
title: "Hello World - 传统版本与简化版本"
date: 2026-08-22
lang: zh
translation_id: hello-world
permalink: /hello-world-zh/
---

学习一门编程语言时，通常会从编写一个名为 **Hello World** 的程序开始。这个程序会将 `Hello World!` 文本显示在设备的标准输出上，通常就是屏幕。在 Java 中，我们可以这样编写这个程序：

```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```

在这个程序中，我们有一个名为 `Hello` 的类。面向对象系统中的类可以帮助我们对所研究的应用领域中的概念进行建模。类将与特定概念相关的数据和行为封装在一起。

`Hello` 类只有一个名为 `main` 的方法。该方法接收一个字符串数组，其中包含运行程序时提供的命令行参数（如果有）。在这个例子中，这些参数不会被使用。

`main` 方法是静态的，这意味着它是类方法，而不是实例方法。因此，可以在不创建 `Hello` 类对象的情况下调用它。

在 `main` 方法内部，我们调用了 `println` 方法。该方法属于 `PrintStream` 类，会将作为参数传入的值输出到屏幕，并在其后输出行终止符。

`println` 方法通过 `System` 类的 `out` 字段调用。该字段的类型为 `PrintStream`，用于访问系统的标准输出。

## 编译与执行

Java 程序首先会被编译成一种称为 **字节码** 的中间表示形式，从而保证可移植性。随后，这些字节码由 Java Virtual Machine（JVM）执行，并转换为适合底层平台的机器代码。

要编译该程序，需要将其保存为名为 `Hello.java` 的文件。在 Java 中，包含 public 类型的文件通常与该类型具有相同的名称。

我们可以使用集成开发环境（**IDE**），也可以在安装了 JDK 的情况下直接从命令行调用编译器。

Java 程序通常在 IDE 中编写。IDE 提供源代码导航、重构、静态分析、编译、测试和调试等功能，可以提高开发过程中的效率。

Java 中一些常用的 IDE 包括：

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

我们也可以使用 `javac` 编译器直接从命令行编译程序：

```text
    javac Hello.java
```

该命令以 `Hello.java` 作为输入，并生成 `Hello.class` 文件，其中包含程序的编译版本。

编译完成后，可以使用 `java` 命令执行程序：

```text
    java Hello
```

输出为：

```text
    Hello World!
```

## 使用 Java 25+ 的更简单方法

从 Java 25 开始，一项自 Java 21 起以 *preview* 形式开发的功能正式成为 Java 的一部分：**Compact Source Files and Instance Main Methods**。它允许通过省略显式的类声明并简化 `main` 方法，以更少的样板代码编写小型程序。

因此，前面的程序现在可以在 Java 26（当前版本）中写成：

```java
    void main() {
        IO.println("Hello World!");
    }
```

在这种情况下，我们不需要显式声明类，也不需要编写 `public static void main(String[] args)`。编译器会将该文件视为隐式声明了一个类，而 `main` 方法可以是实例方法。

我们还可以使用 `IO` 类，它提供简单的控制台输入输出操作。在 Java 26 中，`IO` 属于 `java.lang` 包，因此可以隐式使用。不过，要调用它的方法，仍然需要使用类名，例如 `IO.println(...)`。

由于该功能已经不再处于 *preview* 状态，因此不需要任何特殊的编译选项。程序可以正常编译：

```text
    javac Hello.java
```

并以相同方式执行：

```text
    java Hello
```

还可以使用 `java` 启动器直接执行源文件：

```text
    java Hello.java
```

在这种情况下，启动器会在执行前将源代码直接编译到内存中。这种机制允许程序直接从源文件执行，而无需显式生成 `.class` 文件。

紧凑源文件特别适合小型示例、学习程序、脚本和实验。当程序不断增长并需要更复杂的结构时，我们可以自然地回到使用显式类和方法声明的传统形式。

IDE 所执行的过程本质上也是类似的。除了编译和执行之外，它们还提供调试、测试、重构、项目创建与管理、库创建、版本管理以及许多其他功能。

---

*本文改编自 <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> 一书的内容，作者为 <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>。*
