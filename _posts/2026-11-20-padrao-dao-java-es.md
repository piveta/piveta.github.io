---
layout: post
title: "El patrón DAO para acceder a datos con Java"
date: 2026-11-20
lang: es
translation_id: padrao-dao-java
permalink: /es/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object separa la persistencia de las reglas de negocio y de la presentación.
---

Una aplicación puede abrir conexiones, ejecutar SQL, aplicar reglas de negocio y mostrar resultados en una sola clase. Esa concentración dificulta el mantenimiento cuando el sistema crece. El capítulo «Extender clases: acceso a datos» emplea el patrón DAO (*Data Access Object*) para asignar la persistencia a una responsabilidad específica.

Un DAO ofrece operaciones para insertar, buscar, modificar y eliminar objetos. El cliente no necesita conocer la SQL, los datos de conexión ni la conversión de filas en objetos. En el ejemplo, `Student` representa los datos, `StudentDAO` gestiona la tabla `student` y `DBExample` solicita las operaciones y muestra los resultados.

El capítulo presenta primero un DAO específico y después traslada la infraestructura compartida a `AbstractDAO<T>`. Así, la implementación puede cambiar sin modificar las llamadas del cliente. JDBC se utiliza directamente para dejar visibles estas responsabilidades.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/es/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [La clase Student en el ejemplo DAO](/es/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/es/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [Un record para la conexión JDBC](/es/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/es/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [Crear StudentDAO con operaciones CRUD](/es/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Artículos relacionados

{{ dao_related_links }}

{% endif %}

En inglés: [Versión en inglés](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
