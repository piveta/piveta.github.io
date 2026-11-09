---
layout: post
title: "Kelas di Java"
date: 2026-10-21
lang: id
translation_id: classes-em-java
permalink: /kelas-java-id/
share_text: >-
  Pelajari cara mendefinisikan kelas, field, metode, konstruktor, dan enkapsulasi di Java.
---

Java mendukung konsep utama pemrograman berorientasi objek, termasuk kelas, field, metode, pewarisan, antarmuka, polimorfisme, dan enkapsulasi.

## Kelas, field, dan metode

Di Java, kelas dideklarasikan dengan kata kunci `class`, sebuah nama, dan badan tempat field serta metode dapat didefinisikan. Komponen opsional lainnya dibahas kemudian. Misalkan kita memiliki kelas bernama `Account`. Kelas ini dapat dibuat `public` agar dapat diakses oleh kelas lain:

```java
public class Account {
    // Badan kelas
}
```

Kita dapat menambahkan field dan metode ke badan kelas. Pada contoh berikut, kita menambahkan field `balance` bertipe `Double`[^2] dan metode `withdraw`. Metode ini tidak mengembalikan nilai (`void`) dan menerima parameter formal bernama `amount`, yang juga bertipe `Double`. Metode tersebut mengurangi saldo sebesar nilai yang diberikan sebagai argumen:

```java
public class Account {
    public Double balance;
    public void withdraw(Double amount) {
        balance = balance - amount; // atau balance -= amount;
    }
}
```

Demikian pula, kita dapat menambahkan metode `deposit` untuk menambah saldo rekening:

```java
public class Account {
    // balance dan withdraw dihilangkan
    public void deposit(Double amount) {
        balance = balance + amount; // atau balance += amount;
    }
}
```

Misalkan sebuah klien melakukan beberapa operasi pada rekening. Pertama, klien membuat objek `Account` dengan memanggil konstruktornya dan menyimpan referensinya dalam variabel bernama `account`. Kemudian, klien menetapkan saldo menjadi 100.00, menarik 50.00, menyetor 100.00, dan mencetak saldo:

```java
void main() {
    var account = new Account();
    account.balance = 100.00;
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.balance);
}
```

Keluarannya adalah:

```text
Balance: 150.0
```

Metode `withdraw` dan `deposit` memerlukan objek `Account` untuk dipanggil karena keduanya merupakan metode instans. Pada versi Java terbaru, `main` juga dapat berupa metode statis atau metode instans seperti pada contoh ini[^3].

Contoh sebelumnya menunjukkan klien yang menggunakan field dan metode `Account`. Klien tersebut berada di dalam kelas tanpa nama yang dideklarasikan secara implisit. Namun, klien mengakses `balance` secara langsung sehingga tercipta keterikatan erat antarkelas. Hal ini biasanya tidak diinginkan[^4]. Salah satu alternatifnya adalah mengenkapsulasi akses ke `balance`, sehingga pembacaan dan penulisan dilakukan melalui metode khusus. Cara ini mengurangi keterikatan dan memungkinkan representasi internal saldo diubah nanti, selama operasi baca dan tulis tetap tersedia. Visibilitas field juga sebaiknya dikurangi agar hanya dapat diakses dari dalam kelas.

Java menyediakan visibilitas package-private (bawaan), `private`, `public`, dan `protected`. Tingkat visibilitas tersebut menentukan kelas mana yang dapat mengakses sebuah field atau metode. Setiap tingkat memiliki kata kunci, kecuali visibilitas package-private yang tidak menggunakan kata kunci.

Kode berikut meningkatkan enkapsulasi dan menyembunyikan keadaan internal kelas dari kliennya. Kode ini menambahkan metode baca dan tulis publik (`getBalance` dan `setBalance`), mengubah visibilitas `balance` menjadi `private`, dan memperbarui saldo melalui metode tersebut. Referensi `this` membedakan field `balance` dari parameter metode yang bernama sama. `this.balance` merujuk ke field, bukan ke parameter:

```java
public class Account {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
}
```

Klien juga diubah agar memperbarui saldo melalui metode setter:

```java
void main() {
    var account = new Account();
    account.setBalance(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Jika tidak ada konstruktor yang dideklarasikan secara eksplisit, kelas Java memiliki konstruktor bawaan tanpa parameter. Kita dapat mendefinisikan konstruktor lain untuk memudahkan klien menggunakan kelas. Misalnya, konstruktor `Account` ini menerima jumlah awal dan menetapkan saldo dengannya. Jika konstruktor superclass perlu dipanggil, kita dapat menggunakan `super`:

```java
public class Account {
    // Field dan metode Account
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

Klien sekarang harus menggunakan konstruktor baru dan memberikan saldo awal karena `Account` tidak lagi memiliki konstruktor bawaan tanpa argumen[^5]:

```java
void main() {
    var account = new Account(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

Java tidak memiliki metode destruktor. Objek yang tidak lagi dirujuk akan dikumpulkan secara otomatis oleh garbage collector.

[^2]: `Double` digunakan di sini demi kesederhanaan. Nilai uang biasanya tidak disimpan dalam variabel titik-mengambang, melainkan dalam tipe bilangan bulat seperti `long` atau dalam `BigDecimal`.

[^3]: Lihat [JEP 512](https://openjdk.org/jeps/512).

[^4]: Di sini, “kelas-kelas tersebut” merujuk pada `Account` dan kelas tanpa nama yang dideklarasikan secara implisit dan memuat `main`.

[^5]: Setelah konstruktor didefinisikan, kelas tidak lagi memiliki konstruktor bawaan. Jika diperlukan, kita juga dapat mendefinisikan konstruktor tanpa argumen.

---

*Artikel ini mengadaptasi konten dari buku <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> karya <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artikel terkait

- [Konsep dasar pemrograman berorientasi objek](/konsep-dasar-oop-id/)
- [Pewarisan di Java](/pewarisan-java-id/)
- [Polimorfisme di Java](/polimorfisme-java-id/)
- [Antarmuka di Java](/antarmuka-java-id/)
- [Tautan OOP dan Java](/tautan-oop-java-id/)
- [Latihan pemrograman berorientasi objek](/latihan-oop-id/)
