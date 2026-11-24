---
layout: post
title: "Przechwytywanie i obsługa wyjątków w Javie"
date: 2026-11-24
lang: pl
translation_id: capturando-tratando-excecoes-java
permalink: /pl/catching-and-handling-exceptions-in-java/
share_text: >-
  Bloki try i klauzule catch służą do obsługi wyjątków w Javie. Przykłady JDBC ilustrują SQLException, przechwytywanie wielu typów i osobną obsługę każdego typu.
---

Kiedy wystąpi wyjątek — błąd lub sytuacja wykraczająca poza oczekiwany przebieg — metoda, w której to nastąpiło, tworzy obiekt klasy wyjątku i przekazuje go wraz z odpowiednimi informacjami do systemu uruchomieniowego, czyli JVM.

JVM przeszukuje stos wywołań, szukając procedury obsługi zgodnej z obiektem wyjątku. Zaczyna od metody, w której wyjątek wystąpił. Jeśli jest tam odpowiednia procedura, wyjątek zostaje obsłużony lokalnie. W przeciwnym razie JVM sprawdza metodę wywołującą. Poszukiwanie trwa w górę stosu, aż znajdzie procedurę obsługi albo dotrze do pierwszego wywołującego. Gdy żadna metoda nie obsłuży wyjątku, JVM kończy program i wypisuje komunikat o błędzie oraz ślad stosu prowadzący do wyjątku.

Kod Javy mogący zgłosić wyjątki sprawdzane podlega wymaganiu **przechwyć albo zadeklaruj**:

- Instrukcje mogące zgłosić wyjątek trzeba umieścić w chronionym bloku (`try`) z odpowiednią procedurą obsługi (klauzulą `catch`); albo
- Metoda zawierająca te instrukcje musi zadeklarować za pomocą `throws`, że może zgłosić wyjątek. Sama go nie obsługuje: metoda wywołująca musi go obsłużyć lub również zadeklarować jego propagację.

Java zapewnia do obsługi wyjątków **instrukcję `try`**, która ma trzy części:

- Blok `try` zawiera instrukcje mogące zgłosić wyjątek, ale może zawierać również inne. Opcjonalnie zaraz po słowie `try` można w nawiasach umieścić deklaracje lub inicjalizacje zasobów; jest to `try` z zasobami.
- Zero (Uwaga: sam blok `try` jest dozwolony tylko wtedy, gdy w instrukcji `try` z zasobami deklaruje się lub inicjalizuje zasoby. W przeciwnym razie potrzebna jest co najmniej jedna klauzula `catch` lub blok `finally`) lub więcej klauzul `catch` zawiera bloki obsługi wyjątków. Programista określa, co zrobić z każdym wyjątkiem przeznaczonym do obsługi, jeśli zostanie zgłoszony podczas wykonywania bloku `try`.
- Zero lub jeden blok `finally` zawiera kod porządkujący, zwykle do zamykania plików lub zwalniania zasobów. Jego instrukcje wykonują się niezależnie od powodzenia bloku `try`.

Fragment składni instrukcji `try` (Uwaga: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>) przedstawiono poniżej:

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

Instrukcja `try` (wiersz 1) składa się zatem z:

- Bloku `try` z następującymi po nim klauzulami `catch` (wiersz 2);
- Bloku `try`, opcjonalnych klauzul `catch` i bloku `finally` (wiersz 3); albo
- Instrukcji `try` z zasobami (wiersz 4).

Klauzula `catch` (wiersz 5) składa się ze słowa zastrzeżonego `catch`, parametrów formalnych w nawiasach oraz bloku kodu (wiersz 6). Jak pokazuje `CatchClause {CatchClause}`, można podać kilka klauzul `catch` po kolei. Blok `finally` zawiera słowo zastrzeżone `finally` i blok kodu (wiersz 13).

Artykuł skupia się na bloku `try` i klauzulach `catch`: pierwszy chroni instrukcje mogące zgłaszać wyjątki, a drugie określają sposób ich przechwytywania i obsługi.

## Blok `try`

**Blok `try`** obejmuje kod mogący zgłosić wyjątki sprawdzane lub niesprawdzane, które chcemy jawnie obsłużyć. Po słowie zastrzeżonym `try` następuje blok w nawiasach klamrowych. Jeśli powstanie wyjątek, który może przechwycić jedna z klauzul `catch` tej instrukcji, sterowanie przechodzi do niej.

Poniższy przykład obejmuje instrukcją `try` kilka operacji na bazie danych (wiersze 3–21). Ma blok `try` (wiersze 3–18) oraz klauzulę `catch` dla `SQLException` (wiersze 18–21):

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

Potrzebne są też poniższe importy. Pokazujemy je tutaj; w kolejnych przykładach przyjmujemy, że odpowiednie typy zostały już zaimportowane (IDE zwykle pomagają je dodać):

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

Aby ustalić, które instrukcje przykładu naprawdę mogą zgłaszać wyjątki, można skorzystać z IDE, dokumentacji wywoływanych metod lub błędów kompilatora, które wystąpiłyby bez odpowiedniej klauzuli `catch`.

W tym przykładzie `SQLException` mogą zgłosić następujące metody:

- `DriverManager.getConnection(...)` — wiersz 4;
- `Connection.createStatement()` — wiersz 9;
- `Statement.executeQuery(...)` — wiersz 10;
- `ResultSet.next()` — wiersz 12;
- `ResultSet.getInt(...)` — wiersz 13;
- `ResultSet.getString(...)` — wiersz 14;
- `ResultSet.close()` — wiersz 15;
- `Statement.close()` — wiersz 16;
- `Connection.close()` — wiersz 17.

Innymi słowy, prawie wszystkie pokazane tu operacje bazodanowe — otwarcie połączenia, utworzenie instrukcji, wykonanie zapytania, przejście po wynikach i zamknięcie zasobów — mogą zgłosić `SQLException`.

IDE potrafi też wskazać wywołania wymagające ochrony. Wie, że metoda może zgłosić wyjątek, dzięki wymaganiu „przechwyć albo zadeklaruj”.

Jeśli metoda nie potrafi sensownie obsłużyć wyjątku sprawdzanego lub nie powinna robić tego w tym miejscu, dodaje klauzulę `throws` do swojej sygnatury. Na przykład sygnatura `getConnection` w `DriverManager` wygląda tak:

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

Kod wywołujący `getConnection` musi więc objąć wywołanie instrukcją `try` albo dodać klauzulę `throws` do sygnatury własnej metody.

## Klauzule `catch`

**Klauzule `catch`** obsługują wyjątki z bloku `try`. Dla każdego możliwego wyjątku sprawdzanego można zapewnić odrębną klauzulę. W poniższym przykładzie klauzula `catch` wyświetla szczegóły wyjątku (wiersze 5–10): komunikat (wiersz 7), stan SQL (wiersz 8) i kod błędu właściwy dla bazy danych (wiersz 9):

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

Gdybyśmy na przykład w instrukcji SQL wewnątrz `try` wpisali `studnet` zamiast `student` jako nazwę tabeli, w PostgreSQL zgłoszony zostałby `SQLException` z informacjami podobnymi do poniższych:

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

Jedna klauzula `catch` może również obsłużyć kilka typów wyjątków dzięki pionowej kresce (`|`). Załóżmy, że programista chce jawnie załadować sterownik JDBC przez `Class.forName` (wiersz 4) i obsługiwać oba możliwe typy w ten sam sposób. Pionowa kreska oznacza, że klauzula przechwytuje zarówno `SQLException`, jak i `ClassNotFoundException` (wiersz 7):

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

Jeżeli sterownik nie zostanie znaleziony, program wypisze coś podobnego (Uwaga: w pełnym programie numer wiersza w `DBExample.java` byłby nieco większy, ponieważ znalazłyby się w nim również wiersze `import`):

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

Inna możliwość to osobna klauzula `catch` dla każdego typu, pozwalająca dostosować obsługę. W następnym przykładzie klauzula dla `SQLException` zaczyna się w wierszu 7, a dla `ClassNotFoundException` w wierszu 12:

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

Mamy tu dwa różne bloki obsługi wyjątków, po jednym dla każdego typu. Kilka typów można też obsłużyć w jednym bloku, jeśli mają wspólną nadklasę (lub jeden typ jest nadklasą pozostałych).

---

*Artykuł opracowano na podstawie książki [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) autorstwa Eduardo Kessler Piveta.*
