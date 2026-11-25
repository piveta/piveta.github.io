---
layout: post
title: "Cara menginstal Java dan JDK di Windows"
date: 2026-11-25
lang: id
translation_id: como-instalar-java-jdk-windows
permalink: /id/instal-java-jdk-windows/
share_text: >-
  Unduh dan pasang JDK di Windows, lalu periksa pemasangannya dengan java dan javac.
---

## Pilih distribusi Java
Untuk mengembangkan Java di Windows, unduh **JDK** yang sesuai dengan proyek. Oracle JDK dan Eclipse Temurin adalah beberapa pilihan. Versi LTS dapat sesuai untuk proyek yang memerlukan dukungan jangka panjang. Periksa kebutuhan proyek dan ketentuan distribusinya.

Di Pengaturan Windows, periksa jenis sistem dan arsitektur prosesor. Pilih paket yang cocok, seperti x64 atau AArch64, serta penginstal Windows.

## Unduh dan pasang JDK
Contoh pemasangan Eclipse Temurin:

1. Buka [halaman unduhan Adoptium](https://adoptium.net/temurin/releases/).
2. Pilih versi Java, Windows, arsitektur, dan paket **JDK**.
3. Unduh dan jalankan penginstal MSI.
4. Periksa apakah Java akan ditambahkan ke <code>PATH</code>. Jika alat lain memerlukan <code>JAVA_HOME</code>, pilih opsi itu juga.
5. Selesaikan pemasangan dan buka terminal baru.

Pada Temurin, penambahan ke <code>PATH</code> adalah opsi standar, sedangkan pengaturan <code>JAVA_HOME</code> merupakan opsi tambahan.

## Periksa pemasangan
Jalankan di PowerShell atau Command Prompt:

~~~text
java --version
javac --version
where.exe java
where.exe javac
~~~

Dua perintah pertama menampilkan versi Java dan compiler. Perintah lainnya menunjukkan executable yang ditemukan di <code>PATH</code>. Jika perintah tidak ditemukan, buka terminal baru dan periksa variabel lingkungan. Jika versinya berbeda, periksa urutan direktori di <code>PATH</code>.

Simpan kode berikut sebagai <code>Hello.java</code> untuk menguji kompilasi:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Contoh ini memakai sintaks berkas sumber ringkas dan <code>IO.println</code> yang tersedia mulai Java 25. Jalankan:

~~~text
javac Hello.java
java Hello
~~~

Output-nya <code>Hello World!</code>. Sebelum Java 25, gunakan bentuk program yang didukung JDK terpasang.

## Referensi
- [Penginstal MSI Eclipse Temurin](https://adoptium.net/installation/windows/)
- [Instalasi Oracle JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
