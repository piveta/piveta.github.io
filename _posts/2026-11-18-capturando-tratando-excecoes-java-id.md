---
layout: post
title: "Menangkap dan Menangani Pengecualian dalam Java"
date: 2026-11-24
lang: id
translation_id: capturando-tratando-excecoes-java
permalink: /id/catching-and-handling-exceptions-in-java/
share_text: >-
  Blok try dan klausa catch dalam Java menangani pengecualian. Contoh JDBC menunjukkan SQLException, multi-catch, dan penanganan terpisah untuk berbagai tipe pengecualian.
---

Ketika pengecualian terjadi (baik akibat kesalahan maupun situasi di luar alur yang diharapkan), metode tempat kejadian membuat objek dari kelas pengecualian dan mengirimkannya ke sistem eksekusi (JVM), bersama informasi terkait pengecualian tersebut.

JVM kemudian menelusuri tumpukan pemanggilan untuk menemukan penangan pengecualian yang cocok dengan objek itu. Pencarian dimulai dari metode tempat pengecualian muncul. Jika metode tersebut memiliki penangan yang sesuai, pengecualian ditangani di sana. Jika tidak, JVM memeriksa metode pemanggilnya. Pencarian berlanjut di sepanjang tumpukan pemanggilan sampai penangan ditemukan atau pemanggil awal tercapai. Jika tidak ada metode yang menangani pengecualian, JVM menghentikan program dan mencetak pesan kesalahan serta jejak tumpukan yang mengarah ke pengecualian.

Kode Java yang dapat melempar pengecualian checked wajib **menangkap atau mendeklarasikan** pengecualian. Dengan demikian:

- Pernyataan yang dapat melempar pengecualian harus ditempatkan di dalam blok terlindung (blok `try`) dengan penangan yang sesuai (klausa `catch`); atau
- Metode yang memuat pernyataan tersebut harus mendeklarasikan dengan `throws` bahwa ia dapat melempar pengecualian. Metode itu tidak menanganinya; pemanggil harus menangani pengecualian atau mendeklarasikan bahwa ia juga dapat melemparkannya.

Untuk penanganan pengecualian, Java menyediakan **pernyataan `try`** yang terdiri atas tiga bagian:

- Blok `try` berisi pernyataan yang dapat melempar pengecualian dan dapat pula memuat pernyataan lain. Secara opsional, deklarasi atau inisialisasi sumber daya dapat muncul dalam tanda kurung tepat setelah kata kunci `try`; ini disebut try-with-resources.
- Nol (Catatan: Blok `try` dapat berdiri sendiri hanya ketika sumber daya dideklarasikan atau diinisialisasi dalam pernyataan try-with-resources. Jika tidak, diperlukan setidaknya satu klausa `catch` atau blok `finally`.) atau lebih klausa `catch` berisi blok penanganan pengecualian. Pengembang menentukan tindakan untuk setiap pengecualian yang akan ditangani jika dilempar selama blok `try` berjalan.
- Nol atau satu blok `finally` berisi kode pembersihan, biasanya untuk menutup berkas atau melepaskan sumber daya. Pernyataannya berjalan terlepas dari apakah blok `try` selesai dengan sukses.

Sebagian sintaks pernyataan `try` (Catatan: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20>) ditunjukkan di bawah ini:

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

Jadi, pernyataan `try` (baris 1) terdiri atas:

- Blok `try` diikuti klausa `catch` (baris 2);
- Blok `try` diikuti klausa `catch` opsional dan blok `finally` (baris 3); atau
- Pernyataan try-with-resources (baris 4).

Klausa `catch` (baris 5) terdiri atas kata kunci `catch`, diikuti parameter formal dalam tanda kurung, kemudian blok kode (baris 6). Beberapa klausa `catch` dapat berurutan, seperti ditunjukkan oleh `CatchClause {CatchClause}`. Blok `finally` terdiri atas kata kunci `finally` diikuti blok kode (baris 13).

Artikel ini berfokus pada blok `try` dan klausa `catch`: blok pertama melindungi pernyataan yang dapat melempar pengecualian, sedangkan klausa berikutnya menentukan cara menangkap dan menanganinya.

## Blok `try`

**Blok `try`** membungkus kode yang dapat melempar pengecualian, baik pengecualian checked maupun pengecualian unchecked yang ingin kita tangani secara eksplisit. Kata kunci `try` diikuti blok dalam kurung kurawal. Jika muncul pengecualian yang dapat ditangkap oleh salah satu klausa `catch` milik pernyataan tersebut, kendali berpindah ke klausa itu.

Contoh berikut menunjukkan pernyataan `try` yang membungkus beberapa pernyataan akses basis data (baris 3 hingga 21). Ada blok `try` (baris 3 hingga 18) dan klausa `catch` untuk `SQLException` (baris 18 hingga 21):

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

Impor berikut juga diperlukan. Impor ditampilkan di sini; contoh selanjutnya menganggap tipe yang relevan sudah diimpor (IDE biasanya membantu menambahkan impor):

```java
import java.sql.DriverManager;
import java.sql.SQLException;
```

Untuk mengetahui pernyataan mana dalam contoh yang benar-benar dapat melempar pengecualian, kita dapat menggunakan IDE, membaca dokumentasi metode yang dipanggil, atau melihat kesalahan kompilasi yang muncul tanpa klausa `catch` yang sesuai.

Dalam contoh ini, metode yang dapat melempar `SQLException` adalah:

- `DriverManager.getConnection(...)` — baris 4;
- `Connection.createStatement()` — baris 9;
- `Statement.executeQuery(...)` — baris 10;
- `ResultSet.next()` — baris 12;
- `ResultSet.getInt(...)` — baris 13;
- `ResultSet.getString(...)` — baris 14;
- `ResultSet.close()` — baris 15;
- `Statement.close()` — baris 16;
- `Connection.close()` — baris 17.

Dengan kata lain, hampir semua operasi basis data di sini—membuka koneksi, membuat pernyataan, menjalankan kueri, menelusuri hasil, dan menutup sumber daya—dapat melempar `SQLException`.

IDE juga dapat menunjukkan pemanggilan mana yang harus dilindungi. IDE mengetahui bahwa metode dapat melempar pengecualian karena kewajiban untuk menangkap atau mendeklarasikannya.

Jika metode tidak dapat menangani pengecualian checked, atau penanganan di dalamnya tidak tepat, metode menambahkan klausa `throws` pada tanda tangannya. Sebagai contoh, tanda tangan metode `getConnection` dalam `DriverManager` adalah:

```java
public static Connection getConnection(String url, 
    String user, String password) throws SQLException;    
```

Artinya, kode yang memanggil `getConnection` harus membungkus pemanggilan itu dalam pernyataan `try` atau menambahkan klausa `throws` pada tanda tangan metodenya sendiri.

## Klausa `catch`

**Klausa `catch`** menangani pengecualian yang muncul dalam blok `try`. Kita dapat menyediakan klausa `catch` terpisah untuk setiap pengecualian checked yang mungkin dilempar. Dalam contoh berikut, klausa `catch` menampilkan rincian pengecualian (baris 5 hingga 10): pesan (baris 7), status SQL (baris 8), dan kode kesalahan khusus basis data (baris 9):

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

Jika, misalnya, kita mengetik `studnet` sebagai ganti `student` untuk nama tabel dalam pernyataan SQL di dalam `try`, sebuah `SQLException` akan dilempar dengan informasi seperti berikut (dalam PostgreSQL):

```text
Message: ERROR: relation "studnet" does not exist
  Position: 15
SQLState: 42P01
Error: 0
```

Klausa `catch` juga dapat menangani lebih dari satu tipe pengecualian dengan tanda garis vertikal (`|`). Misalkan pengembang ingin memuat driver JDBC secara eksplisit dengan `Class.forName` (baris 4) dan menangani kedua kemungkinan pengecualian dengan cara yang sama. Garis vertikal menyatakan bahwa klausa `catch` menangkap `SQLException` dan `ClassNotFoundException` (baris 7):

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

Jika driver tidak ditemukan, program menampilkan kira-kira berikut ini (Catatan: Nomor baris dalam `DBExample.java` sebenarnya sedikit lebih tinggi dalam program lengkap karena program juga memuat baris `import`):

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

Pilihan lainnya adalah menyediakan satu klausa `catch` untuk tiap tipe pengecualian dan menyesuaikan penanganannya. Dalam contoh berikut, klausa `catch` untuk `SQLException` dimulai pada baris 7, sedangkan klausa untuk `ClassNotFoundException` dimulai pada baris 12:

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

Di sini terdapat dua blok penanganan pengecualian yang berbeda, satu untuk setiap tipe. Beberapa tipe juga dapat ditangani dalam satu blok jika memiliki kelas induk yang sama (atau jika salah satu tipe merupakan kelas induk tipe lainnya).

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
