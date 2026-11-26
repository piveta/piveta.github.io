---
layout: post
title: "Ekspresi dan pernyataan kondisional di Java"
date: 2026-11-20
lang: id
translation_id: expressoes-condicionais-java
permalink: /id/expressions-and-conditional-statements-in-java/
share_text: >-
  Ekspresi, blok, if, else, operator ternary, dan switch.
---

## Ekspresi dan pernyataan

Ekspresi menghasilkan nilai saat dievaluasi. Ekspresi dapat memuat literal, variabel, operator, pemanggilan metode, atau pembuatan objek. Potongan ini belum membentuk program lengkap.

```text
x + 2 * 1
c.getBalance()
i = 20
```

Pernyataan adalah satuan yang dapat dieksekusi. Pemanggilan metode, penugasan, dan inkremen dapat ditulis sebagai pernyataan yang diakhiri titik koma. Contoh ini membutuhkan deklarasi lain dan kelas `Account`.

```text
c.getBalance();
i = 20;
i++;
Account c1 = new Account();
```

Kurung kurawal mengelompokkan pernyataan dalam satu blok. Program membaca bilangan bulat dan menampilkan dua pesan jika kondisi terpenuhi.

```java
void main() {
    int x = Integer.parseInt(
            IO.readln("Enter an integer: "));
    if (x < 10) {  
        IO.println("X is less than 10."); 
        IO.println("Initialize X with another value."); 
    }
}
```

## Pernyataan kondisional

`if` menjalankan pernyataan ketika kondisi boolean bernilai benar.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18)
        IO.println("Adult");
}
```

`else` menentukan tindakan ketika kondisi bernilai salah.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age:"));
    if (age >= 18)
        IO.println("Adult");
    else
        IO.println("Minor");
}
```

Kurung kurawal memungkinkan beberapa pernyataan dalam satu cabang.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
    }
    else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

Setelah memeriksa apakah pengguna sudah dewasa, `if` bersarang memeriksa apakah pengguna berhak atas akses prioritas.

```java
void main() {
    var age = Integer.parseInt(IO.readln("Age: "));
    if (age >= 18) {
        IO.println("Adult");
        IO.println("Access allowed");
        if (age >= 65)
            IO.println("Priority access granted");
    } else {
        IO.println("Minor");
        IO.println("Access denied");
    }
}
```

Operator ternary memilih satu dari dua nilai berdasarkan kondisi.

```java
void main(){
    var age = Integer.parseInt(IO.readln("Age: "));
    // The ternary operator has this syntax: 
		// (expr) ? true : false
    String message = ((age >= 18) ? "At least" : "Under") + 
                 " 18 years old";
    IO.println(message);
}
```

## Memilih cabang dengan switch

Pernyataan `switch` klasik memilih kasus yang cocok. `break` mengakhirinya dan `default` menangani nilai lainnya.

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message;
    switch (age) {
        case 0: case 1: case 2: case 3: case 4: case 5:
            message = "Very young";
            break;
        case 18:
            message = "Reaching adulthood";
            break;
        case 65:
            message = "Entering senior years";
            break;
        default:
            message = "No special case";
            break;
        }
        IO.println(message);
}
```

Ekspresi `switch` dengan panah menghasilkan nilai. Beberapa nilai dalam satu kasus dipisahkan dengan koma.

```java
void main() {
    int age = Integer.parseInt(IO.readln("Age: "));
    String message = switch (age) {
        case 0, 1, 2, 3, 4, 5 -> "Very young";
        case 18 -> "Reaching adulthood";
        case 65 -> "Entering senior years";
        default -> "No special case";
    };
    IO.println(message);
}
```

Pencocokan pola menggunakan `when` untuk menambahkan kondisi pada pola tipe. Contoh membedakan `Integer`, `String`, `null`, dan nilai lain.

```java
private static String age(Object ageObject) {
    return switch (ageObject) {
        case Integer i when i >= 65 -> 
            "[Integer] Adult: " + i + 
            "\nPriority access granted.";
        case Integer i when i >= 18 -> 
            "[Integer] Adult: " + i + 
             "\nAccess granted.";
        case Integer i -> "[Integer] Minor: " + 
                i + "\nAccess denied.";
        case String s -> 
            "[String] Age provided as text: " + s;
        case null -> "[null] Age not provided";
        default -> "Unexpected data type: " + 
                ageObject.getClass().getName();
    };
}
```

Program memanggil metode itu dengan empat nilai berbeda.

```java
void main() {
    IO.println(age("80"));
    IO.println(age(10));
    IO.println(age(null));
    IO.println(age(10.2));
}
```

Berikut keluarannya.

```text
[String] Age provided as text: 80
[Integer] Minor: 10
Access denied.
[null] Age not provided
Unexpected data type: java.lang.Double
```

Contoh terakhir memerlukan versi Java yang mendukung pencocokan pola dalam `switch`.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
