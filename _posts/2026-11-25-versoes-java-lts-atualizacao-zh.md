---
layout: post
title: "Java 版本：LTS、更新与版本检查方法"
date: 2026-11-25
lang: zh
translation_id: versoes-java-lts-atualizacao
permalink: /zh/java-versions-lts-updates/
share_text: >-
  了解 Java 发布周期、LTS 的含义，以及如何检查和更新 JDK。
---

## 检查 Java 版本
在终端运行以下命令：

~~~text
java --version
javac --version
~~~

第一条显示用于启动应用的 Java 启动器版本，第二条显示编译器版本。如果安装了多个 JDK，<code>PATH</code> 中找到的程序可能与 IDE 配置的 JDK 不同。

## Java 版本与 LTS
Java 每六个月发布一次功能版本。**LTS**（长期支持）版本会由部分供应商提供长期支持。支持时长、费用和条件取决于发行版和供应商。

根据 Oracle 的支持路线图，Java 8、11、17、21 和 25 是 LTS 版本。Oracle 计划每两年发布一个新的 LTS 版本。选择生产环境版本前，请查看最新路线图和供应商政策。

选择还取决于库、工具和应用需求。LTS 提供较长的支持周期，中间版本则能更早使用新功能。

## 在哪里查看版本和 JEP
Oracle 维护 [JDK 版本说明索引](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html)，列出各版本和更新的链接。说明中记录变更、修复以及新增或移除的功能。例如，[JDK 27 版本说明](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html)介绍了新内容并链接相关 JEP。

**JEP**（JDK 增强提案）记录 JDK 改进提案的目标、设计和状态。有些功能会先以 *preview* 或 *incubator* 形式提供，在正式定稿前仍可能变化。

可通过[各版本的 Java 语言变更](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html)和[语言变更摘要](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html)比较正式功能与预览功能。

## 更新 Java
1. 使用 <code>java --version</code> 和 <code>javac --version</code> 确认当前版本。
2. 检查项目、依赖项和生产环境支持的版本。
3. 下载当前发行版的更新，或选择兼容的发行版。
4. 安装 JDK；必要时调整 <code>PATH</code>、<code>JAVA_HOME</code> 和 IDE 配置。
5. 打开新终端，确认版本并运行应用测试。

同一版本系列内更新与迁移到主要版本是不同的决定。迁移前应阅读版本说明并测试应用及其依赖项。

在 Windows 中用 <code>where.exe java</code> 和 <code>where.exe javac</code> 查看可执行程序；在 macOS 或 Linux 中使用 <code>which java</code> 和 <code>which javac</code>。

## 参考资料
- [Oracle Java SE 支持路线图](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [Oracle JDK 许可常见问题](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
