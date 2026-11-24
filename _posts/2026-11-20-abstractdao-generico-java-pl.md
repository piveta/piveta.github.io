---
layout: post
title: "AbstractDAO jako generyczna nadklasa dostępu do danych"
date: 2026-11-24
lang: pl
translation_id: abstractdao-generico-java
permalink: /pl/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T> współdzieli połączenia, wykonywanie poleceń i zapytania między DAO.
---

Osobne DAO dla wielu encji często powielają kod tworzenia połączeń i czytania wyników. Rozdział zbiera te mechanizmy w `AbstractDAO<T>`. Parametr typu `T` oznacza typ obiektu wybrany przez konkretną podklasę.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="Hierarchia klas z książki przedstawiająca AbstractDAO, StudentDAO, Student i ConnectionData; etykiety odpowiadają kodowi angielskiemu." style="width: 100%; height: auto; display: block;">
  <figcaption>Hierarchia klas z książki przedstawiająca AbstractDAO, StudentDAO, Student i ConnectionData; etykiety odpowiadają kodowi angielskiemu.</figcaption>
</figure>

Użyte importy:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

Pełna implementacja z angielskimi identyfikatorami:

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

`open()` uzyskuje połączenie przez `ConnectionData`. `execute()` przyjmuje SQL i listę parametrów, używając `setObject`, bo nadklasa nie zna ich konkretnych typów. `query()` przechodzi przez `ResultSet` i wywołuje `map(rs)` dla każdego wiersza, zbierając obiekty typu `T`.

`map`, `insert`, `update`, `delete` i `findAll` są abstrakcyjne i muszą zostać zdefiniowane w konkretnym DAO. Zasoby są obsługiwane przez try-with-resources, a przykładowe bloki `catch` wypisują ślad błędów SQL.

<!-- DAO_RELATIONS_START -->
## Powiązane artykuły

{% assign related_posts = site.posts | where: "url", "/pl/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [Tworzenie StudentDAO z operacjami CRUD](/pl/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/pl/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [Record z danymi połączenia JDBC](/pl/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/pl/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [StudentDAO dziedziczy po AbstractDAO<Student>](/pl/studentdao-extending-abstractdao-student/){% endif %}

Po angielsku: [Wersja angielska](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*Ten artykuł powstał na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) napisanej przez Eduardo Kessler Piveta.*
