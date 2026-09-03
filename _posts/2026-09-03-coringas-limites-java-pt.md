---
layout: post
title: "Parametros limitados ou restritos em tipos genéricos em Java"
date: 2026-09-03
lang: pt-BR
translation_id: wildcards-limites-java
permalink: /coringas-limites-tipos-genericos-java/
---

Além de tipos genéricos específicos, podemos usar **coringas** (*wildcards*) para expressar tipos desconhecidos (`<?>`), para restringir o tipo informado para incluir subtipos de determinado tipo (`<? extends Tipo>`) ou para incluir supertipos (usando `<? super Tipo>`). As seções a seguir descrevem os coringas sem restrição, com limite superior e com limite inferior, respectivamente. A seguir, mostramos como podemos definir múltiplos limites para tipos genéricos.

## Coringas sem restrição

Nos tipos desconhecidos, usamos o sinal de interrogação como tipo, permitindo que sejam usados quaisquer tipos nesse contexto. Por exemplo, caso eu tenha uma variável declarada como sendo do tipo `List<?>` (ou um atributo ou parâmetro), ela poderia receber objetos do tipo `List` com quaisquer parâmetros de tipos válidos, tais como `String`, `Integer`, etc. Tais tipos genéricos desconhecidos são chamados de **coringas sem restrição** (`<?>`), pois não impõem nenhum limite de tipo.

Por exemplo, poderíamos ter:

```java
List<?> l = new ArrayList<String>();
// ou, por exemplo
l = new LinkedList<Integer>();
```

Embora possa parecer atrativo ter a opção de declarar variáveis dessa forma, existem limitações. Em tais casos, não sabemos o tipo dos objetos da lista. Então, não é permitido, por exemplo, adicionar elementos na lista (exceto `null`, que é compatível com qualquer tipo de referência em Java), pois não há garantias que o objeto que está sendo adicionado é do mesmo tipo do parâmetro de tipo da lista.

Então, caso tentássemos adicionar um elemento ao objeto da lista (no caso, `l`), teríamos um erro em tempo de compilação:

```java
void main(){
    List<?> l = new ArrayList<String>();
    // Erro de compilação: 
    //    "The method add(capture#2-of ?) in the type 
    //     List<capture#2-of ?> is not applicable 
    //     for the arguments (String)"
    l.add("Maria");
}
```

Então, comumente, os tipos desconhecidos sem restrições são usados quando queremos apenas ler dados, sem modificá-los. Por exemplo, poderíamos ter um método que recebe uma lista e imprime seus elementos, sem especificar qual o tipo dos elementos da lista:

```java
public void imprimir(List<?> lista) {
    for (Object obj : lista)
        IO.println(obj);
}
void main(){
    imprimir(List.of(1, 2, 3));
    imprimir(List.of("A", "B", "C"));
}
```

A execução do método `main` mostraria:

```text
1
2
3
A
B
C
```

Aqui usamos a impressão como exemplo, mas poderíamos percorrer os objetos, usá-los em *streams*, filtrar com `instanceof`, obter o tamanho da lista, verificar se determinado objeto está contido, transformar e copiar para uma lista tipada, dentre outros. O que não podemos fazer é modificar a lista diretamente (usando `add` ou `set`, por exemplo - exceto com `null`).

## Coringas com limite superior

Os **coringas com limite superior** (*upper bounded wildcards*) permitem especificar que apenas um objeto de determinado tipo ou de um de seus subtipos (obtidos através de subclasse ou implementação de interface) possa ser usado como parâmetro de tipo. Usa-se a notação `<? extends T>` para especificar que o coringa precisa ser do tipo `T` ou de um tipo que estende o tipo `T`.

Por exemplo, caso eu declare uma lista na qual o coringa estende `Number`, eu poderia atribuir objetos de qualquer uma de suas subclasses (tais como `Double` ou `Integer`). Caso `Number` fosse uma classe concreta (ela é abstrata), também poderíamos atribuir um objeto dela própria. O exemplo a seguir mostra justamente isso:

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

Da mesma forma que ocorre com os coringas sem restrições, não podemos adicionar elementos na lista `l`, pois não sabemos exatamente qual o tipo da lista. Assim, as primeiras duas chamadas ao método `add` geram erros de compilação:

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Erro de compilação
    l.add(1.0); // Erro de compilação
    l.add(null);
}
```

Embora saibamos, lendo o código, que o objeto atribuído à variável `l` é uma lista de inteiros, o compilador sabe que `l` é de um tipo desconhecido, não permitindo a adição de valores. Na leitura, os valores são lidos como `Number`, que é o limite superior (*upper bound*).

## Coringas com limite inferior

Os **coringas com limite inferior** (*lower bounded wildcards*) permitem especificar que apenas um objeto de determinado tipo ou de um de seus supertipos possa ser usado como parâmetro de tipo. Usa-se a notação `<? super T>` para especificar que o coringa precisa ser do tipo `T` ou de uma superclasse de `T`.

Por exemplo, caso eu declare uma lista na qual o coringa tem um limite inferior `Number`, eu poderia atribuir objetos de qualquer uma de suas superclasses (no caso de `Number`, somente `Object`, pois `Number` não tem uma superclasse explícita).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

É permitido adicionar elementos do tipo do limite inferior (no caso `Number` ou de qualquer um de seus subtipos (como `Double` ou `Integer`, por exemplo)). A seguir, temos um exemplo de uma lista cujo coringa tem `Number` como limite inferior. Nesse caso, podemos instanciar um `ArrayList` de números (ou de sua superclasse `Object`). E podemos adicionar elementos de uma de suas subclasses (não podemos adicionar um objeto de `Number` porque é uma classe abstrata, que não pode ter instâncias diretas). O exemplo mostra três adições de elementos. As duas primeiras são permitidas, pois os elementos são de subtipos de `Number` (`10` é um `Integer` e `1.0` é um `Double`). A terceira adição de elemento não é permitida, gerando um erro em tempo de compilação, pois `Object` não é descendente de `Number`.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Permitido
l.add(1.0); // Permitido
l.add(new Object()); // Erro de compilação
```

Caso criássemos o `ArrayList` com `Object` como parâmetro de tipo, mesmo assim a terceira adição não seria permitida em tempo de compilação, gerando o mesmo erro (e as duas primeiras adições continuariam permitidas), pois o tipo da lista continua sendo desconhecido (sabe-se apenas que é `Number` ou uma de suas superclasses).

## Múltiplos limites

Em Java, um tipo genérico pode ter **múltiplos limites** (*multiple bounds*), ou seja, o parâmetro de tipo pode ser restringido para aceitar apenas tipos que estendam (ou sejam de) uma classe específica e que implementem uma ou mais interfaces. A sintaxe segue a forma `\<T extends Classe & Interface1 & Interface2>`. Caso exista uma classe como limite, ela deve ser especificada primeiro, seguida das interfaces. Caso não exista uma classe, podem ser listadas apenas interfaces.

Por exemplo, a classe `MultiplosLimites` possui um tipo genérico `T` que estende a classe `Number` e implementa as interfaces `Comparable<T>` e `Serializable`:

```java
import java.io.Serializable;

public class MultiplosLimites<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

Neste exemplo, `T` só pode ser `Number` ou um tipo que herde de `Number` e que também implemente `Comparable<T>` e `Serializable`. Isto é útil quando precisamos de garantias múltiplas, como acesso a métodos de uma superclasse e contratos definidos por várias interfaces. Essa combinação permite que o código seja mais flexível, mas ainda fortemente tipado, evitando erros em tempo de compilação e garantindo que todos os métodos necessários estarão disponíveis para o tipo genérico usado.

---

*Este artigo é uma adaptação de conteúdo do livro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>*

