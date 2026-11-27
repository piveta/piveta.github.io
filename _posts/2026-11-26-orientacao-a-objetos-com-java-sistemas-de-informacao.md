---
layout: post
title: "Orientação a Objetos com Java em Sistemas de Informação"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-sistemas-de-informacao
permalink: /orientacao-a-objetos-com-java-sistemas-de-informacao/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java em Sistemas de Informação, com competências, capítulos, disciplinas e sugestões de adoção.
---

Um cadastro acadêmico é um exemplo simples de sistema de informação. Ele envolve decidir como representar os dados, quais operações a aplicação oferece e onde ficam as regras de negócio. Os capítulos de acesso a dados apresentam duas etapas desse trabalho. A primeira conecta Java ao PostgreSQL e executa as operações de cadastro. A segunda reorganiza o acesso ao banco em classes dedicadas.

## Referência curricular

O art. 5º, § 4º, VI da Resolução CNE/CES nº 5/2016 prevê modelar e implementar soluções de TI em diferentes domínios. Os caps. 2 e 3 oferecem exemplos dos domínios bancário e acadêmico. O inciso III associa o projeto de soluções ao contexto das organizações, e o IV incorpora a comparação de alternativas, integração e análise de risco. O livro trabalha partes técnicas desses dois incisos. O art. 5º, I e III também se aplica ao aprendizado de programação. O Parecer CNE/CES nº 136/2012, seção 3.5, situa modelagem de sistemas e gerenciamento de dados entre os conteúdos da área.

- [Resolução CNE/CES nº 5/2016](https://portal.mec.gov.br/docman/novembro-2016-pdf/52101-rces005-16-pdf/file)
- [Parecer CNE/CES nº 136/2012](https://portal.mec.gov.br/index.php?gid=11205&option=com_docman&task=doc_download)

## Competências e capítulos do livro

Os caps. 2, 3, 4, 6 e 7 têm o vínculo mais próximo com **modelagem de aplicações e persistência de dados em sistemas de informação**. Os caps. 1 e 5 podem ser usados em unidades de apoio, conforme a ementa e a linguagem de prática. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Art. 5º, § 4º, VI • Modelar um domínio | Cap. 2, §§ 2.1–2.2 | Direta na escala de uma aplicação. Representar entidades e relacionamentos, associando estado e comportamento às classes. |
| Art. 5º, § 4º, VI • Implementar uma solução com dados persistentes | Cap. 3, §§ 3.1–3.2, e cap. 7, § 7.2.4 | Direta na implementação. Operar um cadastro com JDBC, interpretar falhas e exercitar gerenciamento de recursos. |
| Art. 5º, § 4º, III e IV • Projetar e avaliar alternativas | Cap. 6, §§ 6.1–6.3 | Parcial. Comparar a distribuição das responsabilidades com acesso direto, DAO concreto e DAO genérico. A avaliação organizacional depende de uma atividade adicional. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Programação Orientada a Objetos I | Básica em Java | Caps. 2, 4 e 7, com o cap. 1 para revisão. |
| Programação Orientada a Objetos II ou Desenvolvimento de Aplicações | Básica se o foco for implementação Java com persistência | Caps. 3 a 7, da primeira consulta ao DAO genérico. |
| Banco de Dados e Análise ou Projeto Orientado a Objetos | Complementar | Caps. 3 e 6 para integração. Cap. 2 para modelagem de classes. O restante da ementa determina as referências de modelagem relacional e levantamento de requisitos. |
| Paradigmas de Programação | Complementar na disciplina | Caps. 2 e 5 como leituras da unidade de orientação a objetos. |

A ementa da UFSM inclui fundamentos de OO, interfaces e tratamento de exceções em POO I. A UFRB oferece um exemplo de ementa mais ampla, que também inclui interface gráfica e diagramas de casos de uso. Nessa situação, é possível adotar o livro na parte central de implementação e reservar referências específicas para as demais unidades.

- [Programa de Programação Orientada a Objeto I da UFSM](https://www.ufsm.br/cursos/graduacao/sistemas-de-informacao-fw/wp-content/uploads/sites/333/2018/11/SIN_1047_PRG_PROGRAMA%C3%87%C3%83O_ORIENTADA_A_OBJETO_sistemas_novo.pdf)
- [PPC de Sistemas de Informação da UFRB](https://www2.ufrb.edu.br/ead/images/Nucleo_Midias/PPC_de_cursos/PPC_SISTEMAS_DE_INFORMACAO.pdf)

## Atividade sugerida

### Evolução de um cadastro acadêmico

Partir das operações do § 3.2 e migrar a persistência para um DAO do cap. 6. Como extensão, acrescentar uma regra de negócio e identificar em qual classe ela deve ficar.

**Como observar a aprendizagem.** Entregar modelo de classes, código executável e uma justificativa curta sobre a separação entre apresentação, negócios e acesso a dados.

## Alcance e preparação da disciplina

A formação em processos de negócio, governança de TI, viabilidade, segurança organizacional e gestão de projetos precisa de componentes e estudos de caso próprios. O exemplo do cadastro pode servir como aplicação técnica em um projeto que desenvolva essas outras competências.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Nas atividades de persistência, reservar também uma base PostgreSQL e disponibilizar o driver JDBC. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral sobre os cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
