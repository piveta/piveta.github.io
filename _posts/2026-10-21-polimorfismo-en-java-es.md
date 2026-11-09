---
layout: post
title: "Polimorfismo en Java"
date: 2026-10-21
lang: es
translation_id: polimorfismo-em-java
permalink: /polimorfismo-en-java/
share_text: >-
  Introducción al polimorfismo ad hoc, paramétrico y de subtipo, con ejemplos en Java.
---

En la programación orientada a objetos, **polimorfismo** es la capacidad de una operación para comportarse de manera diferente según la clase del objeto involucrado. Sus formas principales son:

- **Polimorfismo ad hoc (o sobrecarga)**: los métodos con el mismo nombre pueden tener distintos parámetros, y la llamada selecciona la versión compatible según sus argumentos;
- **Polimorfismo paramétrico**: las clases y los métodos genéricos trabajan con tipos que se especifican cuando se utilizan;
- **Polimorfismo de subtipo**: una subclase puede sobrescribir un método, y la implementación que se ejecuta depende de la clase concreta del objeto.

Los siguientes ejemplos muestran estas tres formas en Java, empezando por la sobrecarga. La clase `Figure` tiene dos métodos sobrecargados llamados `resize`. El primero recibe un `percentage` de tipo `Double`; el segundo recibe dos coordenadas, `x` e `y`, de tipo `Integer`.

```java
public class Figure {
    public void resize(Double percentage) {
        // Cambiar el tamaño según un porcentaje
    }
    public void resize(Integer x, Integer y) {
        // Cambiar el tamaño según las coordenadas
    }
}
```

Para el **polimorfismo paramétrico**, podemos crear tipos parametrizados mediante `<` y `>`. Por ejemplo, la clase `ArrayList` tiene un parámetro de tipo `E` que especifica el tipo de objetos que puede almacenar la lista. Este parámetro también se usa como parámetro formal del método `add`. Así, el tipo que espera `add` es el mismo que se utiliza al instanciar `ArrayList`. Observa que extiende `AbstractList` e implementa las interfaces `List`, `RandomAccess`, `Cloneable` y `Serializable`, entre otras, usando el mismo tipo `E`.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // Implementación de add
    }
    // Otros métodos y campos de la clase
}
```

Por ejemplo, podemos crear una lista de cadenas con el parámetro de tipo `String` e insertar elementos llamando a `add`[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

En este caso, el compilador espera que el argumento pasado a `add` sea una cadena (`String`). Pasar un objeto de otro tipo produce un error de compilación. Si quisiéramos una lista de números enteros, podríamos pasar otro tipo a `ArrayList`, en este caso `Integer`:

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

Para el **polimorfismo de subtipo**, supongamos que la clase `Figure` tiene un método `draw` que también puede invocarse sobre objetos de las clases `Triangle`, `Circle` y `Rectangle`. Supongamos que cada una sobrescribe el método para implementar su propia forma de dibujar. En el siguiente código, cada llamada a `draw` invoca una implementación distinta según la clase del objeto asignado a `figure`: `Circle`, `Triangle` o `Rectangle`.

```java
Figure figure = new Circle(10);
// Invoca el método draw de Circle
figure.draw();
figure = new Triangle(20);
// Invoca el método draw de Triangle
figure.draw();
figure = new Rectangle(10, 20);
// Invoca el método draw de Rectangle
figure.draw();
```

[^8]: Para usar `ArrayList`, normalmente hay que importarla con `import java.util.ArrayList;`. Los archivos fuente compactos no requieren importaciones. En los archivos fuente convencionales, se puede importar el módulo `java.base` con `import module java.base;`.

---

*Este artículo adapta contenido del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artículos relacionados

- [Conceptos básicos de orientación a objetos](/conceptos-basicos-de-poo/)
- [Clases en Java](/clases-en-java/)
- [Herencia en Java](/herencia-en-java/)
- [Interfaces en Java](/interfaces-en-java/)
- [Enlaces sobre POO y Java](/enlaces-poo-java/)
- [Ejercicios de programación orientada a objetos](/ejercicios-programacion-orientada-objetos/)
