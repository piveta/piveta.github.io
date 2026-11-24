---
layout: post
title: "JDBC로 Java와 PostgreSQL 연결하기"
date: 2026-11-24
lang: ko
translation_id: conectando-postgresql-jdbc-java
permalink: /ko/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager로 academic에 연결한 뒤 SQL 작업을 수행합니다.
---

JDBC는 Java 프로그램을 관계형 데이터베이스에 연결합니다. `DriverManager.getConnection`은 PostgreSQL URL, 사용자 이름, 비밀번호를 받아 `Connection`을 반환합니다. `academic`와 `student(enrollment_number, name)`을 미리 만들고 PostgreSQL JDBC 드라이버를 프로젝트에 추가해야 합니다.

아래는 영어판 전체 프로그램입니다. 학생을 삽입하고 조회하고 수정하고 삭제합니다. 예제의 사용자 이름과 비밀번호는 `postgres`로 고정되어 있으므로 로컬 설치에서도 이 인증 정보를 사용할 수 있어야 합니다.

```java
public class DBExample {
    public static void main(String[] args) 
        throws SQLException {
        var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academic", 
            "postgres", "postgres");
     
        IO.println("Inserting students...");
        var p = c.prepareStatement("insert into student " + 
                "(enrollment_number, name) values (?, ?)");
        p.setInt(1, 1);
        p.setString(2, "Maria");
        p.execute();
        p.setInt(1, 2);
        p.setString(2, "Pedro");
        p.execute();
        p.setInt(1, 3);
        p.setString(2, "João");
        p.execute();

        IO.println("Listing students...");
        var s = c.createStatement();      
        var rs = s.executeQuery(
          "select * from student order by enrollment_number");
        while (rs.next()) 
            IO.println(rs.getInt("enrollment_number") + " - " + 
                rs.getString("name"));

        IO.println("Updating a student...");
        p = c.prepareStatement(
          "update student set name = ? where enrollment_number = ?");
        p.setInt(2, 1);
        p.setString(1, "Maria da Silva");
        p.execute();

        IO.println("Listing students...");
        rs = s.executeQuery(
          "select * from student order by enrollment_number");
        while (rs.next()) 
            IO.println(rs.getInt("enrollment_number") + " - " +
                rs.getString("name"));

        IO.println("Deleting all students...");
        s.executeUpdate("delete from student");
        rs.close();
        s.close();
        p.close();
        c.close();
    }
}
```

URL에서 `localhost`는 서버, `5432`는 포트, `academic`는 데이터베이스 이름입니다. `main`은 `throws SQLException`을 선언해 JDBC 오류를 전파합니다. 정상 흐름의 끝에서는 `close()`를 명시적으로 호출하여 자원을 닫습니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
