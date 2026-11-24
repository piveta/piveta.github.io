---
layout: post
title: "PreparedStatement로 학생 삽입하기"
date: 2026-11-19
lang: ko
translation_id: inserindo-alunos-preparedstatement-java
permalink: /ko/inserting-students-with-preparedstatement-in-java/
share_text: >-
  배열이나 반복문 없이 매개변수화한 문장을 세 번 직접 실행합니다.
---

`PreparedStatement`는 `?` 자리표시자가 있는 SQL 문장입니다. `setInt`와 `setString`으로 값을 지정하면 데이터를 SQL 문자열에 이어 붙이지 않아도 되므로 SQL 인젝션 위험이 줄어듭니다. 여기서 `c`는 `academic` 연결이며, `student`에는 `enrollment_number`와 `name` 열이 있습니다.

```java
IO.println("Inserting students...");
var p = c.prepareStatement("insert into student " +
        "(enrollment_number, name) values (?, ?)");
p.setInt(1, 1); 
p.setString(2, "Maria");
p.execute(); // Inserts 1 - Maria
p.setInt(1, 2);
p.setString(2, "Pedro");
p.execute(); // Inserts 2 - Pedro
p.setInt(1, 3);
p.setString(2, "João");
p.execute(); // Inserts 3 - João
```

위치 1은 학번, 위치 2는 이름입니다. 동일한 문장을 Maria, Pedro, João에 대해 실행합니다. 이에 해당하는 SQL은 다음과 같습니다.

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

중복 학번은 기본 키 제약을 위반하여 `SQLException`을 발생시킵니다. 전체 프로그램의 `main`은 이를 전파하고 마지막에 자원을 닫습니다.

---

*이 글은 Eduardo Kessler Piveta의 저서 [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)의 내용을 바탕으로 작성했습니다.*
