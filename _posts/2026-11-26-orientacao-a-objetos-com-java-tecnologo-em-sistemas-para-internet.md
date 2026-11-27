---
layout: post
title: "Orientação a Objetos com Java no Tecnólogo em Sistemas para Internet"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-tecnologo-em-sistemas-para-internet
permalink: /orientacao-a-objetos-com-java-tecnologo-em-sistemas-para-internet/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java no Tecnólogo em Sistemas para Internet, com competências, capítulos, disciplinas e sugestões de adoção.
---

Uma interface Web precisa de operações que representem regras e manipulem dados. No livro, essas operações são exploradas usando uma aplicação Java e um banco relacional. Essa abordagem ajuda a desenvolver a lógica que pode ficar por trás de uma página ou API. O aproveitamento é maior quando a turma aprende a estruturar o software antes de introduzir o framework Web.

## Referência curricular

A graduação tecnológica integra o eixo Informação e Comunicação, na área de Desenvolvimento de Sistemas do Catálogo Nacional de Cursos Superiores de Tecnologia (CNCST). A Portaria MEC nº 514/2024 aprovou a 4ª edição. O perfil de conclusão orienta o cruzamento. Cada instituição detalha as disciplinas no seu projeto pedagógico.

O CNCST inclui, no perfil de Sistemas para Internet, projetar, desenvolver, testar, implantar e manter aplicações para Internet, além de selecionar métodos e ferramentas e elaborar diretrizes para as interfaces. O cruzamento mais forte é com o desenvolvimento da lógica e da persistência da aplicação. O trabalho com interface Web, publicação e operação depende de outros componentes.

- [Diretrizes Gerais da Educação Profissional e Tecnológica, Resolução CNE/CP nº 1/2021](https://portal.mec.gov.br/dmdocuments/rcp001_21.pdf)
- [Portaria MEC nº 514/2024 e extrato da 4ª edição do CNCST](https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?captchafield=firstAccess&data=06%2F06%2F2024&jornal=515&pagina=28)
- [CNCST, perfil profissional do curso na edição de 2024](https://www.tecnologo.org.br/documentos/CNCST_2024___Catalogo_Nacional_dos_Cursos_Superiores_de_Tecnologia___06_2024_102859.pdf#page=131)

## Competências e capítulos do livro

Os caps. 2, 3, 4, 6 e 7 têm o vínculo mais próximo com **modelagem, lógica de aplicação e persistência do lado do servidor**. Os caps. 1 e 5 podem ser usados em unidades de apoio, conforme a ementa e a linguagem de prática. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Desenvolver a lógica de aplicações | Cap. 2, § 2.2, e caps. 4 e 5 | Direta na parte de programação. Organizar objetos do domínio e definir contratos para que outros componentes possam chamá-los. |
| Implementar a persistência de uma aplicação | Cap. 3, § 3.2, e cap. 6, §§ 6.1–6.3 | Direta na integração com banco. Reutilizar a camada de acesso a dados independentemente da interface apresentada ao usuário. |
| Tratar falhas durante a execução | Cap. 7, §§ 7.2–7.4 | Parcial para teste e manutenção. Distinguir erros de entrada de falhas de infraestrutura. O mapeamento para respostas HTTP é uma extensão do componente Web. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Programação Orientada a Objetos | Básica em Java | Caps. 2, 4, 5 e 7. |
| Programação Orientada a Objetos para Web ou Desenvolvimento Back-end | Complementar | Caps. 2, 3, 6 e 7 para domínio, persistência e falhas. Materiais do componente cobrem o protocolo e o framework. |
| Banco de Dados e Projeto Integrador | Complementar | Caps. 3 e 6 para integrar uma aplicação que precisa gravar e recuperar registros. |

Na UFSM, a matriz de Sistemas para Internet inclui Programação Orientada a Objetos para Web I e II, Banco de Dados II, Padrões de Projeto e Projeto Integrador. A sequência mostra como o mesmo material pode apoiar diferentes componentes, mesmo quando o desenvolvimento Web requer outras ferramentas.

- [Matriz de pré-requisitos de Sistemas para Internet na UFSM](https://www.ufsm.br/app/uploads/sites/491/2023/02/2023_pre_requisitos_SistemasParaInternet.pdf)

## Atividade sugerida

### Uma operação de cadastro usada por duas interfaces

Implemente a operação com base nos caps. 3 e 6 e use uma interface de console para verificar seu comportamento. Em seguida, exponha a mesma operação pelo framework Web adotado pela turma, como extensão didática.

**Como observar a aprendizagem.** Verificar se ambos os caminhos usam a mesma regra, se o SQL permanece isolado na persistência e como o componente Web responde a entradas inválidas.

## Alcance e preparação da disciplina

HTML, CSS, JavaScript de interface, HTTP, segurança Web, acessibilidade, frameworks e implantação exigem material específico. A integração proposta mostra em que ponto os exemplos de Java entram em uma aplicação Web.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Nas atividades de persistência, reservar também uma base PostgreSQL e disponibilizar o driver JDBC. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral sobre os cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
