---
layout: post
title: "Intercettare e gestire le eccezioni in Java"
date: 2026-11-24
lang: it
translation_id: capturando-tratando-excecoes-java
permalink: /it/catching-and-handling-exceptions-in-java/
share_text: >-
  I blocchi try e le clausole catch gestiscono le eccezioni Java. Esempi JDBC illustrano SQLException, la cattura multipla e la gestione distinta per tipo.
---

Quando si verifica un’eccezione — un errore o una situazione fuori dal flusso previsto — il metodo in cui si verifica crea un oggetto di una classe di eccezione e lo trasmette al sistema di esecuzione, la JVM, insieme alle informazioni pertinenti.

La JVM cerca quindi nello stack delle chiamate un gestore compatibile con l’oggetto eccezione. Comincia dal metodo in cui si è verificata. Se il metodo dispone di un gestore adeguato, l’eccezione viene gestita localmente. Altrimenti la JVM esamina il metodo chiamante. La ricerca prosegue lungo lo stack finché trova un gestore o raggiunge il chiamante iniziale. Se nessun metodo gestisce l’eccezione, la JVM termina il programma e stampa un messaggio di errore e lo stack trace che ha condotto all’eccezione.

Il codice Java che può lanciare eccezioni controllate è soggetto al requisito **intercettare o dichiarare**:

- Le istruzioni che possono lanciare un’eccezione devono essere racchiuse in un blocco protetto (un blocco `try`) con un gestore adeguato (una clausola `catch`); oppure
- Il metodo che le contiene deve dichiarare con `throws` che può lanciare l’eccezione. Non la gestisce: il chiamante deve gestirla o dichiarare a sua volta che può propagarla.

Per la gestione delle eccezioni, Java offre l’**istruzione `try`**, composta da tre parti:

- Un blocco `try` contiene le istruzioni che possono lanciare un’eccezione e può contenere anche altre istruzioni. Facoltativamente, subito dopo la parola `try` possono comparire tra parentesi dichiarazioni o inizializzazioni di risorse: è il cosiddetto `try` con risorse.
- Zero (Nota: un blocco `try` può comparire da solo soltanto quando vengono dichiarate o inizializzate risorse in un’istruzione `try` con risorse. Altrimenti serve almeno una clausola `catch` o un blocco `finally`) o più clausole `catch` contengono i blocchi di gestione. Lo sviluppatore specifica che cosa fare per ogni eccezione da gestire, se viene lanciata durante l’esecuzione del blocco `try`.
- Zero o un blocco `finally` contiene codice di pulizia, normalmente per chiudere file o liberare risorse. Le sue istruzioni vengono eseguite indipendentemente dal successo del blocco `try`.

Una parte della sintassi di un’istruzione `try` (Nota: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>) è riportata di seguito:

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

Un’istruzione `try` (riga 1) consiste quindi in:

- Un blocco `try` seguito da clausole `catch` (riga 2);
- Un blocco `try` seguito da clausole `catch` facoltative e da un blocco `finally` (riga 3); oppure
- Un’istruzione `try` con risorse (riga 4).

Una clausola `catch` (riga 5) consiste nella parola riservata `catch`, seguita dai parametri formali tra parentesi e poi da un blocco di codice (riga 6). Possono seguire più clausole `catch`, come indica `CatchClause {CatchClause}`. Un blocco `finally` consiste nella parola riservata `finally` seguita da un blocco di codice (riga 13).

Questo articolo si concentra sul blocco `try` e sulle clausole `catch`: il primo protegge le istruzioni che possono lanciare eccezioni, mentre le seconde definiscono come intercettarle e gestirle.

## Il blocco `try`

Un **blocco `try`** racchiude il codice che può lanciare eccezioni, sia controllate sia non controllate che desideriamo gestire esplicitamente. Alla parola riservata `try` segue un blocco tra parentesi graffe. Se si verifica un’eccezione intercettabile da una delle clausole `catch` dell’istruzione, il controllo passa a quella clausola.

L’esempio seguente mostra un’istruzione `try` che racchiude varie operazioni di accesso a un database (righe da 3 a 21). Contiene un blocco `try` (righe da 3 a 18) e una clausola `catch` per `SQLException` (righe da 18 a 21):

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

Sono necessarie anche le seguenti importazioni. Le mostriamo qui; negli esempi successivi si presume che i tipi pertinenti siano già importati (di solito gli IDE aiutano ad aggiungere le importazioni):

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

Per individuare quali istruzioni dell’esempio possano effettivamente lanciare eccezioni, possiamo usare un IDE, consultare la documentazione dei metodi chiamati o esaminare gli errori del compilatore che comparirebbero senza un’opportuna clausola `catch`.

In questo esempio, i metodi che possono lanciare una `SQLException` sono:

- `DriverManager.getConnection(...)` — riga 4;
- `Connection.createStatement()` — riga 9;
- `Statement.executeQuery(...)` — riga 10;
- `ResultSet.next()` — riga 12;
- `ResultSet.getInt(...)` — riga 13;
- `ResultSet.getString(...)` — riga 14;
- `ResultSet.close()` — riga 15;
- `Statement.close()` — riga 16;
- `Connection.close()` — riga 17.

In altre parole, quasi tutte le operazioni di database qui presenti — apertura della connessione, creazione dello statement, esecuzione della query, scorrimento del risultato e chiusura delle risorse — possono lanciare una `SQLException`.

Un IDE può anche indicare quali chiamate richiedono protezione. Sa che un metodo può lanciare un’eccezione grazie al requisito di intercettare o dichiarare.

Se un metodo non sa come gestire un’eccezione controllata, o se non è opportuno gestirla lì, aggiunge una clausola `throws` alla propria firma. Per esempio, la firma di `getConnection` in `DriverManager` è:

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

Il codice che chiama `getConnection` deve quindi racchiudere la chiamata in un’istruzione `try` oppure aggiungere una clausola `throws` alla firma del proprio metodo.

## Clausole `catch`

Le **clausole `catch`** gestiscono le eccezioni provenienti da un blocco `try`. Possiamo prevedere una clausola distinta per ogni eccezione controllata che potrebbe essere lanciata. Nell’esempio seguente, una clausola `catch` visualizza i dettagli dell’eccezione (righe da 5 a 10): il messaggio (riga 7), lo stato SQL (riga 8) e il codice di errore specifico del database (riga 9):

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

Se, per esempio, scrivessimo `studnet` invece di `student` come nome della tabella nell’istruzione SQL dentro `try`, verrebbe lanciata una `SQLException` con informazioni simili alle seguenti (in PostgreSQL):

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

Una clausola `catch` può gestire anche più tipi di eccezione usando una barra verticale (`|`). Supponiamo che lo sviluppatore voglia caricare esplicitamente il driver JDBC con `Class.forName` (riga 4) e gestire nello stesso modo entrambi i possibili tipi di eccezione. La barra verticale specifica che la clausola `catch` intercetta sia `SQLException` sia `ClassNotFoundException` (riga 7):

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

Se il driver non fosse trovato, il programma mostrerebbe qualcosa del genere (Nota: il numero di riga in `DBExample.java` sarebbe in realtà un po’ più alto nel programma completo, che conterrebbe anche le righe `import`):

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

Un’altra possibilità consiste nel prevedere una clausola `catch` per ogni tipo di eccezione, adattando la gestione a ciascuno. Nell’esempio successivo la clausola per `SQLException` inizia alla riga 7 e quella per `ClassNotFoundException` alla riga 12:

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

Qui abbiamo due blocchi distinti di gestione, uno per ogni tipo. È anche possibile gestire più tipi in un unico blocco se hanno una superclasse comune (o se uno è superclasse degli altri).

---

*Questo articolo adatta contenuti del libro [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), di Eduardo Kessler Piveta.*
