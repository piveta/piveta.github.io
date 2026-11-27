---
layout: post
title: "Perulangan di Java"
date: 2026-11-20
lang: id
translation_id: sentencas-repeticao-java
permalink: /id/loops-in-java/
share_text: >-
  Contoh penghitung dan penjumlahan dengan for, for-each, while, dan do-while.
---

Bagian kepala `for` berisi inisialisasi, kondisi, dan pembaruan. Contoh ini menampilkan angka 1 hingga 5.

```java
void main(){
    for (int i = 1; i < 6; i++)
        IO.println("Value of i: " + i);
}
```

Contoh lain menjumlahkan deret `1/1 + 4/2 + 7/3 + … + 100/34`. Pembilang bertambah tiga dan penyebut bertambah satu.

```java
void main(){
    double sum = 0.0;
    for (int numerator = 1, denominator = 1; 
         numerator <= 100;
         numerator += 3, denominator++)
        sum += (double) numerator / denominator;
    IO.println("Sum: " + sum);
}
```

Hasilnya `93.76358001910911`. `String.format` dapat menampilkan dua angka desimal dengan pengaturan wilayah bawaan.

```java
IO.println("Sum: " + String.format("%.2f",sum));
```

`Locale.US` menggunakan titik sebagai pemisah desimal.

```java
IO.println("Sum: " + String.format(Locale.US,"%.2f",sum));
```

## Menelusuri elemen dengan for-each

Badan perulangan dijalankan sekali untuk setiap elemen larik atau `Iterable`.

```java
void main(){
    // Declares and initializes an integer array
    int[] v = {1,2,3,4,5};
    // Iterates over the array, displaying the elements
    for (var value : v) 
        IO.println("Value: " + value);
}
```

Berikut contoh penelusuran daftar nama.

```java
void main() {
    // Creates a list of people's names
    var people = new ArrayList<String>();
    people.add("Mary");
    people.add("Peter");
    people.add("Paul");
    // Iterates over the collection, displaying names
    for (var p : people)
        IO.println("Person's name: " + p);
}
```

## while dan do-while

`while` memeriksa kondisi sebelum setiap putaran.

```java
void main() {
    int numerator = 1, denominator = 1;
    var sum = 0.0;
    while (numerator <= 100) {
        sum += (double) numerator / denominator;
        numerator += 3;
        denominator++;
    }
    IO.println("Sum: " + sum);
}
```

`do-while` memeriksa kondisi setelah badan dijalankan, sehingga badan berjalan setidaknya sekali.

```java
void main() {
    int numerator = 1, denominator = 1;
    var sum = 0.0;
    do {
        sum += (double) numerator / denominator;
        numerator += 3;
        denominator++;
    } while (numerator <= 100);
    IO.println("Sum: " + sum);
}
```

Ketiga perulangan yang menjumlahkan deret menghasilkan nilai yang sama.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
