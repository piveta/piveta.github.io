---
layout: post
title: "Try-with-resources i Java"
date: 2026-11-18
lang: sv
translation_id: try-com-recursos-java
permalink: /sv/try-with-resources-in-java/
share_text: >-
  Try-with-resources stänger AutoCloseable-objekt automatiskt. Ett JDBC-exempel visar hur anslutning, sats och resultatmängd hanteras i en try-sats.
---

För att förbättra resurshanteringen tillåter Java sedan version 7 att resurser som kan stängas när en `try`-sats avslutas anges direkt i satsen. Enligt språkspecifikationen får en `try`-sats ange en eller flera resurser som implementerar gränssnittet `AutoCloseable`. Enligt dokumentationen implementeras det av mer än hundra klasser i standardbiblioteket. Definitionen följer:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

Syntaxen för try-with-resources är:

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

Resurserna anges inom parentes, vanligen genom att deklarera en lokal variabel eller använda en variabel som redan definitivt har tilldelats ett värde och är *effectively final* (det vill säga inte har tilldelats ett nytt värde; modifieraren `final` krävs inte). Vid en JDBC-fråga måste anslutningen, satsen och resultatmängden stängas. I följande exempel placeras deklarationerna och initialiseringarna av `c` (rad 5), `s` (rad 8) och `rs` (rad 9) i resursspecifikationen för try-with-resources-satsen:

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

Därmed behövs inget `finally`-block: alla angivna resurser stängs automatiskt av Javas körmiljö. Metoden förenklar koden och minskar risken för att en resurs lämnas öppen. Den rekommenderas för kod som hanterar resurser.

---

*Den här artikeln bygger på innehåll från boken [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), av Eduardo Kessler Piveta.*
