---
layout: post
title: "Intercepter et traiter les exceptions en Java"
date: 2026-11-24
lang: fr
translation_id: capturando-tratando-excecoes-java
permalink: /fr/catching-and-handling-exceptions-in-java/
share_text: >-
  Les blocs try et les clauses catch traitent les exceptions Java. Des exemples JDBC présentent SQLException, la capture multiple et le traitement distinct selon le type.
---

Lorsqu’une exception se produit — qu’il s’agisse d’une erreur ou d’une situation hors du déroulement attendu —, la méthode concernée crée un objet d’une classe d’exception et le transmet au système d’exécution, ici la JVM, avec les informations pertinentes.

La JVM recherche ensuite dans la pile d’appels un gestionnaire compatible avec cet objet. Elle commence par la méthode où l’exception s’est produite. Si cette méthode possède un gestionnaire approprié, elle traite l’exception localement. Sinon, la JVM examine la méthode appelante. La recherche remonte ainsi la pile jusqu’à trouver un gestionnaire ou atteindre l’appel initial. Si aucune méthode ne traite l’exception, la JVM termine le programme et affiche un message d’erreur ainsi que la trace de pile ayant conduit à l’exception.

Le code Java susceptible de lever des exceptions vérifiées est soumis à l’obligation **intercepter ou déclarer** :

- Les instructions susceptibles de lever une exception doivent être placées dans un bloc protégé (un bloc `try`) avec un gestionnaire approprié (une clause `catch`) ; ou
- La méthode qui contient ces instructions doit déclarer avec `throws` qu’elle peut lever l’exception. Elle ne la traite pas : la méthode appelante doit la traiter ou déclarer à son tour qu’elle peut la propager.

Pour gérer les exceptions, Java fournit l’**instruction `try`**, composée de trois parties :

- Un bloc `try` contient les instructions susceptibles de lever une exception et peut également en contenir d’autres. Des déclarations ou initialisations de ressources peuvent éventuellement suivre immédiatement le mot-clé `try`, entre parenthèses : c’est `try` avec ressources.
- Zéro (Remarque : un bloc `try` ne peut apparaître seul que si des ressources sont déclarées ou initialisées dans une instruction `try` avec ressources. Sinon, il faut au moins une clause `catch` ou un bloc `finally`) ou plusieurs clauses `catch` contiennent les blocs de traitement. Le développeur indique ce qu’il faut faire pour chaque exception à traiter si elle est levée pendant l’exécution du bloc `try`.
- Zéro ou un bloc `finally` contient le code de nettoyage, généralement pour fermer des fichiers ou libérer des ressources. Ses instructions s’exécutent que le bloc `try` se termine correctement ou non.

Une partie de la syntaxe d’une instruction `try` (Remarque : <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>) est présentée ci-dessous :

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

Une instruction `try` (ligne 1) se compose donc :

- D’un bloc `try` suivi de clauses `catch` (ligne 2) ;
- D’un bloc `try`, de clauses `catch` facultatives et d’un bloc `finally` (ligne 3) ; ou
- D’une instruction `try` avec ressources (ligne 4).

Une clause `catch` (ligne 5) se compose du mot réservé `catch`, de paramètres formels entre parenthèses puis d’un bloc de code (ligne 6). Plusieurs clauses `catch` peuvent se suivre, comme l’indique `CatchClause {CatchClause}`. Un bloc `finally` comprend le mot réservé `finally` suivi d’un bloc de code (ligne 13).

Cet article porte sur le bloc `try` et les clauses `catch` : le premier protège les instructions susceptibles de lever des exceptions, tandis que les secondes définissent comment les intercepter et les traiter.

## Le bloc `try`

Un **bloc `try`** entoure le code susceptible de lever des exceptions, qu’il s’agisse d’exceptions vérifiées ou d’exceptions non vérifiées que nous souhaitons traiter explicitement. Le mot réservé `try` est suivi d’un bloc entre accolades. Si une exception peut être interceptée par l’une des clauses `catch` de l’instruction, le contrôle passe à cette clause.

L’exemple suivant montre une instruction `try` autour de plusieurs opérations d’accès à une base de données (lignes 3 à 21). Elle contient un bloc `try` (lignes 3 à 18) et une clause `catch` pour `SQLException` (lignes 18 à 21) :

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

Les importations suivantes sont également nécessaires. Elles sont indiquées ici ; dans les exemples suivants, on suppose que les types utiles sont déjà importés (les IDE facilitent généralement ces importations) :

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

Pour déterminer quelles instructions de l’exemple peuvent réellement lever des exceptions, nous pouvons utiliser une IDE, consulter la documentation des méthodes appelées ou examiner les erreurs du compilateur qui surviendraient sans clause `catch` appropriée.

Dans cet exemple, les méthodes susceptibles de lever une `SQLException` sont :

- `DriverManager.getConnection(...)` — ligne 4 ;
- `Connection.createStatement()` — ligne 9 ;
- `Statement.executeQuery(...)` — ligne 10 ;
- `ResultSet.next()` — ligne 12 ;
- `ResultSet.getInt(...)` — ligne 13 ;
- `ResultSet.getString(...)` — ligne 14 ;
- `ResultSet.close()` — ligne 15 ;
- `Statement.close()` — ligne 16 ;
- `Connection.close()` — ligne 17.

Autrement dit, presque toutes les opérations de base de données de cet exemple — ouverture de la connexion, création de l’instruction, exécution de la requête, parcours du résultat et fermeture des ressources — peuvent lever une `SQLException`.

Une IDE peut aussi montrer quels appels doivent être protégés. Elle sait qu’une méthode peut lever une exception grâce à l’obligation « intercepter ou déclarer ».

Si une méthode ne sait pas comment traiter une exception vérifiée, ou si ce traitement n’est pas approprié à cet endroit, elle ajoute une clause `throws` à sa signature. Par exemple, la signature de `getConnection` dans `DriverManager` est :

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

Le code qui appelle `getConnection` doit donc entourer cet appel d’une instruction `try` ou ajouter une clause `throws` à la signature de sa propre méthode.

## Les clauses `catch`

Les **clauses `catch`** traitent les exceptions provenant d’un bloc `try`. Nous pouvons prévoir une clause distincte pour chaque exception vérifiée susceptible d’être levée. Dans l’exemple suivant, une clause `catch` affiche les détails de l’exception (lignes 5 à 10) : son message (ligne 7), l’état SQL (ligne 8) et le code d’erreur propre à la base de données (ligne 9) :

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

Si, par exemple, nous écrivions `studnet` au lieu de `student` comme nom de table dans l’instruction SQL du bloc `try`, une `SQLException` serait levée avec des informations telles que les suivantes (dans PostgreSQL) :

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

Une clause `catch` peut également traiter plusieurs types d’exception à l’aide d’une barre verticale (`|`). Supposons que le développeur veuille charger explicitement le pilote JDBC avec `Class.forName` (ligne 4) et traiter les deux types possibles de la même manière. La barre verticale indique que la clause `catch` intercepte à la fois `SQLException` et `ClassNotFoundException` (ligne 7) :

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

Si le pilote était introuvable, le programme afficherait approximativement ce qui suit (Remarque : le numéro de ligne dans `DBExample.java` serait un peu plus élevé dans le programme complet, qui comprendrait aussi des lignes `import`) :

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

Une autre possibilité consiste à prévoir une clause `catch` pour chaque type et à adapter le traitement. Dans l’exemple suivant, la clause pour `SQLException` commence à la ligne 7 et celle pour `ClassNotFoundException` à la ligne 12 :

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

Nous disposons ainsi de deux blocs de traitement distincts, un pour chaque type. Plusieurs types peuvent aussi être traités dans un seul bloc s’ils ont une superclasse commune (ou si l’un d’eux est une superclasse des autres).

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
