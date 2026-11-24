---
layout: post
title: "Classes e métodos genéricos em Java"
date: 2026-11-20
lang: pt-BR
translation_id: classes-metodos-genericos-java
permalink: /classes-metodos-genericos-java/
share_text: >-
  Tipos genéricos permitem reutilizar classes e métodos com segurança de tipos. Veja o Adaptador<T> e métodos que recebem e retornam tipos parametrizados.
---

O **polimorfismo paramétrico** permite que uma classe, interface, registro ou método adapte seu comportamento a um tipo informado no uso. Em Java, os tipos genéricos ajudam a reutilizar código e a evitar conversões desnecessárias. O framework de coleções usa esse mecanismo extensamente: `List<String>` e `List<Integer>` compartilham a mesma interface, mas o compilador verifica os tipos dos elementos em cada caso.

Considere uma classe `Adaptador` que armazena um objeto. Sem um parâmetro de tipo, o atributo, o construtor e os métodos trabalham com `Object`:

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

Essa classe pode receber objetos de qualquer tipo, mas não restringe qual deles um adaptador específico deve armazenar. Ao declarar `T` junto ao nome da classe, a mesma implementação passa a trabalhar com o tipo escolhido pelo cliente:

```java
public class Adaptador<T>{
    T objeto;
    public T obter(){
        return objeto;
    }
    public void escrever(T o){
        objeto = o;
    }
    public Adaptador(T inicial){
        objeto = inicial;
    }
}
```

Por exemplo, este cliente cria um `Adaptador<String>`. O construtor recebe uma `String`, `escrever` recebe uma `String` e `obter` retorna uma `String`:

```java
void main(){
    var a = new Adaptador<String>("Teste");
    IO.println(a.obter());
    a.escrever("Novo Valor");
    IO.println(a.obter());
}
```

A execução imprime `Teste` e, depois, `Novo Valor`.

## Métodos genéricos

Também podemos declarar o parâmetro de tipo em um **método**, antes do tipo de retorno. Assim, `imprimir` aceita listas de tipos diferentes sem abandonar a verificação de tipos:

```java
public static <T> void imprimir(List<T> lista){ 
    for (T elemento : lista)
        IO.println(elemento);
}
void main(){
    List<Integer> inteiros = List.of(1, 2, 3, 4);
    List<String> nomes = List.of("Maria", "João", "Carol");
    imprimir(inteiros);
    imprimir(nomes);
}
```

O mesmo parâmetro pode determinar o tipo do retorno. No exemplo seguinte, `primeiro` recebe uma `List<T>` e retorna um `T`. Assim, o resultado de uma lista de inteiros é `Integer` e o de uma lista de nomes é `String`:

```java
public static <T> T primeiro(List<T> lista) {  
    return lista.isEmpty() ? null : lista.get(0);
}
void main(){
    List<Integer> inteiros = List.of(1, 2, 3, 4); 
    List<String> nomes = List.of("Maria", "João", "Carol");
    Integer inteiro = primeiro(inteiros); 
    String nome = primeiro(nomes);  
    IO.println(inteiro);
    IO.println(nome);
}
```

O programa imprime `1` e `Maria`. As variáveis intermediárias tornam explícitos os tipos; quando isso não for necessário, as expressões podem ser usadas diretamente:

```java
// Implementação do método "primeiro" omitida aqui
void main(){
    IO.println(primeiro(List.of(1, 2, 3, 4)));
    IO.println(primeiro(List.of("Maria", "João", "Carol")));
}
```

## Restringindo um parâmetro de método

O método `multiplicar` aceita listas cujos elementos sejam `Number` ou seus subtipos. O limite `<T extends Number>` permite chamar `doubleValue()` em cada elemento:

```java
public static <T extends Number> Double multiplicar(List<T> lista){
    Double produto = 1.0;
    for (T numero : lista)
        produto *= numero.doubleValue();
    return produto;
}
```

É possível chamá-lo tanto com uma lista de `Integer` quanto com uma lista de `Double`:

```java
void main(){
    IO.println(multiplicar(List.of(1, 2, 3, 4)));
    IO.println(multiplicar(List.of(1.1, 2.2, 3.5)));
}
```

O parâmetro de tipo é verificado na compilação. O método continua sendo único, enquanto o tipo concreto é escolhido em cada chamada.

---

*Este artigo adapta conteúdo do livro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
