---
layout: post
title: "Orientação a Objetos com Java em Engenharia de Software"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-engenharia-de-software
permalink: /orientacao-a-objetos-com-java-engenharia-de-software/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java em Engenharia de Software, com competências, capítulos, disciplinas e sugestões de adoção.
---

Os capítulos de acesso a dados oferecem uma sequência apropriada para Engenharia de Software. Primeiro, o leitor implementa as operações de um cadastro. Depois, move os detalhes de persistência para um DAO e estuda uma forma de reutilizar operações comuns com uma superclasse genérica. A comparação permite discutir o efeito de decisões de projeto sobre o código cliente.

## Referência curricular

O art. 5º, § 3º da Resolução CNE/CES nº 5/2016 prevê aplicar técnicas de construção, evolução e avaliação de software (II), aplicar e validar princípios e padrões (XI), trabalhar com modelos (XII) e projetar, implementar, verificar e documentar soluções (XIV). O Parecer CNE/CES nº 136/2012, seção 3.4, menciona explicitamente paradigmas e ferramentas de construção de software. É a associação curricular mais direta com o paradigma orientado a objetos trabalhado pelo livro.

- [Resolução CNE/CES nº 5/2016](https://portal.mec.gov.br/docman/novembro-2016-pdf/52101-rces005-16-pdf/file)
- [Parecer CNE/CES nº 136/2012](https://portal.mec.gov.br/index.php?gid=11205&option=com_docman&task=doc_download)

## Competências e capítulos do livro

Os caps. 2, 4, 5, 6 e 7 têm o vínculo mais próximo com **construção de software, princípios de projeto e evolução de uma implementação**. Os caps. 1 e 3 podem ser usados em unidades de apoio, conforme a ementa e a linguagem de prática. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Art. 5º, § 3º, II • Construção e evolução | Caps. 3, 5, 6 e 7 | Direta em técnicas de construção. Comparar uma primeira implementação com uma forma de organizar e reutilizar o acesso a dados. |
| Art. 5º, § 3º, XI • Princípios e padrões | Cap. 2, § 2.2, cap. 4, § 4.1, e cap. 6, §§ 6.1–6.3 | Direta em exemplos de substituição, contratos e DAO. A validação pode ser proposta na forma de testes e comparação de projetos. |
| Art. 5º, § 3º, XII e XIV • Modelar, projetar e implementar | Cap. 2 e caps. 3 e 6 | Direta na modelagem de classes e na implementação de uma solução. Parcial em requisitos, verificação e documentação de sistemas completos. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Programação Orientada a Objetos | Básica em Java | Caps. 2, 4, 5 e 7, com persistência como projeto prático. |
| Construção de Software | Básica se a ementa for centrada em construção orientada a objetos em Java | Caps. 2 a 7. Para ementas de ciclo de vida mais amplo, usar como complementar. |
| Análise e Projeto Orientado a Objetos e Padrões de Projeto | Complementar | Cap. 2 para o modelo de classes e cap. 6 para o DAO. Para uma disciplina de padrões, acompanhar com um catálogo de padrões mais amplo. |
| Paradigmas de Programação | Complementar na disciplina e leitura principal da unidade de OO | Caps. 2, 4 e 5. Associar a escolha do paradigma à organização da solução. |

No IFPB, POO antecede Padrões de Projeto de Software. A segunda disciplina abrange famílias de padrões e refatoração. Essa estrutura permite adotar o livro no componente de POO e voltar ao DAO em uma unidade posterior, com leituras sobre outros padrões para ampliar a comparação.

- [Plano de Programação Orientada a Objetos do IFPB](https://estudante.ifpb.edu.br/media/cursos/362/disciplina/ES33.pdf)
- [Plano de Padrões de Projeto de Software do IFPB](https://estudante.ifpb.edu.br/media/cursos/362/disciplina/ES52.pdf)

## Atividade sugerida

### Comparação de alternativas para a persistência

Implementar o cadastro do cap. 3, reorganizá-lo com o DAO concreto do cap. 6 e discutir em que condições um DAO genérico compensa. Como extensão, introduzir uma mudança no cadastro e definir testes de regressão.

**Como observar a aprendizagem.** Avaliar o impacto da mudança nas classes, a repetição eliminada, a clareza das interfaces e os resultados dos testes propostos.

## Alcance e preparação da disciplina

Uma ementa que inclua engenharia de requisitos, arquitetura em escala de sistema, testes automatizados, gerência de projetos e processos de qualidade precisa de referências próprias. O livro contribui com uma aplicação que pode receber atividades nessas frentes.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Nas atividades de persistência, reservar também uma base PostgreSQL e disponibilizar o driver JDBC. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral sobre os cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
