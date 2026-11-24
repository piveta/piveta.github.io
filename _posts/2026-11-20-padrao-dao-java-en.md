---
layout: post
title: "The DAO Pattern for Data Access in Java"
date: 2026-11-20
lang: en
translation_id: padrao-dao-java
permalink: /en/the-dao-pattern-for-data-access-in-java/
share_text: >-
  The Data Access Object pattern separates persistence from business rules and presentation in a Java application.
---

An application can open a connection, run SQL, apply business rules, and display results in one class. That concentration works in a small example but becomes difficult to read and maintain as the system grows. The chapter **Extending Classes: Data Access** uses the DAO (*Data Access Object*) pattern to give persistence its own responsibility.

A DAO offers operations for inserting, finding, updating, and deleting objects. The rest of the application calls those operations without knowing the SQL statements, connection details, or the conversion from database rows to objects. In the book's example, `Student` represents a student's data, `StudentDAO` handles the `student` table, and `DBExample` is the client that requests operations and displays their results.

This separation reduces coupling. A change to the database access code can remain inside the DAO instead of forcing the client to rewrite its presentation and business rules. A defined interface can also make tests easier because a substitute implementation can stand in for the database.

The chapter first builds a DAO specific to students. It then uses **inheritance, an abstract class, and generics** to put common operations in `AbstractDAO<T>`, leaving entity-specific SQL and mapping in `StudentDAO`. The client keeps using the same public operations even when the DAO's internal structure changes.

Larger applications may use Spring JDBC or object-relational mapping tools for different abstractions. The book uses JDBC directly so that the responsibilities and their separation remain visible.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/en/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [The Student Class in the DAO Example](/en/the-student-class-in-the-dao-example/) — student data model.
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/en/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [A Record for JDBC Connection Data](/en/a-record-for-jdbc-connection-data/) — JDBC connection values.
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/en/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [Building StudentDAO with CRUD Operations](/en/building-studentdao-with-crud-operations/) — initial DAO implementation.
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Related articles

{{ dao_related_links }}

{% endif %}

Other language: [Portuguese version](/padrao-dao-java/).

<!-- DAO_RELATIONS_END -->

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
