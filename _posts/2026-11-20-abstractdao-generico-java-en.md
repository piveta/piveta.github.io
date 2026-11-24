---
layout: post
title: "AbstractDAO: A Generic Data Access Superclass"
date: 2026-11-24
lang: en
translation_id: abstractdao-generico-java
permalink: /en/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T> shares connection, command execution, and query logic while subclasses supply entity-specific behavior.
---

<!-- DAO_CONTEXT_START -->
**Context:** The superclass generalizes the infrastructure of the {% assign introductory_dao = site.posts | where: "url", "/en/building-studentdao-with-crud-operations/" %}{% if introductory_dao.size > 0 %}[first StudentDAO implementation](/en/building-studentdao-with-crud-operations/){% else %}first StudentDAO implementation{% endif %}.
<!-- DAO_CONTEXT_END -->

When an application persists several kinds of entity, copying connection setup, statement creation, and result traversal into every DAO repeats the same logic. The chapter uses inheritance, abstract classes, and generics to put that work in `AbstractDAO<T>`. The type parameter `T` represents the object type chosen by a concrete subclass.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="Book UML diagram showing AbstractDAO, StudentDAO, Student and ConnectionData" style="width: 100%; height: auto; display: block;">
  <figcaption>The book's generic DAO class hierarchy, with labels adapted to the English example.</figcaption>
</figure>

The book uses these imports:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

The complete implementation, with identifiers and comments adapted to English, is:

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

`open()` obtains a connection using the `ConnectionData` record: URL `jdbc:postgresql://localhost:5432/academic`, username `postgres`, and password `postgres`. `execute()` receives SQL and a list of parameters, prepares a statement, and calls `setObject` for each parameter because the superclass does not know its concrete types in advance.

`query()` runs a SQL query, traverses its `ResultSet`, and collects objects. For every row, it calls `map(rs)` to create a `T`. That method is abstract: only the subclass knows how to build its entity from a row.

`insert`, `update`, `delete`, and `findAll` are abstract as well. The superclass provides the shared infrastructure, while a concrete DAO supplies the entity-specific operations and mapping. Resources are declared in try-with-resources blocks; the example's `catch` blocks print SQL error stack traces.

<!-- DAO_RELATIONS_START -->
## Related articles

{% assign related_posts = site.posts | where: "url", "/en/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [Building StudentDAO with CRUD Operations](/en/building-studentdao-with-crud-operations/) — initial DAO implementation.{% endif %}
{% assign related_posts = site.posts | where: "url", "/en/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [A Record for JDBC Connection Data](/en/a-record-for-jdbc-connection-data/) — JDBC connection values.{% endif %}
{% assign related_posts = site.posts | where: "url", "/en/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [StudentDAO Extending AbstractDAO<Student>](/en/studentdao-extending-abstractdao-student/) — DAO after inheritance.{% endif %}

Other language: [Portuguese version](/abstractdao-generico-java/).
<!-- DAO_RELATIONS_END -->

---

*This article adapts content from the book [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), by Eduardo Kessler Piveta.*
