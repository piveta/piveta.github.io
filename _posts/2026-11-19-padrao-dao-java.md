---
layout: post
title: "O padrão DAO no acesso a dados com Java"
date: 2026-11-24
lang: pt-BR
translation_id: padrao-dao-java
permalink: /padrao-dao-java/
share_text: >-
  O padrão Data Access Object separa a persistência das regras de negócio e da apresentação em uma aplicação Java.
---

Uma aplicação pode abrir uma conexão, executar SQL, aplicar regras de negócio e mostrar resultados em uma única classe. Essa concentração funciona em exemplos pequenos, mas dificulta a leitura e a manutenção quando o sistema cresce. O capítulo **Estendendo classes: acesso a dados** usa o padrão DAO (*Data Access Object*) para separar a responsabilidade de persistir dados das demais responsabilidades.

Um DAO oferece operações como inserir, buscar, alterar e excluir objetos. O restante da aplicação chama essas operações sem precisar conhecer as instruções SQL, a forma de abrir conexões ou como converter linhas do banco em objetos. No exemplo do livro, `Aluno` representa os dados de um aluno e `AlunoDAO` concentra as operações sobre a tabela `aluno`. A classe `DBExemplo` atua como cliente do DAO: pede as operações e apresenta seus resultados.

Essa separação reduz o acoplamento. Se a forma de acesso ao banco mudar, a implementação do DAO pode ser alterada sem obrigar a camada cliente a reescrever suas regras e sua apresentação. Uma interface bem definida também facilita os testes, pois uma implementação simulada pode substituir o acesso ao banco em cenários de teste.

O livro implementa primeiro um DAO específico para alunos. Depois, aproveita **herança, classe abstrata e tipos genéricos** para colocar operações comuns em `AbstractDAO<T>`, enquanto `AlunoDAO` mantém os detalhes da entidade e das sentenças SQL. A mudança mostra como a mesma interface de uso pode permanecer estável para o cliente, mesmo quando a organização interna do acesso a dados evolui.

Em sistemas maiores, bibliotecas como Spring JDBC e ferramentas de mapeamento objeto-relacional podem oferecer outras abstrações. O exemplo do livro usa JDBC diretamente para tornar visíveis as responsabilidades e os pontos de separação.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/classe-aluno-dao-java/" | first %}
{% if dao_related_post %}
- [A classe Aluno no exemplo de DAO](/classe-aluno-dao-java/) — modelo dos dados do aluno.
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/dados-conexao-record-java/" | first %}
{% if dao_related_post %}
- [Um record para os dados de conexão JDBC](/dados-conexao-record-java/) — valores da conexão JDBC.
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/aluno-dao-crud-java/" | first %}
{% if dao_related_post %}
- [Criando AlunoDAO com operações CRUD](/aluno-dao-crud-java/) — implementação inicial do DAO.
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Artigos relacionados

{{ dao_related_links }}

{% endif %}

Em outro idioma: [Versão em inglês](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
