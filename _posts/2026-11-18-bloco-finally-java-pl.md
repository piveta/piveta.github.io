---
layout: post
title: "Blok finally w Javie"
date: 2026-11-18
lang: pl
translation_id: bloco-finally-java
permalink: /pl/finally-block-in-java/
share_text: >-
  Blok finally wykonuje się po try i catch także wtedy, gdy operacja się nie powiedzie. Przykłady JDBC pokazują trudności ręcznego zamykania ResultSet, Statement i Connection.
---

Instrukcja `try` może mieć powiązany blok końcowy, nazywany **blokiem `finally`**, który wykonuje się niezależnie od tego, czy kod w bloku `try` zakończył się pomyślnie. W poniższym przykładzie blok `finally` (od wiersza 25) zamyka zasoby otwarte w bloku `try`: `ResultSet`, `Statement` i połączenie (`Connection`):

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

Jednak metoda `close` obiektów `ResultSet`, `Statement` i `Connection` sama może zgłosić `SQLException`. Dlatego poprzedni przykład nie skompilowałby się. Musimy obsłużyć wyjątek albo zadeklarować, że go nie obsłużymy. Możemy użyć zagnieżdżonej instrukcji `try` dla każdego wywołania (jeśli wymagają różnej obsługi) albo jednej instrukcji dla wszystkich trzech:

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

Ten kod nadal może zgłosić niesprawdzany `NullPointerException`, jeśli `rs`, `s` lub `c` ma wartość `null` (odpowiednio w wierszach 15, 22 i 28). Zwykle nie wystarczy przechwycić wyjątku niesprawdzanego — należy usunąć przyczynę problemu.

Możemy sprawdzić, czy zmienna ma wartość `null`, zanim wywołamy `close`. Poniższy przykład robi to w wierszach 4, 12 i 20:

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

Nawet wtedy możemy utracić informacje o pierwotnym wyjątku, jeśli instrukcja z pierwszego bloku `try` zgłosi `SQLException`, a jedna z metod `close` zawiedzie i zgłosi kolejną. Można zachować pierwotny wyjątek i dodać wyjątki z `close` jako tłumione, używając metod `Throwable`, takich jak `addSuppressed` i `getSuppressed`. Kod stałby się jednak jeszcze bardziej złożony.

Żeby ograniczyć tę rozwlekłość i trudności związane z zasobami, Java wprowadziła odmianę instrukcji `try`, w której wskazuje się zasoby zamykane po zakończeniu instrukcji, niezależnie od tego, czy kończy się ona normalnie. Jest to **`try` z zasobami** (Uwaga: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*Artykuł opracowano na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) autorstwa Eduardo Kessler Piveta.*
