---
layout: post
title: "Polimorfisme di Java"
date: 2026-10-21
lang: id
translation_id: polimorfismo-em-java
permalink: /polimorfisme-java-id/
share_text: >-
  Pengantar polimorfisme ad hoc, parametrik, dan subtipe dengan contoh Java.
---

Dalam pemrograman berorientasi objek, **polimorfisme** adalah kemampuan suatu operasi untuk berperilaku berbeda bergantung pada kelas objek yang terlibat. Bentuk utamanya adalah:

- **Polimorfisme ad hoc (atau overloading)**: metode dengan nama yang sama dapat memiliki parameter berbeda; pemanggilan memilih versi yang sesuai dengan argumennya.
- **Polimorfisme parametrik**: kelas dan metode generik bekerja dengan tipe yang ditentukan saat digunakan.
- **Polimorfisme subtipe**: subkelas dapat meng-override metode, dan implementasi yang dijalankan bergantung pada kelas konkret objek.

Contoh berikut memperlihatkan ketiga bentuk tersebut di Java, dimulai dengan overloading. Kelas `Figure` memiliki dua metode bernama `resize`. Metode pertama menerima `percentage` bertipe `Double`; metode kedua menerima koordinat `x` dan `y` bertipe `Integer`.

```java
public class Figure {
    public void resize(Double percentage) {
        // Mengubah ukuran berdasarkan persentase
    }
    public void resize(Integer x, Integer y) {
        // Mengubah ukuran berdasarkan koordinat
    }
}
```

Untuk **polimorfisme parametrik**, kita dapat membuat tipe berparameter menggunakan `<` dan `>`. Kelas `ArrayList`, misalnya, memiliki parameter tipe `E` yang menentukan tipe objek yang dapat disimpan oleh daftar. Parameter ini juga digunakan sebagai parameter formal metode `add`. Jadi, tipe yang diharapkan oleh `add` sama dengan tipe yang digunakan saat `ArrayList` dibuat. Perhatikan bahwa kelas ini memperluas `AbstractList` dan mengimplementasikan antarmuka `List`, `RandomAccess`, `Cloneable`, dan `Serializable`, antara lain, dengan tipe `E` yang sama.

```java
public class ArrayList<E> extends AbstractList<E>
       implements List<E>, RandomAccess, Cloneable,
                  java.io.Serializable {
    public boolean add(E element) {
        // Implementasi add
    }
    // Metode dan field lain dari kelas ini
}
```

Sebagai contoh, kita dapat membuat daftar string dengan parameter tipe `String` dan memasukkan elemen dengan memanggil `add`[^8].

```java
var names = new ArrayList<String>();
names.add("Mary");
names.add("John");
```

Dalam hal ini, compiler mengharapkan argumen untuk `add` bertipe `String`. Mengirim objek bertipe lain menyebabkan kesalahan kompilasi. Jika menginginkan daftar bilangan bulat, kita dapat memberikan tipe lain kepada `ArrayList`, yaitu `Integer`:

```java
var numbers = new ArrayList<Integer>();
numbers.add(10);
numbers.add(20);
```

Untuk **polimorfisme subtipe**, misalkan kelas `Figure` memiliki metode `draw` yang juga dapat dipanggil pada objek kelas `Triangle`, `Circle`, dan `Rectangle`. Setiap kelas tersebut meng-override metode untuk menerapkan perilaku menggambarnya sendiri. Pada kode berikut, setiap pemanggilan `draw` menjalankan implementasi berbeda sesuai kelas objek yang diberikan kepada `figure`: `Circle`, `Triangle`, atau `Rectangle`.

```java
Figure figure = new Circle(10);
// Memanggil metode draw milik Circle
figure.draw();
figure = new Triangle(20);
// Memanggil metode draw milik Triangle
figure.draw();
figure = new Rectangle(10, 20);
// Memanggil metode draw milik Rectangle
figure.draw();
```

[^8]: Untuk menggunakan `ArrayList`, biasanya kita perlu mengimpornya dengan `import java.util.ArrayList;`. Berkas sumber ringkas tidak memerlukan import. Dalam berkas sumber biasa, modul `java.base` dapat diimpor dengan `import module java.base;`.

---

*Artikel ini mengadaptasi konten dari buku <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> karya <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artikel terkait

- [Konsep dasar pemrograman berorientasi objek](/konsep-dasar-oop-id/)
- [Kelas di Java](/kelas-java-id/)
- [Pewarisan di Java](/pewarisan-java-id/)
- [Antarmuka di Java](/antarmuka-java-id/)
- [Tautan OOP dan Java](/tautan-oop-java-id/)
- [Latihan pemrograman berorientasi objek](/latihan-oop-id/)
