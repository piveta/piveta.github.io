---
layout: post
title: "Konsep dasar pemrograman berorientasi objek"
date: 2026-10-21
lang: id
translation_id: conceitos-basicos-poo-java
permalink: /konsep-dasar-oop-id/
share_text: >-
  Pengantar konsep dasar pemrograman berorientasi objek: kelas, objek, atribut, metode, enkapsulasi, pewarisan, polimorfisme, dan hubungan antarkelas.
---

Pemrograman terstruktur menyediakan mekanisme untuk memodularisasi konsep dalam sistem perangkat lunak melalui struktur data dan algoritma yang memanipulasinya. Bahasa terstruktur yang umum digunakan memungkinkan berbagai tipe data dan variabel untuk menyatakan karakteristik serta properti konsep terkait, juga prosedur dan fungsi untuk memodelkan operasinya.

Namun, saat mencoba menggunakan kembali komponen yang ditulis dengan bahasa terstruktur, kita perlu mengetahui hubungan antara data — yang direpresentasikan oleh struktur data, tipe data, dan variabel — dan perilaku — yang dinyatakan melalui prosedur dan fungsi. Karena itu, penggunaan kembali biasanya berlangsung pada tingkat yang rinci dan sering membutuhkan usaha besar, misalnya untuk menentukan prosedur dan fungsi mana yang berkaitan dengan struktur data tertentu. Pustaka yang dapat digunakan kembali memang bisa dibuat, tetapi hubungan antara data dan perilaku tidak dinyatakan secara eksplisit atau dipusatkan dalam satu abstraksi.

**Pemrograman berorientasi objek** (OOP) adalah paradigma pemrograman yang merepresentasikan konsep dalam suatu domain aplikasi melalui tipe data abstrak yang disebut kelas. Kelas memodelkan karakteristik dan properti konsep tersebut sekaligus operasinya. OOP memperluas pemrograman terstruktur dengan menyediakan cara untuk menentukan dan menyusun kelas agar dapat memodelkan sistem komputasi yang lengkap, dengan tujuan meningkatkan modularitas dan penggunaan kembali komponen.

Saat ini, pemrograman berorientasi objek merupakan salah satu paradigma yang paling banyak diterima dan digunakan dalam pengembangan perangkat lunak. Banyak bahasa modern mendukungnya, termasuk Java, C++, C#, Python, Kotlin, JavaScript, TypeScript, Swift, dan Ruby.

**Kelas** adalah mekanisme abstraksi untuk merepresentasikan konsep dalam domain aplikasi tertentu. Dalam domain perbankan, misalnya, konsepnya dapat berupa cabang, rekening, nasabah, dan transaksi. Kita dapat mendefinisikan kelas `Branch`, `Account`, `Customer`, dan `Transaction` untuk merepresentasikannya. Gambar berikut memperlihatkan representasi grafis kelas-kelas tersebut.

<img src="/images/en/oopClasses.svg" alt="Kelas Branch, Account, Customer, dan Transaction." style="max-width: 300px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Kelas berfungsi sebagai *templat* untuk membuat contoh konkret dan dapat dimanipulasi dari konsep tersebut. Contoh itu disebut **objek**. Objek merupakan **instans** dari sebuah kelas, sedangkan proses membuat objek disebut **instansiasi**. Sebagai contoh, kita dapat membuat objek untuk merepresentasikan nasabah *John*, *Peter*, dan *Mary*, beserta informasi pribadi dan fungsi yang tersedia bagi nasabah.

<img src="/images/en/oopObjects.svg" alt="Objek John, Peter, dan Mary masing-masing merupakan instans kelas Customer." style="max-width: 380px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Kelas didefinisikan untuk merepresentasikan properti, karakteristik, dan perilaku suatu konsep. Dua mekanisme utama untuk melakukannya adalah atribut dan metode.

**Atribut** merepresentasikan karakteristik atau properti objek dalam suatu kelas. Atribut kelas `Customer` misalnya *name*, *age*, *address*, dan *marital status*. Setiap nasabah dapat memiliki nilai atribut yang berbeda. Sebagai contoh, sebuah objek nasabah dapat memiliki nilai *name* $`=`$ John Smith, *age* $`=`$ 50, *address* $`=`$ 205 President Vargas Street, dan *marital status* $`=`$ married.

**Metode** merepresentasikan perilaku. Metode kelas `Account`, misalnya, dapat berkaitan dengan operasi *membuka*, *menutup*, atau *mengubah pemilik rekening*. **Memanggil** atau **menginvokasi** metode akan menjalankan operasi yang diimplementasikan metode tersebut. Kelas biasanya memiliki metode khusus untuk membuat (menginstansiasi) objek yang disebut **konstruktor**, dan untuk menghancurkan objek yang disebut **destruktor**.

Atribut dan metode juga terbagi menjadi dua kategori: instans dan kelas. **Atribut dan metode instans** paling umum digunakan dan diakses melalui objek dari kelas tersebut. Keduanya merepresentasikan karakteristik serta operasi yang terkait dengan masing-masing instans. Atribut instans kelas `Account` dapat mencakup *bank*, *branch*, *account number*, dan *account holder*; metode instansnya dapat mencakup *withdraw*, *transfer*, dan *deposit*. Sementara itu, **atribut dan metode kelas** dimiliki oleh kelas itu sendiri, bukan instansnya. Contohnya, atribut kelas dapat menghitung jumlah instans `Account` yang telah dibuat dan metode kelas dapat mengembalikan jumlah tersebut.

Untuk membatasi akses ke atribut dan metode, kelas menyediakan mekanisme **enkapsulasi dan penyembunyian informasi**. Bahasa pemrograman biasanya menyediakan modifier visibilitas yang menentukan siapa yang dapat mengakses atribut, metode, atau kelas tertentu.

Kelas merupakan mekanisme abstraksi yang merepresentasikan dan mengenkapsulasi konsep dari dunia nyata dan dunia komputasi. Abstraksi ini dapat digabungkan melalui berbagai hubungan agar kelas-kelas bekerja sama memenuhi kebutuhan aplikasi. Hubungan utama antarkelas meliputi pewarisan, asosiasi, agregasi, komposisi, dan realisasi.

**Pewarisan** adalah mekanisme komposisi yang memungkinkan kelas menggunakan kembali antarmuka dan perilaku kelas yang sudah ada dengan memperluas fungsinya. Kelas yang memperluas kelas lain disebut **subkelas**, sedangkan kelas yang diperluas disebut **superkelas**. Perluasan biasanya dideklarasikan pada subkelas, misalnya `SubClass` memperluas `SuperClass`.

Gambar 3 memperlihatkan kelas `Shape`, `Rectangle`, `Triangle`, dan `Circle`. `Shape` adalah superkelas, sedangkan `Rectangle`, `Triangle`, dan `Circle` merupakan subkelasnya.

<img src="/images/en/oopInheritance.png" alt="Shape merupakan superkelas dari Rectangle, Triangle, dan Circle." style="max-width: 400px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Mekanisme pewarisan berbeda-beda menurut bahasa pemrograman. Perbedaan tersebut biasanya berkaitan dengan visibilitas dan jumlah pewarisan. Beberapa bahasa, seperti C++, memungkinkan **visibilitas pewarisan** ditetapkan sebagai **publik** atau **privat**. Misalkan kelas `B` mewarisi kelas `A`. Dengan pewarisan publik, `B` adalah subtipe `A` dan mewarisi implementasi serta antarmuka `A`. Di mana pun objek `A` diperlukan, objek `B` (atau subkelas `A` lainnya) dapat digunakan karena setiap instans `B` juga dianggap sebagai instans `A`. Prinsip ini disebut **prinsip substitusi Liskov**. Dengan pewarisan privat, `B` bukan `A`; hanya implementasi `A` yang diwarisi dan `B` dibuat berdasarkan `A`. Prinsip substitusi Liskov tidak berlaku dalam kasus ini.

Pewarisan juga dapat berupa **tunggal atau berganda**. Pada pewarisan tunggal, seperti yang digunakan Java dan C#, sebuah kelas hanya boleh memiliki satu superkelas. Pada pewarisan berganda, seperti di C++, kelas dapat memiliki lebih dari satu superkelas. Para perancang bahasa tidak sepakat apakah manfaat pewarisan berganda sebanding dengan masalah yang dapat timbul. Bahasa lain menyediakan alternatif, seperti pewarisan virtual berbasis antarmuka, *traits*, dan *mixins*.

Gambar 4 menunjukkan contoh pewarisan berganda. `Mammal` dan `Bird` mewakili hewan. `Horse`, `Dog`, dan `Bat` adalah subkelas `Mammal`, sedangkan `Ostrich` dan `Duck` merupakan subkelas `Bird`. Kita juga ingin mengelompokkan hewan yang dapat terbang, maka dibuat kelas `Flyer` untuk objek terbang yang belum tentu hewan. Dengan pewarisan berganda, objek `Duck` dan `Bat` dapat sekaligus menjadi objek terbang dengan mewarisi `Flyer`.

<img src="/images/en/oopMultipleInheritance.png" alt="Pewarisan berganda antara kelas Animal, Bird, Flyer, dan Mammal." style="max-width: 500px; width: 100%; height: auto; display: block; margin: 20px auto;"/>

Beberapa kelas bersifat **abstrak**. Seperti kelas **konkret**, kelas abstrak merepresentasikan karakteristik dan perilaku sekumpulan objek dunia nyata, tetapi tidak dapat diinstansiasi secara langsung. Dalam contoh pewarisan berganda tadi, `Mammal`, `Bird`, dan `Flyer` dapat didefinisikan sebagai kelas abstrak karena yang ada di dunia nyata hanya contoh dari subkelasnya, seperti kuda, anjing, dan bebek.

Selain visibilitas dan jumlah pewarisan, pewarisan memungkinkan pembuatan metode polimorfik. Dalam OOP, **polimorfisme** adalah kemampuan suatu operasi untuk berperilaku berbeda, bergantung pada kelas objek yang memanggilnya. Bentuk utamanya adalah:

- **Polimorfisme ad hoc (atau overloading)** terjadi ketika metode dalam kelas memiliki nama yang sama tetapi tipe parameter formal berbeda. Argumen yang digunakan menentukan metode mana yang dipanggil.
- **Polimorfisme parametrik** terjadi ketika metode dibuat secara generik dan terikat pada tipe yang baru ditentukan kemudian, misalnya saat variabel dideklarasikan atau objek dibuat. Dalam bahasa berorientasi objek, tipe seperti ini disebut tipe generik.
- **Polimorfisme subtipe** terjadi ketika subkelas meng-override metode salah satu superkelasnya. Objek yang memanggil metode menentukan implementasi yang dijalankan. Hal ini biasanya ditentukan saat runtime melalui dynamic binding.

Selain pewarisan, ada jenis hubungan lain, termasuk asosiasi, agregasi, dan komposisi. Secara umum, perbedaannya terletak pada tingkat keterikatan antarobjek:

- Dalam **asosiasi**, hubungan antarobjek biasanya sementara dan mudah diubah saat runtime. Dalam sistem lalu lintas, misalnya, seseorang dapat diasosiasikan dengan kendaraan sebagai pengemudi. Jika pengemudinya berubah, kedua objek tetap ada meskipun asosiasinya dihapus.
- Dalam **agregasi**, hubungan lebih kuat daripada asosiasi. Objek yang diagregasi sering dibuat bersamaan dengan objek pengagregasi. Sebuah mobil, misalnya, memiliki empat roda: mobil adalah objek pengagregasi dan roda adalah objek yang diagregasi. Hubungan ini dapat diputus, tetapi mengganti roda lebih jarang dan lebih merepotkan daripada mengganti pengemudi.
- Dalam **komposisi**, hubungan lebih kuat lagi. Objek yang dikomposisikan merupakan bagian dari objek yang lebih besar. Kain jok kendaraan, misalnya, tersusun dari benang. Jika benang tidak ada lagi, jok juga tidak ada atau kehilangan identitasnya.

Hubungan antarobjek tersebut sering bersifat konseptual. Saat menerapkannya dalam bahasa pemrograman, kita dapat mengasosiasikan, mengagregasi, atau mengomposisikan objek melalui atribut kelas, lalu mengisi nilai atribut saat runtime. Waktu pembuatan objek dapat berbeda: dalam komposisi, objek bagian biasanya dibuat di konstruktor keseluruhan; dalam asosiasi, objek terkait umumnya dibuat secara terpisah lalu dihubungkan saat diperlukan.

Hubungan terakhir, yaitu **realisasi**, terjadi ketika kelas menyatakan bahwa dirinya mengimplementasikan suatu antarmuka. **Antarmuka** dapat dipandang sebagai kelas abstrak yang semua metodenya abstrak[^1]. Antarmuka berfungsi sebagai protokol antara klien dan implementornya. Kelas (atau salah satu subkelasnya) harus mengimplementasikan metode yang dideklarasikan antarmuka. Dengan demikian, klien dapat menulis kode yang memenuhi antarmuka tanpa bergantung pada cara kelas yang mengimplementasikannya bekerja.

[^1]: Sejak Java 8, antarmuka juga dapat memiliki metode konkret yang disebut metode default, dengan kata kunci `default`. Kelas yang mengimplementasikan antarmuka dengan metode default tidak wajib menyediakan implementasinya sendiri, tetapi dapat melakukannya.

---

*Artikel ini mengadaptasi konten dari buku <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> karya <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artikel terkait

- [Kelas di Java](/kelas-java-id/)
- [Pewarisan di Java](/pewarisan-java-id/)
- [Polimorfisme di Java](/polimorfisme-java-id/)
- [Antarmuka di Java](/antarmuka-java-id/)
- [Tautan OOP dan Java](/tautan-oop-java-id/)
- [Latihan pemrograman berorientasi objek](/latihan-oop-id/)
