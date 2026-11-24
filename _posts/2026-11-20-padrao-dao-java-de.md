---
layout: post
title: "Das DAO-Muster für Datenzugriff in Java"
date: 2026-11-24
lang: de
translation_id: padrao-dao-java
permalink: /de/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object trennt Persistenz von Geschäftslogik und Darstellung.
---

Eine einzige Klasse kann Verbindungen öffnen, SQL ausführen, Geschäftsregeln anwenden und Ergebnisse anzeigen. Mit wachsender Anwendung erschwert diese Bündelung die Wartung. Das Kapitel „Klassen erweitern: Datenzugriff“ verwendet das DAO-Muster (*Data Access Object*), um die Persistenz als eigene Aufgabe zu behandeln.

Ein DAO bietet Methoden zum Einfügen, Suchen, Ändern und Löschen von Objekten. Der Client muss weder die SQL-Anweisungen noch die Verbindung oder die Umwandlung von Datenbankzeilen in Objekte kennen. Im Beispiel enthält `Student` die Daten, `StudentDAO` verwaltet die Tabelle `student`, und `DBExample` ruft die Operationen auf.

Zuerst zeigt das Buch ein studentenspezifisches DAO. Danach verlagert es gemeinsame Aufgaben mittels Vererbung und Generics nach `AbstractDAO<T>`. Die öffentliche Nutzung durch den Client bleibt dabei gleich. JDBC wird direkt eingesetzt, damit die Zuständigkeiten sichtbar bleiben.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/de/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [Die Klasse Student im DAO-Beispiel](/de/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/de/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [Ein record für JDBC-Verbindungsdaten](/de/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/de/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [StudentDAO mit CRUD-Operationen erstellen](/de/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Verwandte Artikel

{{ dao_related_links }}

{% endif %}

Auf Englisch: [Englische Fassung](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
