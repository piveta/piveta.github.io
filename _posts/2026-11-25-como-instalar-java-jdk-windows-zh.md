---
layout: post
title: "如何在 Windows 上安装 Java 和 JDK"
date: 2026-11-25
lang: zh
translation_id: como-instalar-java-jdk-windows
permalink: /zh/install-java-jdk-windows/
share_text: >-
  了解如何在 Windows 下载并安装 JDK，以及如何用 java 和 javac 验证安装。
---

## 选择 Java 发行版
在 Windows 上开发 Java 程序，需要下载与项目兼容的 **JDK**。Oracle JDK 和 Eclipse Temurin 都是可选发行版。需要长期支持时，可以考虑 LTS 版本。请检查项目要求和发行版使用条款。

在 Windows 设置中确认系统类型和处理器架构，然后选择匹配的软件包，例如 x64 或 AArch64，以及 Windows 安装程序。

## 下载并安装 JDK
以 Eclipse Temurin 为例：

1. 打开 [Adoptium 下载页面](https://adoptium.net/temurin/releases/)。
2. 选择 Java 版本、Windows、架构和 **JDK** 软件包。
3. 下载并运行 MSI 安装程序。
4. 确认是否将 Java 加入 <code>PATH</code>。如果其他工具需要 <code>JAVA_HOME</code>，也选择相应选项。
5. 完成安装并打开新的终端。

在 Temurin 安装程序中，将 Java 加入 <code>PATH</code> 是标准选项；设置 <code>JAVA_HOME</code> 是附加选项。

## 验证安装
在 PowerShell 或命令提示符中运行：

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

前两条显示 Java 和编译器版本，后两条显示在 <code>PATH</code> 中找到的程序。如果找不到命令，请打开新终端并检查环境变量。如果版本不符，请检查 <code>PATH</code> 中目录的顺序。

将以下代码保存为 <code>Hello.java</code> 以测试编译：

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

示例使用 Java 25 起提供的紧凑源文件语法和 <code>IO.println</code>。运行：

~~~text
javac Hello.java
java Hello
~~~

输出为 <code>Hello World!</code>。Java 25 之前请使用已安装 JDK 支持的程序形式。

## 参考资料
- [Eclipse Temurin MSI 安装程序](https://adoptium.net/installation/windows/)
- [Oracle JDK 安装指南](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
