---
layout: post
title: "DAO-mönstret för dataåtkomst i Java"
date: 2026-11-24
lang: sv
translation_id: padrao-dao-java
permalink: /sv/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object skiljer persistens från affärsregler och presentation.
---

En klass kan öppna anslutningar, köra SQL, tillämpa affärsregler och visa resultat. När programmet växer blir en sådan samling av ansvar svår att underhålla. Kapitlet ”Utöka klasser: dataåtkomst” använder DAO-mönstret (*Data Access Object*) för att ge persistens ett eget ansvar.

Ett DAO erbjuder metoder för att lägga till, söka, ändra och ta bort objekt. Klienten behöver inte känna till SQL, anslutningsuppgifter eller hur databasrader blir objekt. I exemplet representerar `Student` data, `StudentDAO` hanterar tabellen `student` och `DBExample` anropar operationerna.

Boken visar först ett DAO för studenter och flyttar sedan gemensam infrastruktur till `AbstractDAO<T>` med arv och generiska typer. Klientens anrop kan vara desamma trots att implementationen ändras. JDBC används direkt så att ansvarsfördelningen syns.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/sv/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [Klassen Student i DAO-exemplet](/sv/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/sv/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [Ett record för JDBC-anslutningsuppgifter](/sv/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/sv/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [Skapa StudentDAO med CRUD-operationer](/sv/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Relaterade artiklar

{{ dao_related_links }}

{% endif %}

På engelska: [Engelsk version](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
