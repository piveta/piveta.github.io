---
layout: post
title: "Java en VS Code: cómo instalar y configurar el JDK"
date: 2026-11-25
lang: es
translation_id: java-no-vscode-configurar
permalink: /es/java-en-vs-code-configuracion/
share_text: >-
  Configura Java en Visual Studio Code, selecciona un JDK y ejecuta un primer programa.
---

## Instala el JDK y Visual Studio Code
Para programar en **Java con VS Code**, instala un JDK compatible con el proyecto y Visual Studio Code. Comprueba en una terminal que el JDK esté disponible:

~~~text
java --version
javac --version
~~~

Si no se encuentran los comandos, revisa la instalación del JDK y <code>PATH</code>. Abre una terminal nueva después de cambiar las variables de entorno.

## Instala las extensiones de Java
En VS Code, abre **Extensions**, busca **Extension Pack for Java** e instala el paquete publicado por Microsoft. Reúne soporte del lenguaje, ejecución, depuración y otras herramientas de Java.

Otra opción es Coding Pack for Java, disponible para Windows y macOS, que incluye VS Code, un JDK y extensiones esenciales.

## Configura el JDK del proyecto
Abre la paleta de comandos con <code>Ctrl+Shift+P</code> en Windows o Linux, o <code>Cmd+Shift+P</code> en macOS. Ejecuta **Java: Configure Java Runtime** y comprueba el JDK asociado al proyecto.

El JDK del proyecto puede ser distinto del que encuentra la terminal. Si tienes varias versiones instaladas, revisa ambos.

## Ejecuta un programa
Abre una carpeta en VS Code y crea <code>Hello.java</code>:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

El ejemplo usa la declaración compacta y <code>IO.println</code>, disponibles desde Java 25. Usa **Run** junto a <code>main</code> y comprueba la salida en la terminal. Para depurar, selecciona **Debug** y establece un punto de interrupción.

Si VS Code no reconoce el archivo, confirma que la carpeta esté abierta, espera a que se inicien las extensiones y revisa el JDK en **Java: Configure Java Runtime**.

## Referencias
- [Primeros pasos con Java en VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Gestión de proyectos Java en VS Code](https://code.visualstudio.com/docs/java/java-project)
