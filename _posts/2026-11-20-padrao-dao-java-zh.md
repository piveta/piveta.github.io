---
layout: post
title: "Java数据访问中的DAO模式"
date: 2026-11-20
lang: zh
translation_id: padrao-dao-java
permalink: /zh/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object将持久化与业务规则、界面展示分开。
---

一个类可以同时建立连接、执行SQL、应用业务规则并显示结果，但系统变大后，这种集中方式会增加维护难度。“扩展类：数据访问”一章使用DAO（*Data Access Object*）模式，将持久化划分为独立职责。

DAO提供对象的插入、查询、更新和删除操作。客户端无需了解SQL语句、连接方式或如何把数据库行转换成对象。在示例中，`Student`表示数据，`StudentDAO`管理`student`表，`DBExample`调用这些操作并显示结果。

书中先实现学生专用DAO，再通过继承和泛型将公共部分移入`AbstractDAO<T>`。内部结构变化时，客户端的公开调用仍可保持不变。直接使用JDBC有助于看清各部分的职责。

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/zh/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [DAO示例中的Student类](/zh/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/zh/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [使用record保存JDBC连接数据](/zh/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/zh/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [创建具有CRUD操作的StudentDAO](/zh/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## 相关文章

{{ dao_related_links }}

{% endif %}

英文版: [英文文章](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*本文改编自 Eduardo Kessler Piveta 所著的 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)。*
