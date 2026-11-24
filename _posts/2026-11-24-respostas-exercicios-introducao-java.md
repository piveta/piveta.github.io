---
layout: post
title: "Respostas dos exercícios da introdução ao Java"
date: 2026-11-24
lang: pt-BR
translation_id: respostas-exercicios-introducao-java
permalink: /respostas-exercicios-introducao-java/
share_text: >-
  Soluções comentadas para os 10 exercícios do capítulo 1 do livro Orientação a Objetos com Java.
---

Capítulo 1 de *Orientação a Objetos com Java*.

[Ler os enunciados]({{ '/exercicios-introducao-java/' | relative_url }})

Use um arquivo separado para cada solução. Em Java 25 ou posterior, coloque o trecho dentro de `void main() { ... }` no arquivo e execute com `java NomeDoArquivo.java`. Quando o programa pedir vários valores, digite um por linha.

## 1. Operações com dois inteiros

Converta um operando para fazer a divisão real. Use `long` nas demais operações para acomodar resultados fora do intervalo de `int`.

~~~java
var a = Integer.parseInt(IO.readln("Primeiro inteiro: ").strip());
var b = Integer.parseInt(IO.readln("Segundo inteiro: ").strip());
IO.println("Soma: " + ((long) a + b));
IO.println("Subtração: " + ((long) a - b));
IO.println("Multiplicação: " + ((long) a * b));
IO.println(b == 0 ? "Divisão indefinida" : "Divisão: " + (double) a / b);
~~~

## 2. Área e perímetro do retângulo

Para lados `3` e `4,5`, a área é `13,5` e o perímetro é `15`. Digite os valores decimais com ponto, como `4.5`.

~~~java
var largura = Double.parseDouble(IO.readln("Largura: ").strip());
var altura = Double.parseDouble(IO.readln("Altura: ").strip());
if (largura > 0 && altura > 0) {
    IO.println("Área: " + largura * altura);
    IO.println("Perímetro: " + 2 * (largura + altura));
} else
    IO.println("Os lados devem ser positivos.");
~~~

## 3. Classificação do triângulo

A soma dos dois menores lados deve superar o maior. Ordená-los reduz a validação a uma desigualdade.

~~~java
var lados = new int[] {
    Integer.parseInt(IO.readln("Primeiro lado: ").strip()),
    Integer.parseInt(IO.readln("Segundo lado: ").strip()),
    Integer.parseInt(IO.readln("Terceiro lado: ").strip())
};
java.util.Arrays.sort(lados);
var a = lados[0];
var b = lados[1];
var c = lados[2];
if (a <= 0 || (long) a + b <= c)
    IO.println("Não forma triângulo.");
else if (a == c)
    IO.println("Equilátero");
else if (a == b || b == c)
    IO.println("Isósceles");
else
    IO.println("Escaleno");
~~~

## 4. Raízes da equação do segundo grau

Para `1, -3, 2`, as raízes são `2` e `1`. Com discriminante zero, há uma raiz real distinta.

~~~java
var a = Double.parseDouble(IO.readln("a: ").strip());
var b = Double.parseDouble(IO.readln("b: ").strip());
var c = Double.parseDouble(IO.readln("c: ").strip());
var delta = b * b - 4 * a * c;
if (a == 0)
    IO.println("O coeficiente a deve ser diferente de zero.");
else if (delta < 0)
    IO.println("Não há raízes reais.");
else {
    var raiz = Math.sqrt(delta);
    IO.println((-b + raiz) / (2 * a));
    if (delta > 0) IO.println((-b - raiz) / (2 * a));
}
~~~

## 5. Valores acima da média

Guarde os valores para poder percorrê-los depois de conhecer a média. Para os números de 1 a 10, imprima de 6 a 10.

~~~java
var numeros = new int[10];
var soma = 0L;
for (var i = 0; i < numeros.length; i++) {
    numeros[i] = Integer.parseInt(IO.readln("Número " + (i + 1) + ": ").strip());
    soma += numeros[i];
}
var media = (double) soma / numeros.length;
for (var numero : numeros)
    if (numero > media) IO.println(numero);
~~~

## 6. Pares e ímpares até o zero

O zero encerra a leitura. Guarde os ímpares porque o maior par pode mudar até a última entrada. Com `-4 -2 -3 1 0`, há dois pares, média ímpar `-1`, maior par `-2` e um ímpar acima dele.

~~~java
var impares = new java.util.ArrayList<Integer>();
var quantidadePares = 0;
Integer maiorPar = null;
var somaImpares = 0L;
while (true) {
    var linha = IO.readln("Inteiro (0 encerra): ");
    if (linha == null) break;
    var n = Integer.parseInt(linha.strip());
    if (n == 0) break;
    if (n % 2 == 0) {
        quantidadePares++;
        maiorPar = maiorPar == null ? n : Math.max(maiorPar, n);
    } else {
        impares.add(n);
        somaImpares += n;
    }
}
IO.println("Quantidade de pares: " + quantidadePares);
IO.println(impares.isEmpty() ? "Sem ímpares" :
        "Média dos ímpares: " + (double) somaImpares / impares.size());
if (maiorPar == null)
    IO.println("Sem maior par para comparar.");
else {
    var acima = 0;
    for (var impar : impares)
        if (impar > maiorPar) acima++;
    IO.println("Maior par: " + maiorPar);
    IO.println("Ímpares acima do maior par: " + acima);
}
~~~

## 7. Busca de países

`equals` compara o nome inteiro e `contains` busca um trecho, ambos com distinção de maiúsculas.

~~~java
var paises = java.util.List.of("Brasil", "Argentina", "Chile", "Peru",
        "Uruguai", "Paraguai", "Colômbia", "Costa Rica", "Japão", "Portugal");
var busca = IO.readln("Nome ou trecho: ");
var exato = false;
for (var pais : paises) {
    if (pais.equals(busca)) exato = true;
    if (busca != null && pais.contains(busca)) IO.println(pais);
}
IO.println(exato ? "Nome exato encontrado." : "Nome exato ausente.");
~~~

## 8. Tabuada de 1 a 9

O laço interno percorre os multiplicadores para cada número do laço externo.

~~~java
for (var numero = 1; numero <= 9; numero++)
    for (var multiplicador = 1; multiplicador <= 9; multiplicador++)
        IO.println("%d x %d = %d".formatted(numero, multiplicador, numero * multiplicador));
~~~

## 9. Contagem regressiva

Para `5`, a saída é `5 4 3 2 1 0`. Uma entrada negativa fica fora da contagem regressiva até zero.

~~~java
var inicio = Integer.parseInt(IO.readln("Início: ").strip());
if (inicio < 0)
    IO.println("Informe um inteiro não negativo.");
for (var n = inicio; n >= 0; n--)
    IO.print(n + (n == 0 ? System.lineSeparator() : " "));
~~~

## 10. Menu de quatro opções

O `do-while` exibe o menu ao menos uma vez. Uma opção inválida recebe uma mensagem e o menu reaparece.

~~~java
String opcao;
do {
    IO.println("1. Consultar | 2. Cadastrar | 3. Listar | 4. Sair");
    var linha = IO.readln("Opção: ");
    if (linha == null) break;
    opcao = linha.strip();
    switch (opcao) {
        case "1" -> IO.println("Consultar");
        case "2" -> IO.println("Cadastrar");
        case "3" -> IO.println("Listar");
        case "4" -> IO.println("Encerrando.");
        default -> IO.println("Opção inválida.");
    }
} while (!opcao.equals("4"));
~~~

*As soluções acompanham os exercícios do livro [Orientação a Objetos com Java](/livro-orientacao-a-objetos-com-java/), de Eduardo Kessler Piveta.*
