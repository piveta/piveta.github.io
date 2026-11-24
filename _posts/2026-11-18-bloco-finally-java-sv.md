---
layout: post
title: "Finally-blocket i Java"
date: 2026-11-24
lang: sv
translation_id: bloco-finally-java
permalink: /sv/finally-block-in-java/
share_text: >-
  Ett finally-block körs efter try och catch även om körningen misslyckas. JDBC-exempel visar svårigheterna med att stänga ResultSet, Statement och Connection manuellt.
---

En `try`-sats kan ha ett avslutande block, ett **`finally`-block**, som körs oavsett om koden i `try`-blocket slutfördes utan fel. I följande exempel har `try`-satsen ett `finally`-block (från rad 25) som stänger resurserna som öppnats i `try`-blocket: `ResultSet`, `Statement` och anslutningen (`Connection`):

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

Observera dock att metoden `close` i `ResultSet`, `Statement` och `Connection` själv kan kasta ett `SQLException`. Därför skulle föregående exempel inte kompileras. Vi måste antingen hantera undantaget eller deklarera att vi inte hanterar det. Vi kan använda en nästlad `try`-sats för varje anrop (om de kräver olika hantering) eller en sats för alla tre anrop:

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

Den här koden kan fortfarande kasta ett okontrollerat `NullPointerException` om `rs`, `s` eller `c` är `null` (på raderna 15, 22 respektive 28). Normalt fångar och hanterar man inte okontrollerade undantag; i stället rättar man orsaken till problemet.

Vi kan kontrollera att varje variabel inte är `null` innan `close` anropas. Detta görs i följande exempel på raderna 4, 12 och 20:

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

Även efter dessa åtgärder kan information om det ursprungliga undantaget gå förlorad om en sats i det första `try`-blocket kastar ett `SQLException` och en av `close`-metoderna misslyckas med ett nytt `SQLException`. Vi kan bevara det ursprungliga undantaget och lägga till undantagen från `close` som undertryckta undantag, med metoder som `addSuppressed` och `getSuppressed` i `Throwable`. Det skulle göra koden ännu mer komplicerad.

För att minska mängden kod och svårigheterna med resurshantering införde Java en variant av `try`-satsen där resurser anges för automatisk stängning när satsen avslutas, oavsett om den slutförs normalt. Den kallas **try-with-resources** (Anmärkning: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
