---
layout: post
title: "Associação, agregação e composição em Java"
date: 2026-11-24
lang: pt-BR
translation_id: relacionamentos-entre-classes-java
permalink: /relacionamentos-entre-classes-java/
share_text: >-
  Um condutor pode trocar de veículo, as rodas podem ser substituídas e o tecido depende dos fios que o compõem. Esses exemplos mostram como distinguir associação, agregação e composição na modelagem orientada a objetos.
---

Na orientação a objetos, classes se relacionam para representar o domínio de uma aplicação. Associação, agregação e composição descrevem formas de relacionar objetos com diferentes graus de dependência.

## Associação

Uma associação pode ser transitória e mudar durante a execução do programa. Em um sistema de trânsito, uma pessoa pode estar associada a um veículo no papel de condutora. Ao trocar o condutor, a pessoa que dirigia e o veículo continuam a existir, mesmo que o vínculo entre eles termine.

## Agregação

A agregação representa uma relação de todo e parte. Um carro tem quatro rodas. O carro é o agregador e as rodas são as partes agregadas. É possível separar as rodas do carro e substituí-las. Nesse exemplo, o vínculo é mais forte que o de um condutor com o veículo.

## Composição

Na composição, as partes integram o objeto maior de maneira mais estreita. O tecido que reveste o assento do veículo é composto de fios. Sem os fios, o tecido deixa de existir como tal e o assento perde aquele revestimento.

## Como representar esses vínculos em Java

Os três relacionamentos podem ser representados com atributos que guardam referências a objetos. As regras do domínio determinam o tipo de vínculo. Na associação, os objetos podem ser criados separadamente e ligados quando necessário. Na composição, é comum criar as partes no construtor do objeto que as contém.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
