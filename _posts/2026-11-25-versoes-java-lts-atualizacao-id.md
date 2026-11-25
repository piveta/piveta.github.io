---
layout: post
title: "Versi Java: LTS, pembaruan, dan cara memeriksa versi"
date: 2026-11-25
lang: id
translation_id: versoes-java-lts-atualizacao
permalink: /id/versi-java-lts-pembaruan/
share_text: >-
  Pelajari siklus rilis Java, arti LTS, serta cara memeriksa dan memperbarui JDK.
---

## Periksa versi Java
Jalankan perintah berikut di terminal:

~~~text
java --version
javac --version
~~~

Perintah pertama menunjukkan peluncur Java yang digunakan untuk memulai aplikasi; perintah kedua menunjukkan compiler. Jika beberapa JDK terpasang, executable yang ditemukan di <code>PATH</code> dapat berbeda dari JDK yang dikonfigurasi di IDE.

## Versi Java dan LTS
Java merilis fitur baru setiap enam bulan. Versi **LTS** (*long-term support*) mendapat dukungan jangka panjang dari vendor tertentu. Durasi, harga, dan ketentuannya bergantung pada distribusi dan vendor.

Dalam peta dukungan Oracle, Java 8, 11, 17, 21, dan 25 adalah versi LTS. Oracle merencanakan LTS baru setiap dua tahun. Periksa peta terbaru dan kebijakan vendor sebelum memilih versi untuk produksi.

Pilihan juga bergantung pada pustaka, alat, dan kebutuhan aplikasi. LTS menawarkan masa dukungan lebih panjang, sedangkan rilis antara menghadirkan fitur lebih cepat.

## Tempat melihat versi dan JEP
Oracle menyediakan [indeks catatan rilis JDK](https://www.oracle.com/java/technologies/javase/jdk-relnotes-index.html) yang menautkan rilis dan pembaruannya. Catatan tersebut menjelaskan perubahan, perbaikan, serta fitur yang ditambahkan atau dihapus. [Catatan rilis JDK 27](https://www.oracle.com/java/technologies/javase/27-relnote-issues.html) menjelaskan hal baru dan JEP terkait.

**JEP** (*JDK Enhancement Proposal*) mendokumentasikan usulan peningkatan JDK, tujuan, rancangan, dan statusnya. Fitur tertentu pertama kali hadir sebagai *preview* atau *incubator* dan dapat berubah sebelum ditetapkan secara permanen.

Lihat [perubahan bahasa Java per rilis](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-release.html) dan [ringkasan perubahan bahasa](https://docs.oracle.com/en/java/javase/27/language/java-language-changes-summary.html) untuk membandingkan fitur permanen dan pratinjau.

## Perbarui Java
1. Periksa versi dengan <code>java --version</code> dan <code>javac --version</code>.
2. Pastikan versi yang didukung proyek, dependensi, dan lingkungan produksi.
3. Unduh pembaruan dari distribusi yang digunakan atau pilih distribusi yang kompatibel.
4. Pasang JDK dan sesuaikan <code>PATH</code>, <code>JAVA_HOME</code>, serta IDE bila perlu.
5. Buka terminal baru, periksa versi, dan jalankan pengujian aplikasi.

Pembaruan dalam seri versi yang sama berbeda dari migrasi ke versi utama baru. Sebelum migrasi, tinjau catatan rilis dan uji aplikasi beserta dependensinya.

Di Windows, <code>where.exe java</code> dan <code>where.exe javac</code> menampilkan executable yang ditemukan. Di macOS dan Linux, gunakan <code>which java</code> dan <code>which javac</code>.

## Referensi
- [Peta dukungan Oracle Java SE](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- [FAQ lisensi Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
