---
layout: post
title: "Orientação a Objetos com Java no Tecnólogo em Redes de Computadores"
date: 2026-11-27
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-tecnologo-em-redes-de-computadores
permalink: /orientacao-a-objetos-com-java-tecnologo-em-redes-de-computadores/
description: "O livro Orientação a Objetos com Java no curso de Redes de Computadores: competências do CNCST, programação, disciplinas e bibliografia."
share_text: >-
  Como o livro contribui para a formação em programação de estudantes de Redes de Computadores, com competências, capítulos e possibilidades de adoção.
---

Projetar e administrar redes exige compreender sua infraestrutura e, em muitas atividades, usar programas para organizar informações e apoiar o trabalho técnico. *Orientação a Objetos com Java* contribui para a formação em programação do tecnólogo em Redes de Computadores. A obra apresenta a construção de pequenos programas, a organização de dados em classes e coleções e o tratamento de falhas.

Um cadastro de dispositivos, por exemplo, pode representar nome, endereço e características de equipamentos em objetos Java. Esse é um projeto didático que o professor pode desenvolver a partir dos conceitos do livro. Ele permite praticar programação usando um domínio próximo ao curso.

## Referência curricular

O Catálogo Nacional de Cursos Superiores de Tecnologia (CNCST), em sua 4ª edição, descreve um perfil que inclui projetar, implantar, gerenciar e integrar redes, avaliar soluções de segurança, documentar projetos e avaliar desempenho. A Resolução CNE/CP nº 1/2021 estabelece as diretrizes gerais da Educação Profissional e Tecnológica. O projeto pedagógico de cada curso define os componentes curriculares e suas ementas.

O livro contribui para o raciocínio lógico e a construção de programas de apoio a essas atividades. O exemplo de cadastro pode organizar dados empregados na documentação de uma rede. A avaliação de desempenho e as configurações de segurança são competências profissionais mais amplas, que exigem exercícios e referências específicas.

- [Diretrizes da Educação Profissional e Tecnológica](https://portal.mec.gov.br/dmdocuments/rcp001_21.pdf)
- [Portaria MEC nº 514/2024 e extrato do CNCST](https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?captchafield=firstAccess&data=06%2F06%2F2024&jornal=515&pagina=28)
- [Catálogo Nacional de Cursos Superiores de Tecnologia](https://cncst.mec.gov.br/)

## Competências e capítulos do livro

| Capacidade relacionada ao curso | Capítulos e seções | Contribuição da obra |
| --- | --- | --- |
| Resolver problemas usando programação | Cap. 1, §§ 1.2–1.5 | Desenvolver rotinas com entrada e saída, tipos, operadores, decisões e repetições. |
| Organizar informações para documentação técnica | Cap. 2, §§ 2.1–2.2, e cap. 4, §§ 4.2–4.5 | Modelar equipamentos e registros como objetos e guardá-los em listas, conjuntos ou mapas. O inventário de rede é uma extensão didática. |
| Construir e manter ferramentas de apoio | Cap. 2 e cap. 7, §§ 7.2–7.4 | Dividir responsabilidades entre classes e tratar entradas inválidas e falhas de execução. |
| Persistir informações de um projeto | Cap. 3, §§ 3.1–3.2, e cap. 6, §§ 6.1–6.3 | Adaptar o exemplo de cadastro em PostgreSQL e JDBC para guardar dados de um inventário. O DAO ajuda a separar o acesso ao banco. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Possibilidade de uso |
| --- | --- | --- |
| Algoritmos e Programação | Complementar | Cap. 1 para praticar estruturas fundamentais em Java. A linguagem e a abrangência da disciplina orientam a escolha da bibliografia principal. |
| Programação Orientada a Objetos | Básica quando a disciplina adota Java | Caps. 2, 4, 5 e 7 para classes, interfaces, coleções, tipos genéricos e exceções. |
| Projeto Integrador ou Automação | Complementar | Caps. 1, 2, 4 e 7 para implementar uma ferramenta de apoio. Caps. 3 e 6 se o projeto armazenar dados em banco relacional. |
| Redes de Computadores | Complementar para uma atividade de programação | Usar os capítulos de programação em uma ferramenta ou simulação. A disciplina mantém suas referências de arquitetura, protocolos e operação de redes. |

## Atividade sugerida

### Inventário de dispositivos

Como extensão didática dos exemplos do livro, modele uma classe para representar um dispositivo, com identificação, endereço e descrição. Guarde os objetos em uma coleção e implemente operações de inclusão, listagem e busca. Em uma segunda etapa, registre os dados em PostgreSQL usando JDBC e organize a persistência com DAO.

**Como observar a aprendizagem.** Verifique se as responsabilidades foram distribuídas entre classes, se a busca retorna o resultado esperado e como o programa se comporta diante de uma entrada inválida ou falha de acesso ao banco. Compare o código antes e depois da separação da persistência.

## Preparação da disciplina

O livro usa Java 25 e inclui exemplos com recursos em *preview*. Para a etapa de persistência, são necessários PostgreSQL e o driver JDBC. Planejamento, protocolos, segurança e operação de redes exigem material especializado e laboratórios compatíveis com os objetivos da disciplina.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral sobre os cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
