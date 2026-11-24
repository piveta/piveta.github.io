---
layout: post
title: "Pola DAO untuk akses data dalam Java"
date: 2026-11-20
lang: id
translation_id: padrao-dao-java
permalink: /id/the-dao-pattern-for-data-access-in-java/
share_text: >-
  Data Access Object memisahkan persistensi dari aturan bisnis dan tampilan.
---

Satu kelas dapat membuka koneksi, menjalankan SQL, menerapkan aturan bisnis, dan menampilkan hasil. Saat aplikasi membesar, pemusatan ini menyulitkan pemeliharaan. Bab “Memperluas kelas: akses data” memakai pola DAO (*Data Access Object*) agar persistensi memiliki tanggung jawab tersendiri.

DAO menyediakan operasi menambah, mencari, mengubah, dan menghapus objek. Klien tidak perlu mengetahui perintah SQL, cara membuat koneksi, atau cara mengubah baris basis data menjadi objek. Dalam contoh, `Student` mewakili data, `StudentDAO` menangani tabel `student`, dan `DBExample` memanggil operasinya.

Buku mula-mula membuat DAO khusus mahasiswa, lalu memindahkan infrastruktur bersama ke `AbstractDAO<T>` dengan pewarisan dan generik. Cara klien memanggil metode publik tetap sama. JDBC digunakan langsung agar pembagian tanggung jawab terlihat jelas.

<!-- DAO_RELATIONS_START -->
{% capture dao_related_links %}
{% assign dao_related_post = site.posts | where: "url", "/id/the-student-class-in-the-dao-example/" | first %}
{% if dao_related_post %}
- [Kelas Student dalam contoh DAO](/id/the-student-class-in-the-dao-example/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/id/a-record-for-jdbc-connection-data/" | first %}
{% if dao_related_post %}
- [Record untuk data koneksi JDBC](/id/a-record-for-jdbc-connection-data/)
{% endif %}
{% assign dao_related_post = site.posts | where: "url", "/id/building-studentdao-with-crud-operations/" | first %}
{% if dao_related_post %}
- [Membuat StudentDAO dengan operasi CRUD](/id/building-studentdao-with-crud-operations/)
{% endif %}
{% endcapture %}
{% assign dao_related_links = dao_related_links | strip %}
{% if dao_related_links != "" %}
## Artikel terkait

{{ dao_related_links }}

{% endif %}

Dalam bahasa Inggris: [Versi bahasa Inggris](/en/the-dao-pattern-for-data-access-in-java/).

<!-- DAO_RELATIONS_END -->

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
