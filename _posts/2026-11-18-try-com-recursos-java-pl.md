---
layout: post
title: "try z zasobami w Javie"
date: 2026-11-18
lang: pl
translation_id: try-com-recursos-java
permalink: /pl/try-with-resources-in-java/
share_text: >-
  Instrukcja try z zasobami automatycznie zamyka obiekty AutoCloseable. Przykład JDBC pokazuje zarządzanie połączeniem, instrukcją i zbiorem wyników.
---

Aby usprawnić zarządzanie zasobami, od Javy 7 można wskazać w instrukcji `try` zasoby zamykane po zakończeniu jej wykonywania. Specyfikacja języka dopuszcza jeden lub więcej zasobów implementujących interfejs `AutoCloseable`. Według dokumentacji interfejs ten implementuje ponad sto klas biblioteki standardowej. Jego definicja wygląda tak:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

Składnia instrukcji `try` z zasobami jest następująca:

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

Zasoby podaje się w nawiasach, zwykle jako deklarację zmiennej lokalnej albo dostęp do zmiennej już na pewno przypisanej i efektywnie finalnej (czyli nieprzypisywanej ponownie; modyfikator `final` nie jest wymagany). W zapytaniu JDBC trzeba zamknąć połączenie, instrukcję oraz zbiór wyników. W poniższym przykładzie deklaracje i inicjalizacje `c` (wiersz 5), `s` (wiersz 8) i `rs` (wiersz 9) umieszczono w specyfikacji zasobów instrukcji `try`:

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

Nie jest wtedy potrzebny blok `finally`: środowisko uruchomieniowe Javy automatycznie zamyka wszystkie wskazane zasoby. Upraszcza to kod i zmniejsza ryzyko pozostawienia otwartego zasobu, dlatego jest zalecanym sposobem postępowania w kodzie zarządzającym zasobami.

---

*Artykuł opracowano na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) autorstwa Eduardo Kessler Piveta.*
