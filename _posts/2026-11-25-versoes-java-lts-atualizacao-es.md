---
layout: post
title: "Versiones de Java: LTS, actualizaciones y cómo comprobar la versión"
date: 2026-11-25
lang: es
translation_id: versoes-java-lts-atualizacao
permalink: /es/versiones-java-lts-actualizaciones/
share_text: >-
  Conoce el ciclo de versiones de Java, qué significa LTS y cómo comprobar y actualizar un JDK.
---

## Comprueba tu versión de Java
Ejecuta estos comandos en una terminal:

~~~text
java --version
javac --version
~~~

El primero identifica el lanzador de Java que inicia las aplicaciones; el segundo, el compilador. Si hay varios JDK instalados, el ejecutable encontrado en <code>PATH</code> puede ser distinto del configurado en el IDE.

## Versiones de Java y LTS
Java publica versiones con nuevas funciones cada seis meses. Una versión **LTS** (*long-term support*) recibe soporte a largo plazo de ciertos proveedores. La duración, el precio y las condiciones dependen de la distribución y del proveedor.

En la hoja de ruta de soporte de Oracle, Java 8, 11, 17, 21 y 25 son versiones LTS. Oracle planea publicar una nueva versión LTS cada dos años. Consulta la hoja de ruta vigente y la política del proveedor antes de elegir una versión para producción.

La decisión también depende de bibliotecas, herramientas y requisitos de la aplicación. Una LTS ofrece un horizonte de soporte más largo; las versiones intermedias incorporan antes las novedades.

## Dónde consultar versiones y JEP
Oracle mantiene un [índice de notas de versión del JDK](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html), con enlaces a versiones y actualizaciones. Las notas describen cambios, correcciones y funciones añadidas o retiradas. Por ejemplo, las [notas de JDK 27](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) explican novedades y enlazan las JEP relacionadas.

Una **JEP** (*JDK Enhancement Proposal*) documenta una propuesta de mejora del JDK, sus objetivos, diseño y estado. Algunas funciones aparecen primero como *preview* o *incubator* y pueden cambiar antes de ser definitivas.

Consulta los [cambios del lenguaje Java por versión](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html) y el [resumen de cambios](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html) para comparar funciones permanentes y preliminares.

## Actualiza Java
1. Identifica la versión con <code>java --version</code> y <code>javac --version</code>.
2. Comprueba qué admiten el proyecto, sus dependencias y producción.
3. Descarga una actualización de tu distribución o elige otra compatible.
4. Instala el JDK y ajusta <code>PATH</code>, <code>JAVA_HOME</code> y el IDE si hace falta.
5. Abre una terminal nueva, comprueba las versiones y ejecuta las pruebas de la aplicación.

Actualizar dentro de una misma línea y migrar a una versión principal son decisiones distintas. Antes de migrar, revisa las notas y prueba la aplicación y sus dependencias.

En Windows, <code>where.exe java</code> y <code>where.exe javac</code> muestran los ejecutables encontrados. En macOS o Linux, usa <code>which java</code> y <code>which javac</code>.

## Referencias
- [Hoja de ruta de soporte de Oracle Java SE](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [Preguntas frecuentes sobre licencias de Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
