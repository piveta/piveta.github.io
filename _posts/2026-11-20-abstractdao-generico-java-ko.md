---
layout: post
title: "공통 데이터 접근 상위 클래스 AbstractDAO"
date: 2026-11-24
lang: ko
translation_id: abstractdao-generico-java
permalink: /ko/abstractdao-a-generic-data-access-superclass/
image: /images/dao/diagrama-abstractdao-en.png
share_text: >-
  AbstractDAO<T>는 연결, 명령 실행, 조회 기능을 여러 DAO에서 공유합니다.
---

엔터티마다 DAO를 만들면 연결 열기와 결과 읽기 코드가 반복됩니다. 이 장은 공통 처리 기능을 `AbstractDAO<T>`에 모읍니다. 타입 매개변수 `T`는 구체적인 하위 클래스가 다루는 객체의 타입입니다.

<figure style="max-width: 540px; margin: 1.5rem auto;">
  <img src="/images/dao/diagrama-abstractdao-en.png" alt="책의 AbstractDAO, StudentDAO, Student, ConnectionData 클래스 계층 다이어그램입니다. 레이블은 영어 코드와 일치합니다." style="width: 100%; height: auto; display: block;">
  <figcaption>책의 AbstractDAO, StudentDAO, Student, ConnectionData 클래스 계층 다이어그램입니다. 레이블은 영어 코드와 일치합니다.</figcaption>
</figure>

책에서 사용하는 import입니다.

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
```

식별자를 영어로 맞춘 전체 구현입니다.

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

`open()`은 `ConnectionData`를 이용해 연결합니다. `execute()`는 SQL과 매개변수를 받아, 상위 클래스가 구체적 타입을 모르므로 `setObject`로 값을 설정합니다. `query()`는 `ResultSet`을 순회하고 각 행에 `map(rs)`를 호출해 `T` 객체를 모읍니다.

`map`, `insert`, `update`, `delete`, `findAll`은 추상 메서드이며 구체 DAO가 구현합니다. 자원은 try-with-resources에서 관리하고, 예제의 `catch`는 SQL 오류의 스택 추적을 출력합니다.

<!-- DAO_RELATIONS_START -->
## 관련 글

{% assign related_posts = site.posts | where: "url", "/ko/building-studentdao-with-crud-operations/" %}{% if related_posts.size > 0 %}- [CRUD 작업을 수행하는 StudentDAO 만들기](/ko/building-studentdao-with-crud-operations/){% endif %}
{% assign related_posts = site.posts | where: "url", "/ko/a-record-for-jdbc-connection-data/" %}{% if related_posts.size > 0 %}- [JDBC 연결 데이터를 담는 record](/ko/a-record-for-jdbc-connection-data/){% endif %}
{% assign related_posts = site.posts | where: "url", "/ko/studentdao-extending-abstractdao-student/" %}{% if related_posts.size > 0 %}- [AbstractDAO<Student>를 상속하는 StudentDAO](/ko/studentdao-extending-abstractdao-student/){% endif %}

영어판: [영어 기사](/en/abstractdao-a-generic-data-access-superclass/).
<!-- DAO_RELATIONS_END -->

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
