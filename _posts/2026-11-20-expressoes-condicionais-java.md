---
layout: post
title: "Expressões e sentenças condicionais em Java"
date: 2026-11-20
lang: pt-BR
translation_id: expressoes-condicionais-java
permalink: /expressoes-condicionais-java/
share_text: >-
  Expressões, blocos, if, else, operador ternário e switch nos exemplos do capítulo inicial.
---

## Expressões e sentenças

Uma **expressão** é avaliada e produz um valor. Pode combinar literais, variáveis, operadores, chamadas de métodos ou construção de objetos. O livro mostra estes fragmentos como exemplos de expressões; isoladamente, eles não formam um programa completo:

```text
x + 2 * 1
c.getSaldo()
i = 20
```

Uma **sentença** é uma unidade executável. Chamadas de métodos, atribuições e incrementos podem ser sentenças quando usados no contexto adequado e terminados por `;`. O fragmento a seguir também depende de declarações e de uma classe `Conta` não mostradas nele:

```text
c.getSaldo();
i = 20;
i++;
Conta c1 = new Conta();
```

Além das sentenças de expressão, há declarações de variáveis e sentenças de controle, como `if`, `while` e `for`. Chaves agrupam várias sentenças em um **bloco**. O programa abaixo lê um inteiro, testa uma condição e executa duas saídas dentro de um bloco:

```java
void main() {
    int x = Integer.parseInt(
            IO.readln("Digite um inteiro: "));
    if (x < 10) {  
        IO.println("X menor que 10."); 
        IO.println("Inicialize X com outro valor."); 
    }
}
```

A condição decide se o bloco é executado. Os laços, por sua vez, repetem sentenças enquanto suas próprias regras de controle forem satisfeitas.

## Sentenças condicionais

Uma sentença condicional escolhe o caminho da execução segundo uma expressão booleana. No caso mais simples, `if` executa a sentença controlada apenas quando a condição é verdadeira:

```java
void main() {
    var idade = Integer.parseInt(IO.readln("Idade: "));
    if (idade >= 18)
        IO.println("Maior de idade");
}
```

Com `else`, é possível definir também o comportamento para a condição falsa:

```java
void main() {
    var idade = Integer.parseInt(IO.readln("Idade:"));
    if (idade >= 18)
        IO.println("Maior de idade");
    else
        IO.println("Menor de idade");
}
```

Chaves agrupam várias sentenças em cada caminho. O exemplo apresenta duas mensagens para cada resultado da comparação:

```java
void main() {
    var idade = Integer.parseInt(IO.readln("Idade: "));
    if (idade >= 18) {
        IO.println("Maior de idade");
        IO.println("Acesso permitido");
    }
    else {
        IO.println("Menor de idade");
        IO.println("Acesso negado");
    }
}
```

As condições também podem ser **aninhadas**. Depois de confirmar a maioridade, o programa testa se há direito a acesso prioritário:

```java
void main() {
    var idade = Integer.parseInt(IO.readln("Idade: "));
    if (idade >= 18) {
        IO.println("Maior de idade");
        IO.println("Acesso permitido");
        if (idade >= 65)
            IO.println("Acesso prioritário concedido");
    } else {
        IO.println("Menor de idade");
        IO.println("Acesso negado");
    }
}
```

O **operador ternário** é uma expressão: avalia a condição e escolhe entre dois valores. No exemplo, o resultado compõe a mensagem final:

```java
void main(){
    var idade = Integer.parseInt(IO.readln("Idade: "));
    // O operador ternário tem sintaxe: 
		// (expr) ? true : false
    String msg = ((idade >= 18) ? "Maior" : "Menor") + 
                 " de 18 anos";
    IO.println(msg);
}
```

### Escolhas entre vários caminhos

Uma sentença `switch` escolhe um caso, usa `break` para encerrar sua execução e possui `default` para os demais valores:

```java
void main() {
    int idade = Integer.parseInt(IO.readln("Idade: "));
    String mensagem;
    switch (idade) {
        case 0: case 1: case 2: case 3: case 4: case 5:
            mensagem = "Muito jovem";
            break;
        case 18:
            mensagem = "Entrando na maioridade";
            break;
        case 65:
            mensagem = "Entrando na terceira idade";
            break;
        default:
            mensagem = "Sem particularidades";
            break;
        }
        IO.println(mensagem);
}
```

Uma **expressão `switch`** usa setas, separa vários valores por vírgulas e produz um resultado, sem `break` em cada caso:

```java
void main() {
    int idade = Integer.parseInt(IO.readln("Idade: "));
    String mensagem = switch (idade) {
        case 0, 1, 2, 3, 4, 5 -> "Muito jovem";
        case 18 -> "Entrando na maioridade";
        case 65 -> "Entrando na terceira idade";
        default -> "Sem particularidades";
    };
    IO.println(mensagem);
}
```

O livro mostra ainda **pattern matching** com guardas `when`, que combinam o tipo do objeto e uma condição adicional. O método trata `Integer`, `String`, `null` e outros tipos:

```java
private static String idade(Object idadeObj) {
    return switch (idadeObj) {
        case Integer i when i >= 65 -> 
            "[Integer] Maior de idade: " + i + 
            "\nAcesso prioritário concedido.";
        case Integer i when i >= 18 -> 
            "[Integer] Maior de idade: " + i + 
             "\nAcesso concedido.";
        case Integer i -> "[Integer] Menor de idade: " + 
                i + "\nAcesso negado.";
        case String s -> 
            "[String] Idade informada como texto: " + s;
        case null -> "[null] Idade não informada";
        default -> "Tipo de dado inesperado: " + 
                idadeObj.getClass().getName();
    };
}
```

O cliente invoca o método com quatro valores distintos:

```java
void main() {
    IO.println(idade("80"));
    IO.println(idade(10));
    IO.println(idade(null));
    IO.println(idade(10.2));
}
```

A saída apresentada pelo livro é:

```text
[String] Idade informada como texto: 80
[Integer] Menor de idade: 10
Acesso negado.
[null] Idade não informada
Tipo de dado inesperado: java.lang.Double
```

As três formas de `switch` ilustram a evolução da linguagem. O último exemplo requer uma versão de Java que ofereça correspondência de padrões em `switch`.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
