---
layout: post
title: "Fånga och hantera undantag i Java"
date: 2026-11-24
lang: sv
translation_id: capturando-tratando-excecoes-java
permalink: /sv/catching-and-handling-exceptions-in-java/
share_text: >-
  Javas try-block och catch-satser hanterar undantag. JDBC-exempel visar SQLException, multi-catch och separat hantering av olika undantagstyper.
---

När ett undantag uppstår (på grund av ett fel eller en situation utanför det förväntade flödet) skapar metoden där det uppstår ett objekt av en undantagsklass och skickar det, tillsammans med relevant information, till körmiljön (JVM).

JVM söker sedan i anropsstacken efter en undantagshanterare som är kompatibel med objektet. Sökningen börjar i metoden där undantaget uppstod. Om metoden har en lämplig hanterare behandlas undantaget där. Annars granskar JVM metodens anropare. Sökningen fortsätter genom anropsstacken tills en hanterare hittas eller den ursprungliga anroparen nås. Om ingen metod hanterar undantaget avslutar JVM programmet och skriver ut ett felmeddelande och stackspårningen som ledde till undantaget.

Java-kod som kan kasta kontrollerade undantag omfattas av kravet att **fånga eller deklarera** undantaget. Därför gäller något av följande:

- Satserna som kan kasta ett undantag placeras i ett skyddat block (ett `try`-block) med en lämplig hanterare (en `catch`-sats); eller
- Metoden som innehåller satserna deklarerar med `throws` att den kan kasta undantaget. Metoden hanterar det inte; anroparen måste hantera det eller i sin tur deklarera att den kan kasta det.

För undantagshantering har Java en **`try`-sats** med tre delar:

- Ett `try`-block innehåller satser som kan kasta undantag och kan även innehålla andra satser. Valfritt kan resursdeklarationer eller initialiseringar stå inom parentes direkt efter nyckelordet `try`; det kallas try-with-resources.
- Noll (Anmärkning: Ett `try`-block kan stå ensamt endast när resurser deklareras eller initialiseras i en try-with-resources-sats. Annars krävs minst en `catch`-sats eller ett `finally`-block.) eller flera `catch`-satser innehåller block som hanterar undantag. Utvecklaren anger vad som ska ske för varje undantag som hanteras om det kastas när `try`-blocket körs.
- Noll eller ett `finally`-block innehåller städkod, vanligen för att stänga filer eller frigöra resurser. Satserna körs oavsett om `try`-blocket slutförs utan fel.

En del av syntaxen för `try`-satsen (Anmärkning: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>) visas nedan:

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

En `try`-sats (rad 1) består alltså av:

- Ett `try`-block följt av `catch`-satser (rad 2);
- Ett `try`-block följt av valfria `catch`-satser och ett `finally`-block (rad 3); eller
- En try-with-resources-sats (rad 4).

En `catch`-sats (rad 5) består av det reserverade ordet `catch`, följt av formella parametrar inom parentes och sedan ett kodblock (rad 6). Flera `catch`-satser kan följa på varandra, som `CatchClause {CatchClause}` visar. Ett `finally`-block består av det reserverade ordet `finally` följt av ett kodblock (rad 13).

Den här artikeln behandlar `try`-blocket och `catch`-satserna: det förra skyddar satser som kan kasta undantag, medan de senare definierar hur undantagen fångas och hanteras.

## `try`-blocket

Ett **`try`-block** omsluter kod som kan kasta undantag, både kontrollerade undantag och okontrollerade undantag som vi uttryckligen vill hantera. Efter det reserverade ordet `try` följer ett block inom klammerparenteser. Om ett undantag uppstår som kan fångas av någon av satsens `catch`-satser övergår kontrollen till den satsen.

Följande exempel visar en `try`-sats kring flera satser som använder en databas (raderna 3–21). Den har ett `try`-block (raderna 3–18) och en `catch`-sats för `SQLException` (raderna 18–21):

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

Följande importer behövs också. De visas här; i efterföljande exempel förutsätts att relevanta typer har importerats (IDE:er brukar hjälpa till med detta):

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

För att avgöra vilka satser i exemplet som faktiskt kan kasta undantag kan vi använda en IDE, läsa dokumentationen för metoderna som anropas eller granska kompileringsfelen som skulle uppstå utan en lämplig `catch`-sats.

I det här exemplet kan följande metoder kasta `SQLException`:

- `DriverManager.getConnection(...)` — rad 4;
- `Connection.createStatement()` — rad 9;
- `Statement.executeQuery(...)` — rad 10;
- `ResultSet.next()` — rad 12;
- `ResultSet.getInt(...)` — rad 13;
- `ResultSet.getString(...)` — rad 14;
- `ResultSet.close()` — rad 15;
- `Statement.close()` — rad 16;
- `Connection.close()` — rad 17.

Nästan varje databasåtgärd här — att öppna anslutningen, skapa satsen, köra frågan, gå igenom resultatet och stänga resurserna — kan alltså kasta `SQLException`.

En IDE kan också visa vilka anrop som behöver skyddas. Den vet att metoden kan kasta ett undantag eftersom undantaget måste fångas eller deklareras.

Om en metod inte kan hantera ett kontrollerat undantag, eller om det är olämpligt att hantera det där, lägger den till en `throws`-sats i sin signatur. Signaturen för metoden `getConnection` i `DriverManager` är till exempel:

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

Kod som anropar `getConnection` måste därför antingen omsluta anropet med en `try`-sats eller lägga till en `throws`-sats i den egna metodsignaturen.

## `catch`-satser

**`catch`-satser** hanterar undantag som uppstår i ett `try`-block. Vi kan ange en separat `catch`-sats för varje kontrollerat undantag som kan kastas. I följande exempel visar en `catch`-sats detaljer om undantaget (raderna 5–10): meddelandet (rad 7), SQL-tillståndet (rad 8) och databasens felkod (rad 9):

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

Om vi exempelvis skrev `studnet` i stället för `student` som tabellnamn i SQL-satsen i `try`, skulle ett `SQLException` kastas med information som följande (i PostgreSQL):

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

En `catch`-sats kan också hantera flera undantagstyper med ett lodrätt streck (`|`). Anta att utvecklaren vill läsa in JDBC-drivrutinen uttryckligen med `Class.forName` (rad 4) och hantera båda möjliga undantagstyperna på samma sätt. Strecket anger att `catch`-satsen fångar både `SQLException` och `ClassNotFoundException` (rad 7):

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

Om drivrutinen inte hittas visas ungefär följande (Anmärkning: Radnumret i `DBExample.java` skulle vara något högre i det fullständiga programmet eftersom det även innehåller `import`-rader):

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

Ett annat alternativ är att ange en `catch`-sats för varje undantagstyp och anpassa hanteringen. I nästa exempel börjar `catch`-satsen för `SQLException` på rad 7 och satsen för `ClassNotFoundException` på rad 12:

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

Här finns två olika undantagshanteringsblock, ett för varje undantagstyp. Det går också att hantera flera typer i ett enda block om de har en gemensam superklass (eller om en typ är superklass till de andra).

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
