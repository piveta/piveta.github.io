---
layout: post
title: "Konstruktor dalam Java"
date: 2026-11-24
lang: id
translation_id: construtores-java
permalink: /id/constructors-in-java/
share_text: "Konstruktor dalam Java"
---

Konstruktor menginisialisasi objek saat dibuat. Pada kelas `Account` dalam buku, konstruktor menerima saldo awal dan menetapkannya melalui `setBalance`. Cuplikan pertama tidak menampilkan field dan metode lainnya.

```java
public class Account{
    // Account fields and methods
    public Account(Double value){
        setBalance(value);
    }
}
```

Dengan `new Account(100.00)`, kode pemanggil membuat rekening bersaldo 100, menarik 50, lalu menyetor 100. Saldo yang dicetak adalah `150.0`.

```java
void main(){
    var c = new Account(100.00);
    c.withdraw(50.00);
    c.deposit(100.00);
    IO.println("Balance: " + c.getBalance());
}
```

Kompiler menyediakan konstruktor bawaan jika kelas biasa tidak mendeklarasikan konstruktor. Setelah `Account(Double value)` dideklarasikan, konstruktor implisit tersebut tidak lagi tersedia. Agar `new Account()` juga dapat digunakan, deklarasikan konstruktor tanpa argumen secara eksplisit. Subkelas tidak mewarisi konstruktor `Account`, tetapi dapat memanggil salah satunya dengan `super(value)`.

[Java Language Specification, §8.8.9](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9)

*Diadaptasi dari [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP) — Eduardo Kessler Piveta.*

