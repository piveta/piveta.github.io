---
layout: post
title: "Java에서 예외 포착하고 처리하기"
date: 2026-11-24
lang: ko
translation_id: capturando-tratando-excecoes-java
permalink: /ko/catching-and-handling-exceptions-in-java/
share_text: >-
  Java의 try 블록과 catch 절을 이용한 예외 처리를 설명합니다. JDBC 예제로 SQLException, 다중 포착, 타입별 처리를 보여 줍니다.
---

예외가 발생하면(오류이든 예상한 정상 흐름에서 벗어난 상황이든), 발생 지점의 메서드는 예외 클래스의 객체를 만들어 관련 정보와 함께 실행 시스템인 JVM에 전달합니다.

JVM은 호출 스택에서 그 객체와 호환되는 예외 처리기를 찾습니다. 먼저 예외가 발생한 메서드를 확인합니다. 적절한 처리기가 있으면 그곳에서 처리합니다. 없으면 호출한 메서드를 확인합니다. 처리기를 찾거나 최초 호출자에 도달할 때까지 스택을 거슬러 올라갑니다. 어느 메서드도 예외를 처리하지 않으면 JVM은 프로그램을 종료하고 오류 메시지와 예외에 이른 스택 추적을 출력합니다.

검사 예외를 던질 수 있는 Java 코드에는 **포착하거나 선언하기** 요구 사항이 적용됩니다.

- 예외를 던질 수 있는 문을 적절한 처리기(`catch` 절)가 있는 보호 블록(`try` 블록)으로 감싸거나,
- 해당 문을 포함한 메서드가 `throws`를 사용해 예외를 던질 수 있음을 선언해야 합니다. 이 메서드는 예외를 직접 처리하지 않으므로 호출자가 처리하거나 자신도 전파한다고 선언합니다.

예외 처리를 위해 Java는 세 부분으로 이루어진 **`try` 문**을 제공합니다.

- `try` 블록에는 예외를 던질 수 있는 문을 넣으며 다른 문도 포함할 수 있습니다. 선택적으로 `try` 키워드 바로 뒤에 괄호로 리소스 선언이나 초기화를 둘 수 있습니다. 이를 리소스 포함 `try` 문이라고 합니다.
- 0개(참고: 리소스 포함 `try` 문에서 리소스를 선언하거나 초기화한 경우에만 `try` 블록을 단독으로 사용할 수 있습니다. 그렇지 않으면 `catch` 절이나 `finally` 블록이 하나 이상 필요합니다) 이상의 `catch` 절에는 예외 처리 블록을 둡니다. 개발자는 `try` 블록 실행 중 예외가 발생하면 처리할 각 예외에 대해 수행할 작업을 지정합니다.
- 0개 또는 1개의 `finally` 블록에는 파일을 닫거나 리소스를 해제하는 등의 정리 코드를 둡니다. `try` 블록이 정상적으로 끝났는지와 관계없이 실행됩니다.

`try` 문의 문법 일부는 다음과 같습니다(참고: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>).

```text
TryStatement:  
    try Block Catches 
    try Block [Catches] Finally 
    TryWithResourcesStatement 
Catches: 
    CatchClause {CatchClause}
CatchClause:
    catch ( CatchFormalParameter ) Block 
CatchFormalParameter:
    {VariableModifier} CatchType VariableDeclaratorId
CatchType:
    UnannClassType {| ClassType}
Finally: 
    finally Block    
```

따라서 `try` 문(1행)은 다음 중 하나입니다.

- `try` 블록 뒤에 `catch` 절이 오는 형태(2행).
- `try` 블록 뒤에 선택적인 `catch` 절과 `finally` 블록이 오는 형태(3행).
- 리소스 포함 `try` 문(4행).

`catch` 절(5행)은 예약어 `catch`, 괄호 안의 형식 매개변수, 코드 블록(6행)으로 이루어집니다. `CatchClause {CatchClause}`처럼 여러 `catch` 절이 연달아 올 수 있습니다. `finally` 블록은 예약어 `finally`와 코드 블록으로 이루어집니다(13행).

이 글은 `try` 블록과 `catch` 절을 다룹니다. 앞의 것은 예외를 던질 수 있는 문을 보호하고, 뒤의 것은 예외를 포착하고 처리하는 방법을 정의합니다.

## `try` 블록

**`try` 블록**은 검사 예외나 명시적으로 처리하려는 비검사 예외를 던질 수 있는 코드를 감쌉니다. 예약어 `try` 뒤에 중괄호로 둘러싼 블록이 옵니다. 발생한 예외를 해당 문의 `catch` 절 중 하나가 포착할 수 있다면 제어가 그 절로 넘어갑니다.

다음 예제는 데이터베이스에 접근하는 여러 문을 `try` 문으로 감쌉니다(3~21행). `try` 블록(3~18행)과 `SQLException`을 처리하는 `catch` 절(18~21행)이 있습니다.

```java
public class DBExample {
    public static void main(String[] args) {
        try {   
            var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academic",
            "postgres", "postgres");
           
            IO.println("Listing students...");
            var s = c.createStatement();      
            var rs = s.executeQuery( 
                "select * from student order by enrollment_number");
            while (rs.next()) 
                IO.println(rs.getInt("enrollment_number") + " - " +
                           rs.getString("name"));
            rs.close(); 
            s.close();   
            c.close();   
        } catch (SQLException e){   
            // TODO Handle SQL exceptions
            e.printStackTrace();
        } 
    }
}
```

다음 import도 필요합니다. 여기에서 한 번 보여 주고, 이후 예제에서는 필요한 타입을 이미 import했다고 가정합니다(일반적으로 IDE가 import를 돕습니다).

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

예제의 어떤 문이 실제로 예외를 던질 수 있는지는 IDE, 호출한 메서드의 문서, 적절한 `catch` 절이 없을 때의 컴파일러 오류를 통해 확인할 수 있습니다.

이 예제에서 `SQLException`을 던질 수 있는 메서드는 다음과 같습니다.

- `DriverManager.getConnection(...)` — 4행.
- `Connection.createStatement()` — 9행.
- `Statement.executeQuery(...)` — 10행.
- `ResultSet.next()` — 12행.
- `ResultSet.getInt(...)` — 13행.
- `ResultSet.getString(...)` — 14행.
- `ResultSet.close()` — 15행.
- `Statement.close()` — 16행.
- `Connection.close()` — 17행.

즉 연결 열기, 문 생성, 질의 실행, 결과 순회, 리소스 닫기처럼 이 예제의 거의 모든 데이터베이스 작업이 `SQLException`을 던질 수 있습니다.

IDE는 보호가 필요한 호출도 보여 줄 수 있습니다. 메서드가 예외를 던질 수 있다는 사실을 알 수 있는 것은 포착하거나 선언하기 요구 사항 덕분입니다.

메서드가 검사 예외를 스스로 처리할 방법을 모르거나 그곳에서 처리하는 것이 적절하지 않다면 시그니처에 `throws` 절을 추가합니다. 예를 들어 `DriverManager`의 `getConnection` 시그니처는 다음과 같습니다.

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

따라서 `getConnection`을 호출하는 코드는 호출을 `try` 문으로 감싸거나 자체 메서드 시그니처에 `throws` 절을 추가해야 합니다.

## `catch` 절

**`catch` 절**은 `try` 블록에서 발생한 예외를 처리합니다. 던져질 수 있는 검사 예외마다 별도의 절을 둘 수 있습니다. 다음 예제의 `catch` 절은 예외의 세부 정보(5~10행), 즉 메시지(7행), SQL 상태(8행), 데이터베이스별 오류 코드(9행)를 표시합니다.

```java
public class DBExample {
    public static void main(String[] args) {
        try { 
            // try code identical to the previous listing
        } catch (SQLException e){   
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage()); 
            IO.println("SQLState: " + e.getSQLState()); 
            IO.println("Error: " + e.getErrorCode());
        } 
    }
}
```

예를 들어 `try` 안의 SQL 문에서 테이블 이름 `student` 대신 `studnet`을 입력하면 PostgreSQL에서 다음과 같은 정보를 가진 `SQLException`이 발생합니다.

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

세로 막대(`|`)를 사용하면 하나의 `catch` 절에서 여러 예외 타입을 처리할 수 있습니다. 개발자가 `Class.forName`으로 JDBC 드라이버를 명시적으로 로드하고(4행) 가능한 두 예외 타입을 같은 방식으로 처리하려 한다고 가정해 봅시다. 세로 막대를 통해 `catch` 절이 `SQLException`과 `ClassNotFoundException`을 모두 포착하도록 지정할 수 있습니다(7행).

```java
public class DBExample {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver"); 
            // Database access code
            // omitted
        } catch (SQLException | ClassNotFoundException e){ 
            IO.println("Error! Contact support.");
            IO.println("Message: " + e.getMessage());
            IO.println("Stack Trace: ");
            e.printStackTrace();
        }
    }
}
```

드라이버를 찾지 못하면 프로그램은 다음과 비슷하게 출력합니다(참고: 전체 프로그램에는 `import` 행도 포함되므로 `DBExample.java`의 실제 행 번호는 조금 더 큽니다).

```text
Error! Contact support.
Message: org.postgresql.Driver
Stack Trace: 
java.lang.ClassNotFoundException: org.postgresql.Driver
	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:580)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:490)
	at java.base/java.lang.Class.forName0(Native Method)
	at java.base/java.lang.Class.forName(Class.java:467)
	at java.base/java.lang.Class.forName(Class.java:458)
	at DBExample.main(DBExample.java:4)
```

예외 타입마다 별도의 `catch` 절을 두어 처리 방식을 달리할 수도 있습니다. 다음 예제에서는 `SQLException`용 절이 7행, `ClassNotFoundException`용 절이 12행에서 시작합니다.

```java
public class DBExample {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver");
            // Database access code
            // omitted
        } catch (SQLException e){ 
            IO.println("SQLException caught!");
            IO.println("Message: " + e.getMessage());
            IO.println("SQLState: " + e.getSQLState());
            IO.println("Error: " + e.getErrorCode());  
        } catch (ClassNotFoundException e){ 
            IO.println("Error loading the JDBC driver!"); 
            IO.println("Contact support.");
            IO.println("Message: " + e.getMessage());
            IO.println("Stack Trace: ");
            e.printStackTrace();
        }
    }
}
```

여기에는 타입별로 서로 다른 두 개의 예외 처리 블록이 있습니다. 여러 타입이 공통 상위 클래스를 갖거나 한 타입이 다른 타입의 상위 클래스라면 하나의 블록에서 처리할 수도 있습니다.

---

*이 글은 Eduardo Kessler Piveta의 책 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
