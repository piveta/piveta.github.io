---
layout: post
title: "Herança em Java"
date: 2026-10-21
lang: pt-BR
translation_id: heranca-em-java
permalink: /heranca-em-java/
share_text: >-
  O artigo explica a herança em Java, o uso de superclasses e subclasses, sobrescrita de métodos e conversões entre tipos.
---

A **herança** é um mecanismo de composição que permite que as classes reutilizem a interface e o comportamento de classes existentes, estendendo suas funcionalidades. Normalmente, a classe que estende outra é chamada de **subclasse**, e a classe estendida é chamada de **superclasse**.

Em Java, a herança entre classes é simples: uma classe pode estender apenas uma superclasse, enquanto interfaces podem estender múltiplas interfaces. As subclasses são subtipos de suas superclasses. A herança é declarada na subclasse com a palavra reservada `extends`: `Classe extends SuperClasse`. Classes que não declaram uma superclasse são implicitamente subclasses de `Object`, a classe raiz da hierarquia de classes de Java.

Considere, por exemplo, a classe `ContaCorrente` a seguir. Tal classe
estende a classe `Conta`, podendo fornecer
novos atributos, métodos e construtores à superclasse. No exemplo, ela
define um atributo chamado `limiteDiarioSaque`, bem como seus métodos
de leitura e escrita (`getLimiteDiarioSaque` e `set­Li­mi­te­Di­a­rio­Sa­que`). Adicionalmente, é implementado o construtor para a
classe, dado que a
classe `Conta` não possui um construtor padrão (sem parâmetros). Neste
caso, o construtor de `ContaCorrente` apenas chama o construtor da
superclasse `Conta` através de uma chamada a `super`.

``` java
public class ContaCorrente extends Conta{
    private Double limiteDiarioSaque;
    public Double getLimiteDiarioSaque(){
        return limiteDiarioSaque;
    }
    public void setLimiteDiarioSaque(Double
        limiteDiarioSaque){
        this.limiteDiarioSaque = limiteDiarioSaque;
    }
    public ContaCorrente(Double valor) {
        super(valor);
    }
}
```

Nas subclasses, é comum termos **métodos sobrescritos**, que são métodos
definidos em uma superclasse e que são estendidos ou substituídos por
métodos das subclasses. No exemplo a seguir, a classe `ContaCorrente`
sobrescreve o método `sacar` de `Conta`, através da definição de um
método com a mesma assinatura[^6] do método de `Conta`. Tal sobrescrita faz
com que o método original da superclasse seja executado (através de uma
chamada a `super`  e que, posteriormente,
seja calculado o valor da tarifa de saque (caso aplicável) através do
método `descontarTarifa`,
que abate 1% do valor da transação do saldo a título de tarifa:

``` java
public class ContaCorrente extends Conta{
    public void sacar(Double valor){
        super.sacar(valor);
        descontarTarifa(valor);
    }
    private void descontarTarifa(Double valor) {
        setSaldo(getSaldo() - valor * 0.01);
    }
    // Outros construtores, atributos e métodos.
}
```

Então, por exemplo, se tivéssemos um objeto da classe `ContaCorrente`
com saldo inicial de R\$ 100,00 e sacássemos R\$ 50,00, teríamos apenas
R\$ 49,50 de saldo remanescente, pois R\$ 0,50 seriam descontados pela
tarifa:

``` java
void main(){
    var c = new ContaCorrente(100.00);
    c.sacar(50.00);
    IO.println("Saldo: " + c.getSaldo());
}
```

Pelo princípio de substituição de Liskov, podemos atribuir objetos de
uma subclasse sempre que for esperado um objeto da superclasse (todo
objeto de uma classe também é um objeto de sua superclasse - toda
instância de `ContaCorrente` é também uma instância de `Conta`). O
contrário nem sempre é verdadeiro (nem toda `Conta` é uma
`ContaCorrente` - poderia ser uma `ContaPoupança`, por exemplo). Nesses
casos, é necessário fazer uma conversão explícita (*cast*).

No exemplo a seguir, temos uma variável `cc`, do tipo `ContaCorrente`,
que recebe uma instância de um objeto da classe `ContaCorrente`. A seguir, é
declarada uma variável `c`, do tipo `Conta`, que recebe o objeto
apontado por `cc`. Como toda
`ContaCorrente` é uma `Conta`, essa atribuição é permitida, sem
conversões. No sentido inverso, o
inverso: o conteúdo da variável `c` é atribuído para `cc`. Nesse caso, é
necessária uma conversão explícita de `Conta` para `ContaCorrente`.

``` java
ContaCorrente cc = new ContaCorrente(100.00);
Conta c = cc;  // cc é uma ContaCorrente, que é uma Conta.
cc = (ContaCorrente) c;  // Conversão explícita, ok.
```

Considere, por exemplo, que a classe `ContaPoupança` seja uma subclasse
de `Conta`. No exemplo a seguir, temos uma variável `c` do tipo `Conta`
que armazena um objeto do tipo `ContaCorrente`. Se tentássemos
atribuir a variável `c` a uma variável `cp` do tipo `ContaPoupança`,
precisaríamos fazer uma conversão explícita. Nesse caso, a
conversão falharia, pois o objeto referenciado por `c` não é uma
`ContaPoupança`, e sim uma `ContaCorrente` que não é uma subclasse de
`ContaPoupança`. Desta forma, seria lançada uma exceção em tempo de
execução.

``` java
Conta c = new ContaCorrente(100.00);
// Conversão explícita a seguir. Erro de conversão.
ContaPoupança cp = (ContaPoupança) c;
```

As IDEs atuais emitem avisos quando tentamos fazer algo que seja
claramente um equívoco, como neste caso. Mas em alguns outros casos, não
há esta certeza. Quando temos parâmetros de métodos, por exemplo, não
sabemos que objetos serão passados para esses métodos de antemão. Muitas
vezes podemos ter problemas de conversão (são lançadas exceções do tipo
`Class­Cast­Ex­cep­tion`[^7] quando isso ocorre).

Dado que a classe `Conta` possui diferentes subtipos, tais como
`Con­ta­Cor­ren­te` e `Con­ta­Pou­pan­ça`, além de outros em potencial
(`Con­ta­In­ves­ti­men­to`, por exemplo), podemos fazer com que apenas
instâncias das subclasses possam ser criadas tornando a classe `Conta`
abstrata:

``` java
public abstract class Conta{
    // Atributos e métodos comuns a todos os tipos de conta.
}
```

Neste caso, não podemos mais instanciar a classe `Conta` diretamente.
Precisamos fornecer um construtor de uma de suas subclasses. Aqui temos
o exemplo inicial modificado, para usar a classe `Con­ta­Cor­ren­te`:

``` java
void main(){
    var c = new ContaCorrente(100.00);
    c.sacar(50.00);
    c.depositar(100.00);
    IO.println("Saldo: " + c.getSaldo());
}
```

[^6]: Em Java, a assinatura de um método é composta pelo nome do método,
    pelos seus parâmetros de tipo (caso existam) e pelos parâmetros
    formais do método. Vide
    <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2>

[^7]: <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html>

---

*Este artigo é uma adaptação de conteúdo do livro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Leia também

- [Conceitos Básicos de Orientação a Objetos](/conceitos-basicos-poo-java/)
- [Classes em Java](/classes-em-java/)
- [Polimorfismo em Java](/polimorfismo-em-java/)
- [Interfaces em Java](/interfaces-em-java/)
- [Links POO - Java](/links-poo-java/)
- [Exercícios de Orientação a Objetos](/exercicios-poo-java/)
