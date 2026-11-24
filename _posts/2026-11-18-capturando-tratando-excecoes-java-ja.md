---
layout: post
title: "Javaで例外を捕捉して処理する"
date: 2026-11-24
lang: ja
translation_id: capturando-tratando-excecoes-java
permalink: /ja/catching-and-handling-exceptions-in-java/
share_text: >-
  Javaのtryブロックとcatch節による例外処理を説明します。JDBCの例でSQLException、複数型の捕捉、型別の処理を示します。
---

例外が発生すると（エラーであれ、予想した通常の流れから外れた状況であれ）、発生したメソッドは例外クラスのオブジェクトを作成し、関連情報とともに実行システムであるJVMに渡します。

JVMはその例外オブジェクトに適合するハンドラを呼び出しスタックから探します。まず例外が発生したメソッドを調べます。適切なハンドラがあれば、その場で処理します。なければ呼び出し元を調べます。この探索はハンドラが見つかるか、最初の呼び出し元に達するまで続きます。どのメソッドも処理しなければ、JVMはプログラムを終了し、エラーメッセージと例外に至るスタックトレースを出力します。

検査例外をスローする可能性のあるJavaコードには、**捕捉または宣言**という要件があります。

- 例外をスローし得る文を、適切なハンドラ（`catch`節）を備えた保護ブロック（`try`ブロック）で囲むか、
- それらを含むメソッドが`throws`を使って例外をスローし得ることを宣言します。このメソッドは例外を処理しません。呼び出し元が処理するか、さらに伝播を宣言します。

例外処理のため、Javaには三つの部分からなる**`try`文**があります。

- `try`ブロックには例外をスローし得る文を入れ、他の文も含められます。必要なら`try`キーワードの直後に括弧で囲んだリソースの宣言や初期化を記述できます。これがリソース付き`try`文です。
- 0個（注: リソース付き`try`文でリソースを宣言または初期化する場合に限り、`try`ブロックを単独で記述できます。それ以外では少なくとも一つの`catch`節または`finally`ブロックが必要です）以上の`catch`節には、例外処理のブロックを記述します。開発者は、`try`ブロックの実行中に例外がスローされた場合、処理対象の各例外にどう対処するかを指定します。
- 0個または1個の`finally`ブロックには、通常、ファイルを閉じたりリソースを解放したりする後始末のコードを置きます。`try`ブロックが正常に終わったかどうかに関係なく実行されます。

`try`文の構文の一部を次に示します（注: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>）。

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

したがって、`try`文（1行目）は次のいずれかです。

- `try`ブロックの後に`catch`節が続く形式（2行目）。
- `try`ブロックの後に任意の`catch`節と`finally`ブロックが続く形式（3行目）。
- リソース付き`try`文（4行目）。

`catch`節（5行目）は、予約語`catch`、括弧内の仮引数、コードブロック（6行目）からなります。`CatchClause {CatchClause}`が示すように、複数の`catch`節を続けられます。`finally`ブロックは予約語`finally`とコードブロックからなります（13行目）。

この記事では`try`ブロックと`catch`節を扱います。前者は例外をスローし得る文を保護し、後者は例外の捕捉と処理を定義します。

## `try`ブロック

**`try`ブロック**は、検査例外や、明示的に処理したい非検査例外をスローし得るコードを囲みます。予約語`try`の後に波括弧で囲んだブロックが続きます。例外が発生し、その文の`catch`節のいずれかで捕捉できる場合、制御はその節に移ります。

次の例では、データベースにアクセスする複数の文を`try`文で囲んでいます（3〜21行目）。`try`ブロック（3〜18行目）と、`SQLException`を対象にした`catch`節（18〜21行目）があります。

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

次のimportも必要です。ここに示した後の例では、必要な型がすでにimportされているものとします（通常、IDEがimportの追加を支援します）。

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

例のどの文が実際に例外をスローし得るかは、IDE、呼び出すメソッドのドキュメント、あるいは適切な`catch`節がない場合に生じるコンパイルエラーから確認できます。

この例で`SQLException`をスローし得るメソッドは次のとおりです。

- `DriverManager.getConnection(...)` — 4行目。
- `Connection.createStatement()` — 9行目。
- `Statement.executeQuery(...)` — 10行目。
- `ResultSet.next()` — 12行目。
- `ResultSet.getInt(...)` — 13行目。
- `ResultSet.getString(...)` — 14行目。
- `ResultSet.close()` — 15行目。
- `Statement.close()` — 16行目。
- `Connection.close()` — 17行目。

つまり、接続の開始、文の作成、問い合わせの実行、結果の走査、リソースの解放といった、この例のほとんどのデータベース操作が`SQLException`をスローし得ます。

IDEは保護が必要な呼び出しも示せます。メソッドが例外をスローし得ることが分かるのは、「捕捉または宣言」の要件があるためです。

メソッド自身で検査例外を処理する方法が分からない場合、あるいはそこで処理するのが適切でない場合は、シグネチャに`throws`節を追加します。たとえば`DriverManager`の`getConnection`のシグネチャは次のとおりです。

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

このため、`getConnection`を呼び出すコードは、呼び出しを`try`文で囲むか、自身のメソッドのシグネチャに`throws`節を追加しなければなりません。

## `catch`節

**`catch`節**は`try`ブロックで生じた例外を処理します。スローされ得る検査例外ごとに別の節を設けられます。次の例の`catch`節は、例外の詳細（5〜10行目）、すなわちメッセージ（7行目）、SQL状態（8行目）、データベース固有のエラーコード（9行目）を表示します。

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

たとえば`try`内のSQL文でテーブル名`student`を`studnet`と誤入力すると、PostgreSQLでは次のような情報を持つ`SQLException`がスローされます。

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

縦棒（`|`）を使えば、一つの`catch`節で複数の例外型を処理できます。開発者が`Class.forName`でJDBCドライバを明示的にロードし（4行目）、二種類の例外を同じ方法で処理したいとします。縦棒によって、`catch`節が`SQLException`と`ClassNotFoundException`の両方を捕捉すると指定できます（7行目）。

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

ドライバが見つからなければ、プログラムは次のような出力を行います（注: 完全なプログラムには`import`行もあるため、`DBExample.java`の実際の行番号はもう少し大きくなります）。

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

例外型ごとに`catch`節を設け、処理を変える方法もあります。次の例では、`SQLException`用の節は7行目、`ClassNotFoundException`用の節は12行目から始まります。

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

ここでは型ごとに異なる二つの例外処理ブロックがあります。複数の型が共通のスーパークラスを持つ場合（あるいは一方が他方のスーパークラスの場合）は、一つのブロックで処理することもできます。

---

*この記事は、Eduardo Kessler Piveta著『[Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP)』の内容をもとにしています。*
