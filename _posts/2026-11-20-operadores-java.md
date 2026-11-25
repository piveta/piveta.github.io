---
layout: post
title: "Operadores em Java"
date: 2026-11-20
lang: pt-BR
translation_id: operadores-java
permalink: /operadores-java/
share_text: >-
  Operadores aritméticos, de atribuição e relacionais, com exemplos do capítulo introdutório.
---

## Operadores aritméticos

Operadores aplicam operações a valores, variáveis e expressões. Entre os **operadores aritméticos** binários estão `+` (adição), `-` (subtração), `*` (multiplicação), `/` (divisão) e `%` (resto). A precedência dos operadores influencia a avaliação das expressões.

### Incremento e decremento

Os operadores `++` e `--` alteram uma variável numérica em uma unidade. Como sentenças isoladas, as formas pós-fixadas abaixo levam `x` de 10 para 11 e depois de volta para 10:

```java
void main(){
    var x = 10;
    x++;
    IO.println("X vale " + x);
    x--;
    IO.println("E agora x vale " + x);
}
```

Quando o valor é usado em uma expressão, a posição do operador importa. Em `y = x++`, o valor antigo de `x` é atribuído a `y` antes do incremento. Ao final, `x` é 11 e `y` é 10:

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X vale " + x);
    IO.println("E y vale " + y);
}
```

Em `y = ++x`, o incremento ocorre antes da atribuição. As duas variáveis ficam com 11:

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X vale " + x);
    IO.println("E y vale " + y);
}
```

Outros operadores unários incluem `+`, `-`, `~` (complemento bit a bit) e `!` (negação lógica). Operadores binários recebem dois operandos; a avaliação também depende da precedência e da ordem definidas pela linguagem.

## Operadores de atribuição

O operador `=` atribui à variável à esquerda o valor calculado pela expressão à direita. Uma variável pode ser declarada e receber seu valor depois:

```java
int idade;
String nome;
Double altura;
```

```java
idade = 20;
nome = "Maria";
altura = 1.70;
```

Também pode ser inicializada na própria declaração, quando o valor já está disponível:

```java
int idade = 20;
String nome = "Maria";
Double altura = 1.70;
```

### Atribuição composta

Operadores como `+=`, `-=`, `*=`, `/=` e `%=` combinam uma operação com a atribuição. O livro modifica repetidamente a variável `a`:

```java
void main() {
    int a = 10;
    a += 10;
    IO.println("a = " + a);
    a -= 10;
    IO.println("a = " + a); 
    a *= 10;
    IO.println("a = " + a); 
    a /= 10;
    IO.println("a = " + a); 
    a %= 3;
    IO.println("a = " + a); 
}
```

Os valores impressos, nessa ordem, são:

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

Uma atribuição composta não deve ser tratada como mera substituição textual em todos os casos: a especificação considera o tipo da variável à esquerda e avalia essa expressão uma única vez. A linguagem também possui atribuições compostas para deslocamentos e operações bit a bit.

## Operadores relacionais

Os **operadores relacionais** comparam dois operandos e produzem `true` ou `false`. Os principais são `==` (igual), `!=` (diferente), `>` (maior), `>=` (maior ou igual), `<` (menor) e `<=` (menor ou igual). Seus resultados aparecem frequentemente em `if` e nas condições de laços.

O exemplo do livro lê uma idade e testa várias relações de modo independente:

```java
void main(){
    var idade = Integer.parseInt(IO.readln("Idade:"));
    if (idade == 10)
        IO.println("Idade igual a 10 anos");
    if (idade != 20)
        IO.println("Idade diferente de 20 anos");
    if (idade > 30)
        IO.println("Idade maior de 30 anos");
    if (idade <= 80)
        IO.println("Idade menor ou igual a 80 anos");
}
```

Se a idade informada for 10, as mensagens exibidas são “Idade igual a 10 anos”, “Idade diferente de 20 anos” e “Idade menor ou igual a 80 anos”. Como cada condição é um `if` separado, mais de uma mensagem pode ser exibida. `Integer.parseInt` converte para inteiro a cadeia retornada por `IO.readln`.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
