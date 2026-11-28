---
layout: post
title: "Membaca dan menulis di konsol Java"
date: 2026-11-20
lang: id
translation_id: leitura-escrita-java
permalink: /id/reading-and-writing-on-the-java-console/
share_text: >-
  Membaca dan menampilkan nilai dengan IO, Scanner, dan readln.
---

Di Java 25, `IO` menyediakan `print` dan `println` untuk keluaran serta `readln` untuk masukan. Impor statis memungkinkan metode itu dipanggil tanpa nama kelas.

## Menampilkan nilai

`print` tidak menambahkan baris baru, sedangkan `println` mengakhiri baris.

```java
import static java.lang.IO.*;
void main(){
    var a = 10;
    var b = 20;
    print("Result: ");
    println("Sum of a and b: " + (a + b));
}
```

Jumlah 10 dan 20 muncul bersama keterangannya dalam satu baris.

## Membaca dengan Scanner

`nextLine()` membaca satu baris dan `nextInt()` membaca bilangan bulat. Panggilan tambahan ke `nextLine()` menghabiskan karakter akhir baris sebelum alamat dibaca.

```java
import java.util.Scanner;
void main(){
    var s = new Scanner(System.in);
    IO.println("Name: ");
    var name = s.nextLine(); 
    IO.println("Age: ");
    var age = s.nextInt(); 
    s.nextLine(); // Consumes the line break
    IO.println("Address: ");
    var address = s.nextLine(); 
    IO.println("Entered data:");
    IO.println("Name: " + name + ", Age: " + age);
    IO.println("Address: " + address);
}
```

## Membaca dengan IO.readln

`readln` menampilkan teks petunjuk dan mengembalikan `String`. `Integer.parseInt` mengubah teks usia menjadi bilangan bulat.

```java
import static java.lang.IO.*; 
void main(){
    var name = readln("Name: ");
    var age = Integer.parseInt(readln("Age: ")); 
    var address = readln("Address: ");
    println("Entered data:");
    println("Name: " + name + ", Age: " + age);
    println("Address: " + address);
}
```

Masukan yang tidak valid memicu `NumberFormatException`, yang tidak ditangani dalam contoh ini. Konsol cocok untuk latihan. Aplikasi juga dapat memakai formulir atau antarmuka grafis.

Komentar satu baris dimulai dengan `//`. Komentar beberapa baris diapit oleh `/*` dan `*/`.

```java
// Single-line comment text
   
/* Comment text
   spanning multiple lines. */
```

Contoh dengan berkas sumber ringkas mungkin memerlukan fitur pratinjau.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
