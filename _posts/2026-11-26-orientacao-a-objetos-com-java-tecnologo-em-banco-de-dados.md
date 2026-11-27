---
layout: post
title: "Orientação a Objetos com Java no Tecnólogo em Banco de Dados"
date: 2026-11-26
lang: pt-BR
translation_id: orientacao-a-objetos-com-java-tecnologo-em-banco-de-dados
permalink: /orientacao-a-objetos-com-java-tecnologo-em-banco-de-dados/
share_text: >-
  O papel da primeira edição de Orientação a Objetos com Java no Tecnólogo em Banco de Dados, com competências, capítulos, disciplinas e sugestões de adoção.
---

A perspectiva do livro é a de quem precisa gravar e ler dados em uma aplicação. O estudante configura uma tabela, usa JDBC para consultar e modificar registros e depois encapsula o acesso em classes Java. Essa perspectiva ajuda a relacionar decisões do banco ao comportamento do programa cliente.

## Referência curricular

A graduação tecnológica integra o eixo Informação e Comunicação, na área de Desenvolvimento de Sistemas do Catálogo Nacional de Cursos Superiores de Tecnologia (CNCST). A Portaria MEC nº 514/2024 aprovou a 4ª edição. O perfil de conclusão orienta o cruzamento. Cada instituição detalha as disciplinas no seu projeto pedagógico.

O CNCST prevê projetar, implementar, documentar, testar e gerenciar bancos de dados, além de criar soluções de coleta, tratamento e manipulação de dados. O livro contribui para a implementação relacional em pequena escala e para a integração de aplicações com o banco. O perfil inclui também desempenho, segurança, grandes volumes e análise de dados.

- [Diretrizes Gerais da Educação Profissional e Tecnológica, Resolução CNE/CP nº 1/2021](https://portal.mec.gov.br/dmdocuments/rcp001_21.pdf)
- [Portaria MEC nº 514/2024 e extrato da 4ª edição do CNCST](https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?captchafield=firstAccess&data=06%2F06%2F2024&jornal=515&pagina=28)
- [CNCST, perfil profissional do curso na edição de 2024](https://www.tecnologo.org.br/documentos/CNCST_2024___Catalogo_Nacional_dos_Cursos_Superiores_de_Tecnologia___06_2024_102859.pdf#page=123)

## Competências e capítulos do livro

Os caps. 3, 6 e 7 têm o vínculo mais próximo com **a integração de aplicações Java com bancos de dados relacionais**. Os caps. 1, 2, 4 e 5 podem ser usados em unidades de apoio, conforme a ementa e a linguagem de prática. A cobertura é direta quando a obra permite praticar a habilidade descrita. É parcial ou preparatória quando a competência exige uma atividade ou uma tecnologia adicional.

| Competência ou capacidade profissional | Leitura na 1ª edição | Aplicação e alcance |
| --- | --- | --- |
| Implementar uma estrutura relacional simples | Cap. 3, § 3.1 | Direta para o exemplo. Criar a tabela do cadastro e relacionar suas colunas às informações manipuladas pela aplicação. |
| Manipular dados e resultados de uma consulta | Cap. 3, §§ 3.2.1–3.2.6 | Direta. Conectar a aplicação, parametrizar operações e percorrer os resultados. |
| Organizar a interface de acesso ao banco | Cap. 6, §§ 6.2–6.3, e cap. 7, § 7.2.4 | Direta para o código cliente. Centralizar o mapeamento dos registros, separar responsabilidades e fechar recursos. |
| Projetar e gerenciar bancos em escala | Exemplo introdutório do cap. 3 | Preparatória. A atividade estabelece a conexão entre programa e banco e pode ser ampliada com exercícios de transações e desempenho. |

## Disciplinas e recomendação bibliográfica

| Disciplina ou unidade | Indicação | Capítulos e condições de adoção |
| --- | --- | --- |
| Integração com Banco de Dados ou Persistência com Java | Básica se o laboratório for centrado em JDBC | Caps. 3, 6 e 7, acompanhando a criação da tabela até o fechamento de recursos. |
| Programação Orientada a Objetos | Básica em Java | Caps. 2, 4, 5 e 7. Usar o DAO como exemplo de aplicação orientada a objetos. |
| Banco de Dados Relacionais ou SQL | Complementar | Caps. 3 e 6 para observar como comandos SQL são chamados por uma aplicação. Adotar textos próprios para normalização, transações, índices e administração. |

A matriz de Tecnologia em Banco de Dados do SENAI-RS inclui Programação Orientada a Objetos. Quando o curso oferece um componente desse tipo, há espaço para adoção na formação de software, com o cadastro dos caps. 3 e 6 servindo de exercício de integração.

- [Matriz de Tecnologia em Banco de Dados do SENAI-RS](https://www.senairs.org.br/sites/default/files/paragraph--files/grade_banco_de_dados_presencial.pdf)

## Atividade sugerida

### Da consulta para o objeto

Executar uma consulta com parâmetro e converter seu resultado em um objeto da aplicação. Encapsular a operação em um DAO e observar o comportamento quando nenhum registro é encontrado.

**Como observar a aprendizagem.** Avaliar o uso dos parâmetros, a conversão entre colunas e atributos, a liberação dos recursos e a distinção entre resultado vazio e falha de acesso.

## Alcance e preparação da disciplina

A formação em modelagem relacional, bancos distribuídos, NoSQL, segurança, desempenho, administração e análise de dados pede bibliografia própria. O livro se concentra na fronteira entre a aplicação Java e um banco relacional.

A primeira edição usa Java 25. Em laboratório, testar previamente os exemplos selecionados e habilitar os recursos em *preview* quando o trecho exigir. Nas atividades de persistência, reservar também uma base PostgreSQL e disponibilizar o driver JDBC. Se a turma adotar outra versão ou linguagem, explicitar quais exemplos serão adaptados.

## Referência da obra

PIVETA, Eduardo Kessler. **Orientação a Objetos com Java**. 1. ed. Santa Maria, RS: Ed. do Autor, 2025. ISBN da edição impressa 978-65-01-77821-1. ISBN do livro eletrônico em PDF 978-65-01-74605-0. [Sumário e acesso à amostra](/)

[Leia também o artigo geral com os 15 cursos]({% link orientacao-a-objetos-com-java-nos-curriculos-de-computacao.md %})
