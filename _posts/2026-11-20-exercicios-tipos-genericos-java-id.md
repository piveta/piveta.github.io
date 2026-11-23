---
layout: post
title: "Latihan generik Java"
date: 2026-11-20
lang: id
translation_id: exercicios-tipos-genericos-java
permalink: /id/java-generics-exercises/
share_text: >-
  Sepuluh latihan tentang metode generik, wildcard, pewarisan, Optional<T>, dan Box<T>.
---

Latihan ini berasal dari bab generik **Orientação a Objetos com Java**. Struktur kode mengikuti buku; pengenal, komentar, dan pesan menggunakan bahasa Inggris.

1. Pelajari antarmuka utama framework koleksi Java dan jelaskan bagaimana generik memungkinkan struktur dipakai ulang tanpa mengubah kelasnya.
2. Buat metode statis generik `max` yang menerima dua objek `Comparable` dan mengembalikan yang lebih besar.
3. Buat metode statis yang menerima serta mencetak daftar bertipe apa saja. Gunakan wildcard.
4. Buat metode yang menjumlahkan daftar numerik. Gunakan `extends` agar hanya menerima daftar `Number`.
5. Perhatikan hierarki berikut:

   ```java
   class Instrument { }
   class Strings extends Instrument { }
   class Percussion extends Instrument { }
   class Wind extends Instrument { }
   class Guitar extends Strings { }
   class Drums extends Percussion { }
   class Flute extends Wind { }
   ```

   Metode ini menerima daftar instrumen atau subkelasnya:

   ```java
   static void play(List<? extends Instrument> instruments) {
       for (Instrument i : instruments)
           IO.println("Playing " +
                       i.getClass().getSimpleName());
   }
   ```

   Kirim daftar `Guitar` dan `Flute`. Lalu coba tambahkan instrumen di dalam metode dan amati kesalahan kompilasinya.
6. Implementasikan metode generik yang menerima elemen yang sekaligus `Number` dan `Comparable`, lalu mengembalikan yang terbesar.
7. Implementasikan metode berikut dan uji dengan daftar `Car`, `Motorcycle`, dan `Vehicle`:

   ```java
   void printInvariant(List<Vehicle> list){
       // Implement
   }
   void printCovariant(List<? extends Vehicle> list){
       // Implement
   }
   void printContravariant(List<? super Vehicle> list){
       // Implement
   }
   ```

8. Coba tulis `boolean checkList(Object obj)` untuk mengenali hanya `List<String>`. Selidiki apakah Java mendukungnya secara langsung dan usulkan alternatif memakai `List<?>` atau `List<Object>`.
9. Pelajari `Optional<T>` dan buat `printOptional(Optional<T> opt)` untuk mencetak nilainya atau *empty*. Uji dengan `Optional<String>` dan `Optional<Integer>`.
10. Buat `Box<T>` dengan `store(T item)` (menolak `null`), `get()`, dan `compare(Box<T> b1, Box<T> b2)` menggunakan `compareTo`. Tambahkan `compareWithInheritance` untuk kotak bertipe berbeda yang terkait pewarisan, memakai `<? extends T>` atau `<? super T>`. Uji:

    ```java
     Box<Integer> box1 = new Box<>();
     Box<Integer> box2 = new Box<>();
     box1.store(10);
     box2.store(5);
     boolean result = Box.compare(box1, box2); // true

     Box<Double> box3 = new Box<>();
     Box<Integer> box4 = new Box<>();
     box3.store(7.5);
     box4.store(5);
     boolean result2 = Box.compareWithInheritance(box3,
        box4); // true
    ```

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
