---
layout: post
title: "Il blocco finally in Java"
date: 2026-11-18
lang: it
translation_id: bloco-finally-java
permalink: /it/finally-block-in-java/
share_text: >-
  Un blocco finally viene eseguito dopo try e catch anche in caso di errore. Gli esempi JDBC mostrano le difficoltà della chiusura manuale di ResultSet, Statement e Connection.
---

Un’istruzione `try` può avere un blocco finale associato, chiamato **blocco `finally`**, che viene eseguito indipendentemente dal completamento del codice nel blocco `try`. Nell’esempio seguente, l’istruzione `try` contiene un blocco `finally` (dalla riga 25) che chiude le risorse aperte nel blocco `try`: il `ResultSet`, lo `Statement` e la connessione (`Connection`):

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

Il metodo `close` di `ResultSet`, `Statement` e `Connection`, tuttavia, può a sua volta lanciare una `SQLException`. Per questo l’esempio precedente non compilerebbe. Dobbiamo gestire l’eccezione oppure dichiarare che non la gestiremo. Possiamo usare un’istruzione `try` annidata per ogni chiamata (se ciascuna richiede un trattamento diverso) oppure un’unica istruzione per tutte e tre:

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

Questo codice potrebbe ancora lanciare una `NullPointerException` non controllata se `rs`, `s` o `c` fossero `null` (rispettivamente alle righe 15, 22 e 28). Di norma non ci si limita a intercettare le eccezioni non controllate: si corregge la causa del problema.

Possiamo verificare se ogni variabile vale `null` prima di chiamare `close`. L’esempio seguente lo fa alle righe 4, 12 e 20:

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

Anche così, potremmo perdere informazioni sull’eccezione originale se un’istruzione nel primo blocco `try` lanciasse una `SQLException` e uno dei metodi `close` fallisse lanciandone un’altra. Potremmo conservare l’eccezione originale e aggiungere quelle di `close` come eccezioni soppresse, usando metodi di `Throwable` come `addSuppressed` e `getSuppressed`. Il codice diventerebbe però ancora più complesso.

Per ridurre questa verbosità e le difficoltà nella gestione delle risorse, Java ha introdotto una variante dell’istruzione `try` in cui si indicano le risorse da chiudere al termine dell’istruzione, sia che essa termini normalmente sia che non lo faccia. Si chiama **`try` con risorse** (Nota: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
