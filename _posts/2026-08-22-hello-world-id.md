---
layout: post
title: "Hello World - Versi Tradisional vs. Versi Sederhana"
date: 2026-08-22
lang: id
translation_id: hello-world
permalink: /hello-world-id/
share_text: >-
  Contoh ini membandingkan kelas Java tradisional dengan metode main dan bentuk peluncuran yang lebih ringkas di Java 25+. Kedua cara menghasilkan keluaran Hello World yang sama.
---

Sudah umum untuk memulai mempelajari bahasa pemrograman dengan menulis program bernama **Hello World**, yang menampilkan teks `Hello World!` pada keluaran standar perangkat, biasanya layar. Dalam Java, kita dapat menulis program ini sebagai berikut:

```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
```

Dalam program ini, kita memiliki kelas bernama `Hello`. Dalam sistem berorientasi objek, kelas membantu memodelkan konsep dari domain aplikasi yang sedang dipelajari. Kelas mengenkapsulasi data dan perilaku yang terkait dengan konsep tertentu.

Kelas `Hello` memiliki satu metode bernama `main`, yang menerima array string yang berisi argumen baris perintah yang diberikan ketika program dijalankan, jika ada. Dalam contoh ini, argumen tersebut tidak digunakan.

Metode `main` bersifat static, yang berarti metode tersebut merupakan metode kelas, bukan metode instance. Oleh karena itu, metode tersebut dapat dipanggil tanpa membuat objek dari kelas `Hello`.

Di dalam metode `main`, terdapat pemanggilan metode `println`. Metode ini merupakan bagian dari kelas `PrintStream` dan mencetak nilai yang diberikan sebagai argumen ke layar, diikuti terminator baris.

Metode `println` dipanggil melalui field `out` dari kelas `System`. Field ini bertipe `PrintStream` dan menyediakan akses ke keluaran standar sistem.

## Kompilasi dan eksekusi

Program Java pertama-tama dikompilasi menjadi representasi perantara yang disebut **bytecode**, yang memastikan portabilitas. Bytecode tersebut kemudian dieksekusi oleh Java Virtual Machine (JVM), yang mengubahnya menjadi kode mesin yang sesuai dengan platform yang mendasarinya.

Untuk mengompilasi program, program harus disimpan dalam file bernama `Hello.java`. Dalam Java, file yang berisi tipe public biasanya memiliki nama yang sama dengan tipe tersebut.

Kita dapat menggunakan integrated development environment (**IDE**) atau menjalankan compiler secara langsung dari command line, asalkan JDK telah terpasang.

Program Java biasanya ditulis dalam IDE, yang menyediakan berbagai fitur untuk meningkatkan produktivitas selama pengembangan, seperti navigasi kode sumber, refactoring, analisis statis, kompilasi, pengujian, dan debugging.

Beberapa IDE Java yang populer adalah:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Eclipse](https://www.eclipse.org/)
- [VS Code](https://code.visualstudio.com/)

Kita juga dapat mengompilasi program secara langsung dari command line menggunakan compiler `javac`:

```text
    javac Hello.java
```

Perintah tersebut menerima `Hello.java` sebagai input dan menghasilkan file `Hello.class`, yang berisi versi program yang telah dikompilasi.

Setelah kompilasi, kita dapat menjalankan program menggunakan perintah `java`:

```text
    java Hello
```

Outputnya adalah:

```text
    Hello World!
```

## Pendekatan yang lebih sederhana dengan Java 25+

Mulai Java 25, sebuah fitur yang dikembangkan sebagai *preview* sejak Java 21 menjadi permanen: **Compact Source Files and Instance Main Methods**. Fitur ini memungkinkan program kecil ditulis dengan lebih sedikit boilerplate dengan menghilangkan deklarasi kelas secara eksplisit dan menyederhanakan metode `main`.

Dengan demikian, program sebelumnya dapat ditulis dalam Java 26 (versi saat ini) sebagai berikut:

```java
    void main() {
        IO.println("Hello World!");
    }
```

Dalam kasus ini, kita tidak perlu mendeklarasikan kelas secara eksplisit atau menulis `public static void main(String[] args)`. Compiler memperlakukan file tersebut seolah-olah mendeklarasikan sebuah kelas secara implisit, dan metode `main` dapat menjadi metode instance.

Kita juga dapat menggunakan kelas `IO`, yang menyediakan operasi input dan output konsol sederhana. Dalam Java 26, `IO` berada dalam package `java.lang` dan karena itu tersedia secara implisit. Namun, untuk memanggil metodenya, kita tetap perlu menggunakan nama kelas, seperti pada `IO.println(...)`.

Karena fitur ini tidak lagi berstatus *preview*, kita tidak memerlukan opsi kompilasi khusus. Program dapat dikompilasi secara normal:

```text
    javac Hello.java
```

dan dijalankan dengan cara yang sama:

```text
    java Hello
```

Kita juga dapat menjalankan file sumber secara langsung menggunakan launcher `java`:

```text
    java Hello.java
```

Dalam kasus ini, kode sumber dikompilasi di memori oleh launcher itu sendiri sebelum eksekusi. Mekanisme ini memungkinkan program dijalankan langsung dari file sumber tanpa menghasilkan file `.class` secara eksplisit.

Penggunaan compact source files sangat menarik untuk contoh-contoh kecil, program pembelajaran, script, dan eksperimen. Ketika program berkembang dan membutuhkan struktur yang lebih rumit, kita dapat kembali secara alami ke bentuk tradisional dengan deklarasi kelas dan metode yang eksplisit.

Proses yang dilakukan oleh IDE pada dasarnya serupa. Selain kompilasi dan eksekusi, IDE menyediakan fitur untuk debugging, pengujian, refactoring, pembuatan dan pengelolaan proyek, pembuatan library, manajemen versi, dan berbagai tugas lainnya.

---

*Artikel ini merupakan adaptasi dari isi buku <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, karya <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
