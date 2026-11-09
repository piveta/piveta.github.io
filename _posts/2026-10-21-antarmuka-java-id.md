---
layout: post
title: "Antarmuka di Java"
date: 2026-10-21
lang: id
translation_id: interfaces-em-java
permalink: /antarmuka-java-id/
share_text: >-
  Pelajari bagaimana antarmuka Java mendefinisikan kontrak dan bagaimana kelas mengimplementasikannya.
---

Di Java, antarmuka didefinisikan dengan cara yang mirip dengan kelas. Antarmuka biasanya mendeklarasikan metode tanpa implementasi, tetapi Java juga mendukung metode default (*default methods*) yang memiliki implementasi bawaan. Kelas yang mengimplementasikan antarmuka dapat memilih apakah akan meng-override metode default tersebut.

Antarmuka dideklarasikan dengan kata kunci `interface` dan dapat memperluas antarmuka lain. Pewarisan berganda diperbolehkan untuk antarmuka. Misalnya, antarmuka Java `List` memperluas `Collection` dan `Iterable`.

Contoh berikut mendeklarasikan antarmuka bernama `AccountOperations`. Kelas yang mengimplementasikannya harus menyediakan setidaknya metode `withdraw` dan `transfer`:

```java
public interface AccountOperations {
    public void withdraw(Double amount);
    public void transfer(Account destination, Double amount);
}
```

Ketika `Account` mengimplementasikan `AccountOperations`, subkelasnya mewarisi metode tersebut dan juga memenuhi kontrak antarmukanya. Di sini, kelas konkret `Account` mengimplementasikan `withdraw` dan `transfer`, sehingga subkelasnya tidak perlu mengimplementasikannya lagi:

```java
public class Account implements AccountOperations {
    private Double balance;
    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    // Implementasi konkret withdraw
    public void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
    // Implementasi konkret transfer
    public void transfer(Account destination, Double amount) {
        this.withdraw(amount);
        destination.deposit(amount);
    }
}
```

Pilihan lain adalah memindahkan implementasi `withdraw`, `deposit`, dan `transfer` ke dalam antarmuka `AccountOperations` sebagai metode `default`. Antarmuka tersebut juga harus mendeklarasikan `getBalance` dan `setBalance`:

```java
public interface AccountOperations {
    public Double getBalance();
    public void setBalance(Double balance);
    public default void withdraw(Double amount) {
        setBalance(getBalance() - amount);
    }
    public default void transfer(AccountOperations destination,
                                 Double amount) {
        destination.deposit(amount);
        this.withdraw(amount);
    }
    public default void deposit(Double amount) {
        setBalance(getBalance() + amount);
    }
}
```

Kelas `Account` yang disederhanakan menjadi:

```java
public class Account implements AccountOperations {
    private Double balance;

    public Double getBalance() {
        return balance;
    }
    public void setBalance(Double balance) {
        this.balance = balance;
    }
    public Account(Double amount) {
        setBalance(amount);
    }
}
```

Memisahkan antarmuka dari `Account` dapat memberi kelas lebih banyak keleluasaan dalam menyimpan dan mengelola saldo. Misalnya, framework koleksi Java memiliki antarmuka `List` yang mendefinisikan operasi untuk daftar. Implementasi konkret seperti `ArrayList` dan `LinkedList` menggunakan strategi penyimpanan dan akses yang berbeda: yang pertama menggunakan array, sedangkan yang kedua menggunakan daftar berantai ganda.

---

*Artikel ini mengadaptasi konten dari buku <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a> karya <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.*

## Artikel terkait

- [Konsep dasar pemrograman berorientasi objek](/konsep-dasar-oop-id/)
- [Kelas di Java](/kelas-java-id/)
- [Pewarisan di Java](/pewarisan-java-id/)
- [Polimorfisme di Java](/polimorfisme-java-id/)
- [Tautan OOP dan Java](/tautan-oop-java-id/)
- [Latihan pemrograman berorientasi objek](/latihan-oop-id/)
