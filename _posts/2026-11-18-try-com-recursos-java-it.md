---
layout: post
title: "try con risorse in Java"
date: 2026-11-18
lang: it
translation_id: try-com-recursos-java
permalink: /it/try-with-resources-in-java/
share_text: >-
  L’istruzione try con risorse chiude automaticamente gli oggetti AutoCloseable. Un esempio JDBC gestisce una connessione, uno statement e un insieme di risultati.
---

Per migliorare la gestione delle risorse, dalla versione 7 Java consente di indicare in un’istruzione `try` le risorse che possono essere chiuse al termine della sua esecuzione. Secondo la specifica del linguaggio, un’istruzione `try` può dichiarare una o più risorse che implementano l’interfaccia `AutoCloseable`. La documentazione indica che questa interfaccia è implementata da oltre cento classi della libreria standard. Ecco la sua definizione:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

La sintassi di `try` con risorse è la seguente:

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

Le risorse si specificano tra parentesi, di solito dichiarando una variabile locale o accedendo a una variabile già assegnata in modo definitivo ed effettivamente finale (cioè non riassegnata; il modificatore `final` non è obbligatorio). In una query JDBC occorre chiudere la connessione, lo statement e l’insieme di risultati. L’esempio seguente colloca le dichiarazioni e le inizializzazioni di `c` (riga 5), `s` (riga 8) e `rs` (riga 9) nella specifica delle risorse dell’istruzione `try`:

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

In questo modo non serve un blocco `finally`: l’ambiente di esecuzione Java chiude automaticamente tutte le risorse indicate. L’approccio semplifica il codice e riduce il rischio di lasciare aperta una risorsa. È la soluzione consigliata per il codice che gestisce risorse.

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
