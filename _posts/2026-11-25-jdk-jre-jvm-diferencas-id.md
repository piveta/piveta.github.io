---
layout: post
title: "JDK, JRE, dan JVM: apa perbedaannya di Java?"
date: 2026-11-25
lang: id
translation_id: jdk-jre-jvm-diferencas
permalink: /id/perbedaan-jdk-jre-jvm/
share_text: >-
  Pahami fungsi JVM, JRE, dan JDK serta perintah untuk memeriksa lingkungan Java.
---

## JVM, JRE, dan JDK
**JVM** (Java Virtual Machine) menjalankan bytecode Java. JVM memuat kelas, memeriksa dan menjalankan instruksi, serta mengelola sumber daya seperti memori. Bytecode yang sama dapat dijalankan di sistem berbeda jika tersedia JVM yang kompatibel.

**JRE** (Java Runtime Environment) adalah lingkungan untuk menjalankan aplikasi Java, termasuk JVM dan pustaka. Ketersediaan paket JRE mandiri bergantung pada distribusi dan versinya. Beberapa aplikasi menyertakan runtime sendiri.

**JDK** (Java Development Kit) mencakup runtime dan alat pengembangan: compiler <code>javac</code>, peluncur <code>java</code>, serta alat untuk membuat, menjalankan, dan mendiagnosis aplikasi.

## Apa yang perlu dipasang untuk pemrograman?
Untuk mengembangkan program Java, pasang JDK yang sesuai dengan proyek. Distribusi yang dipilih menyediakan JVM dan alat yang diperlukan. Oracle JDK dan Eclipse Temurin adalah contoh distribusi.

Periksa perintah berikut di terminal:

~~~text
java --version
javac --version
~~~

Perintah pertama menampilkan versi peluncur Java, sedangkan yang kedua versi compiler. Jika <code>java</code> berfungsi tetapi <code>javac</code> tidak ditemukan, pastikan JDK sudah terpasang dan direktori <code>bin</code>-nya ada di <code>PATH</code>.

Di Windows, <code>where java</code> dan <code>where javac</code> membantu menemukan executable yang digunakan. Di macOS dan Linux, gunakan <code>which java</code> dan <code>which javac</code>.

## Dari kode sumber hingga dijalankan
Di file <code>Hello.java</code>, compiler mengubah kode sumber menjadi bytecode:

~~~text
javac Hello.java
java Hello
~~~

Perintah pertama menghasilkan <code>Hello.class</code>. Perintah kedua memulai JVM untuk menjalankan kelas. Kompatibilitas bergantung pada versi yang dipakai untuk kompilasi dan versi untuk menjalankan program.

## Referensi
- [Gambaran umum platform Java dan JVM](https://docs.oracle.com/javase/7/docs/technotes/guides/)
- [Panduan instalasi JDK](https://docs.oracle.com/en/java/javase/26/install/overview-jdk-installation.html)
