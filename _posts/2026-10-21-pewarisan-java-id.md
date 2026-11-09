---
layout: post
title: "Pewarisan di Java"
date: 2026-10-21
lang: id
translation_id: heranca-em-java
permalink: /pewarisan-java-id/
share_text: >-
  Pengantar pewarisan di Java, overriding, konversi subtipe, dan kelas abstrak.
---

**Pewarisan** adalah mekanisme komposisi yang memungkinkan kelas menggunakan kembali antarmuka dan perilaku kelas yang sudah ada dengan memperluas fungsinya. Kelas yang memperluas kelas lain melalui pewarisan disebut **subkelas**, sedangkan kelas yang diperluas disebut **superkelas**.

Java mendukung pewarisan tunggal untuk kelas (pewarisan berganda tersedia bagi antarmuka), dan subkelas merupakan subtipe dari superkelasnya. Pewarisan dideklarasikan di subkelas dengan kata kunci `extends`: `Kelas extends SuperKelas`. Kelas tanpa superkelas yang dideklarasikan secara eksplisit secara implisit merupakan subkelas dari `Object`, akar hierarki kelas Java.

Perhatikan kelas `CheckingAccount` berikut. Kelas ini memperluas `Account` dan menambahkan field, metode untuk membaca dan menulis field tersebut, serta sebuah konstruktor. Karena `Account` tidak memiliki konstruktor tanpa argumen, konstruktor `CheckingAccount` memanggil konstruktor superkelas dengan `super`:

```java
public class CheckingAccount extends Account {
    private Double dailyWithdrawalLimit;
    public Double getDailyWithdrawalLimit() {
        return dailyWithdrawalLimit;
    }
    public void setDailyWithdrawalLimit(Double dailyWithdrawalLimit) {
        this.dailyWithdrawalLimit = dailyWithdrawalLimit;
    }
    public CheckingAccount(Double amount) {
        super(amount);
    }
}
```

Subkelas sering memiliki **metode yang dioverride**: metode yang dideklarasikan di superkelas dan perilakunya diperluas atau diganti oleh subkelas. Di sini, `CheckingAccount` meng-override metode `withdraw` milik `Account` dengan mendeklarasikan metode yang memiliki signature sama[^6]. Mula-mula metode ini memanggil metode superkelas melalui `super`, kemudian menghitung biaya melalui `deductFee`, yang mengurangi saldo sebesar 1% dari jumlah transaksi:

```java
public class CheckingAccount extends Account {
    public void withdraw(Double amount) {
        super.withdraw(amount);
        deductFee(amount);
    }
    private void deductFee(Double amount) {
        setBalance(getBalance() - amount * 0.01);
    }
    // Konstruktor, field, dan metode lainnya.
}
```

Sebagai contoh, jika saldo awal `CheckingAccount` adalah 100.00 lalu kita menarik 50.00, saldo yang tersisa ialah 49.50 karena ada biaya sebesar 0.50:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    IO.println("Balance: " + account.getBalance());
}
```

Menurut prinsip substitusi Liskov, objek subkelas dapat diberikan di mana pun objek superkelas diharapkan: setiap instans `CheckingAccount` juga merupakan instans `Account`. Sebaliknya tidak selalu berlaku, karena sebuah `Account` dapat berupa `SavingsAccount`, misalnya. Dalam kasus seperti itu, konversi eksplisit (*cast*) diperlukan.

Pada contoh berikut, `checkingAccount` bertipe `CheckingAccount` dan merujuk ke instans kelas tersebut. Variabel `account` bertipe `Account` dan diberi objek yang sama. Penugasan ini tidak memerlukan konversi. Penugasan sebaliknya memerlukan *cast* eksplisit:

```java
CheckingAccount checkingAccount = new CheckingAccount(100.00);
Account account = checkingAccount; // CheckingAccount adalah Account.
checkingAccount = (CheckingAccount) account; // Cast eksplisit yang valid.
```

Misalkan `SavingsAccount` adalah subkelas lain dari `Account`. Pada contoh berikut, `account` merujuk ke `CheckingAccount`. Meng-cast-nya menjadi `SavingsAccount` gagal saat runtime karena objek tersebut bukan `SavingsAccount`:

```java
Account account = new CheckingAccount(100.00);
// Cast eksplisit berikut gagal saat runtime.
SavingsAccount savingsAccount = (SavingsAccount) account;
```

IDE modern memberi peringatan untuk konversi yang jelas salah, tetapi terkadang hasilnya belum diketahui sebelumnya. Misalnya, argumen metode baru diketahui saat metode dipanggil. Karena itu, cast yang salah dapat menyebabkan exception runtime bertipe `ClassCastException`[^7].

Karena `Account` dapat memiliki beberapa subtipe, seperti `CheckingAccount`, `SavingsAccount`, dan mungkin `InvestmentAccount`, kita dapat menjadikannya abstrak agar hanya instans subkelasnya yang dapat dibuat:

```java
public abstract class Account {
    // Field dan metode yang sama-sama dimiliki semua jenis rekening.
}
```

Kita tidak dapat lagi membuat instans `Account` secara langsung. Kita harus menggunakan konstruktor salah satu subkelasnya, misalnya `CheckingAccount`:

```java
void main() {
    var account = new CheckingAccount(100.00);
    account.withdraw(50.00);
    account.deposit(100.00);
    IO.println("Balance: " + account.getBalance());
}
```

[^6]: Di Java, signature metode terdiri atas namanya, parameter tipenya (jika ada), dan parameter formalnya. Lihat [Spesifikasi Bahasa Java](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.2).

[^7]: Lihat [dokumentasi API ClassCastException](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ClassCastException.html).

---

*Artikel ini mengadaptasi konten dari buku <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> karya <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artikel terkait

- [Konsep dasar pemrograman berorientasi objek](/konsep-dasar-oop-id/)
- [Kelas di Java](/kelas-java-id/)
- [Polimorfisme di Java](/polimorfisme-java-id/)
- [Antarmuka di Java](/antarmuka-java-id/)
- [Tautan OOP dan Java](/tautan-oop-java-id/)
- [Latihan pemrograman berorientasi objek](/latihan-oop-id/)
