---
layout: post
title: "Variabel dan tipe di Java"
date: 2026-11-20
lang: id
translation_id: variaveis-tipos-java
permalink: /id/variables-and-types-in-java/
share_text: >-
  Variabel lokal, inferensi dengan var, tipe primitif, dan tipe referensi.
---

Variabel lokal memiliki nama, tipe, dan cakupan. Java tidak memberi nilai bawaan untuk variabel lokal, sehingga variabel harus diberi nilai sebelum digunakan.

```java
void main(){
    String name = "Mary";
    int i = 10;
    ArrayList<Double> list = new ArrayList<Double>();
}
```

Jika deklarasi mencantumkan tipe daftar, kompilator dapat menyimpulkan argumen tipe yang diwakili `<>`.

```java
ArrayList<Double> list = new ArrayList<>();
```

Dengan `var`, kompilator menyimpulkan tipe dari ekspresi inisialisasi yang wajib ada. Dalam contoh ini, `Double` dicantumkan pada pemanggilan konstruktor.

```java
var name = "Mary";
var i = 10;
var list = new ArrayList<Double>();
```

Java membedakan huruf besar dan kecil. Menurut konvensi, nama kelas dan antarmuka dimulai dengan huruf besar, nama variabel dan metode dengan huruf kecil. Nama konstanta menggunakan huruf besar dan garis bawah.

## Tipe primitif

Tipe ini mencakup `byte`, `short`, `int`, `long`, `float`, `double`, `boolean`, dan `char`.

```java
void main() {
    byte b;
    short s;
    int x, y, z;
    long l;
    float f;
    double d;
    boolean test;
    char c;
}
```

Variabel dapat langsung diinisialisasi dengan literal. Akhiran `L` menandai `long` dan `f` menandai `float`.

```java
void main() {
    byte b = 10;
    short s = 20;
    int x = 10, y = 20, z = 30;
    long l = 100L;
    float f = 12.3f;
    double d = 20.45;
    boolean test = true;
    char c = 'a';
}
```

Literal bilangan bulat juga dapat ditulis dalam bentuk biner dengan `0b` atau heksadesimal dengan `0x`.

## Tipe referensi

Kelas, antarmuka, enumerasi, record, dan larik merupakan tipe referensi. Literal `String` ditulis dalam tanda kutip ganda.

```java
void main() {
    String s = "This is a string...";
}
```

Kelas pembungkus merepresentasikan nilai primitif sebagai objek. Contoh lain dalam bab ini juga sering menggunakan API koleksi.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
