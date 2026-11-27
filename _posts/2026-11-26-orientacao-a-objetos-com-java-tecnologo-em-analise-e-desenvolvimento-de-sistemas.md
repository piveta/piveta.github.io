---
layout: post
title: "Orientação a Objetos com Java no Tecnólogo em Análise e Desenvolvimento de Sistemas"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-tecnologo-em-analise-e-desenvolvimento-de-sistemas
permalink: /orientacao-a-objetos-com-java-tecnologo-em-analise-e-desenvolvimento-de-sistemas/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java no Tecnólogo em Análise e Desenvolvimento de Sistemas, com competências, capítulos, disciplinas e sugestões de adoção.
---

Em Análise e Desenvolvimento de Sistemas (ADS), os sete capítulos podem ser usados ao longo de uma sequência de componentes. O estudante começa escrevendo pequenos programas, passa a organizar dados e operações em classes e termina implementando um cadastro com persistência. O mesmo problema pode reaparecer em mais de uma disciplina, com uma responsabilidade nova a cada etapa.

## Referência curricular

A graduação tecnológica integra o eixo Informação e Comunicação, na área de Desenvolvimento de Sistemas do Catálogo Nacional de Cursos Superiores de Tecnologia (CNCST). A Portaria MEC nº 514/2024 aprovou a 4ª edição. O perfil de conclusão orienta o cruzamento. Cada instituição detalha as disciplinas no seu projeto pedagógico.

O perfil do CNCST inclui analisar, projetar, desenvolver, testar, implantar e manter sistemas de informação. Também prevê selecionar e usar tecnologias de Engenharia de Software, linguagens e bancos de dados. O livro contribui diretamente para aprender a projetar classes, desenvolver aplicações e usar ferramentas. Teste, implantação e manutenção em produção exigem atividades adicionais.

- [Diretrizes Gerais da Educação Profissional e Tecnológica, Resolução CNE/CP nº 1/2021](https://portal.mec.gov.br/dmdocuments/rcp001_21.pdf)
- [Portaria MEC nº 514/2024 e extrato da 4ª edição do CNCST](https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?captchafield=firstAccess&data=06%2F06%2F2024&jornal=515&pagina=28)
- [CNCST, perfil profissional do curso na edição de 2024](https://www.tecnologo.org.br/documentos/CNCST_2024___Catalogo_Nacional_dos_Cursos_Superiores_de_Tecnologia___06_2024_102859.pdf#page=120)

## Competências e capítulos do livro

Os sete capítulos têm o vínculo mais próximo com **uma sequência de programação, modelagem e persistência para construir aplicações**. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Projetar e codificar aplicações | Caps. 1 e 2, sobretudo §§ 1.5 e 2.2 | Direta. Transformar um requisito de cadastro em operações e classes que separem dados, comportamento e regras. |
| Usar linguagens e escolher recursos de software | Caps. 4 e 5 | Direta para Java. Selecionar interfaces e coleções e escrever código parametrizado com tipos. |
| Integrar o software a um banco de dados | Cap. 3, § 3.2, cap. 6, §§ 6.1–6.3, e cap. 7, § 7.2.4 | Direta. Executar operações de cadastro, reorganizar o acesso com DAO e gerenciar exceções e recursos. |
| Testar, implantar e manter sistemas | Caps. 6 e 7 como base para uma prática | Parcial. As implementações principais oferecem um ponto de partida para testar alterações e falhas. O docente acrescenta teste sistemático e implantação. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Programação Orientada a Objetos ou Programação II | Básica em Java | Caps. 2, 4, 5 e 7. Usar o cap. 1 para revisão. |
| Desenvolvimento de Aplicações ou Persistência com Java | Básica se a unidade for centrada em JDBC e DAO | Caps. 3, 6 e 7. Se a ementa centralizar frameworks, usar como complementar para explicar o acesso relacional subjacente. |
| Estruturas de Dados, Banco de Dados e Projeto Integrador | Complementar | Cap. 4 para coleções. Caps. 3 e 6 para acesso à base. Cap. 7 para cenários de falha. |

Uma ementa de ADS da UFPR descreve construção de aplicações orientadas a objetos com banco de dados, DAO e frameworks de persistência. Também inclui tópicos de comunicação e programação paralela. O livro sustenta a unidade de JDBC e DAO nessa ementa e pode ocupar um papel mais amplo em um componente de POO que siga Java.

- [Ementas de ADS da UFPR](https://www.tads.ufpr.br/ementas/ementas/tudo/ficha2_tudo/12)
- [Plano de Programação Orientada a Objetos em ADS no IFPB](https://estudante.ifpb.edu.br/media/cursos/12/disciplina/3_-_poo_ycKwjzG.pdf)

## Atividade sugerida

### Do primeiro cadastro à separação em camadas

Implementar inserção e consulta a partir do § 3.2. Em uma segunda entrega, introduzir o DAO e distinguir a regra de negócio da consulta SQL. Em uma terceira, acrescentar testes para um dado inválido e uma falha na conexão.

**Como observar a aprendizagem.** Avaliar o funcionamento do cadastro, a clareza da separação entre classes e a repetibilidade dos testes propostos.

## Alcance e preparação da disciplina

Processos de desenvolvimento, automação de testes, interfaces de usuário, implantação e coordenação de equipes pedem outras referências. Uma disciplina que atravessa o ciclo de vida inteiro pode usar o cadastro como projeto em que essas práticas serão introduzidas.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Nas atividades de persistência, reservar também uma base PostgreSQL e disponibilizar o driver JDBC. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral sobre os cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
