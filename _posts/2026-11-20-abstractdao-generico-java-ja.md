---
layout: post
title: "汎用データアクセス基底クラスAbstractDAO"
date: 2026-11-24
lang: ja
translation_id: abstractdao-generico-java
permalink: /ja/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T>が接続、コマンド実行、問い合わせの共通処理をまとめます。
---

エンティティごとにDAOを作ると、接続や結果の読み取りが重複しがちです。この章は共通処理を`AbstractDAO<T>`にまとめます。型引数`T`は具象サブクラスが扱うオブジェクトの型です。

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="書籍のAbstractDAO、StudentDAO、Student、ConnectionDataのクラス階層図。ラベルは英語版コードに合わせています。" style="width: 100%; height: auto; display: block;">
  <figcaption>書籍のAbstractDAO、StudentDAO、Student、ConnectionDataのクラス階層図。ラベルは英語版コードに合わせています。</figcaption>
</figure>

書籍で使用するimportです。

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

識別子を英語に合わせた実装全体です。

```java
public abstract class AbstractDAO<T>{
    public Connection open() throws SQLException{ 
        var data = new ConnectionData();
        return DriverManager.getConnection(
            data.server(), data.user(), data.password());
    }
    
    public void execute(String sql,
                         List<Object> parameters){
       try (var connection = open(); 
            var ps = connection.prepareStatement(sql)){
            int count = 1;
            for (Object p : parameters) 
                ps.setObject(count++, p); 
                ps.execute(); 
        } catch (SQLException e){
            e.printStackTrace();
        }
    } 

    public Collection<T> query(String sql){ 
        var result = new ArrayList<T>();
        try (var connection = open(); 
             var s = connection.createStatement(); 
             var rs = s.executeQuery(sql)){
            while (rs.next())
                result.add(map(rs));
        } catch (SQLException e){
            e.printStackTrace();
        }
        return result;
    } 
		
    public abstract void insert(T t);
    public abstract void update(T t);
    public abstract void delete(T t);
    public abstract Collection<T> findAll();
    protected abstract T map(ResultSet rs);
}    
```

`open()`は`ConnectionData`を使って接続します。`execute()`はSQLとパラメーターを受け取り、具象型が分からないため`setObject`で値を設定します。`query()`は`ResultSet`をたどり、各行に`map(rs)`を適用して`T`型のオブジェクトを集めます。

`map`、`insert`、`update`、`delete`、`findAll`は抽象メソッドで、具象DAOが実装します。リソースはtry-with-resourcesで管理し、例の`catch`はSQLエラーのスタックトレースを表示します。

<!-- DAO_RELATIONS_START -->
## 関連記事

{% assign related_posts = site.posts | where: "url", "/ja/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [CRUD操作を持つStudentDAOを作る](/ja/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/ja/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [JDBC接続情報をまとめるrecord](/ja/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/ja/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [AbstractDAO<Student>を継承するStudentDAO](/ja/studentdao-extending-abstractdao-student/){% endif %}

英語版: [英語の記事](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*この記事は Eduardo Kessler Piveta 著 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) の内容を基にしています。*
