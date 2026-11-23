---
layout: post
title: "Exercícios de tipos genéricos em Java"
date: 2026-11-20
lang: pt-BR
translation_id: exercicios-tipos-genericos-java
permalink: /exercicios-tipos-genericos-java/
share_text: >-
  Dez exercícios sobre classes e métodos genéricos, coringas, herança, apagamento de tipos, Optional<T> e Caixa<T>.
---

Os exercícios abaixo são baseados no capítulo de tipos genéricos do livro **Orientação a Objetos com Java**. Os trechos de código fornecidos nos enunciados preservam os exemplos do livro.

1. Estude as principais interfaces do framework de coleções de Java e identifique como elas usam tipos genéricos para permitir o uso das estruturas de dados em contextos diferentes, sem modificar suas classes e interfaces.

2. Crie um método estático `maior` que receba dois objetos comparáveis, isto é, que implementem `Comparable`, e retorne o maior. Use tipos genéricos para definir seus parâmetros.

3. Crie um método estático que receba uma lista parametrizada com qualquer tipo e a imprima. Use coringas.

4. Crie um método estático que receba uma lista parametrizada com um tipo numérico e some seus elementos. Use um coringa com `extends` para aceitar apenas listas de números (`Number`).

5. Considere esta hierarquia de classes:

   ```java
   class Instrumento { }
   class Cordas extends Instrumento { }
   class Percussao extends Instrumento { }
   class Sopro extends Instrumento { }
   class Violao extends Cordas { }
   class Bateria extends Percussao { }
   class Flauta extends Sopro { }
   ```

   O método a seguir recebe uma lista de `Instrumento` ou de objetos de suas subclasses e mostra os elementos:

   ```java
   static void tocar(List<? extends Instrumento> instrumentos) {
       for (Instrumento i : instrumentos) 
           IO.println("Tocando " + 
                       i.getClass().getSimpleName());
   }
   ```

   Passe uma lista de `Violao` e outra de `Flauta`. Depois, tente adicionar um novo instrumento na lista dentro do método e observe o resultado da compilação.

6. Implemente um método genérico que receba uma lista de elementos que sejam `Number` e `Comparable` e retorne o maior elemento.

7. Crie os três métodos abaixo, implemente seus corpos e teste com listas de `Carro`, `Moto` e `Veiculo`:

   ```java
   void imprimirInvariante(List<Veiculo> lista){
       // Implemente
   }
   void imprimirCovariante(List<? extends Veiculo> lista){
       // Implemente
   }
   void imprimirContravariante(List<? super Veiculo> lista){
       // Implemente
   }
   ```

8. Tente implementar `boolean verificaLista(Object obj)` para retornar `true` apenas quando `obj` for uma `List<String>`. Investigue se isso é possível diretamente em Java e proponha uma alternativa com `List<?>` ou `List<Object>`.

9. Estude a documentação de `Optional<T>`. Crie `public static <T> void imprimirOpcional(Optional<T> opt)` para imprimir o valor quando estiver presente ou *vazio* caso contrário. Teste com `Optional<String>` e `Optional<Integer>`.

10. Crie uma classe genérica `Caixa<T>` que armazene um item de tipo `T`:

    - `public void guardar(T item)` armazena o item e não deve permitir `null`.
    - `public T pegar()` retorna o item armazenado.
    - `public static <T extends Comparable<T>> boolean comparar(Caixa<T> c1, Caixa<T> c2)` retorna `true` quando o item da primeira caixa for maior, usando `compareTo`.

    Crie também `compararComHeranca`, para comparar caixas de tipos diferentes que compartilhem uma relação de herança. Use `<? extends T>` ou `<? super T>`. Teste com os exemplos do livro:

    ```java
     Caixa<Integer> caixa1 = new Caixa<>();
     Caixa<Integer> caixa2 = new Caixa<>();
     caixa1.guardar(10);
     caixa2.guardar(5);
     boolean resultado = Caixa.comparar(caixa1, caixa2); // true
     
     Caixa<Double> caixa3 = new Caixa<>();
     Caixa<Integer> caixa4 = new Caixa<>();
     caixa3.guardar(7.5);
     caixa4.guardar(5);
     boolean resultado2 = Caixa.compararComHeranca(caixa3, 
        caixa4); // true
    ```

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
