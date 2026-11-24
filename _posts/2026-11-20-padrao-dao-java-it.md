---
layout: post
title: "Il pattern DAO per l'accesso ai dati in Java"
date: 2026-11-24
lang: it
translation_id: padrao-dao-java
permalink: /it/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object separa la persistenza dalla logica applicativa e dalla presentazione.
---

Un'applicazione può aprire connessioni, eseguire SQL, applicare regole e mostrare risultati in un'unica classe. Quando cresce, questa concentrazione rende più difficile la manutenzione. Il capitolo «Estendere le classi: accesso ai dati» usa il pattern DAO (*Data Access Object*) per isolare la responsabilità della persistenza.

Un DAO offre operazioni per inserire, cercare, aggiornare ed eliminare oggetti. Il client non deve conoscere le istruzioni SQL, i dati di connessione o la trasformazione delle righe in oggetti. Nell'esempio `Student` rappresenta i dati, `StudentDAO` gestisce la tabella `student` e `DBExample` invoca le operazioni.

Il libro presenta prima un DAO specifico per gli studenti, poi sposta le funzionalità comuni in `AbstractDAO<T>` tramite ereditarietà e generics. Le chiamate del client rimangono stabili. JDBC viene usato direttamente per rendere visibili le responsabilità.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/it/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [La classe Student nell'esempio DAO](/it/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/it/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [Un record per i dati di connessione JDBC](/it/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/it/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [Creare StudentDAO con operazioni CRUD](/it/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Articoli correlati

{{ dao_related_links }}

{% endif %}

In inglese: [Versione inglese](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
