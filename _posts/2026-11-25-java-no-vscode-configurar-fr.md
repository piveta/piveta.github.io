---
layout: post
title: "Java dans VS Code : installer et configurer le JDK"
date: 2026-11-25
lang: fr
translation_id: java-no-vscode-configurar
permalink: /fr/java-dans-vs-code-configuration/
share_text: >-
  Configurez Java dans Visual Studio Code, choisissez un JDK et exécutez un premier programme.
---

## Installer le JDK et Visual Studio Code
Pour programmer en **Java avec VS Code**, installez un JDK compatible avec le projet, ainsi que Visual Studio Code. Vérifiez dans un terminal que le JDK est accessible :

~~~text
java --version
javac --version
~~~

Si les commandes sont introuvables, vérifiez l’installation du JDK et le <code>PATH</code>. Ouvrez un nouveau terminal après avoir modifié les variables d’environnement.

## Installer les extensions Java
Dans VS Code, ouvrez **Extensions**, recherchez **Extension Pack for Java** et installez le pack publié par Microsoft. Il rassemble la prise en charge du langage, l’exécution, le débogage et d’autres outils Java.

Le Coding Pack for Java, disponible pour Windows et macOS, constitue une autre option : il regroupe VS Code, un JDK et les extensions essentielles.

## Configurer le JDK du projet
Ouvrez la palette de commandes avec <code>Ctrl+Shift+P</code> sous Windows ou Linux, ou <code>Cmd+Shift+P</code> sous macOS. Lancez **Java: Configure Java Runtime** et vérifiez le JDK associé au projet.

Le JDK du projet peut différer de celui du terminal. Si plusieurs versions sont installées, vérifiez les deux.

## Exécuter un programme
Ouvrez un dossier dans VS Code et créez <code>Hello.java</code> :

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Cet exemple utilise la déclaration compacte et <code>IO.println</code>, disponibles depuis Java 25. Cliquez sur **Run** à côté de <code>main</code> et vérifiez la sortie dans le terminal. Pour déboguer, choisissez **Debug** et placez un point d’arrêt.

Si VS Code ne reconnaît pas le fichier, vérifiez que le dossier est ouvert, attendez le démarrage des extensions et contrôlez le JDK dans **Java: Configure Java Runtime**.

## Références
- [Premiers pas avec Java dans VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Gestion de projets Java dans VS Code](https://code.visualstudio.com/docs/java/java-project)
