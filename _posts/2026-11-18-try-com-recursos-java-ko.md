---
layout: post
title: "Java의 리소스 포함 try 문"
date: 2026-11-18
lang: ko
translation_id: try-com-recursos-java
permalink: /ko/try-with-resources-in-java/
share_text: >-
  리소스 포함 try 문은 AutoCloseable 객체를 자동으로 닫습니다. JDBC 연결, 문, 결과 집합을 하나의 try 문에서 관리하는 예를 보여 줍니다.
---

리소스 관리를 개선하기 위해 Java 7부터는 `try` 문이 끝날 때 닫을 수 있는 리소스를 그 문 안에 지정할 수 있습니다. 언어 명세에 따르면 `try` 문에는 `AutoCloseable` 인터페이스를 구현하는 리소스를 하나 이상 지정할 수 있습니다. 문서에 따르면 표준 라이브러리의 100개가 넘는 클래스가 이 인터페이스를 구현합니다. 정의는 다음과 같습니다.

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

리소스 포함 `try` 문의 문법은 다음과 같습니다.

```text
TryWithResourcesStatement:
    try ResourceSpecification Block [Catches] [Finally]
ResourceSpecification:
    ( ResourceList [;] )
ResourceList:
    Resource {; Resource}
Resource:
    LocalVariableDeclaration
    VariableAccess
VariableAccess:
    ExpressionName
    FieldAccess
```

리소스는 괄호 안에 지정하며, 보통 지역 변수 선언이나 이미 확실히 할당되었고 사실상 final인 변수에 대한 접근을 사용합니다(다시 할당하지 않은 변수이며, `final` 한정자는 필수가 아닙니다). JDBC 질의에서는 연결, 문, 결과 집합을 닫아야 합니다. 다음 예는 `c`(5행), `s`(8행), `rs`(9행)의 선언과 초기화를 `try` 문의 리소스 지정 부분에 배치합니다.

```java
import java.sql.*;

public class DBExample {
    public static void main(String[] args) {
        try (var c = DriverManager.getConnection(
              "jdbc:postgresql://localhost:5432/academic",
              "postgres", "postgres");
             var s = c.createStatement();
             var rs = s.executeQuery(
              "select * from student order by enrollment_number");){
            IO.println("Listing students...");
            while (rs.next())
                IO.println(rs.getInt("enrollment_number") + " - " +
                           rs.getString("name"));
        } catch (SQLException e){
            // TODO Handle SQL exceptions
        }
    }
}
```

이렇게 하면 `finally` 블록이 필요하지 않습니다. 지정한 리소스는 Java 실행 환경이 모두 자동으로 닫습니다. 코드가 단순해지고 리소스를 닫는 일을 잊을 가능성이 줄어들므로, 리소스를 다루는 코드에 권장되는 방식입니다.

---

*이 글은 Eduardo Kessler Piveta의 책 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
