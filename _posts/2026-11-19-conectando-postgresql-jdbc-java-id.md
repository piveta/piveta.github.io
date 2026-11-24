---
layout: post
title: "Menghubungkan Java ke PostgreSQL dengan JDBC"
date: 2026-11-24
lang: id
translation_id: conectando-postgresql-jdbc-java
permalink: /id/connecting-to-postgresql-with-jdbc-in-java/
share_text: >-
  DriverManager membuka koneksi ke academic sebelum menjalankan operasi SQL.
---

JDBC memungkinkan program Java mengakses basis data relasional. `DriverManager.getConnection` menerima URL PostgreSQL, nama pengguna, dan kata sandi, lalu mengembalikan `Connection`. Basis data `academic` dan tabel `student(enrollment_number, name)` harus ada; proyek juga memerlukan driver JDBC PostgreSQL.

Program lengkap berikut menggunakan kode bahasa Inggris untuk menyisipkan, menampilkan, mengubah, dan menghapus mahasiswa. Nama pengguna dan kata sandi tetapnya adalah `postgres`; instalasi lokal harus menerima kredensial tersebut.

```java
public class DBExample {
    public static void main(String[] args) 
        throws SQLException {
        var c = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/academic", 
            "postgres", "postgres");
     
        IO.println("Inserting students...");
        var p = c.prepareStatement("insert into student " + 
                "(enrollment_number, name) values (?, ?)");
        p.setInt(1, 1);
        p.setString(2, "Maria");
        p.execute();
        p.setInt(1, 2);
        p.setString(2, "Pedro");
        p.execute();
        p.setInt(1, 3);
        p.setString(2, "João");
        p.execute();

        IO.println("Listing students...");
        var s = c.createStatement();      
        var rs = s.executeQuery(
          "select * from student order by enrollment_number");
        while (rs.next()) 
            IO.println(rs.getInt("enrollment_number") + " - " + 
                rs.getString("name"));

        IO.println("Updating a student...");
        p = c.prepareStatement(
          "update student set name = ? where enrollment_number = ?");
        p.setInt(2, 1);
        p.setString(1, "Maria da Silva");
        p.execute();

        IO.println("Listing students...");
        rs = s.executeQuery(
          "select * from student order by enrollment_number");
        while (rs.next()) 
            IO.println(rs.getInt("enrollment_number") + " - " +
                rs.getString("name"));

        IO.println("Deleting all students...");
        s.executeUpdate("delete from student");
        rs.close();
        s.close();
        p.close();
        c.close();
    }
}
```

Dalam URL, `localhost` adalah server, `5432` adalah port, dan `academic` adalah nama basis data. `main` mendeklarasikan `throws SQLException` sehingga kesalahan JDBC diteruskan. Setelah alur normal selesai, sumber daya ditutup secara eksplisit dengan `close()`.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
