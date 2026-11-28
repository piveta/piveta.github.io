---
layout: post
title: "Leitura e escrita no console em Java"
date: 2026-11-20
lang: pt-BR
translation_id: leitura-escrita-java
permalink: /leitura-escrita-java/
share_text: >-
  Como usar IO, Scanner e readln para escrever e ler valores em programas Java 25.
---

Muitos programas recebem dados, processam esses dados e apresentam um resultado. Em Java 25, a classe `IO` simplifica a escrita no console com `print`, `println` e a leitura com `readln`. Os exemplos de código-fonte compacto deste capítulo usam recursos que podem exigir a habilitação do modo *preview*.

## Escrevendo valores

`print` escreve sem acrescentar uma quebra de linha; `println` encerra a linha. O livro importa estaticamente os métodos de `java.lang.IO`, permitindo chamá-los sem prefixo:

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Resultado: ");
    println("Soma de a e b: " + (a + b));
}
```

As variáveis `a` e `b` recebem 10 e 20. Como a primeira chamada não quebra a linha, a saída é `Resultado: Soma de a e b: 30` em uma só linha.

## Lendo com `Scanner`

`Scanner` lê valores da entrada padrão. No exemplo, `nextLine()` obtém texto e `nextInt()` obtém a idade. Depois de `nextInt()`, uma chamada adicional a `nextLine()` consome a quebra de linha pendente antes da leitura do endereço:

```java
import java.util.Scanner;
void main(){
    var s = new Scanner(System.in);
    IO.println("Nome: ");
    var nome = s.nextLine(); 
    IO.println("Idade: ");
    var idade = s.nextInt(); 
    s.nextLine(); // Consome a quebra de linha
    IO.println("Endereço: ");
    var endereco = s.nextLine(); 
    IO.println("Dados informados:");
    IO.println("Nome: " + nome + ", Idade: " + idade);
    IO.println("Endereço: " + endereco);
}
```

## Lendo com `IO.readln`

`readln` recebe um texto de solicitação e retorna uma `String`. O mesmo exemplo pode ser escrito com a importação estática de `IO`:

```java
import static java.lang.IO.*; 
void main(){
    var nome = readln("Nome: ");
    var idade = Integer.parseInt(readln("Idade: ")); 
    var endereco = readln("Endereço: ");
    println("Dados informados:");
    println("Nome: " + nome + ", Idade: " + idade);
    println("Endereço: " + endereco);
}
```

Como a idade lida é uma `String`, o programa usa `Integer.parseInt` para convertê-la em inteiro. Uma entrada que não represente um inteiro causa `NumberFormatException`; o exemplo do livro não trata essa exceção. O uso do console aqui serve para apresentar a linguagem, embora aplicações também possam receber dados por formulários e interfaces gráficas.

Comentários de uma linha começam com `//`; comentários de várias linhas usam `/*` e `*/`:

```java
// Texto comentado de uma linha
   
/* Texto comentado
   com mais linhas. */
```

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
