---
layout: post
title: "Installer Java et le JDK sous Windows"
date: 2026-11-25
lang: fr
translation_id: como-instalar-java-jdk-windows
permalink: /fr/installer-java-jdk-windows/
share_text: >-
  Téléchargez et installez un JDK sous Windows, puis vérifiez-le avec java et javac.
---

## Choisir une distribution Java
Pour programmer en Java sous Windows, téléchargez un **JDK** compatible avec le projet. Oracle JDK et Eclipse Temurin sont disponibles. Une version LTS peut convenir aux projets qui exigent un support à long terme. Vérifiez les exigences et les conditions de la distribution.

Dans les paramètres Windows, vérifiez le type de système et l’architecture du processeur. Choisissez le paquet adapté, par exemple x64 ou AArch64, puis l’installateur Windows.

## Télécharger et installer le JDK
Pour Eclipse Temurin :

1. Ouvrez la [page de téléchargement d’Adoptium](https://adoptium.net/temurin/releases/).
2. Choisissez la version de Java, Windows, l’architecture et le paquet **JDK**.
3. Téléchargez et lancez l’installateur MSI.
4. Vérifiez si Java doit être ajouté au <code>PATH</code>. Si un autre outil a besoin de <code>JAVA_HOME</code>, activez aussi cette option.
5. Terminez l’installation et ouvrez un nouveau terminal.

Dans Temurin, l’ajout au <code>PATH</code> est une option standard ; la configuration de <code>JAVA_HOME</code> est supplémentaire.

## Vérifier l’installation
Dans PowerShell ou l’invite de commandes, exécutez :

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

Les deux premières commandes affichent les versions de Java et du compilateur. Les autres montrent les exécutables trouvés dans le <code>PATH</code>. Si une commande est introuvable, ouvrez un nouveau terminal et vérifiez les variables d’environnement. Si une autre version apparaît, examinez l’ordre des dossiers dans le <code>PATH</code>.

Enregistrez ce code dans <code>Hello.java</code> pour tester la compilation :

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

L’exemple utilise la déclaration compacte et <code>IO.println</code>, disponibles depuis Java 25. Exécutez :

~~~text
javac Hello.java
java Hello
~~~

Le résultat est <code>Hello World!</code>. Avant Java 25, utilisez la forme de programme prise en charge par votre JDK.

## Références
- [Installateur MSI d’Eclipse Temurin](https://adoptium.net/installation/windows/)
- [Installation d’Oracle JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
