---
layout: post
title: "Try-with-resources dalam Java"
date: 2026-11-18
lang: id
translation_id: try-com-recursos-java
permalink: /id/try-with-resources-in-java/
share_text: >-
  Try-with-resources menutup objek AutoCloseable secara otomatis. Contoh JDBC menunjukkan pengelolaan koneksi, pernyataan, dan hasil kueri dalam satu pernyataan try.
---

Untuk memperbaiki pengelolaan sumber daya, sejak versi 7 Java mengizinkan sumber daya yang dapat ditutup pada akhir pernyataan `try` untuk dinyatakan di dalam pernyataan itu. Menurut spesifikasi bahasa, pernyataan `try` dapat menyatakan satu atau beberapa sumber daya yang mengimplementasikan antarmuka `AutoCloseable`. Menurut dokumentasinya, lebih dari seratus kelas dalam pustaka standar mengimplementasikan antarmuka tersebut. Definisinya sebagai berikut:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

Sintaks try-with-resources adalah:

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

Sumber daya dinyatakan dalam tanda kurung, biasanya melalui deklarasi variabel lokal atau akses ke variabel yang sudah pasti diberi nilai dan bersifat *effectively final* (tidak pernah diberi nilai baru; modifier `final` tidak wajib). Dalam kueri JDBC, koneksi, pernyataan, dan himpunan hasil harus ditutup. Contoh berikut menempatkan deklarasi dan inisialisasi `c` (baris 5), `s` (baris 8), dan `rs` (baris 9) di dalam spesifikasi sumber daya untuk try-with-resources:

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

Dengan demikian, blok `finally` tidak diperlukan: semua sumber daya yang dinyatakan ditutup secara otomatis oleh lingkungan eksekusi Java. Pendekatan ini menyederhanakan kode dan mengurangi kemungkinan sumber daya dibiarkan terbuka. Inilah pendekatan yang disarankan untuk kode yang mengelola sumber daya.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
