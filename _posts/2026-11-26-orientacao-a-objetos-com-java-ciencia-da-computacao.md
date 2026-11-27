---
layout: post
title: "Orientação a Objetos com Java em Ciência da Computação"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-ciencia-da-computacao
permalink: /orientacao-a-objetos-com-java-ciencia-da-computacao/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java em Ciência da Computação, com competências, capítulos, disciplinas e sugestões de adoção.
---

Em Ciência da Computação, um estudo de orientação a objetos pode partir da pergunta sobre quais operações um tipo oferece e avançar até a representação concreta dos dados. O livro permite percorrer esse caminho em Java. Um estudante pode implementar um programa primeiro usando classes e depois separar o contrato exposto por uma interface da implementação escolhida. Esse é um ponto de partida para discutir abstração, representação e os limites das soluções propostas.

## Referência curricular

A Resolução CNE/CES nº 5/2016 estabelece competências comuns de resolução de problemas no art. 5º, I e III. Para Ciência da Computação, o § 1º, I trata dos fundamentos da área, o V abrange o ciclo de desenvolvimento de sistemas, e o X inclui a abstração entre os princípios recorrentes. O Parecer CNE/CES nº 136/2012, seção 3.2, ajuda a situar fundamentos da programação e tipos abstratos de dados na formação.

- [Resolução CNE/CES nº 5/2016](https://portal.mec.gov.br/docman/novembro-2016-pdf/52101-rces005-16-pdf/file)
- [Parecer CNE/CES nº 136/2012](https://portal.mec.gov.br/index.php?gid=11205&option=com_docman&task=doc_download)

## Competências e capítulos do livro

Os caps. 2, 4 e 5 têm o vínculo mais próximo com **abstração, tipos e estruturas de dados na prática de programação**. Os caps. 1, 3, 6 e 7 podem ser usados em unidades de apoio, conforme a ementa e a linguagem de prática. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Art. 5º, I e III • Formular e programar uma solução | Cap. 1, §§ 1.2–1.5, e cap. 4, § 4.3 | Direta na prática. Traduzir condições e repetições em código e usar uma pilha para verificar o balanceamento de uma expressão. |
| Art. 5º, § 1º, I e X • Fundamentos e abstração | Cap. 2, §§ 2.1–2.2, cap. 4, §§ 4.1–4.5, e cap. 5, §§ 5.1–5.4 | Direta no recorte. Distinguir contrato, representação e escolha de implementação. Raciocinar sobre subtipos, variância e apagamento de tipos em Java. |
| Art. 5º, § 1º, V • Projeto e implementação | Caps. 2, 3, 6 e 7 | Parcial. Modelar classes, implementar um cadastro, separar a persistência e tratar falhas de execução em uma aplicação de pequeno porte. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Programação Orientada a Objetos | Básica quando a prática é em Java | Caps. 2, 4, 5 e 7. Usar o cap. 6 como aplicação de tipos e interfaces. |
| Paradigmas de Programação | Complementar na disciplina e leitura principal da unidade de OO | Caps. 2 e 5. O cap. 1 serve de apoio para contrastar o controle de fluxo imperativo com a organização por objetos. |
| Algoritmos e Estruturas de Dados | Complementar | Cap. 4. Usar coleções prontas para discutir contratos e critérios de escolha. Implementação interna e análise assintótica requerem leitura específica. |
| Linguagens de Programação | Complementar | Cap. 5 para tipagem paramétrica em Java e cap. 7 para propagação de exceções. |

O plano de Paradigmas de Programação da UFSM propõe conhecer e selecionar paradigmas para resolver problemas. Para uma oferta com esse objetivo, a melhor adoção é usar o livro na unidade de OO e propor que a turma compare a mesma solução com a escrita em outro paradigma. As diretrizes de prova do Enade servem como referência adicional de avaliação da área.

- [Plano de Paradigmas de Programação da UFSM](https://www-usr.inf.ufsm.br/~juvizzotto/elc117-2020a/Plano_de_ensino_elc117_2020a.pdf)
- [Diretrizes de prova de Ciência da Computação no Enade 2026](https://mecnormas.mec.gov.br/pesquisa/detalhar/9766)

## Atividade sugerida

### Escolha de uma estrutura pelo contrato

Implemente o verificador do § 4.3 com uma pilha e formule exemplos de entrada bem e mal formados. Em outro exercício, modele uma fila de espera e explique por que a ordem de remoção muda. A segunda parte é uma extensão didática.

**Como observar a aprendizagem.** Avaliar a justificativa das operações, a ordem dos elementos e o comportamento nos casos de teste. Pedir que o aluno explique quais propriedades vêm do contrato da interface e quais decorrem da implementação.

## Alcance e preparação da disciplina

O aprofundamento em análise de algoritmos, computabilidade, semântica formal e paradigmas funcional e lógico deve ser previsto nos componentes correspondentes. A discussão de tipos genéricos fornece um caso concreto de linguagem para esses estudos.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral com os 15 cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
