---
layout: post
title: "在 VS Code 中使用 Java：安装和配置 JDK"
date: 2026-11-25
lang: zh
translation_id: java-no-vscode-configurar
permalink: /zh/java-vscode-setup/
share_text: >-
  在 Visual Studio Code 中配置 Java、选择 JDK 并运行第一个程序。
---

## 安装 JDK 和 Visual Studio Code
要在 **VS Code 中开发 Java**，请安装与项目兼容的 JDK 和 Visual Studio Code。在终端检查 JDK 是否可用：

~~~text
java --version
javac --version
~~~

如果找不到命令，请检查 JDK 安装和 <code>PATH</code>。修改环境变量后，打开新的终端。

## 安装 Java 扩展
在 VS Code 中打开 **Extensions**，搜索 **Extension Pack for Java**，并安装 Microsoft 发布的扩展包。它包含语言支持、运行、调试等 Java 工具。

Windows 和 macOS 用户也可以选择 Coding Pack for Java，其中包含 VS Code、JDK 和必要扩展。

## 配置项目 JDK
在 Windows 或 Linux 上按 <code>Ctrl+Shift+P</code>，在 macOS 上按 <code>Cmd+Shift+P</code> 打开命令面板。运行 **Java: Configure Java Runtime**，检查项目关联的 JDK。

项目选择的 JDK 可能与终端找到的不同。若安装了多个版本，请分别确认。

## 运行程序
在 VS Code 中打开一个文件夹并创建 <code>Hello.java</code>：

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

此示例使用 Java 25 起提供的紧凑源文件语法和 <code>IO.println</code>。点击 <code>main</code> 旁的 **Run**，检查终端输出。调试时选择 **Debug** 并设置断点。

如果 VS Code 无法识别文件，请确认已打开文件夹、扩展已启动，并检查 **Java: Configure Java Runtime** 中的 JDK。

## 参考资料
- [在 VS Code 中开始使用 Java](https://code.visualstudio.com/docs/java/java-tutorial)
- [VS Code 中的 Java 项目管理](https://code.visualstudio.com/docs/java/java-project)
