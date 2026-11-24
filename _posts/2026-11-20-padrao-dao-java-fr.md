---
layout: post
title: "Le patron DAO pour accéder aux données en Java"
date: 2026-11-20
lang: fr
translation_id: padrao-dao-java
permalink: /fr/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object sépare la persistance des règles métier et de la présentation.
---

Une application peut ouvrir une connexion, exécuter du SQL, appliquer des règles métier et afficher les résultats dans une seule classe. Cette concentration complique la maintenance lorsque le système grandit. Le chapitre « Étendre les classes : accès aux données » utilise le patron DAO (*Data Access Object*) pour isoler la responsabilité de la persistance.

Un DAO propose des opérations d'insertion, de recherche, de modification et de suppression d'objets. Le client n'a pas besoin de connaître le SQL, les paramètres de connexion ni la conversion des lignes en objets. Dans l'exemple, `Student` représente les données, `StudentDAO` gère la table `student` et `DBExample` appelle les opérations.

Le livre présente d'abord un DAO propre aux étudiants, puis déplace l'infrastructure commune vers `AbstractDAO<T>` au moyen de l'héritage et des génériques. L'interface utilisée par le client reste stable. JDBC est employé directement pour rendre les responsabilités visibles.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/fr/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [La classe Student dans l'exemple DAO](/fr/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/fr/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [Un record pour les données de connexion JDBC](/fr/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/fr/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [Créer StudentDAO avec les opérations CRUD](/fr/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Articles associés

{{ dao_related_links }}

{% endif %}

En anglais: [Version anglaise](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
