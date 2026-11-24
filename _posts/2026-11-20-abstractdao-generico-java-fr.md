---
layout: post
title: "AbstractDAO : une superclasse générique d'accès aux données"
date: 2026-11-24
lang: fr
translation_id: abstractdao-generico-java
permalink: /fr/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T> partage la connexion, l'exécution et les requêtes entre les DAO concrets.
---

Si plusieurs entités possèdent chacune leur DAO, l'ouverture des connexions et le traitement des résultats se répètent. Le chapitre rassemble ce mécanisme dans `AbstractDAO<T>`. Le paramètre `T` désigne le type choisi par une sous-classe concrète.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="Hiérarchie de classes du livre avec AbstractDAO, StudentDAO, Student et ConnectionData ; les libellés suivent le code anglais." style="width: 100%; height: auto; display: block;">
  <figcaption>Hiérarchie de classes du livre avec AbstractDAO, StudentDAO, Student et ConnectionData ; les libellés suivent le code anglais.</figcaption>
</figure>

Les importations sont :

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

L'implémentation complète, avec identifiants anglais, est :

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

`open()` obtient une connexion à l'aide de `ConnectionData`. `execute()` reçoit du SQL et une liste de paramètres ; il utilise `setObject` parce que la superclasse ignore leurs types concrets. `query()` parcourt le `ResultSet` et rassemble des objets en appelant `map(rs)` pour chaque ligne.

`map`, `insert`, `update`, `delete` et `findAll` sont abstraites : le DAO concret doit les définir. Les ressources sont déclarées dans des blocs try-with-resources et les blocs `catch` de l'exemple affichent la trace des erreurs SQL.

<!-- DAO_RELATIONS_START -->
## Articles associés

{% assign related_posts = site.posts | where: "url", "/fr/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [Créer StudentDAO avec les opérations CRUD](/fr/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/fr/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [Un record pour les données de connexion JDBC](/fr/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/fr/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [StudentDAO hérite de AbstractDAO<Student>](/fr/studentdao-extending-abstractdao-student/){% endif %}

En anglais: [Version anglaise](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
