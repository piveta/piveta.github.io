---
layout: post
title: "JavaのデータアクセスにおけるDAOパターン"
date: 2026-11-24
lang: ja
translation_id: padrao-dao-java
permalink: /ja/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Objectは永続化を業務ロジックや表示処理から分離します。
---

一つのクラスで接続の作成、SQLの実行、業務規則の適用、結果の表示をすべて行うことはできます。しかし規模が大きくなると、変更箇所が分かりにくくなります。「クラスの拡張：データアクセス」の章では、DAO（*Data Access Object*）パターンを使って永続化の責務を分けます。

DAOはオブジェクトの追加、検索、更新、削除を提供します。利用側はSQL文、接続方法、データベースの行をオブジェクトへ変換する方法を知る必要がありません。例では`Student`がデータを表し、`StudentDAO`が`student`表を扱い、`DBExample`が操作を呼び出します。

書籍は最初に学生専用のDAOを示し、その後、継承とジェネリクスで共通部分を`AbstractDAO<T>`へ移します。内部構造が変わっても利用側の呼び出しは維持されます。JDBCを直接使うことで、それぞれの責務が確認できます。

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/ja/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [DAOの例で使うStudentクラス](/ja/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/ja/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [JDBC接続情報をまとめるrecord](/ja/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/ja/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [CRUD操作を持つStudentDAOを作る](/ja/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## 関連記事

{{ dao_related_links }}

{% endif %}

英語版: [英語の記事](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
