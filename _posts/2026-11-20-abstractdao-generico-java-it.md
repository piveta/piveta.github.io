---
layout: post
title: "AbstractDAO come superclasse generica di accesso ai dati"
date: 2026-11-24
lang: it
translation_id: abstractdao-generico-java
permalink: /it/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T> condivide connessione, esecuzione e query tra i DAO concreti.
---

Quando più entità hanno DAO distinti, l'apertura delle connessioni e la lettura dei risultati vengono spesso duplicate. Il capitolo riunisce queste attività in `AbstractDAO<T>`. Il parametro `T` rappresenta il tipo scelto da una sottoclasse concreta.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="Gerarchia delle classi del libro con AbstractDAO, StudentDAO, Student e ConnectionData; le etichette seguono il codice inglese." style="width: 100%; height: auto; display: block;">
  <figcaption>Gerarchia delle classi del libro con AbstractDAO, StudentDAO, Student e ConnectionData; le etichette seguono il codice inglese.</figcaption>
</figure>

Gli import sono:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

L'implementazione completa, con identificatori in inglese, è:

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

`open()` ottiene la connessione tramite `ConnectionData`. `execute()` riceve SQL e parametri e usa `setObject` perché la superclasse non conosce i tipi concreti. `query()` percorre il `ResultSet` e raccoglie oggetti chiamando `map(rs)` per ogni riga.

`map`, `insert`, `update`, `delete` e `findAll` sono astratti: il DAO concreto deve definirli. Le risorse sono dichiarate in try-with-resources e i blocchi `catch` dell'esempio mostrano gli errori SQL con uno stack trace.

<!-- DAO_RELATIONS_START -->
## Articoli correlati

{% assign related_posts = site.posts | where: "url", "/it/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [Creare StudentDAO con operazioni CRUD](/it/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/it/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [Un record per i dati di connessione JDBC](/it/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/it/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [StudentDAO eredita da AbstractDAO<Student>](/it/studentdao-extending-abstractdao-student/){% endif %}

In inglese: [Versione inglese](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
