---
layout: post
title: "AbstractDAO: una superclase genérica de acceso a datos"
date: 2026-11-24
lang: es
translation_id: abstractdao-generico-java
permalink: /es/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T> comparte la conexión, la ejecución y las consultas; las subclases completan los detalles.
---

Si cada entidad tiene su propio DAO, repetir la apertura de conexiones, la creación de sentencias y el recorrido de resultados produce código duplicado. El capítulo reúne ese mecanismo en `AbstractDAO<T>`. El parámetro `T` representa el tipo elegido por una subclase concreta.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="Jerarquía de clases del libro con AbstractDAO, StudentDAO, Student y ConnectionData; las etiquetas siguen el código en inglés." style="width: 100%; height: auto; display: block;">
  <figcaption>Jerarquía de clases del libro con AbstractDAO, StudentDAO, Student y ConnectionData; las etiquetas siguen el código en inglés.</figcaption>
</figure>

El libro utiliza estas importaciones:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

Su implementación completa, con identificadores traducidos al inglés, es:

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

`open()` obtiene una conexión mediante `ConnectionData`. `execute()` recibe SQL y parámetros, prepara una sentencia y usa `setObject` porque la superclase no conoce de antemano los tipos concretos. `query()` recorre el `ResultSet` y reúne objetos llamando a `map(rs)` para cada fila.

`map`, `insert`, `update`, `delete` y `findAll` son abstractos: el DAO concreto debe definirlos. Los recursos se declaran en try-with-resources y los bloques `catch` del ejemplo imprimen los errores SQL.

<!-- DAO_RELATIONS_START -->
## Artículos relacionados

{% assign related_posts = site.posts | where: "url", "/es/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [Crear StudentDAO con operaciones CRUD](/es/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/es/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [Un record para la conexión JDBC](/es/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/es/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [StudentDAO hereda de AbstractDAO<Student>](/es/studentdao-extending-abstractdao-student/){% endif %}

En inglés: [Versión en inglés](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*Este artículo adapta contenido del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), de Eduardo Kessler Piveta.*
