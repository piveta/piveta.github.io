---
layout: post
title: "Insérer des étudiants avec PreparedStatement"
date: 2026-11-19
lang: fr
translation_id: inserindo-alunos-preparedstatement-java
permalink: /fr/inserting-students-with-preparedstatement-in-java/
share_text: >-
  Trois insertions directes réutilisent une requête paramétrée sans tableau ni boucle.
---

Un `PreparedStatement` contient une instruction SQL avec des paramètres `?`. `setInt` et `setString` fournissent les valeurs sans les concaténer à la requête, ce qui réduit le risque d’injection SQL. Ici, `c` est la connexion à `academic` et `student` contient `enrollment_number` et `name`.

```java
IO.println("Inserting students...");
var p = c.prepareStatement("insert into student " +
        "(enrollment_number, name) values (?, ?)");
p.setInt(1, 1); 
p.setString(2, "Maria");
p.execute(); // Inserts 1 - Maria
p.setInt(1, 2);
p.setString(2, "Pedro");
p.execute(); // Inserts 2 - Pedro
p.setInt(1, 3);
p.setString(2, "João");
p.execute(); // Inserts 3 - João
```

La position 1 correspond au numéro d’inscription, la position 2 au nom. La même instruction est exécutée pour Maria, Pedro et João. Les commandes SQL équivalentes sont :

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

Un numéro déjà présent viole la clé primaire et entraîne une `SQLException`. Dans le programme complet, `main` propage cette exception et les ressources sont fermées à la fin.

---

*Cet article adapte le contenu du livre [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), d’Eduardo Kessler Piveta.*
