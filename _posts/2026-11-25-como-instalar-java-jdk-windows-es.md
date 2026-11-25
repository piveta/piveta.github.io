---
layout: post
title: "Cómo instalar Java y el JDK en Windows"
date: 2026-11-25
lang: es
translation_id: como-instalar-java-jdk-windows
permalink: /es/instalar-java-jdk-windows/
share_text: >-
  Descarga e instala un JDK en Windows y comprueba la instalación con java y javac.
---

## Elige una distribución de Java
Para programar en Java en Windows, descarga un **JDK** compatible con el proyecto. Oracle JDK y Eclipse Temurin son distribuciones disponibles. Una versión LTS puede servir a proyectos que necesitan soporte prolongado. Comprueba los requisitos del proyecto y las condiciones de la distribución.

En Configuración de Windows, revisa el tipo de sistema y la arquitectura del procesador. En la página de descarga, elige el paquete correspondiente, como x64 o AArch64, y el instalador para Windows.

## Descargar e instalar el JDK
Para instalar Eclipse Temurin:

1. Abre la [página de descargas de Adoptium](https://adoptium.net/temurin/releases/).
2. Selecciona la versión de Java, Windows, la arquitectura y el paquete **JDK**.
3. Descarga y ejecuta el instalador MSI.
4. Comprueba si Java se agregará a <code>PATH</code>. Si otra herramienta necesita <code>JAVA_HOME</code>, activa también esa opción.
5. Termina la instalación y abre una terminal nueva.

En Temurin, agregar Java a <code>PATH</code> es una opción estándar; configurar <code>JAVA_HOME</code> es adicional.

## Comprueba la instalación
En PowerShell o en el Símbolo del sistema, ejecuta:

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

Los dos primeros comandos muestran las versiones de Java y del compilador. Los demás indican los ejecutables encontrados en <code>PATH</code>. Si no se reconoce un comando, abre una terminal nueva y revisa las variables de entorno. Si aparece otra versión, comprueba el orden de los directorios en <code>PATH</code>.

Guarda este código como <code>Hello.java</code> para probar la compilación:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Usa la declaración compacta y <code>IO.println</code>, disponibles desde Java 25. Ejecuta:

~~~text
javac Hello.java
java Hello
~~~

La salida es <code>Hello World!</code>. En versiones anteriores, utiliza la forma de programa admitida por tu JDK.

## Referencias
- [Instalador MSI de Eclipse Temurin](https://adoptium.net/installation/windows/)
- [Instalación de Oracle JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
