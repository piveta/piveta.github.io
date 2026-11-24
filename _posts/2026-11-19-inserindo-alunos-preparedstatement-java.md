---
layout: post
title: "Inserindo alunos com PreparedStatement em Java"
date: 2026-11-19
lang: pt-BR
translation_id: inserindo-alunos-preparedstatement-java
permalink: /inserindo-alunos-preparedstatement-java/
share_text: >-
  O exemplo do livro insere Maria, Pedro e João por JDBC, reutilizando um PreparedStatement com dois parâmetros.
---

No exemplo do livro, um `PreparedStatement` representa uma sentença SQL parametrizada. Os valores variáveis ocupam os pontos de interrogação (`?`) e são informados por métodos como `setInt` e `setString`. Isso evita montar a SQL por concatenação dos dados e reduz o risco de injeção de SQL.

O trecho abaixo pertence ao método `main` de `DBExemplo`. A variável `c` é a conexão aberta com `DriverManager.getConnection` para o banco PostgreSQL `academico`. A tabela `aluno` possui `matricula` (inteiro, chave primária) e `nome` (texto). O código do livro insere os três alunos diretamente, sem vetores ou laços:

```java
IO.println("Inserindo alunos...");
var p = c.prepareStatement("insert into aluno " +
        "(matricula, nome) values (?, ?)");
p.setInt(1, 1); 
p.setString(2, "Maria");
p.execute(); // Insere 1 - Maria
p.setInt(1, 2);
p.setString(2, "Pedro");
p.execute(); // Insere 2 - Pedro
p.setInt(1, 3);
p.setString(2, "João");
p.execute(); // Insere 3 - João
```

A posição **1** corresponde à matrícula e a posição **2** ao nome. O `PreparedStatement` é reutilizado: após cada par de valores, `execute()` executa a inserção. As três operações equivalem a estas sentenças SQL mostradas no livro:

```sql
insert into aluno(matricula, nome) values (1, 'Maria');
insert into aluno(matricula, nome) values (2, 'Pedro');
insert into aluno(matricula, nome) values (3, 'João');
```

Como a matrícula é chave primária, uma inserção com matrícula repetida é rejeitada pelo banco. Nesse exemplo, o método `main` declara `throws SQLException`, de modo que a falha é propagada. A conexão, a sentença e os demais recursos são fechados explicitamente no final do programa completo do livro.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
