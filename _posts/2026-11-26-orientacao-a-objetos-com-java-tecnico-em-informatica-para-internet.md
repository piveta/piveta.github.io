---
layout: post
title: "Orientação a Objetos com Java no curso Técnico em Informática para Internet"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-tecnico-em-informatica-para-internet
permalink: /orientacao-a-objetos-com-java-tecnico-em-informatica-para-internet/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java no curso Técnico em Informática para Internet, com competências, capítulos, disciplinas e sugestões de adoção.
---

Um formulário Web é um modo de receber dados. Por trás dele, a aplicação precisa decidir se os valores são válidos, representar um registro e guardá-lo para uso posterior. O livro ensina essa parte em Java através de exemplos de console e banco de dados, que podem ser aproveitados antes de colocar o programa em um ambiente Web.

## Referência curricular

A formação é de nível médio e integra a área de Desenvolvimento de Sistemas no eixo Informação e Comunicação. A Resolução CNE/CEB nº 2/2020 aprovou a 4ª edição do Catálogo Nacional de Cursos Técnicos (CNCT). O perfil de conclusão é a referência para as capacidades profissionais.

O perfil do CNCT inclui planejar, documentar, codificar, testar e publicar aplicações Web e móveis. Também inclui estruturar e implementar bancos de dados para aplicações Web. O livro atende à programação de regras e à integração com banco, duas partes que podem ser ensinadas em um componente de POO ou em um projeto de aplicação.

- [Diretrizes Gerais da Educação Profissional e Tecnológica, Resolução CNE/CP nº 1/2021](https://portal.mec.gov.br/dmdocuments/rcp001_21.pdf)
- [Resolução CNE/CEB nº 2/2020, que aprova a 4ª edição do CNCT](https://portal.mec.gov.br/docman/dezembro-2020-pdf/167211-rceb002-20/file)
- [CNCT, perfil profissional e itinerário do curso](https://www.gov.br/saude/pt-br/composicao/sgtes/diretrizes-para-formacao-tecnica-na-saude/publicacoes/catalogo-nacional-de-cursos-tecnicos.pdf/%40%40download/file#page=239)

## Competências e capítulos do livro

Os caps. 2, 3, 6 e 7 têm o vínculo mais próximo com **programação de aplicações, regras de negócio e persistência para projetos Web**. Os caps. 1, 4 e 5 podem ser usados em unidades de apoio, conforme a ementa e a linguagem de prática. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Codificar a lógica de uma aplicação | Caps. 1 e 2, especialmente §§ 1.5 e 2.2 | Direta para Java. Transformar dados de entrada em objetos e aplicar regras antes de persistir o resultado. |
| Implementar acesso a dados para uma aplicação | Cap. 3, §§ 3.1–3.2, e cap. 6, §§ 6.1–6.2 | Direta para banco relacional em ambiente Java. Criar a estrutura do exemplo, executar as operações e separar o código responsável pelo banco. |
| Testar e publicar a aplicação Web | Cap. 7, §§ 7.2–7.4, como base | Indireta. Usar o comportamento da aplicação em caso de falha como cenário de teste. Publicação e interação via navegador são tarefas de outros materiais. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Programação Orientada a Objetos | Básica em Java | Caps. 2, 4 e 7. Incluir os caps. 3 e 6 se a ementa já introduzir persistência. |
| Programação para Internet | Complementar | Caps. 2, 6 e 7 para o código que recebe os dados e aplica as regras do programa. |
| Banco de Dados ou Projeto Integrador | Complementar | Caps. 3 e 6 para a unidade de integração. |

O PPC do Ifes reúne orientação a objetos, tratamento de erros, interface e persistência em arquivo e em banco em um dos componentes. Para uma ementa desse tipo, o livro cobre a implementação orientada a objetos e o caso relacional. A parte de interface e o armazenamento em arquivos podem usar leituras próprias.

- [PPC do Técnico em Informática para Internet do Ifes](https://santateresa.ifes.edu.br/images/stories/Cursos/informatica_para_internet/projeto_curso.pdf)

## Atividade sugerida

### Validar e registrar dados recebidos de um formulário

Implementar primeiro o cadastro no console e encapsular a persistência com DAO. Como extensão, ligar uma página simples à mesma operação usando a tecnologia de servidor da turma.

**Como observar a aprendizagem.** Demonstrar um registro aceito e um rejeitado. Verificar se a validação funciona sem depender do formulário e se o acesso ao banco fica na classe prevista.

## Alcance e preparação da disciplina

A estrutura visual das páginas, os protocolos Web, as ferramentas de frontend, o servidor e a publicação exigem referências específicas. O cadastro do livro fornece a lógica que a interface vai acionar.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Nas atividades de persistência, reservar também uma base PostgreSQL e disponibilizar o driver JDBC. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral sobre os cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
