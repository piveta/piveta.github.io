---
layout: post
title: "Wildcard dan Batasan pada Tipe Generik Java"
date: 2026-09-03
lang: id
translation_id: wildcards-limites-java
permalink: /wildcard-batasan-tipe-generik-java/
share_text: >-
  Dalam generik Java, <?> mewakili tipe yang tidak diketahui, sedangkan <? extends T> dan <? super T> menetapkan batas atas dan bawah. Artikel ini juga menunjukkan bahwa parameter tipe dapat memiliki beberapa batas.
---

Selain tipe generik tertentu, kita dapat menggunakan **wildcard** untuk menyatakan tipe yang tidak diketahui (`<?>`), membatasi tipe yang ditentukan agar mencakup subtipe dari tipe tertentu (`<? extends Type>`), atau mencakup supertipe (menggunakan `<? super Type>`). Bagian berikut menjelaskan wildcard tanpa batas, wildcard dengan batas atas, dan wildcard dengan batas bawah. Selanjutnya, kita menunjukkan cara mendefinisikan beberapa batas untuk tipe generik.

## Wildcard Tanpa Batas

Untuk tipe yang tidak diketahui, kita menggunakan tanda tanya sebagai tipe, sehingga tipe apa pun dapat digunakan dalam konteks tersebut. Misalnya, jika sebuah variabel dideklarasikan sebagai `List<?>` (atau sebuah atribut atau parameter), variabel tersebut dapat menerima objek `List` dengan parameter tipe valid apa pun, seperti `String`, `Integer`, dan sebagainya. Tipe generik yang tidak diketahui seperti ini disebut **wildcard tanpa batas** (`<?>`), karena tidak menetapkan batas tipe apa pun.

Sebagai contoh:

```java
List<?> l = new ArrayList<String>();
// atau, misalnya
l = new LinkedList<Integer>();
```

Meskipun cara mendeklarasikan variabel seperti ini mungkin tampak menarik, ada keterbatasan. Dalam kasus ini, kita tidak mengetahui tipe objek di dalam list. Oleh karena itu, kita tidak dapat, misalnya, menambahkan elemen ke dalam list (kecuali `null`, yang kompatibel dengan tipe referensi apa pun di Java), karena tidak ada jaminan bahwa objek yang ditambahkan memiliki tipe yang sama dengan parameter tipe list.

Jika kita mencoba menambahkan elemen ke objek list (dalam hal ini `l`), kita akan mendapatkan kesalahan saat kompilasi:

```java
void main(){
    List<?> l = new ArrayList<String>();
    // Compilation error: 
    //    "The method add(capture#2-of ?) in the type 
    //     List<capture#2-of ?> is not applicable 
    //     for the arguments (String)"
    l.add("Maria");
}
```

Tipe tanpa batas sering digunakan ketika kita hanya ingin membaca data tanpa memodifikasinya. Misalnya, kita dapat memiliki metode yang menerima sebuah list dan mencetak elemennya tanpa menentukan tipe elemen list:

```java
public void print(List<?> list) {
    for (Object obj : list)
        IO.println(obj);
}
void main(){
    print(List.of(1, 2, 3));
    print(List.of("A", "B", "C"));
}
```

Menjalankan metode `main` akan menampilkan:

```text
1
2
3
A
B
C
```

Di sini pencetakan digunakan sebagai contoh, tetapi kita juga dapat melakukan iterasi pada objek, menggunakannya dalam *streams*, memfilternya dengan `instanceof`, memperoleh ukuran list, memeriksa apakah suatu objek tertentu terdapat di dalamnya, mentransformasikan dan menyalinnya ke list bertipe, serta melakukan operasi lainnya. Yang tidak dapat kita lakukan adalah memodifikasi list secara langsung (misalnya menggunakan `add` atau `set`, kecuali `null`).

## Wildcard dengan Batas Atas

**Wildcard dengan batas atas** memungkinkan kita menentukan bahwa hanya objek dari tipe tertentu atau salah satu subtipenya (yang diperoleh melalui pewarisan atau implementasi interface) yang dapat digunakan sebagai parameter tipe. Notasi `<? extends T>` menyatakan bahwa wildcard harus bertipe `T` atau tipe yang memperluas `T`.

Misalnya, jika saya mendeklarasikan list yang wildcard-nya memperluas `Number`, saya dapat menetapkan objek dari salah satu subclass-nya (seperti `Double` atau `Integer`). Jika `Number` adalah kelas konkret (sebenarnya abstrak), kita juga dapat menetapkan objek dari kelas tersebut sendiri. Contoh berikut menunjukkan hal ini:

```java
void main(){
    List<? extends Number> l;
    l = new ArrayList<Double>();
    l = new LinkedList<Integer>();
}
```

Seperti pada wildcard tanpa batas, kita tidak dapat menambahkan elemen ke list `l`, karena kita tidak mengetahui tipe persis dari list tersebut. Oleh karena itu, dua pemanggilan pertama terhadap `add` menghasilkan kesalahan kompilasi:

```java
void main(){
    List<? extends Number> l = new ArrayList<Integer>();
    l.add(1); // Compilation error
    l.add(1.0); // Compilation error
    l.add(null);
}
```

Meskipun dari kode kita mengetahui bahwa objek yang ditetapkan ke variabel `l` adalah list integer, compiler hanya mengetahui bahwa `l` memiliki tipe yang tidak diketahui dan karena itu tidak mengizinkan penambahan nilai. Saat dibaca, nilainya diperlakukan sebagai `Number`, yang merupakan batas atasnya.

## Wildcard dengan Batas Bawah

**Wildcard dengan batas bawah** memungkinkan kita menentukan bahwa hanya objek dari tipe tertentu atau salah satu supertipenya yang dapat digunakan sebagai parameter tipe. Notasi `<? super T>` menyatakan bahwa wildcard harus bertipe `T` atau superclass dari `T`.

Misalnya, jika saya mendeklarasikan list yang wildcard-nya memiliki `Number` sebagai batas bawah, saya dapat menetapkan objek dari salah satu superclass-nya (dalam kasus `Number`, hanya `Object`, karena `Number` tidak memiliki superclass eksplisit).

```java
void main(){
    List<? super Number> l;
    l = new ArrayList<Number>();
    l = new LinkedList<Object>();
}
```

Kita diperbolehkan menambahkan elemen bertipe batas bawah (dalam hal ini `Number`) atau salah satu subtipenya (seperti `Double` atau `Integer`). Contoh berikut menunjukkan list yang wildcard-nya memiliki `Number` sebagai batas bawah. Dalam kasus ini, kita dapat membuat `ArrayList` angka (atau superclass-nya, `Object`). Kita dapat menambahkan elemen dari subclass-nya (kita tidak dapat menambahkan objek bertipe `Number` karena merupakan kelas abstrak yang tidak dapat memiliki instance langsung). Contoh menunjukkan tiga penambahan elemen. Dua yang pertama diizinkan karena elemennya adalah subtipe `Number` (`10` adalah `Integer` dan `1.0` adalah `Double`). Penambahan ketiga tidak diizinkan dan menghasilkan kesalahan kompilasi karena `Object` bukan turunan dari `Number`.

```java
List<? super Number> l = new ArrayList<Number>();
l.add(10);  // Allowed
l.add(1.0); // Allowed
l.add(new Object()); // Compilation error
```

Jika kita membuat `ArrayList` dengan `Object` sebagai parameter tipenya, penambahan ketiga tetap tidak diizinkan saat kompilasi dan menghasilkan kesalahan yang sama (dua penambahan pertama tetap diizinkan), karena tipe list masih tidak diketahui (kita hanya tahu bahwa tipenya adalah `Number` atau salah satu supertipenya).

## Batas Ganda

Dalam Java, sebuah tipe generik dapat memiliki **beberapa batas**, yang berarti parameter tipe dapat dibatasi hanya pada tipe yang memperluas (atau merupakan) kelas tertentu dan mengimplementasikan satu atau lebih interface. Sintaksnya berbentuk `<T extends Class & Interface1 & Interface2>`. Jika sebuah kelas digunakan sebagai batas, kelas tersebut harus dituliskan terlebih dahulu, kemudian diikuti oleh interface. Jika tidak ada kelas, hanya interface yang dapat dicantumkan.

Sebagai contoh, kelas `MultipleBounds` memiliki tipe generik `T` yang memperluas kelas `Number` dan mengimplementasikan interface `Comparable<T>` dan `Serializable`:

```java
import java.io.Serializable;

public class MultipleBounds<T extends Number 
    & Comparable<T> & Serializable> {
    // ...
}
```

Dalam contoh ini, `T` hanya dapat berupa `Number` atau tipe yang mewarisi `Number` dan juga mengimplementasikan `Comparable<T>` serta `Serializable`. Hal ini berguna ketika kita memerlukan beberapa jaminan, seperti akses ke metode superclass dan kontrak yang didefinisikan oleh beberapa interface. Kombinasi ini membuat kode lebih fleksibel sambil tetap bertipe kuat, menghindari kesalahan kompilasi, dan memastikan bahwa semua metode yang diperlukan tersedia untuk tipe generik yang digunakan.

---

*Artikel ini diadaptasi dari isi buku <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, oleh <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*
