---
layout: post
title: "JDK, JRE y JVM: ¿cuál es la diferencia en Java?"
date: 2026-11-25
lang: es
translation_id: jdk-jre-jvm-diferencas
permalink: /es/diferencias-jdk-jre-jvm/
share_text: >-
  Comprende las funciones de la JVM, el JRE y el JDK, y aprende qué comandos verifican el entorno Java.
---

## JVM, JRE y JDK
La **JVM** (Java Virtual Machine) ejecuta bytecode de Java. Carga clases, verifica y ejecuta instrucciones, y administra recursos como la memoria. El mismo bytecode puede ejecutarse en distintos sistemas cuando hay una JVM compatible.

El **JRE** (Java Runtime Environment) designa el entorno necesario para ejecutar aplicaciones Java, incluida la JVM y sus bibliotecas. La disponibilidad de paquetes JRE independientes depende de la distribución y la versión. Algunas aplicaciones incluyen su propio entorno de ejecución.

El **JDK** (Java Development Kit) reúne el entorno de ejecución y herramientas de desarrollo: el compilador <code>javac</code>, el lanzador <code>java</code> y otras herramientas para crear, ejecutar y diagnosticar aplicaciones.

## ¿Qué instalar para programar?
Para desarrollar en Java, instala un JDK adecuado al proyecto. La distribución elegida proporciona la JVM y las herramientas necesarias. Oracle JDK y Eclipse Temurin son ejemplos de distribuciones.

En una terminal, comprueba estos comandos:

~~~text
java --version
javac --version
~~~

El primero muestra la versión del lanzador Java y el segundo la del compilador. Si <code>java</code> funciona pero no se encuentra <code>javac</code>, comprueba que haya un JDK instalado y que su directorio <code>bin</code> esté en <code>PATH</code>.

En Windows, <code>where java</code> y <code>where javac</code> ayudan a identificar el ejecutable utilizado. En macOS y Linux, usa <code>which java</code> y <code>which javac</code>.

## Del código fuente a la ejecución
En un archivo <code>Hello.java</code>, el compilador transforma el código fuente en bytecode:

~~~text
javac Hello.java
java Hello
~~~

La primera línea genera <code>Hello.class</code>. La segunda inicia la JVM para ejecutar la clase. La compatibilidad depende de la versión usada para compilar y de la usada para ejecutar.

## Referencias
- [Descripción general de la plataforma Java y la JVM](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [Guía de instalación del JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
