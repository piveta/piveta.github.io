---
layout: post
title: "Wzorzec DAO w dostępie do danych w Javie"
date: 2026-11-20
lang: pl
translation_id: padrao-dao-java
permalink: /pl/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object oddziela trwałość danych od logiki biznesowej i prezentacji.
---

Jedna klasa może otwierać połączenia, wykonywać SQL, stosować reguły biznesowe i wyświetlać wyniki. W większym programie takie skupienie odpowiedzialności utrudnia utrzymanie. Rozdział „Rozszerzanie klas: dostęp do danych” wykorzystuje wzorzec DAO (*Data Access Object*), aby wydzielić operacje trwałego przechowywania danych.

DAO udostępnia wstawianie, wyszukiwanie, aktualizowanie i usuwanie obiektów. Klient nie musi znać instrukcji SQL, sposobu tworzenia połączeń ani mapowania wierszy na obiekty. W przykładzie `Student` reprezentuje dane, `StudentDAO` obsługuje tabelę `student`, a `DBExample` wywołuje operacje.

Książka najpierw pokazuje DAO dla studentów, a następnie przenosi wspólną infrastrukturę do `AbstractDAO<T>` za pomocą dziedziczenia i typów generycznych. Wywołania klienta pozostają takie same. Bezpośrednie użycie JDBC uwidacznia podział odpowiedzialności.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/pl/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [Klasa Student w przykładzie DAO](/pl/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/pl/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [Record z danymi połączenia JDBC](/pl/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/pl/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [Tworzenie StudentDAO z operacjami CRUD](/pl/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Powiązane artykuły

{{ dao_related_links }}

{% endif %}

Po angielsku: [Wersja angielska](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
