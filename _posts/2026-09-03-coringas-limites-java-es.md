---
layout: post
title: "Comodines y límites en tipos genéricos de Java"
date: 2026-09-03
lang: es
translation_id: wildcards-limites-java
permalink: /comodines-limites-tipos-genericos-java/
---

Además de tipos genéricos específicos, podemos utilizar **comodines** (*wildcards*) para expresar tipos desconocidos (`<?>`), para restringir el tipo especificado de modo que incluya subtipos de un tipo determinado (`<? extends Tipo>`), o para incluir supertipos (utilizando `<? super Tipo>`). Las siguientes secciones describen los comodines sin restricción, con límite superior y con límite inferior, respectivamente. A continuación, mostramos cómo podemos definir múltiples límites para tipos genéricos.

## Comodines sin restricción

En los tipos desconocidos, usamos el signo de interrogación como tipo, lo que permite utilizar cualquier tipo en ese contexto. Por ejemplo, si tengo una variable declarada como `List<?>` (o un atributo o parámetro), podría recibir objetos de tipo `List` con cualquier parámetro de tipo válido, como `String`, `Integer`, etc. Estos tipos genéricos desconocidos se denominan **comodines sin restricción** (`<?>`), porque no imponen ningún límite de tipo.

Por ejemplo, podríamos tener:

```java
List<?> l = new ArrayList<String>();
// o, por ejemplo
l = new LinkedList<Integer>();
```

Aunque puede parecer atractivo tener la opción de declarar variables de esta forma, existen limitaciones. En estos casos, no sabemos el tipo de los objetos de la lista. Por lo tanto, no está permitido, por ejemplo, agregar elementos a la lista (excepto `null`, que es compatible con cualquier tipo de referencia en Java), ya que no hay garantías de que el objeto que se está agregando sea del mismo tipo que el parámetro de tipo de la lista.

Entonces, si intentáramos agregar un elemento al objeto lista (en este caso, `l`), tendríamos un error en tiempo de compilación:

```java
void main(){
    List<?> l = new ArrayList<String>();
    // Error de compilación: 
    //    "The method add(capture#2-of ?) in the type 
    //     List<capture#2-of ?> is not applicable 
    //     for the arguments (String)"
    l.add("Maria");
}
```

Por ello, los tipos desconocidos sin restricciones se utilizan habitualmente cuando solo queremos leer datos, sin modificarlos. Por ejemplo, podríamos tener un método que recibe una lista e imprime sus elementos, sin especificar cuál es el tipo de los elementos de la lista:

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

La ejecución del método `main` mostraría:

```text
1
2
3
A
B
C
```

Aquí usamos la impresión como ejemplo, pero podríamos recorrer los objetos, usarlos en *streams*, filtrarlos con `instanceof`, obtener el tamaño de la lista, comprobar si determinado objeto está contenido, transformarlos y copiarlos a una lista tipada, entre otras operaciones. Lo que no podemos hacer es modificar la lista directamente (usando `add` o `set`, por ejemplo, excepto con `null`).

## Comodines con límite superior

Los **comodines con límite superior** (*upper bounded wildcards*) permiten especificar que solo un objeto de determinado tipo o de uno de sus subtipos (obtenidos mediante una subclase o la implementación de una interfaz) pueda utilizarse como parámetro de tipo. Se utiliza la notación `<? extends T>` para especificar que el comodín debe ser del tipo `T` o de un tipo que extienda `T`.

Por ejemplo, si declaro una lista cuyo comodín extiende `Number`, podría asignarle objetos de cualquiera de sus subclases (como `Double` o `Integer`). Si `Number` fuera una clase concreta (es abstracta), también podríamos asignarle un objeto de la propia clase. El siguiente ejemplo muestra precisamente esto:

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

Al igual que ocurre con los comodines sin restricciones, no podemos agregar elementos a la lista `l`, porque no sabemos exactamente cuál es el tipo de la lista. Por lo tanto, las dos primeras llamadas al método `add` generan errores de compilación:

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Error de compilación
    l.add(1.0); // Error de compilación
    l.add(null);
}
```

Aunque sepamos, al leer el código, que el objeto asignado a la variable `l` es una lista de enteros, el compilador sabe que `l` es de un tipo desconocido y no permite agregar valores. Al leer, los valores se leen como `Number`, que es el límite superior (*upper bound*).

## Comodines con límite inferior

Los **comodines con límite inferior** (*lower bounded wildcards*) permiten especificar que solo un objeto de determinado tipo o de uno de sus supertipos pueda utilizarse como parámetro de tipo. Se utiliza la notación `<? super T>` para especificar que el comodín debe ser del tipo `T` o de una superclase de `T`.

Por ejemplo, si declaro una lista cuyo comodín tiene como límite inferior `Number`, podría asignarle objetos de cualquiera de sus superclases (en el caso de `Number`, solamente `Object`, ya que `Number` no tiene una superclase explícita).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

Está permitido agregar elementos del tipo del límite inferior (en este caso, `Number`) o de cualquiera de sus subtipos (como `Double` o `Integer`, por ejemplo). A continuación, tenemos un ejemplo de una lista cuyo comodín tiene `Number` como límite inferior. En este caso, podemos instanciar un `ArrayList` de números (o de su superclase `Object`). Y podemos agregar elementos de una de sus subclases (no podemos agregar un objeto de `Number` porque es una clase abstracta, que no puede tener instancias directas). El ejemplo muestra tres adiciones de elementos. Las dos primeras están permitidas, porque los elementos son subtipos de `Number` (`10` es un `Integer` y `1.0` es un `Double`). La tercera adición no está permitida, generando un error en tiempo de compilación, porque `Object` no es descendiente de `Number`.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Permitido
l.add(1.0); // Permitido
l.add(new Object()); // Error de compilación
```

Si creáramos el `ArrayList` con `Object` como parámetro de tipo, aun así la tercera adición no estaría permitida en tiempo de compilación, generando el mismo error (y las dos primeras seguirían permitidas), porque el tipo de la lista continúa siendo desconocido (solo se sabe que es `Number` o una de sus superclases).

## Múltiples límites

En Java, un tipo genérico puede tener **múltiples límites** (*multiple bounds*), es decir, el parámetro de tipo puede restringirse para aceptar únicamente tipos que extiendan (o sean de) una clase específica y que implementen una o más interfaces. La sintaxis sigue la forma `\<T extends Clase & Interface1 & Interface2>`. Si existe una clase como límite, debe especificarse primero, seguida de las interfaces. Si no existe una clase, solo pueden enumerarse interfaces.

Por ejemplo, la clase `MultiplosLimites` posee un tipo genérico `T` que extiende la clase `Number` e implementa las interfaces `Comparable<T>` y `Serializable`:

```java
import java.io.Serializable;

public class MultiplosLimites<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

En este ejemplo, `T` solo puede ser `Number` o un tipo que herede de `Number` y que también implemente `Comparable<T>` y `Serializable`. Esto es útil cuando necesitamos múltiples garantías, como acceso a métodos de una superclase y contratos definidos por varias interfaces. Esta combinación permite que el código sea más flexible, pero siga estando fuertemente tipado, evitando errores en tiempo de compilación y garantizando que todos los métodos necesarios estarán disponibles para el tipo genérico utilizado.

---

*Este artículo es una adaptación de contenido del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
