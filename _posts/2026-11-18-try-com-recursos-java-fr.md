---
layout: post
title: "try avec ressources en Java"
date: 2026-11-18
lang: fr
translation_id: try-com-recursos-java
permalink: /fr/try-with-resources-in-java/
share_text: >-
  L’instruction try avec ressources ferme automatiquement les objets AutoCloseable. Un exemple JDBC gère une connexion, une instruction et un ensemble de résultats.
---

Pour améliorer la gestion des ressources, Java permet depuis sa version 7 d’indiquer dans une instruction `try` les ressources qui peuvent être fermées à la fin de son exécution. La spécification du langage précise qu’une instruction `try` peut déclarer une ou plusieurs ressources qui implémentent l’interface `AutoCloseable`. Selon sa documentation, cette interface est implémentée par plus d’une centaine de classes de la bibliothèque standard. Voici sa définition :

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

La syntaxe de `try` avec ressources est la suivante :

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

Les ressources sont indiquées entre parenthèses, généralement au moyen d’une déclaration de variable locale ou de l’accès à une variable déjà définitivement assignée et effectivement finale (elle n’a pas été réassignée ; le modificateur `final` n’est pas obligatoire). Dans une requête JDBC, la connexion, l’instruction et l’ensemble de résultats doivent être fermés. L’exemple suivant place les déclarations et initialisations de `c` (ligne 5), `s` (ligne 8) et `rs` (ligne 9) dans la spécification des ressources de l’instruction `try` :

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

Ainsi, un bloc `finally` n’est pas nécessaire : l’environnement d’exécution Java ferme automatiquement toutes les ressources indiquées. Cette approche simplifie le code et réduit le risque d’oublier de fermer une ressource. Elle est recommandée pour le code qui gère des ressources.

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
