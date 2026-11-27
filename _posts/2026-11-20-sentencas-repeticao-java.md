---
layout: post
title: "Laços de repetição em Java"
date: 2026-11-20
lang: pt-BR
translation_id: sentencas-repeticao-java
permalink: /sentencas-repeticao-java/
share_text: >-
  for, for-each, while e do-while com os exemplos de contagem e soma do livro.
---

Laços repetem uma sentença ou bloco. Em um `for` de contagem, a inicialização, a condição e a atualização aparecem no cabeçalho. O exemplo imprime os números de 1 a 5:

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Valor de i: " + i);
}
```

O livro usa outro `for` para somar a série `1/1 + 4/2 + 7/3 + … + 100/34`. O numerador aumenta de três em três e o denominador de um em um:

```java
void main(){
    double soma = 0.0;
    for (int numerador = 1, denominador = 1; 
         numerador <= 100;
         numerador += 3, denominador++)
        soma += (double) numerador / denominador;
    IO.println("Soma: " + soma);
}
```

A soma impressa no exemplo é `93.76358001910911`. `String.format("%.2f", soma)` pode mostrar duas casas decimais usando o *locale* padrão; com `Locale.US`, o separador decimal é o ponto:

```java
IO.println("Soma: " + String.format("%.2f",soma));
```

```java
IO.println("Soma: " + String.format(Locale.US,"%.2f",soma));
```

## Percorrendo elementos com `for-each`

O **for-each** executa o corpo uma vez para cada elemento de um vetor ou de um `Iterable`. O livro percorre primeiro um vetor de inteiros:

```java
void main(){
    // Declara e inicializa um vetor de inteiros
    int[] v = {1,2,3,4,5};
    // Itera sobre o vetor, mostrando os elementos
    for (var valor : v) 
        IO.println("Valor: " + valor);
}
```

Depois percorre uma lista de nomes:

```java
void main() {
    // Cria uma lista de nomes de pessoas
    var pessoas = new ArrayList<String>();
    pessoas.add("Maria");
    pessoas.add("Pedro");
    pessoas.add("Paulo");
    // Itera sobre a colecao, mostrando os nomes
    for (var p : pessoas)
        IO.println("Nome da pessoa: " + p);
}
```

## `while` e `do-while`

O `while` verifica a condição antes de cada repetição. A mesma soma da série pode ser feita assim:

```java
void main() {
    int numerador = 1, denominador = 1;
    var soma = 0.0;
    while (numerador <= 100) {
        soma += (double) numerador / denominador;
        numerador += 3;
        denominador++;
    }
    IO.println("Soma: " + soma);
}
```

O `do-while` verifica a condição **depois** do corpo e, portanto, executa o corpo ao menos uma vez. O livro reapresenta a série nessa forma:

```java
void main() {
    int numerador = 1, denominador = 1;
    var soma = 0.0;
    do {
        soma += (double) numerador / denominador;
        numerador += 3;
        denominador++;
    } while (numerador <= 100);
    IO.println("Soma: " + soma);
}
```

Os três laços de soma chegam ao mesmo resultado; o momento da verificação e a forma de atualização determinam qual construção é mais adequada em cada situação.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
