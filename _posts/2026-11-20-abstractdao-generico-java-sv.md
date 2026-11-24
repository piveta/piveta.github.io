---
layout: post
title: "AbstractDAO som generisk superklass för dataåtkomst"
date: 2026-11-24
lang: sv
translation_id: abstractdao-generico-java
permalink: /sv/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T> delar anslutnings-, exekverings- och frågelogik mellan konkreta DAO:n.
---

Om flera entiteter har egna DAO:n upprepas ofta kod för anslutningar och resultat. Kapitlet samlar denna mekanism i `AbstractDAO<T>`. Typparametern `T` är den objekttyp som en konkret subklass väljer.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="Klasshierarki från boken med AbstractDAO, StudentDAO, Student och ConnectionData; etiketterna följer den engelska koden." style="width: 100%; height: auto; display: block;">
  <figcaption>Klasshierarki från boken med AbstractDAO, StudentDAO, Student och ConnectionData; etiketterna följer den engelska koden.</figcaption>
</figure>

Importer som används:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

Den fullständiga implementationen med engelska identifierare:

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

`open()` skapar en anslutning via `ConnectionData`. `execute()` tar emot SQL och parametrar och använder `setObject` eftersom superklassen inte känner deras konkreta typer. `query()` går igenom `ResultSet` och anropar `map(rs)` för varje rad för att samla objekt av typen `T`.

`map`, `insert`, `update`, `delete` och `findAll` är abstrakta och måste definieras av ett konkret DAO. Resurserna ligger i try-with-resources och exemplets `catch`-block skriver ut stackspår för SQL-fel.

<!-- DAO_RELATIONS_START -->
## Relaterade artiklar

{% assign related_posts = site.posts | where: "url", "/sv/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [Skapa StudentDAO med CRUD-operationer](/sv/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/sv/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [Ett record för JDBC-anslutningsuppgifter](/sv/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/sv/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [StudentDAO ärver från AbstractDAO<Student>](/sv/studentdao-extending-abstractdao-student/){% endif %}

På engelska: [Engelsk version](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
