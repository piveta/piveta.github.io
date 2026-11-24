---
layout: post
title: "AbstractDAO sebagai superclass generik akses data"
date: 2026-11-24
lang: id
translation_id: abstractdao-generico-java
permalink: /id/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T> berbagi logika koneksi, eksekusi perintah, dan kueri antar-DAO.
---

DAO terpisah untuk banyak entitas sering menggandakan kode pembukaan koneksi dan pembacaan hasil. Bab ini mengumpulkan mekanisme bersama dalam `AbstractDAO<T>`. Parameter tipe `T` adalah tipe objek yang dipilih subclass konkret.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="Hierarki kelas dari buku yang memuat AbstractDAO, StudentDAO, Student, dan ConnectionData; label mengikuti kode bahasa Inggris." style="width: 100%; height: auto; display: block;">
  <figcaption>Hierarki kelas dari buku yang memuat AbstractDAO, StudentDAO, Student, dan ConnectionData; label mengikuti kode bahasa Inggris.</figcaption>
</figure>

Import yang digunakan adalah:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

Implementasi lengkap dengan pengenal bahasa Inggris adalah:

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

`open()` membuka koneksi melalui `ConnectionData`. `execute()` menerima SQL dan parameter serta memakai `setObject` karena superclass belum mengetahui tipe konkretnya. `query()` menelusuri `ResultSet` dan memanggil `map(rs)` pada setiap baris untuk mengumpulkan objek bertipe `T`.

`map`, `insert`, `update`, `delete`, dan `findAll` bersifat abstrak dan harus didefinisikan DAO konkret. Sumber daya dikelola oleh try-with-resources; blok `catch` contoh mencetak stack trace kesalahan SQL.

<!-- DAO_RELATIONS_START -->
## Artikel terkait

{% assign related_posts = site.posts | where: "url", "/id/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [Membuat StudentDAO dengan operasi CRUD](/id/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/id/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [Record untuk data koneksi JDBC](/id/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/id/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [StudentDAO mewarisi AbstractDAO<Student>](/id/studentdao-extending-abstractdao-student/){% endif %}

Dalam bahasa Inggris: [Versi bahasa Inggris](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
