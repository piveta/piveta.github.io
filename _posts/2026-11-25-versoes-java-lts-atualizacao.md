---
layout: post
title: "Versões do Java: LTS, atualização e como verificar a versão"
date: 2026-11-25
lang: pt-BR
translation_id: versoes-java-lts-atualizacao
permalink: /versoes-java-lts-atualizacao/
share_text: >-
  Entenda o ciclo de versões do Java, o significado de LTS e como verificar e atualizar um JDK.
---

## Como verificar a versão do Java

No terminal, execute:

```text
java --version
javac --version
```

O primeiro comando identifica o Java usado para iniciar aplicações. O segundo identifica o compilador. Se houver vários JDKs instalados, a ferramenta encontrada no `PATH` pode diferir da configurada em uma IDE.

## Versões do Java e LTS

O Java recebe versões de funcionalidades em uma cadência de seis meses. Uma versão **LTS** (*long-term support*) recebe suporte de longo prazo de determinados fornecedores. A duração, o preço e as condições desse suporte dependem da distribuição e do fornecedor.

No roteiro de suporte da Oracle, Java 8, 11, 17, 21 e 25 são versões LTS. A Oracle planeja uma nova versão LTS a cada dois anos. Consulte o roteiro atualizado e a política do fornecedor antes de definir uma versão para produção.

A escolha depende também das bibliotecas, ferramentas e requisitos da aplicação. Uma versão LTS oferece um horizonte de suporte mais longo, enquanto versões intermediárias dão acesso mais cedo a recursos recentes.

## Onde consultar as versões e as JEPs

A Oracle mantém um [índice de notas de versão do JDK](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html), com links para os lançamentos e suas atualizações. Nas notas, você encontra alterações, correções e recursos introduzidos ou removidos. Por exemplo, as [notas do JDK 27](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) descrevem as novidades e apontam para as JEPs correspondentes.

Uma **JEP** (*JDK Enhancement Proposal*) documenta uma proposta de melhoria para o JDK. A página de uma JEP apresenta seus objetivos, a solução proposta e seu estado. Alguns recursos são entregues inicialmente como *preview* ou *incubator* e podem mudar antes de se tornarem permanentes.

Para acompanhar a evolução da linguagem, consulte as [mudanças do Java por versão](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html). A página reúne recursos de cada versão e links para as respectivas JEPs. Há também o [resumo de mudanças da linguagem](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html), que facilita comparar versões e identificar recursos permanentes e em prévia.
## Como atualizar o Java

1. Identifique a versão atual com `java --version` e `javac --version`.
2. Confira a versão suportada pelo projeto, por suas dependências e pelo ambiente de produção.
3. Baixe a atualização da distribuição utilizada ou escolha uma distribuição compatível.
4. Instale o JDK e ajuste o `PATH`, o `JAVA_HOME` e a configuração da IDE quando necessário.
5. Abra um novo terminal, confira as versões e execute os testes da aplicação.

Atualizações da mesma linha e mudanças de versão principal são decisões diferentes. Antes de migrar entre versões principais, revise as notas de lançamento e teste a aplicação e suas dependências.

No Windows, `where.exe java` e `where.exe javac` mostram os executáveis encontrados. No macOS ou Linux, use `which java` e `which javac`.

## Referências

- [Roteiro de suporte do Oracle Java SE](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [Licenças do Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
