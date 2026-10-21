---
layout: post
title: "Polimorfismo em Java"
date: 2026-10-21
lang: pt-BR
translation_id: polimorfismo-em-java
permalink: /polimorfismo-em-java/
share_text: >-
  O artigo apresenta polimorfismo de sobrecarga, paramétrico e de subtipo, com exemplos em Java.
---

Em relação ao polimorfismo, vamos ver alguns exemplos. Em Java, o
**polimorfismo *ad-hoc*** (ou de sobrecarga) é expresso através da
definição de métodos de um mesmo nome com assinaturas diferentes. No
exemplo a seguir, a classe `Figura` (linha
) possui dois métodos
sobrecarregados (iniciando nas linhas
 e
). Ambos
tem o mesmo nome (`redimensionar`), mas possuem parâmetros formais
diferentes. O primeiro deles requer um `percentual` do tipo `Double`,
enquanto o segundo requer duas coordenadas `x` e `y` do tipo `Integer`.

``` java
public class Figura {
    public void redimensionar(Double percentual){
        // Redimensionar por percentual
    }
    public void redimensionar(Integer x, Integer y){
        // Redimensionar por coordenadas
    }
}
```

Em relação ao **polimorfismo paramétrico**, podemos criar tipos
parametrizados, através dos sinais $`<`$ e $`>`$. Por exemplo, a classe
`ArrayList` possui um parâmetro de tipos `E` que define o tipo dos
objetos que podem ser armazenados pela lista (linha
). Este mesmo
parâmetro de tipos é usado como parâmetro formal do método `add` (linha
). Desta forma, o
tipo esperado por `add` é o mesmo usado na instanciação da classe
`ArrayList`. Note também, que ela estende uma classe chamada
`AbstractList` e implementa a interface `List`, ambas usando o mesmo
tipo `E`, além de outras interfaces.

``` java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable{
    public boolean add(E e){
        // Implementação de add
    }
    // Outros métodos e atributos da classe
}
```

Por exemplo, podemos criar uma lista de cadeias de caracteres com o
parâmetro de tipo `String` (linha
) e inserir
elementos através de chamadas ao método `add`[^8].

``` java
var c = new ArrayList<String>();
c.add("Maria");
c.add("João");
```

Neste caso, o compilador espera que o parâmetro recebido por `add` seja
uma `String`. Caso seja passado um objeto de outro tipo, ocorre um erro
em tempo de compilação. Caso quiséssemos uma lista de inteiros,
poderíamos usar esse tipo de polimorfismo passando outro tipo para
`ArrayList` (no caso o tipo `Integer` - linha
):

``` java
var c = new ArrayList<Integer>();
c.add(10);
c.add(20);
```

Em relação ao **polimorfismo de subtipo**, suponha que a classe `Figura`
possua um método `desenhar` e que esse método também possa ser chamado
por objetos das classes `Triângulo`, `Círculo` e `Retângulo`. Suponha
também que esse método seja sobrescrito nas três classes para
implementar as especificidades do desenho de cada uma delas. Caso
tivéssemos o seguinte código, cada chamada ao método desenhar do objeto
`figura` seria feita para uma classe diferente (de acordo com a classe
de cada objeto criado). Neste caso, na linha
 o método
`desenhar` chamado é o de `Círculo`, na linha
 o de `Triângulo` e
na linha  o de `Retângulo`:

``` java
Figura figura = new Círculo(10);
// Aqui, o desenhar de Círculo é chamado
figura.desenhar();
figura = new Triângulo(20);
// Aqui é o desenhar de Triângulo
figura.desenhar();
figura = new Retângulo(10, 20);
// Aqui é o desenhar de Retângulo
figura.desenhar();
```

[^8]: Note que para usar a classe `ArrayList` usualmente precisamos
    importá-la: `import java.util.ArrayList;`. Atualmente, para arquivos
    compactos não é necessário importá-la. No caso de arquivos
    regulares, pode-se importar o módulo `java.base` com
    `import module java.base;`.

---

*Este artigo é uma adaptação de conteúdo do livro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Leia também

- [Conceitos Básicos](/conceitos-basicos-poo-java/)
- [Classes em Java](/classes-em-java/)
- [Herança em Java](/heranca-em-java/)
- [Interfaces em Java](/interfaces-em-java/)
- [Links POO - Java](/links-poo-java/)
- [Exercícios](/exercicios-poo-java/)
