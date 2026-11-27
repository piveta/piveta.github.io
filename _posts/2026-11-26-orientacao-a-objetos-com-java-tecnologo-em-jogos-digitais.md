---
layout: post
title: "Orientação a Objetos com Java no Tecnólogo em Jogos Digitais"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-tecnologo-em-jogos-digitais
permalink: /orientacao-a-objetos-com-java-tecnologo-em-jogos-digitais/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java no Tecnólogo em Jogos Digitais, com competências, capítulos, disciplinas e sugestões de adoção.
---

Mesmo um jogo simples exige que o programador decida como representar personagens, regras e mudanças de estado. Um exercício de orientação a objetos pode isolar essas decisões em uma implementação pequena. O livro fornece conceitos para organizar o código e traz um exercício de implementação de jogo que pode ser usado antes ou junto de um trabalho com motores gráficos.

## Referência curricular

A graduação tecnológica integra o eixo Informação e Comunicação, na área de Desenvolvimento de Sistemas do Catálogo Nacional de Cursos Superiores de Tecnologia (CNCST). A Portaria MEC nº 514/2024 aprovou a 4ª edição. O perfil de conclusão orienta o cruzamento. Cada instituição detalha as disciplinas no seu projeto pedagógico.

O perfil do CNCST inclui projetar, implementar, testar e manter jogos, selecionar ferramentas e métodos, desenvolver roteiros e mecânicas e gerenciar projetos com equipes multidisciplinares. O cruzamento direto está na modelagem e na implementação da lógica do jogo. A seleção de motores, a produção de conteúdo e a gestão do projeto têm referências e práticas próprias.

- [Diretrizes Gerais da Educação Profissional e Tecnológica, Resolução CNE/CP nº 1/2021](https://portal.mec.gov.br/dmdocuments/rcp001_21.pdf)
- [Portaria MEC nº 514/2024 e extrato da 4ª edição do CNCST](https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?captchafield=firstAccess&data=06%2F06%2F2024&jornal=515&pagina=28)
- [CNCST, perfil profissional do curso na edição de 2024](https://www.tecnologo.org.br/documentos/CNCST_2024___Catalogo_Nacional_dos_Cursos_Superiores_de_Tecnologia___06_2024_102859.pdf#page=127)

## Competências e capítulos do livro

Os caps. 2 e 4 têm o vínculo mais próximo com **modelagem de objetos, coleções e implementação de regras de jogos**. Os caps. 1, 5 e 7 podem ser usados em unidades de apoio, conforme a ementa e a linguagem de prática. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Projetar e implementar a lógica de um jogo | Cap. 2, §§ 2.1–2.2 e 2.4 | Direta para a programação de regras. Representar entidades do jogo, seus estados e operações e avaliar onde usar composição e polimorfismo. |
| Selecionar recursos de implementação | Cap. 4, §§ 4.2–4.5, e cap. 5, § 5.1 | Direta para abstrações da linguagem. Escolher, por exemplo, uma fila de turnos ou um mapa de itens identificados. |
| Testar e manter o software do jogo | Cap. 7 e exercício do cap. 2 | Parcial. Isolar um comportamento torna possível testá-lo. A criação de uma suíte de testes e a integração com um motor são extensões didáticas. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Programação Orientada a Objetos para Jogos Digitais | Básica quando o componente usa Java e prioriza POO | Caps. 2, 4 e 5. Consultar o cap. 7 conforme o tratamento de falhas exigido. |
| Programação para Jogos ou Projeto de Jogos | Complementar | Caps. 2 e 4 para modelagem e regras. Em componentes de motor gráfico, utilizar bibliografia da ferramenta adotada. |
| Algoritmos e Estruturas de Dados | Complementar | Cap. 4 para seleção de coleções em tarefas da lógica do jogo. |

O IFBA inclui Programação Orientada a Objetos para Jogos Digitais em seu projeto pedagógico. É o ponto natural para avaliar a adoção do livro. Em um componente já voltado ao uso de um motor ou a outra linguagem, os exemplos podem ser estudados como preparação e transpostos para o ambiente da turma.

- [PPC de Tecnologia em Jogos Digitais do IFBA](https://portal.ifba.edu.br/lauro-de-freitas/menu-cursos/superior/tec-jogos-digitais/copy_of__PPC_Jogos_Digitais_emRevisaoJaneiro_2022.pdf)

## Atividade sugerida

### Protótipo da lógica de um jogo por turnos

Partir do exercício do cap. 2 e, como extensão didática, representar participantes e turnos. Usar uma coleção do cap. 4 e comparar como o código organiza o estado antes e depois de adicionar uma nova regra.

**Como observar a aprendizagem.** Avaliar a coerência das responsabilidades, o uso da coleção e o comportamento em cenários como fim de turno e ação inválida.

## Alcance e preparação da disciplina

Renderização, animação, áudio, física, interação, distribuição e produção de jogos são frentes cobertas por outros materiais. O protótipo proposto foca na regra que pode depois ser integrada à apresentação.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral sobre os cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
