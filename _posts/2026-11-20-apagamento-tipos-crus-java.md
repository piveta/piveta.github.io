---
layout: post
title: "Apagamento de tipos e tipos crus em Java"
date: 2026-11-20
lang: pt-BR
translation_id: apagamento-tipos-crus-java
permalink: /apagamento-tipos-crus-java/
share_text: >-
  Entenda por que Java apaga parâmetros genéricos na compilação, como isso favorece compatibilidade com código antigo e quais riscos os tipos crus introduzem.
---

Os genéricos foram introduzidos em Java 5 com uma preocupação de compatibilidade com código anterior. Para isso, o compilador aplica o **apagamento de tipos** (*type erasure*): ele verifica os tipos genéricos durante a compilação e remove os parâmetros de tipo da representação executada pela JVM. Os tipos são substituídos por seus limites, em geral `Object` ou o primeiro limite declarado.

Por exemplo, a classe genérica `Adaptador<T>` do livro fica, de maneira aproximada, como uma classe que trabalha com `Object` após o apagamento:

```java
public class Adaptador{
    Object objeto;
    public Object obter(){
        return objeto;
    }
    public void escrever(Object o){
        objeto = o;
    }
    public Adaptador(Object inicial){
        objeto = inicial;
    }
}
```

O cliente correspondente, escrito sem parâmetros de tipo, teria esta forma:

```java
void main(){
    Adaptador a = new Adaptador("Teste");
    IO.println(a.obter());
    a.escrever("Novo Valor");    
    IO.println(a.obter());
}
```

Esses trechos servem para **ilustrar** o apagamento; não são uma transcrição literal do bytecode. A informação de tipo que ajuda o compilador a rejeitar usos incompatíveis não está disponível da mesma forma durante a execução. Isso traz limitações, sobretudo para operações que dependem de reconhecer parâmetros genéricos em tempo de execução.

## Tipos crus

Para que código antigo continue válido, Java também permite usar um tipo genérico **sem informar seu parâmetro**. Compare primeiro uma lista parametrizada:

```java
void main(){
    List<String> nomes = new ArrayList<>();
}
```

Com um tipo cru (*raw type*), tanto a declaração quanto a construção omitem o parâmetro:

```java
void main(){
    List nomes = new ArrayList();    
}
```

Essa escolha perde a verificação dos elementos que uma `List<String>` forneceria. O código a seguir aceita tanto uma cadeia de caracteres quanto um inteiro na mesma lista:

```java
void main(){
    List nomes = new ArrayList();    
    nomes.add("Maria");
    nomes.add(35); // permitido
}
```

`List` e `List<?>` não significam a mesma coisa. `List<?>` é uma lista de um tipo **desconhecido**: não podemos adicionar um elemento arbitrário, exceto `null`. Já `List` é um tipo cru: aceita elementos sem a verificação oferecida pelo parâmetro de tipo.

Em código novo, informe o parâmetro adequado ou use um coringa quando o tipo for desconhecido. Tipos crus são úteis principalmente na interação com bibliotecas legadas.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
