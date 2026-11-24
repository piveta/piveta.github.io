---
layout: post
title: "Borrado de tipos y tipos sin parametrizar en Java"
date: 2026-11-20
lang: es
translation_id: apagamento-tipos-crus-java
permalink: /es/type-erasure-and-raw-types-in-java/
share_text: >-
  El borrado de tipos favorece la compatibilidad; los tipos sin parametrizar pierden comprobaciones del compilador.
---

Java 5 introdujo los genéricos conservando la compatibilidad con código anterior. Mediante el **borrado de tipos** (*type erasure*), el compilador comprueba los parámetros genéricos y los elimina de la representación ejecutada por la JVM. Los sustituye por sus límites, normalmente `Object` o el primer límite declarado.

Tras el borrado, `Adapter<T>` se parece aproximadamente a una clase que utiliza `Object`:

```java
public class Adapter{
    Object object;
    public Object get(){
        return object;
    }
    public void set(Object value){
        object = value;
    }
    public Adapter(Object initial){
        object = initial;
    }
}
```

Un cliente sin parámetros de tipo tendría esta forma:

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

Estos fragmentos **ilustran** el proceso; no transcriben literalmente el bytecode. Parte de la información disponible durante la compilación deja de estar accesible de la misma manera en ejecución, lo que limita ciertas operaciones de reflexión.

## Tipos sin parametrizar

Una lista parametrizada conserva la comprobación de sus elementos:

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

Un *raw type* omite el argumento de tipo tanto en la declaración como en la construcción:

```java
void main(){
    List names = new ArrayList();
}
```

Así se pierde la comprobación que ofrece `List<String>`. Esta lista admite una cadena y un entero:

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>` significa una lista de un tipo **desconocido** y no permite añadir elementos arbitrarios, salvo `null`. Una `List` sin parametrizar sí los acepta sin comprobar su tipo. En código nuevo, use un argumento de tipo o un comodín; reserve los tipos sin parametrizar para interoperar con código antiguo.

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
