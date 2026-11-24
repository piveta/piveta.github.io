---
layout: post
title: "Java의 finally 블록"
date: 2026-11-18
lang: ko
translation_id: bloco-finally-java
permalink: /ko/finally-block-in-java/
share_text: >-
  finally 블록은 try와 catch 이후 작업이 실패해도 실행됩니다. JDBC 예제를 통해 ResultSet, Statement, Connection을 직접 닫을 때의 주의점을 설명합니다.
---

`try` 문에는 **`finally` 블록**이라는 마무리 블록을 붙일 수 있습니다. `try` 블록의 코드가 정상적으로 끝났는지와 관계없이 실행됩니다. 다음 예제의 `finally` 블록(25행부터)은 `try` 블록에서 연 `ResultSet`, `Statement`, 연결(`Connection`)을 닫습니다.

```java
import java.sql.*; 

public class DBExample {
    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        ResultSet rs = null;
        try {
            c = DriverManager.getConnection(
               "jdbc:postgresql://localhost:5432/academic",
               "postgres", "postgres");

            IO.println("Listing students...");
            s = c.createStatement();
            rs = s.executeQuery(
               "select * from student order by enrollment_number");
            while (rs.next())
                IO.println(rs.getInt("enrollment_number") + " - " +
                           rs.getString("name"));
        } catch (SQLException e) {
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage()); 
            IO.println("SQLState: " + e.getSQLState()); 
            IO.println("Error: " + e.getErrorCode()); 
        } finally { 
            rs.close(); // Closes the ResultSet
            s.close();  // Closes the Statement
            c.close();  // Closes the Connection
        }
    }
}
```

하지만 `ResultSet`, `Statement`, `Connection`의 `close` 메서드도 `SQLException`을 던질 수 있습니다. 따라서 앞의 예제는 컴파일되지 않습니다. 이 예외를 처리하거나 처리하지 않겠다고 선언해야 합니다. 호출마다 다른 처리가 필요하면 각각 중첩된 `try` 문을 사용하고, 세 호출을 하나의 문으로 처리할 수도 있습니다.

```java
import java.sql.*; 

public class DBExample {
    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        ResultSet rs = null;
        try {
            // Remaining code omitted
        } catch (SQLException e){
            // TODO Handle SQL exceptions
        } 
        finally {
            try {
                rs.close(); 
            } catch (SQLException e) {
                // Ignore or log the exception
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
            try {
                s.close(); 
            } catch (SQLException e) {
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
            try {
                c.close(); 
            } catch (SQLException e) {
                System.err.println("Error while closing: "
                        + e.getMessage());
            }
        }
    }
}
```

이 코드에서도 `rs`, `s`, `c` 중 하나가 `null`이면 각각 15, 22, 28행에서 비검사 예외인 `NullPointerException`이 발생할 수 있습니다. 보통 비검사 예외를 단순히 포착하기보다 문제의 원인을 수정합니다.

따라서 `close`를 호출하기 전에 각 변수가 `null`인지 검사할 수 있습니다. 다음 예제에서는 4, 12, 20행에서 검사합니다.

```java
    // Code omitted - same as the previous listing...
    finally {
        try {
            if (rs != null) 
                rs.close(); // Closes the ResultSet
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
        try {
            if (s != null) 
                s.close();  // Closes the Statement
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
        try {
            if (c != null) 
                c.close();  // Closes the Connection
        } catch(SQLException e){
            // Ignore or log the exception
            System.err.println("Error while closing: " 
               + e.getMessage());
        }
    }
```

이렇게 해도 첫 `try` 블록의 문이 `SQLException`을 던지고 이후 `close` 메서드 중 하나가 실패하여 새 `SQLException`을 던지면 원래 예외의 정보가 사라질 수 있습니다. `Throwable`의 `addSuppressed`, `getSuppressed` 등을 이용해 원래 예외를 유지하고 `close`에서 발생한 예외를 억제된 예외로 추가할 수 있습니다. 하지만 코드가 더 복잡해집니다.

이런 장황함과 리소스 처리의 어려움을 줄이기 위해 Java에는 문이 끝날 때 닫을 리소스를 지정하는 `try` 문의 변형이 추가되었습니다. 정상 종료 여부와 관계없이 리소스를 닫습니다. 이를 **리소스 포함 `try` 문**이라고 합니다(참고: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*이 글은 Eduardo Kessler Piveta의 책 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
