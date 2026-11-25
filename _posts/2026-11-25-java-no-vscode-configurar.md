---
layout: post
title: "Java no VS Code: como instalar e configurar o JDK"
date: 2026-11-25
lang: pt-BR
translation_id: java-no-vscode-configurar
permalink: /java-no-vscode-configurar/
share_text: >-
  Configure Java no Visual Studio Code, selecione o JDK e execute um primeiro programa.
---

## Instale o JDK e o Visual Studio Code

Para programar em **Java no VS Code**, instale um JDK compatível com o projeto e o Visual Studio Code. No terminal, verifique se o JDK está acessível:

```text
java --version
javac --version
```

Se os comandos não forem encontrados, confira a instalação do JDK e o `PATH`. Abra um novo terminal após alterar as variáveis de ambiente.

## Instale as extensões Java

No VS Code, abra **Extensions**, procure **Extension Pack for Java** e instale o pacote publicado pela Microsoft. Ele reúne suporte à linguagem, execução, depuração e outras ferramentas Java.

Outra opção é o Coding Pack for Java, disponível para Windows e macOS, que reúne VS Code, JDK e extensões essenciais.

## Configure o JDK do projeto

Abra a paleta de comandos com `Ctrl+Shift+P` no Windows ou Linux, ou `Cmd+Shift+P` no macOS. Execute **Java: Configure Java Runtime** e confira o JDK associado ao projeto.

O JDK selecionado para o projeto pode ser diferente daquele encontrado no terminal. Quando houver mais de uma versão instalada, confira ambos.

## Execute um programa

Abra uma pasta no VS Code e crie `Hello.java`:

```java
void main() {
    IO.println("Hello World!");
}
```

O exemplo usa a declaração compacta e `IO.println`, disponíveis no Java 25 ou posterior. Use a ação **Run** apresentada junto ao método `main` e confira a saída no terminal. Para depurar, use **Debug** e marque uma linha de interrupção.

Caso o VS Code não reconheça o arquivo, confirme que a pasta está aberta, aguarde a inicialização das extensões e confira o JDK em **Java: Configure Java Runtime**.

## Referências

- [Primeiros passos com Java no VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Gerenciamento de projetos Java no VS Code](https://code.visualstudio.com/docs/java/java-project)
