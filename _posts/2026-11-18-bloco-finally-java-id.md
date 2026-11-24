---
layout: post
title: "Blok finally dalam Java"
date: 2026-11-18
lang: id
translation_id: bloco-finally-java
permalink: /id/finally-block-in-java/
share_text: >-
  Blok finally berjalan setelah try dan catch meskipun eksekusi gagal. Contoh JDBC menunjukkan kesulitan menutup ResultSet, Statement, dan Connection secara manual.
---

Pernyataan `try` dapat memiliki blok akhir, yang disebut **blok `finally`**, yang berjalan terlepas dari apakah kode dalam blok `try` selesai dengan sukses. Dalam contoh berikut, pernyataan `try` memiliki blok `finally` (dimulai pada baris 25) yang menutup sumber daya yang dibuka dalam blok `try`: `ResultSet`, `Statement`, dan koneksi (`Connection`):

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

Namun, perhatikan bahwa metode `close` pada `ResultSet`, `Statement`, dan `Connection` sendiri dapat melempar `SQLException`. Karena itu, contoh sebelumnya tidak dapat dikompilasi. Kita harus menangani pengecualian tersebut atau mendeklarasikan bahwa kita tidak menanganinya. Kita dapat menggunakan pernyataan `try` bersarang untuk setiap pemanggilan (jika tiap pemanggilan memerlukan penanganan berbeda), atau satu pernyataan untuk ketiga pemanggilan:

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

Kode ini masih dapat melempar `NullPointerException` yang bersifat unchecked jika `rs`, `s`, atau `c` bernilai `null` (masing-masing pada baris 15, 22, dan 28). Biasanya pengecualian unchecked tidak ditangkap dan ditangani; penyebab masalahnya yang diperbaiki.

Kita dapat memeriksa bahwa setiap variabel tidak bernilai `null` sebelum memanggil `close`. Hal ini dilakukan dalam contoh berikut pada baris 4, 12, dan 20:

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

Meskipun semua langkah ini sudah dilakukan, jika pernyataan dalam blok `try` awal melempar `SQLException` dan salah satu metode `close` gagal (melempar `SQLException` baru), informasi mengenai pengecualian asli dapat hilang. Kita dapat menyimpan pengecualian asli dan menambahkan pengecualian dari `close` sebagai pengecualian yang ditekan (*suppressed exceptions*) dengan metode seperti `addSuppressed` dan `getSuppressed` pada `Throwable`. Namun, kode akan menjadi lebih rumit.

Untuk mengurangi kerumitan ini, Java menambahkan variasi pernyataan `try` yang menyatakan sumber daya untuk ditutup saat pernyataan selesai, baik eksekusi berakhir secara normal maupun tidak. Variasi ini disebut **try-with-resources** (Catatan: <https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20.3>).

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
