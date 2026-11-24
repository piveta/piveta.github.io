---
layout: post
title: "Menyisipkan Mahasiswa dengan PreparedStatement"
date: 2026-11-24
lang: id
translation_id: inserindo-alunos-preparedstatement-java
permalink: /id/inserting-students-with-preparedstatement-in-java/
share_text: >-
  Tiga penyisipan langsung memakai pernyataan berparameter yang sama tanpa array atau perulangan.
---

`PreparedStatement` memuat SQL dengan parameter `?`. `setInt` dan `setString` memberikan nilai tanpa menggabungkannya ke teks SQL, sehingga mengurangi risiko injeksi SQL. Dalam potongan ini, `c` adalah koneksi ke `academic`; tabel `student` memiliki `enrollment_number` dan `name`.

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

Posisi 1 adalah nomor registrasi dan posisi 2 adalah nama. Pernyataan yang sama dijalankan untuk Maria, Pedro, dan João. SQL yang setara adalah:

```sql
insert into student(enrollment_number, name) values (1, 'Maria');
insert into student(enrollment_number, name) values (2, 'Pedro');
insert into student(enrollment_number, name) values (3, 'João');
```

Nomor yang duplikat melanggar kunci primer dan menimbulkan `SQLException`. Metode `main` dalam program lengkap meneruskan pengecualian tersebut dan menutup sumber daya pada akhir proses.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
