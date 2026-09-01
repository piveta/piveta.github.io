---
layout: post
title: "Hello World - Versión Tradicional vs. Versión Simplificada"
date: 2026-08-22
lang: es
translation_id: hello-world
permalink: /es/hola-mundo/
---

Es habitual iniciar el estudio de un lenguaje de programación escribiendo un programa llamado **Hello World**, que muestra el texto `Hello World!` en la salida estándar del dispositivo, normalmente la pantalla. En Java, podemos escribir este programa de la siguiente manera:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

En este programa, tenemos una clase denominada `Hello`. Las clases en los sistemas orientados a objetos ayudan a modelar conceptos del dominio de la aplicación que está siendo estudiada. Las clases encapsulan tanto los datos como el comportamiento de un determinado concepto.

La clase `Hello` posee un único método, llamado `main`, que recibe un vector de cadenas de caracteres que contiene los argumentos de línea de comandos proporcionados al ejecutar el programa, si los hubiera. En este ejemplo, dichos argumentos no se utilizan.

El método `main` es estático, lo que significa que es un método de clase y no un método de instancia. Por lo tanto, puede ser llamado sin necesidad de crear un objeto de la clase `Hello`.

Dentro del método `main` hay una llamada al método `println`. Este método pertenece a la clase `PrintStream` e imprime en la pantalla lo que se le proporciona como parámetro, seguido de un salto de línea.

El método `println` se llama a partir del atributo `out` de la clase `System`. Este atributo es de tipo `PrintStream` y proporciona acceso a la salida estándar del sistema.

## Compilación y ejecución

Los programas en Java se compilan primero a una representación intermedia, denominada **bytecode**, con el fin de garantizar su portabilidad. Posteriormente, estos bytecodes se ejecutan en una Máquina Virtual de Java (JVM), que los convierte en código máquina adecuado para la plataforma subyacente.

Para compilar el programa, este debe estar almacenado en un archivo llamado `Hello.java`. En Java, los archivos que contienen tipos públicos normalmente tienen el mismo nombre que el tipo.

Podemos utilizar un entorno integrado de desarrollo (**IDE**, *Integrated Development Environment*) o ejecutar el compilador directamente desde la línea de comandos, siempre que haya un JDK instalado.

Normalmente, los programas Java se escriben en una IDE, que ofrece recursos para aumentar la productividad durante el desarrollo, como navegación por el código fuente, refactorización, análisis estático, compilación, pruebas y depuración.

Algunas de las IDE más populares para Java son:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

También podemos compilar el programa directamente desde la línea de comandos utilizando el compilador `javac`:

```text
javac Hello.java
```

El comando recibe `Hello.java` como entrada y produce el archivo `Hello.class`, que contiene la versión compilada del programa.

Después de la compilación, podemos ejecutar el programa utilizando el comando `java`:

```text
java Hello
```

La salida será:

```text
Hello World!
```

## Una forma más sencilla con Java 25+

A partir de Java 25, una funcionalidad que había estado en desarrollo como *preview* desde Java 21 se convirtió en permanente: **Compact Source Files and Instance Main Methods**. Esta funcionalidad permite escribir pequeños programas con menos código de infraestructura, omitiendo la declaración explícita de la clase y simplificando el método `main`.

Así, el programa anterior puede escribirse en Java 26 como:

```java
void main() {
    IO.println("Hello World!");
}
```

En este caso, no necesitamos declarar explícitamente la clase ni escribir `public static void main(String[] args)`. El compilador considera que el archivo declara implícitamente una clase, y el método `main` puede ser un método de instancia.

También podemos utilizar la clase `IO`, que proporciona operaciones sencillas para la entrada y salida en la consola. En Java 26, `IO` pertenece al paquete `java.lang` y, por lo tanto, está disponible implícitamente. Para llamar a sus métodos, sin embargo, es necesario utilizar el nombre de la clase, como en `IO.println(...)`.

Como esta funcionalidad ya no está en modo *preview*, no necesitamos utilizar opciones especiales de compilación. El programa puede compilarse normalmente:

```text
javac Hello.java
```

y ejecutarse de la misma manera:

```text
java Hello
```

También es posible ejecutar directamente un archivo fuente utilizando el lanzador `java`:

```text
java Hello.java
```

En este caso, el código fuente es compilado en memoria por el propio lanzador antes de su ejecución. Este mecanismo permite ejecutar programas directamente desde los archivos fuente sin necesidad de producir explícitamente un archivo `.class`.

El uso de archivos compactos de código fuente es especialmente interesante para ejemplos pequeños, programas de aprendizaje, scripts y experimentos. A medida que el programa crece y pasa a requerir una estructura más elaborada, podemos volver naturalmente a la forma tradicional, con declaraciones explícitas de clases y métodos.

El proceso realizado por las IDE es esencialmente similar. Además de la compilación y ejecución, proporcionan recursos para depuración, pruebas, refactorización, creación y gestión de proyectos, creación de bibliotecas y gestión de versiones, entre muchas otras funcionalidades.

---

*Este artículo es una adaptación de contenido del libro <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, de <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
