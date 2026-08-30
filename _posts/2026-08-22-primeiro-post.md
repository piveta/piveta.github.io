---
layout: post
title: "Hello World - Versão Tradicional vs. Versão Simplificada"
date: 2026-08-22
---
**Por Eduardo Piveta**  
*Professor Titular - UFSM*

É de praxe iniciarmos o estudo de uma linguagem de programação com a escrita de um programa chamado **Hello World**, que mostra o texto `Hello World!` na saída padrão do dispositivo, usualmente a tela. Em Java, podemos escrever esse programa da seguinte forma:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

Neste programa, temos uma classe denominada `Hello`. As classes em sistemas orientados a objetos auxiliam a modelar conceitos do domínio da aplicação que está sendo objeto de estudo. As classes encapsulam tanto os dados quanto o comportamento de determinado conceito.

A classe `Hello` possui um único método, chamado `main`, que recebe um vetor de cadeias de caracteres contendo os argumentos de linha de comando fornecidos na execução do programa, caso existam. Neste exemplo, tais argumentos não são utilizados.

O método `main` é estático, o que significa que é um método de classe, e não um método de instância. Assim, ele pode ser chamado sem que seja necessário criar um objeto da classe `Hello`.

Dentro do método `main` existe uma chamada ao método `println`. Esse método pertence à classe `PrintStream` e imprime na tela o que for passado como parâmetro, seguido de um término de linha.

O método `println` é chamado a partir do atributo `out` da classe `System`. Esse atributo é do tipo `PrintStream` e fornece acesso à saída padrão do sistema.

## Uma forma mais simples com Java 25+

A partir do Java 25, uma funcionalidade que vinha sendo desenvolvida como *preview* desde o Java 21 tornou-se permanente: **Compact Source Files and Instance Main Methods**. Ela permite escrever pequenos programas com menos código de infraestrutura, omitindo a declaração explícita da classe e simplificando o método `main`.

Assim, o programa anterior pode ser escrito em Java 26 como:

```java
void main() {
    IO.println("Hello World!");
}
```

Nesse caso, não precisamos declarar explicitamente a classe nem escrever `public static void main(String[] args)`. O compilador considera que o arquivo declara implicitamente uma classe, e o método `main` pode ser um método de instância.

Também podemos utilizar a classe `IO`, que fornece operações simples para entrada e saída no console. Em Java 26, `IO` pertence ao pacote `java.lang` e, portanto, está implicitamente disponível. Para chamar seus métodos, entretanto, é necessário utilizar o nome da classe, como em `IO.println(...)`.

Como essa funcionalidade não está mais em modo *preview*, não precisamos utilizar opções especiais de compilação. O programa pode ser compilado normalmente:

```text
javac Hello.java
```

e executado da mesma forma:

```text
java Hello
```

Também é possível executar diretamente um arquivo-fonte usando o lançador `java`:

```text
java Hello.java
```

Nesse caso, o código-fonte é compilado em memória pelo próprio lançador antes da execução. Esse mecanismo permite executar programas diretamente a partir dos arquivos-fonte sem a necessidade de produzir explicitamente um arquivo `.class`.

O uso de arquivos compactos de código-fonte é especialmente interessante para exemplos pequenos, programas de aprendizado, scripts e experimentos. À medida que o programa cresce e passa a exigir uma estrutura mais elaborada, podemos retornar naturalmente à forma tradicional, com declarações explícitas de classes e métodos.

## Compilação e execução

Os programas em Java são primeiro compilados para uma representação intermediária, denominada **bytecode**, de forma a garantir sua portabilidade. Posteriormente, esses bytecodes são executados em uma Máquina Virtual Java (JVM), que os converte em código de máquina adequado à plataforma subjacente.

Para compilar o programa, ele deve estar armazenado em um arquivo chamado `Hello.java`. Em Java, arquivos que contêm tipos públicos normalmente possuem o mesmo nome do tipo.

Podemos utilizar um ambiente integrado de desenvolvimento (**IDE**, *Integrated Development Environment*) ou executar o compilador diretamente pela linha de comando, desde que um JDK esteja instalado.

Normalmente, os programas Java são escritos em uma IDE, que oferece recursos para aumentar a produtividade durante o desenvolvimento, como navegação pelo código-fonte, refatoração, análise estática, compilação, testes e depuração.

Algumas das IDEs mais populares para Java são:

- [IntelliJ IDEA](https://www.jetbrains.com/pt-br/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

Também podemos compilar o programa diretamente pela linha de comando usando o compilador `javac`:

```text
javac Hello.java
```

O comando recebe `Hello.java` como entrada e produz o arquivo `Hello.class`, que contém a versão compilada do programa.

Depois da compilação, podemos executar o programa utilizando o comando `java`:

```text
java Hello
```

A saída será:

```text
Hello World!
```

O processo realizado pelas IDEs é essencialmente semelhante. Além da compilação e execução, elas fornecem recursos para depuração, testes, refatoração, criação e gerenciamento de projetos, criação de bibliotecas e gerenciamento de versões, entre diversas outras funcionalidades.

---

*Este artigo é uma adaptação de conteúdo do livro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>*
