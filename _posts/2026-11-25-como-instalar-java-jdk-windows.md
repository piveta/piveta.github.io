---
layout: post
title: "Como instalar Java e o JDK no Windows"
date: 2026-11-25
lang: pt-BR
translation_id: como-instalar-java-jdk-windows
permalink: /como-instalar-java-jdk-windows/
share_text: >-
  Veja como baixar e instalar um JDK no Windows e verificar a configuração usando java e javac.
---

## Escolha uma distribuição Java

Para programar em Java no Windows, baixe um **JDK** compatível com seu projeto. O Oracle JDK e o Eclipse Temurin são distribuições disponíveis. Para projetos que desejam suporte de longo prazo, uma versão LTS é uma opção. Confira a versão exigida pelo projeto e as condições da distribuição escolhida.

Nas configurações do Windows, verifique o tipo de sistema e a arquitetura do processador. Na página de download, selecione o pacote correspondente, como x64 ou AArch64. Escolha o instalador para Windows.

## Download e instalação do JDK

Um exemplo é a instalação do Eclipse Temurin:

1. Acesse a [página de downloads do Adoptium](https://adoptium.net/temurin/releases/).
2. Selecione a versão do Java, o sistema Windows, a arquitetura e o pacote **JDK**.
3. Baixe e execute o instalador MSI.
4. Na configuração, confira a opção de adicionar o Java ao `PATH`. Se outra ferramenta exigir `JAVA_HOME`, selecione também a opção de configurá-lo.
5. Conclua a instalação e abra um novo terminal.

No instalador Temurin, adicionar o Java ao `PATH` é uma opção padrão. Configurar `JAVA_HOME` é uma opção adicional.

## Verifique a instalação

No PowerShell ou no Prompt de Comando, execute:

```text
java --version
javac --version
where.exe java
where.exe javac
```

Os dois primeiros comandos mostram as versões do Java e do compilador. Os demais mostram os executáveis encontrados no `PATH`. Se o comando não for encontrado, abra um novo terminal e confira as variáveis de ambiente. Se aparecer uma versão diferente da esperada, examine a ordem dos diretórios no `PATH`.

Para testar a compilação, salve o arquivo `Hello.java`:

```java
void main() {
    IO.println("Hello World!");
}
```

O exemplo usa a declaração compacta e `IO.println`, disponíveis a partir do Java 25. Execute:

```text
javac Hello.java
java Hello
```

A saída é `Hello World!`. Em versões anteriores ao Java 25, use a forma de programa compatível com o JDK instalado.

## Referências

- [Instalador MSI do Eclipse Temurin](https://adoptium.net/installation/windows/)
- [Instalação do Oracle JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
