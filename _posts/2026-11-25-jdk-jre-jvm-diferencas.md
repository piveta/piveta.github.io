---
layout: post
title: "JDK, JRE e JVM: qual é a diferença em Java?"
date: 2026-11-25
lang: pt-BR
translation_id: jdk-jre-jvm-diferencas
permalink: /jdk-jre-jvm-diferencas/
share_text: >-
  Entenda as funções da JVM, do JRE e do JDK e saiba quais comandos usar para verificar o ambiente Java.
---

## JVM, JRE e JDK

A **JVM** (Java Virtual Machine) executa bytecode Java. Ela carrega classes, verifica e executa instruções e administra recursos como memória. O mesmo bytecode pode ser executado em sistemas diferentes quando há uma JVM compatível.

O **JRE** (Java Runtime Environment) designa o ambiente necessário para executar aplicações Java, incluindo a JVM e bibliotecas. A disponibilidade de pacotes JRE independentes depende da distribuição e da versão. Algumas aplicações incluem seu próprio ambiente de execução.

O **JDK** (Java Development Kit) reúne o ambiente de execução e ferramentas de desenvolvimento. Entre elas estão o compilador `javac`, o lançador `java` e outras ferramentas para criar, executar e diagnosticar aplicações.

## O que instalar para programar?

Para desenvolver em Java, instale um JDK adequado ao projeto. A distribuição escolhida fornece a JVM e as ferramentas necessárias. Oracle JDK e Eclipse Temurin são exemplos de distribuições.

No terminal, confira os comandos:

```text
java --version
javac --version
```

O primeiro mostra a versão do lançador Java. O segundo mostra a versão do compilador. Se `java` funcionar e `javac` não for encontrado, confira se um JDK está instalado e se seu diretório `bin` está no `PATH`.

No Windows, `where java` e `where javac` ajudam a identificar qual executável está sendo usado. No macOS e no Linux, use `which java` e `which javac`.

## Do código à execução

Em um arquivo `Hello.java`, o compilador transforma código-fonte em bytecode:

```text
javac Hello.java
java Hello
```

A primeira linha gera `Hello.class`. A segunda inicia a JVM para executar a classe. A compatibilidade depende da versão usada para compilar e daquela usada para executar.

## Referências

- [Visão geral da plataforma Java e da JVM](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [Guia de instalação do JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
