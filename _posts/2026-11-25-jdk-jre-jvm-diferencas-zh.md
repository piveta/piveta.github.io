---
layout: post
title: "JDK、JRE 和 JVM：Java 中有什么区别？"
date: 2026-11-25
lang: zh
translation_id: jdk-jre-jvm-diferencas
permalink: /zh/jdk-jre-jvm-differences/
share_text: >-
  了解 JVM、JRE 和 JDK 各自的作用，以及检查 Java 环境的命令。
---

## JVM、JRE 和 JDK
**JVM**（Java 虚拟机）负责执行 Java 字节码。它加载类、验证并执行指令，还管理内存等资源。只要系统提供兼容的 JVM，同一份字节码就能在不同系统上运行。

**JRE**（Java 运行时环境）指运行 Java 应用所需的环境，包括 JVM 和库。是否提供独立的 JRE 安装包取决于发行版和版本。有些应用会附带自己的运行环境。

**JDK**（Java 开发工具包）包含运行环境和开发工具，例如编译器 <code>javac</code>、启动器 <code>java</code>，以及用于构建、运行和诊断应用的其他工具。

## 编程应该安装什么？
开发 Java 程序时，应安装适合项目的 JDK。所选发行版会提供 JVM 和所需工具。Oracle JDK 和 Eclipse Temurin 都是发行版的例子。

在终端中检查以下命令：

~~~text
java --version
javac --version
~~~

第一条显示 Java 启动器的版本，第二条显示编译器版本。如果 <code>java</code> 可以运行，但找不到 <code>javac</code>，请确认已安装 JDK，并且其 <code>bin</code> 目录已加入 <code>PATH</code>。

在 Windows 中，使用 <code>where java</code> 和 <code>where javac</code> 查看实际调用的程序；在 macOS 和 Linux 中，使用 <code>which java</code> 和 <code>which javac</code>。

## 从源代码到运行
在 <code>Hello.java</code> 文件中，编译器会把源代码转换为字节码：

~~~text
javac Hello.java
java Hello
~~~

第一条命令生成 <code>Hello.class</code>，第二条启动 JVM 来运行该类。兼容性取决于编译和运行时所使用的版本。

## 参考资料
- [Java 平台与 JVM 概览](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [JDK 安装指南](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
