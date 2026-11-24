---
layout: post
title: "Herança e subtipos com tipos genéricos em Java"
date: 2026-11-24
lang: pt-BR
translation_id: heranca-subtipos-genericos-java
permalink: /heranca-subtipos-genericos-java/
share_text: >-
  List<Carro> não é List<Veiculo>. Entenda invariância, leitura com extends e escrita com super em tipos genéricos Java.
---

Em Java, tipos genéricos são **invariantes** por padrão: mesmo que `Carro` herde de `Veiculo`, `List<Carro>` não é um subtipo de `List<Veiculo>`. Coringas com `extends` e `super` permitem expressar relações úteis entre esses tipos em pontos de uso.

## Invariância

Considere as classes do exemplo do livro. `Carro` e `Moto` estendem `Veiculo`:

```java
public class Veiculo {
    public void mover() {
        IO.println("Veículo em movimento");
    }
}

public class Carro extends Veiculo {
    public void buzinar() {
        IO.println("Buzina acionada");
    }
}

public class Moto extends Veiculo {
    public void empinar() {
        IO.println("Moto empinando");
    }
}
```

Uma lista de carros não pode ser atribuída a uma variável declarada como lista de veículos. A atribuição a seguir produz um **erro de compilação**:

```java
void main() {
    List<Carro> carros = new ArrayList<>();
    carros.add(new Carro());
    // ERRO: List<Carro> não é um subtipo de List<Veiculo>
    List<Veiculo> veiculos = carros; // Erro de compilação!
}
```

A proibição preserva a segurança de tipos. Se a atribuição compilasse, seria possível adicionar uma `Moto` por meio da variável `veiculos`, embora o objeto continuasse sendo uma lista de carros. O trecho abaixo é **hipotético** e não deve ser executado como exemplo válido:

```java
    // Se compilasse, isso seria possível...
    veiculos.add(new Moto()); 
    // Mas geraria erros em tempo de execução 
    Carro c = carros.get(0);  
    // Gera uma ClassCastException
```

## Covariância no uso: `extends`

Quando um método precisa **ler** elementos de uma lista de veículos ou de qualquer subtipo, pode receber `List<? extends Veiculo>`. Cada elemento lido é, no mínimo, um `Veiculo`:

```java
public static void imprimir(List<? extends Veiculo> lista) {
   for (Veiculo v : lista)
      v.mover(); // ok
   // lista.add(new Carro()); // Não permitido!
}
```

Esse método aceita `List<Veiculo>`, `List<Carro>` e `List<Moto>`. Ele não pode adicionar um `Carro`, pois a lista recebida poderia ser, por exemplo, uma lista de motos. O tipo concreto atrás do coringa é desconhecido.

## Contravariância no uso: `super`

Quando o objetivo é **adicionar** carros, o método pode receber uma lista de `Carro` ou de uma de suas superclasses:

```java
public void adicionar(List<? super Carro> lista) {
    lista.add(new Carro()); // permitido
}
```

Assim, `List<Carro>`, `List<Veiculo>` e `List<Object>` são argumentos possíveis. Ao ler um elemento dessa lista, o único tipo garantido estaticamente é `Object`.

A covariância e a contravariância aqui pertencem ao **uso com coringa**: `List<? extends Veiculo>` e `List<? super Carro>`. A declaração de `List<T>` permanece invariante.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
