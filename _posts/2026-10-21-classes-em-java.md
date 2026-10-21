---
layout: post
title: "Classes em Java"
date: 2026-10-21
lang: pt-BR
translation_id: classes-em-java
permalink: /classes-em-java/
share_text: >-
  O artigo mostra como declarar classes em Java e trabalhar com atributos, métodos, construtores, visibilidade, objetos e encapsulamento.
---

Java fornece suporte aos principais conceitos de orientação de objetos, incluindo: classes, atributos, métodos, herança, interfaces, polimorfismo e encapsulamento.

## Classes, atributos e métodos

Em Java, uma classe pode ser definida através de uma declaração contendo
a palavra reservada `class`, um nome e um corpo (no qual podem ser
definidos atributos e métodos). Além disso, existem outros componentes
opcionais, alguns dos quais serão discutidos em mais detalhes no
decorrer desta parte. Considere, por exemplo, uma classe `Conta`.
Poderíamos criar essa classe em Java, de maneira pública (palavra
reservada `public`), de forma que possa ser acessada por outras classes,
da seguinte forma:

``` java
public class Conta{
    // Corpo da classe
}
```

No corpo da classe, podemos adicionar atributos e métodos. No exemplo a
seguir, adicionamos um atributo `saldo` do tipo `Double`[^2] (linha
), e um método `sacar`
(linhas  a
), que não retorna
nada (`void`) e que tem um parâmetro formal chamado `valor` do tipo
`Double`. Este método retira do `saldo` o valor passado como parâmetro
(note que no corpo de `sacar` temos um acesso de leitura e de escrita ao
atributo `saldo`):

``` java
public class Conta{
    public Double saldo;
    public void sacar(Double valor){
        saldo = saldo - valor; // ou saldo -= valor;
    }
}
```

Analogamente, poderíamos ter também um método `depositar`, que
incrementa o saldo da `Conta`:

``` java
public class Conta{
    // saldo e sacar omitidos
    public void depositar(Double valor){
        saldo = saldo + valor; // ou saldo += valor;
    }
}
```

Considere, por exemplo, um cliente que exercita algumas operações
possíveis em uma conta. Primeiro, é criado um objeto da classe `Conta`
através da chamada ao construtor, sendo a referência ao objeto atribuída
à uma variável `c` (linha
). A seguir, o
saldo da conta é modificado para R\$ 100,00 através de uma referência ao
atributo `saldo` (linha ). Então, é feito um saque
de R\$ 50,00 (via chamada a `sacar`) (linha
) e um depósito de
R\$ 100,00 (via chamada a `depositar`) na linha
. Por fim, a linha
 mostra a
impressão do saldo.

``` java
void main(){
    var c = new Conta();
    c.saldo = 100.00;
    c.sacar(50.00);
    c.depositar(100.00);
    IO.println("Saldo: " + c.saldo);
}
```

A saída deste programa seria:

``` java
Saldo: 150.0
```

Note que os métodos `sacar` e `depositar` (chamadas nas linhas
 e
, respectivamente)
precisam de um objeto da classe `Conta` para serem invocados, pois são
métodos de instância, bem como o método `main`, que agora nas versões
mais recentes também pode ser ou um método estático ou um método de
instância (como neste caso)[^3].

O exemplo anterior ilustra o uso de atributos e métodos por parte de um
cliente da classe `Conta`, de uma classe implicitamente declarada, sem
nome. O exemplo, no entanto, em seu método `main`, acessa diretamente o
`saldo` da `Conta` e faz com que o acoplamento entre as classes seja
forte (o que não é recomendável)[^4]. Uma alternativa é encapsular o
acesso ao atributo `saldo`, fazendo com que as leituras e escritas sejam
feitas através de métodos específicos para tal. Isso desacopla as
classes ao permitir que a representação interna do saldo possa ser
modificada posteriormente (desde que as operações de leitura e escrita
sejam mantidas). Além disso, é recomendável diminuir a visibilidade do
atributo, de forma que ele só possa ser acessado de dentro da classe.

Em Java, por exemplo, existem as seguintes visibilidades: padrão
(visível dentro do pacote), privada (visível apenas dentro da classe),
pública (visível por todas as classes), e protegida (visível na classe e
em todas as suas subclasses). Para cada tipo de visibilidade, pode
existir uma palavra chave associada (exceto para o padrão, para o qual
nenhuma palavra chave é informada).

O código a seguir mostra as modificações feitas de forma a melhorar o
encapsulamento do saldo e ocultar informações internas da classe de seus
clientes. Isso é feito através da criação de dois métodos públicos de
leitura e de escrita (`getSaldo` e `setSaldo`, iniciando nas linhas
 e
, respectivamente),
da alteração do modificador de visibilidade de `saldo` para `private`
(linha ) e da escrita do saldo
(dentro dos métodos `sacar` e `depositar`). Note que o método `setSaldo`
usa uma referência a `this` para desambiguar o saldo (existe o atributo
`saldo` e o parâmetro formal do método chamado `saldo`). O `this`
representa o objeto atual. Então quando fazemos `this.saldo` estamos nos
referindo ao atributo `saldo` (e não ao parâmetro):

``` java
public class Conta{
    private Double saldo;
    public Double getSaldo(){
        return saldo;
    }
    public void setSaldo(Double saldo){
        this.saldo = saldo;
    }
    public void sacar(Double valor){
        setSaldo(getSaldo() - valor);
    }
    public void depositar(Double valor){
        setSaldo(getSaldo() + valor);
    }
}
```

O cliente da classe também é alterado, passando a modificar o saldo
através do método de escrita (`setSaldo`):

``` java
void main(){
    var c = new Conta();
    c.setSaldo(100.00);
    c.sacar(50.00);
    c.depositar(100.00);
    IO.println("Saldo: " + c.getSaldo());
}
```

Em Java, as classes possuem um construtor padrão, sem parâmetros, que é
herdado da classe `Object`. Podem ser definidos novos construtores para
facilitar o uso da classe por parte dos clientes. Considere, por
exemplo, a classe `Conta` com um construtor que recebe um `valor` como
parâmetro (linha ) e preenche o
saldo com este valor (através de uma chamada a `setSaldo` - linha
). Caso fosse
necessário chamar o construtor da superclasse, o método `super` poderia
ser usado:

``` java
public class Conta{
    // Atributos e métodos de Conta
    public Conta(Double valor){
        setSaldo(valor);
    }
}
```

O cliente precisaria ser modificado de forma a usar o novo construtor
definido (linha ), passando o
saldo inicial como parâmetro, pois a classe `Conta` agora não tem mais o
construtor padrão[^5].

``` java
void main(){
    var c = new Conta(100.00);
    c.sacar(50.00);
    c.depositar(100.00);
    IO.println("Saldo: " + c.getSaldo());
}
```

Em Java não há métodos destrutores, pois os objetos que não estão mais
sendo referenciados são coletados automaticamente pelo coletor de lixo.

[^2]: Estamos usando um `Double` para fins de simplificação. Usualmente
    valores monetários não são armazenados em variáveis do tipo ponto
    flutuante, mas sim em inteiros longos (como `long` ou `BigDecimal`).

[^3]: Vide JEP 512: <https://openjdk.org/jeps/512>

[^4]: Nesta frase, o trecho “as classes” refere-se à classe `Conta` e a
    classe implícita, não nomeada, que contém o método `main`.

[^5]: Ao definirmos um novo construtor, a classe deixa de ter o
    construtor padrão. Caso desejado, pode ser criado também um
    construtor padrão, sem parâmetros.

---

*Este artigo é uma adaptação de conteúdo do livro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Leia também

- [Conceitos Básicos](/conceitos-basicos-poo-java/)
- [Herança em Java](/heranca-em-java/)
- [Polimorfismo em Java](/polimorfismo-em-java/)
- [Interfaces em Java](/interfaces-em-java/)
- [Links POO - Java](/links-poo-java/)
- [Exercícios de Orientação a Objetos](/exercicios-poo-java/)
