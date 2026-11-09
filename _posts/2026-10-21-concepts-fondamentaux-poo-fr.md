---
layout: post
title: "Concepts fondamentaux de la programmation orientée objet"
date: 2026-10-21
lang: fr
translation_id: conceitos-basicos-poo-java
permalink: /concepts-fondamentaux-poo-fr/
share_text: >-
  Introduction aux notions fondamentales de la programmation orientée objet : classes, objets, attributs, méthodes, encapsulation, héritage, polymorphisme et relations entre classes.
---

La programmation structurée fournit des mécanismes pour modulariser les concepts d’un système logiciel au moyen de structures de données et des algorithmes qui les manipulent. Les langages structurés courants permettent de représenter différents types de données et variables afin d’exprimer les propriétés et caractéristiques des concepts concernés, ainsi que des procédures et fonctions pour modéliser les opérations correspondantes.

Cependant, pour réutiliser des composants écrits dans des langages structurés, il faut identifier les relations entre les données — représentées par des structures, des types de données et des variables — et le comportement — exprimé par des procédures et des fonctions. La réutilisation se fait donc souvent à un niveau très fin et peut demander un effort considérable, par exemple pour déterminer quelles procédures et fonctions correspondent à quelles structures de données. Des bibliothèques réutilisables peuvent être créées, mais la relation entre les données et le comportement n’est ni explicite ni réunie dans une seule abstraction.

La **programmation orientée objet** (POO) est un paradigme qui représente les concepts d’un domaine d’application au moyen de types abstraits de données appelés classes. Ces classes modélisent les caractéristiques et propriétés des concepts ainsi que leurs opérations. La POO étend la programmation structurée en fournissant des moyens de spécifier et de composer des classes pour modéliser des systèmes informatiques complets, avec pour objectifs une meilleure modularité et la réutilisation des composants.

Aujourd’hui, la programmation orientée objet est l’un des paradigmes les plus utilisés et acceptés pour le développement logiciel. De nombreux langages modernes la prennent en charge, notamment Java, C++, C#, Python, Kotlin, JavaScript, TypeScript, Swift et Ruby.

Une **classe** est un mécanisme d’abstraction qui représente les concepts d’un domaine d’application. Dans un domaine bancaire, par exemple, ces concepts peuvent inclure des agences, des comptes, des clients et des transactions. On pourrait définir les classes `Branch`, `Account`, `Customer` et `Transaction` pour les représenter. La figure présente une représentation graphique de ces classes.

<img src="/images/en/oopClasses.svg" alt="Les classes Branch, Account, Customer et Transaction." style="max-width: 300px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Les classes servent de *modèles* pour créer des exemples concrets et manipulables de ces concepts. Ces exemples s’appellent des **objets**. Un objet est une **instance** d’une classe, et le processus de création d’objets s’appelle l’**instanciation**. On pourrait, par exemple, créer des objets représentant les clients *John*, *Peter* et *Mary*, avec leurs informations personnelles et les fonctionnalités accessibles aux clients.

<img src="/images/en/oopObjects.svg" alt="Les objets John, Peter et Mary sont des instances de Customer." style="max-width: 380px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Une classe est définie pour représenter les propriétés, les caractéristiques et le comportement d’un concept. Les deux mécanismes principaux sont les attributs et les méthodes.

Les **attributs** représentent les caractéristiques ou propriétés des objets d’une classe. Parmi les attributs d’une classe `Customer`, on peut citer *name*, *age*, *address* et *marital status*. Chaque client peut avoir des valeurs différentes pour ces attributs. Par exemple : *name* $`=`$ John Smith, *age* $`=`$ 50, *address* $`=`$ 205 President Vargas Street et *marital status* $`=`$ married.

Les **méthodes** représentent le comportement. Les méthodes possibles d’une classe `Account` peuvent correspondre aux opérations consistant à *ouvrir*, *clôturer* ou *changer le titulaire* d’un compte. L’**invocation** d’une méthode (ou son **appel**) exécute l’opération qu’elle implémente. Les classes comportent souvent des méthodes spéciales pour créer (instancier) des objets, appelées **constructeurs**, et pour détruire des objets, appelées **destructeurs**.

Les attributs et les méthodes se répartissent aussi en deux catégories : ceux d’instance et ceux de classe. Les **attributs et méthodes d’instance** sont les plus courants et s’utilisent à partir des objets de la classe. Ils représentent les caractéristiques et opérations propres à chaque instance. Les attributs d’instance d’`Account` peuvent inclure *bank*, *branch*, *account number* et *account holder* ; ses méthodes d’instance peuvent inclure *withdraw*, *transfer* et *deposit*. Les **attributs et méthodes de classe**, eux, appartiennent à la classe et non à ses instances. Un attribut de classe pourrait compter le nombre d’instances d’`Account` créées, et une méthode de classe pourrait renvoyer ce nombre.

Pour restreindre l’accès aux attributs et aux méthodes, les classes proposent des mécanismes d’**encapsulation et de masquage de l’information**. Les langages de programmation fournissent généralement des modificateurs de visibilité qui précisent qui peut accéder à un attribut, une méthode ou une classe.

Les classes abstraient et encapsulent des concepts du monde réel et du monde informatique. Ces abstractions peuvent être combinées par des relations afin que les classes collaborent à la satisfaction des exigences d’une application. Parmi les principales relations entre classes figurent l’héritage, l’association, l’agrégation, la composition et la réalisation.

L’**héritage** est un mécanisme de composition qui permet aux classes de réutiliser l’interface et le comportement de classes existantes en étendant leurs fonctionnalités. Une classe qui en étend une autre est appelée **sous-classe** ; la classe étendue est la **superclasse**. L’extension est généralement déclarée dans la sous-classe, par exemple : `SubClass` étend `SuperClass`.

La figure 3 présente les classes `Shape`, `Rectangle`, `Triangle` et `Circle`. `Shape` est la superclasse ; `Rectangle`, `Triangle` et `Circle` sont ses sous-classes.

<img src="/images/en/oopInheritance.png" alt="Shape est la superclasse de Rectangle, Triangle et Circle." style="max-width: 400px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Les mécanismes d’héritage varient selon les langages. Certaines différences portent sur la visibilité et la multiplicité de l’héritage. Des langages comme C++ permettent de spécifier un héritage **public** ou **privé**. Considérons une classe `A` et une classe `B` qui hérite de `A`. `A` est alors la superclasse de `B`, et `B` sa sous-classe. Avec l’héritage public, `B` est un sous-type de `A` et hérite de son implémentation comme de son interface. Partout où un objet `A` est attendu, on peut donc utiliser un objet `B` (ou d’une autre sous-classe de `A`), puisque toute instance de `B` est aussi considérée comme une instance de `A`. Ce principe est appelé **principe de substitution de Liskov**. Avec l’héritage privé, `B` n’est pas un `A` : elle hérite seulement de l’implémentation de `A` et est construite à partir d’elle. Le principe de substitution de Liskov ne s’applique pas.

L’héritage peut également être **simple ou multiple**. Avec l’héritage simple, adopté par Java et C#, une classe ne peut avoir qu’une superclasse. Avec l’héritage multiple, comme en C++, une classe peut avoir plusieurs superclasses. Les concepteurs de langages ne s’accordent pas sur le fait que les avantages de l’héritage multiple justifient les problèmes qu’il peut entraîner. D’autres langages proposent des solutions de remplacement, comme l’héritage virtuel fondé sur des interfaces, les *traits* et les *mixins*.

La figure 4 montre un exemple d’héritage multiple. `Mammal` et `Bird` représentent des animaux. `Horse`, `Dog` et `Bat` sont des sous-classes de `Mammal`, tandis que `Ostrich` et `Duck` sont des sous-classes de `Bird`. On souhaite également représenter les animaux capables de voler. On crée donc `Flyer`, une classe qui représente des objets volants, pas nécessairement des animaux. Grâce à l’héritage multiple, les objets `Duck` et `Bat` peuvent également être des objets volants en héritant de `Flyer`.

<img src="/images/en/oopMultipleInheritance.png" alt="Héritage multiple entre les classes Animal, Bird, Flyer et Mammal." style="max-width: 500px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Certaines classes sont **abstraites**. Comme les classes **concrètes**, elles représentent les caractéristiques et le comportement d’un ensemble d’objets du monde réel, mais elles ne peuvent pas être instanciées directement. Dans l’exemple d’héritage multiple, `Mammal`, `Bird` et `Flyer` pourraient être abstraites, car seuls des objets de leurs sous-classes — chevaux, chiens ou canards, par exemple — existent dans le monde réel.

Outre la visibilité et la multiplicité, l’héritage permet de créer des méthodes polymorphes. En programmation orientée objet, le **polymorphisme** est la capacité d’une opération à se comporter différemment selon la classe de l’objet qui l’appelle. Ses principales formes sont :

- Le **polymorphisme ad hoc (ou surcharge)** apparaît lorsque plusieurs méthodes d’une classe ont le même nom, mais des types de paramètres formels différents. L’argument utilisé détermine la méthode appelée.
- Le **polymorphisme paramétrique** apparaît lorsqu’une méthode est définie de manière générique et liée à un type qui ne sera précisé que plus tard, par exemple lors de la déclaration d’une variable ou de l’instanciation d’un objet. Dans les langages orientés objet, il s’agit de types génériques.
- Le **polymorphisme de sous-type** apparaît lorsque des sous-classes redéfinissent des méthodes d’une superclasse. L’objet qui effectue l’appel détermine la méthode exécutée. Cela se résout généralement à l’exécution, par liaison dynamique.

Il existe d’autres relations que l’héritage, notamment l’association, l’agrégation et la composition. En général, leur différence tient au degré de couplage entre les participants :

- Dans une **association**, la relation entre objets est souvent temporaire et facile à modifier à l’exécution. Dans un système de circulation, une personne peut, par exemple, être associée à un véhicule en tant que conductrice. Si la conductrice change, les deux objets continuent d’exister même si l’association est supprimée.
- Dans une **agrégation**, la relation est plus forte que dans une association. Les objets agrégés sont souvent créés en même temps que l’objet agrégateur. Une voiture peut ainsi posséder quatre roues : la voiture est l’objet agrégateur et les roues sont les objets agrégés. On peut mettre fin à cette relation, mais remplacer les roues est moins courant et plus contraignant que changer de conducteur.
- Dans une **composition**, la relation est encore plus forte : les objets composés font partie d’un objet plus grand. Le tissu du siège d’un véhicule est, par exemple, constitué de fils. Si ces fils n’existent plus, le siège cesse lui aussi d’exister ou perd son identité.

Ces relations entre objets sont souvent conceptuelles. Lorsqu’on les traduit dans un langage de programmation, on associe, agrège ou compose par exemple des objets au moyen des attributs d’une classe, en leur affectant des valeurs à l’exécution. Le moment de création peut varier : dans une composition, les objets composants sont souvent créés dans le constructeur de l’ensemble ; dans une association, les objets associés sont généralement créés indépendamment puis liés au besoin.

Enfin, la **réalisation** a lieu lorsqu’une classe déclare qu’elle implémente une interface. Une **interface** peut être considérée comme une classe abstraite dont toutes les méthodes sont abstraites[^1]. Elle sert de protocole entre les clients et les implémenteurs. La classe (ou l’une de ses sous-classes) doit fournir les méthodes déclarées par l’interface. Les clients peuvent ainsi écrire du code conforme à l’interface sans dépendre de la façon dont les classes l’implémentent.

[^1]: Depuis Java 8, les interfaces peuvent aussi définir des méthodes concrètes, appelées méthodes par défaut, au moyen du mot-clé `default`. Une classe qui implémente une interface contenant une méthode par défaut n’est pas obligée de la redéfinir, mais elle peut le faire.

---

*Cet article adapte du contenu du livre <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, d’<a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Articles associés

- [Classes en Java](/classes-en-java-fr/)
- [Héritage en Java](/heritage-java-fr/)
- [Polymorphisme en Java](/polymorphisme-java-fr/)
- [Interfaces en Java](/interfaces-java-fr/)
- [Liens sur la POO et Java](/liens-poo-java-fr/)
- [Exercices de programmation orientée objet](/exercices-poo-fr/)
