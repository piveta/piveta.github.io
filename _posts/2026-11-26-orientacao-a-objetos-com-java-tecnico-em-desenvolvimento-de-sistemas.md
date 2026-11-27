---
layout: post
title: "Orientação a Objetos com Java no curso Técnico em Desenvolvimento de Sistemas"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-tecnico-em-desenvolvimento-de-sistemas
permalink: /orientacao-a-objetos-com-java-tecnico-em-desenvolvimento-de-sistemas/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java no curso Técnico em Desenvolvimento de Sistemas, com competências, capítulos, disciplinas e sugestões de adoção.
---

O livro pode acompanhar a passagem de um primeiro programa até um cadastro que grava dados de forma persistente. Esse percurso se encaixa em um curso técnico que aproxima lógica, programação orientada a objetos, banco de dados e projeto integrador. O mesmo exemplo permite trabalhar os fundamentos e, depois, mostrar por que uma aplicação em crescimento precisa separar responsabilidades.

## Referência curricular

A formação é de nível médio e integra a área de Desenvolvimento de Sistemas no eixo Informação e Comunicação. A Resolução CNE/CEB nº 2/2020 aprovou a 4ª edição do Catálogo Nacional de Cursos Técnicos (CNCT). O perfil de conclusão é a referência para as capacidades profissionais.

O perfil de conclusão do CNCT inclui desenvolver sistemas em um ambiente de programação, modelar aplicações e codificar rotinas. Também inclui dimensionar requisitos, executar alterações, realizar testes funcionais e apoiar a documentação. Os três primeiros vínculos aparecem diretamente nos exemplos da obra. Os demais podem ser exercitados com tarefas adicionais de projeto.

- [Diretrizes Gerais da Educação Profissional e Tecnológica, Resolução CNE/CP nº 1/2021](https://portal.mec.gov.br/dmdocuments/rcp001_21.pdf)
- [Resolução CNE/CEB nº 2/2020, que aprova a 4ª edição do CNCT](https://portal.mec.gov.br/docman/dezembro-2020-pdf/167211-rceb002-20/file)
- [CNCT, perfil profissional e itinerário do curso](https://www.gov.br/saude/pt-br/composicao/sgtes/diretrizes-para-formacao-tecnica-na-saude/publicacoes/catalogo-nacional-de-cursos-tecnicos.pdf/%40%40download/file#page=234)

## Competências e capítulos do livro

Os caps. 1, 2, 3, 4, 6 e 7 têm o vínculo mais próximo com **modelagem, codificação e implementação de um cadastro com persistência**. O cap. 5 pode ser usado em unidades de apoio, conforme a ementa e a linguagem de prática. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Codificar rotinas com uma linguagem de programação | Cap. 1, §§ 1.2–1.5 | Direta. Ler dados, avaliar condições e repetir operações em pequenos programas. |
| Modelar aplicações computacionais | Cap. 2, §§ 2.1–2.2 | Direta. Representar estado e comportamento de entidades, distribuir responsabilidades e encapsular dados. |
| Desenvolver aplicações com persistência | Cap. 3, §§ 3.1–3.2, cap. 6, §§ 6.1–6.2, e cap. 7 | Direta. Conectar o programa ao banco, executar as operações do cadastro, organizar o acesso a dados e tratar exceções. |
| Alterar software e realizar testes funcionais | Cap. 6 e exercícios do cap. 7 | Parcial. Usar os exemplos como base para introduzir uma alteração e verificar o resultado. O roteiro de teste é elaborado no componente. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Programação Orientada a Objetos | Básica em Java | Cap. 2 como eixo. Caps. 4 e 7 para coleções e erros. Introduzir o cap. 5 conforme o nível da turma. |
| Lógica de Programação | Complementar | Cap. 1 para implementar as primeiras rotinas com Java. |
| Banco de Dados ou Projeto Integrador | Complementar | Caps. 3 e 6 para a aplicação com banco. Cap. 7 para tratar falhas e liberar recursos. |

O PPC do IFAL inclui, em um componente de POO, estudos da linguagem, estruturas de dados, exceções, integração com banco e interface do usuário. O livro dialoga com as unidades de programação e persistência. A interface de usuário pode usar material complementar da tecnologia adotada.

- [PPC do Técnico em Desenvolvimento de Sistemas do IFAL](https://www2.ifal.edu.br/acesso-a-informacao/institucional/orgaos-colegiados/conselho-de-ensino-pesquisa-e-extensao/arquivos/arquivos-ate-2024/resolucao-no-158-2023-cepe-plano-pedagogico-do-curso-tecnico-integrado-ao-ensino-medio-em-desenvolvimento-de-sistemas-c-maceio.pdf)

## Atividade sugerida

### Cadastro em três entregas

Primeiro, ler e validar dados no console. Depois, representar os registros com classes e executar inserção e listagem no PostgreSQL. Por fim, acrescentar o DAO e demonstrar um caso de entrada inválida.

**Como observar a aprendizagem.** Verificar cada entrega em execução. Pedir uma descrição breve da alteração feita e um roteiro com a entrada, o resultado esperado e o resultado observado.

## Alcance e preparação da disciplina

Documentação formal, interface gráfica ou Web, testes sistemáticos, manutenção e suporte requerem práticas próprias. O cadastro pode permanecer como projeto de referência para essas etapas.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Nas atividades de persistência, reservar também uma base PostgreSQL e disponibilizar o driver JDBC. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral sobre os cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
