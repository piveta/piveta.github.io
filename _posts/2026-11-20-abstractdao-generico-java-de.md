---
layout: post
title: "AbstractDAO als generische Datenzugriffs-Superklasse"
date: 2026-11-24
lang: de
translation_id: abstractdao-generico-java
permalink: /de/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T> teilt Verbindungs-, Ausführungs- und Abfragelogik mit konkreten DAOs.
---

Für mehrere Entitätstypen würden getrennte DAOs häufig dieselbe Verbindungs- und Abfragelogik wiederholen. Das Kapitel führt diese Aufgaben in `AbstractDAO<T>` zusammen. Der Typparameter `T` steht für den Typ, den eine konkrete Unterklasse festlegt.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="Klassenhierarchie aus dem Buch mit AbstractDAO, StudentDAO, Student und ConnectionData; die Beschriftungen entsprechen dem englischen Code." style="width: 100%; height: auto; display: block;">
  <figcaption>Klassenhierarchie aus dem Buch mit AbstractDAO, StudentDAO, Student und ConnectionData; die Beschriftungen entsprechen dem englischen Code.</figcaption>
</figure>

Die verwendeten Importe sind:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

Die vollständige, mit englischen Bezeichnern angepasste Implementierung lautet:

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

`open()` verbindet sich über `ConnectionData`. `execute()` nimmt SQL und Parameter entgegen und setzt deren Werte mit `setObject`, weil die Superklasse die konkreten Typen nicht kennt. `query()` durchläuft das `ResultSet` und erzeugt für jede Zeile über `map(rs)` ein Objekt vom Typ `T`.

`map`, `insert`, `update`, `delete` und `findAll` sind abstrakt und müssen im konkreten DAO ergänzt werden. Die Ressourcen stehen in Try-with-resources-Blöcken; die `catch`-Blöcke geben SQL-Fehler als Stacktrace aus.

<!-- DAO_RELATIONS_START -->
## Verwandte Artikel

{% assign related_posts = site.posts | where: "url", "/de/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [StudentDAO mit CRUD-Operationen erstellen](/de/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/de/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [Ein record für JDBC-Verbindungsdaten](/de/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/de/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [StudentDAO erbt von AbstractDAO<Student>](/de/studentdao-extending-abstractdao-student/){% endif %}

Auf Englisch: [Englische Fassung](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*Dieser Artikel beruht auf Inhalten des Buches [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) von Eduardo Kessler Piveta.*
