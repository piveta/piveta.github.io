---
layout: post
title: "Java 데이터 접근을 위한 DAO 패턴"
date: 2026-11-24
lang: ko
translation_id: padrao-dao-java
permalink: /ko/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object는 영속성 처리를 비즈니스 규칙과 화면 표시에서 분리합니다.
---

한 클래스에서 연결을 열고 SQL을 실행하며 비즈니스 규칙을 적용하고 결과를 보여 줄 수 있습니다. 하지만 시스템이 커질수록 이런 집중은 유지보수를 어렵게 합니다. 「클래스 확장: 데이터 접근」 장은 DAO(*Data Access Object*) 패턴으로 영속성 책임을 분리합니다.

DAO는 객체의 삽입, 검색, 수정, 삭제 기능을 제공합니다. 클라이언트는 SQL 문장, 연결 방법, 데이터베이스 행을 객체로 바꾸는 방법을 알 필요가 없습니다. 예제에서 `Student`는 데이터를 나타내고, `StudentDAO`는 `student` 테이블을 관리하며, `DBExample`은 작업을 요청합니다.

책은 먼저 학생 전용 DAO를 만들고, 이어서 상속과 제네릭을 사용해 공통 부분을 `AbstractDAO<T>`로 옮깁니다. 내부 구현이 달라져도 클라이언트가 호출하는 메서드는 같습니다. JDBC를 직접 사용하여 각 책임을 분명히 보여 줍니다.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/ko/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [DAO 예제의 Student 클래스](/ko/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/ko/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [JDBC 연결 데이터를 담는 record](/ko/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/ko/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [CRUD 작업을 수행하는 StudentDAO 만들기](/ko/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## 관련 글

{{ dao_related_links }}

{% endif %}

영어판: [영어 기사](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
