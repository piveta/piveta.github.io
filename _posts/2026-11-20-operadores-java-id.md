---
layout: post
title: "Operator di Java"
date: 2026-11-20
lang: id
translation_id: operadores-java
permalink: /id/operators-in-java/
share_text: >-
  Operator aritmetika, penugasan, dan perbandingan dengan contoh dari buku.
---

## Operator aritmetika

`+`, `-`, `*`, `/`, dan `%` berarti penjumlahan, pengurangan, perkalian, pembagian, dan sisa. Prioritas operator menentukan pengelompokan operasi. `++` dan `--` mengubah nilai variabel sebesar satu.

```java
void main(){
    var x = 10;
    x++;
    IO.println("X is " + x);
    x--;
    IO.println("And now x is " + x);
}
```

Pada `y = x++`, `y` menerima nilai lama, yaitu 10. Setelah itu `x` menjadi 11.

```java
void main(){
    var x = 10;
    var y = x++;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Pada `y = ++x`, penambahan dilakukan lebih dahulu. Kedua variabel bernilai 11.

```java
void main(){
    var x = 10;
    var y = ++x;
    IO.println("X is " + x);
    IO.println("And y is " + y);
}
```

Operator uner lain mencakup `+`, `-`, `~`, dan `!`.

## Penugasan

`=` menetapkan nilai ekspresi di kanan ke variabel di kiri.

```java
int age;
String name;
Double height;
```

Penugasan dapat dilakukan setelah deklarasi.

```java
age = 20;
name = "Mary";
height = 1.70;
```

Variabel juga dapat langsung diberi nilai ketika dideklarasikan.

```java
int age = 20;
String name = "Mary";
Double height = 1.70;
```

## Penugasan gabungan

`+=`, `-=`, `*=`, `/=`, dan `%=` menggabungkan operasi dengan penugasan.

```java
void main() {
    int a = 10;
    a += 10;
    IO.println("a = " + a);
    a -= 10;
    IO.println("a = " + a); 
    a *= 10;
    IO.println("a = " + a); 
    a /= 10;
    IO.println("a = " + a); 
    a %= 3;
    IO.println("a = " + a); 
}
```

Program menampilkan nilai dalam urutan berikut.

```text
a = 20
a = 10
a = 100
a = 10
a = 1
```

Penugasan gabungan mengevaluasi ekspresi kiri sekali saja dan memperhitungkan tipenya. Bentuk gabungan juga tersedia untuk operasi pergeseran dan operasi bit.

## Perbandingan

`==`, `!=`, `>`, `>=`, `<`, dan `<=` menghasilkan nilai boolean.

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age == 10)
        IO.println("Age equals 10 years");
    if (age != 20)
        IO.println("Age differs from 20 years");
    if (age > 30)
        IO.println("Age is over 30 years");
    if (age <= 80)
        IO.println("Age is at most 80 years");
}
```

Untuk masukan 10, tiga kondisi bernilai benar karena setiap `if` diperiksa sendiri. `Integer.parseInt` mengubah masukan menjadi bilangan bulat.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
