---
layout: post
title: "Java di VS Code: cara memasang dan mengonfigurasi JDK"
date: 2026-11-25
lang: id
translation_id: java-no-vscode-configurar
permalink: /id/java-di-vs-code-konfigurasi/
share_text: >-
  Atur Java di Visual Studio Code, pilih JDK, lalu jalankan program pertama.
---

## Pasang JDK dan Visual Studio Code
Untuk mengembangkan **Java di VS Code**, pasang JDK yang sesuai dengan proyek dan Visual Studio Code. Periksa ketersediaan JDK di terminal:

~~~text
java --version
javac --version
~~~

Jika perintah tidak ditemukan, periksa pemasangan JDK dan <code>PATH</code>. Buka terminal baru setelah mengubah variabel lingkungan.

## Pasang ekstensi Java
Di VS Code, buka **Extensions**, cari **Extension Pack for Java**, lalu pasang paket dari Microsoft. Paket ini mencakup dukungan bahasa, menjalankan program, debugging, dan alat Java lainnya.

Pilihan lain adalah Coding Pack for Java untuk Windows dan macOS, yang mencakup VS Code, JDK, dan ekstensi penting.

## Konfigurasikan JDK proyek
Buka Command Palette dengan <code>Ctrl+Shift+P</code> di Windows atau Linux, atau <code>Cmd+Shift+P</code> di macOS. Jalankan **Java: Configure Java Runtime** dan periksa JDK yang terhubung dengan proyek.

JDK proyek dapat berbeda dari JDK di terminal. Jika beberapa versi terpasang, periksa keduanya.

## Jalankan program
Buka folder di VS Code dan buat <code>Hello.java</code>:

~~~java
void main() {
    IO.println("Hello World!");
}
~~~

Contoh ini memakai sintaks berkas sumber ringkas dan <code>IO.println</code>, tersedia mulai Java 25. Pilih **Run** di samping <code>main</code> dan periksa keluaran terminal. Untuk debugging, pilih **Debug** dan tetapkan breakpoint.

Jika VS Code tidak mengenali berkas, pastikan folder terbuka, tunggu ekstensi dimulai, lalu periksa JDK di **Java: Configure Java Runtime**.

## Referensi
- [Memulai Java di VS Code](https://code.visualstudio.com/docs/java/java-tutorial)
- [Pengelolaan proyek Java di VS Code](https://code.visualstudio.com/docs/java/java-project)
