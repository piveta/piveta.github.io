---
layout: post
title: "Kelas Pengecualian di Java"
date: 2026-08-27
lang: id
translation_id: classes-de-excecao
permalink: /kelas-pengecualian-java-id/
image: /images/descendentesThrowable.png
share_text: >-
  Di Java, Throwable menjadi dasar hierarki yang mencakup Error dan Exception, sedangkan RuntimeException termasuk pengecualian tidak terperiksa. Artikel ini membahas perbedaan antara pengecualian terperiksa dan tidak terperiksa.
---
Selama eksekusi program, dapat muncul situasi yang memerlukan penanganan khusus. Situasi tersebut dapat berupa kondisi yang tidak normal atau salah, situasi yang tidak diperkirakan oleh programmer, atau bahkan alur eksekusi alternatif. Kondisi-kondisi ini disebut **pengecualian**.

Di Java, pengecualian direpresentasikan oleh objek yang termasuk dalam kelas `Throwable` atau salah satu subkelasnya. Hierarki pengecualian penting untuk memahami pengecualian mana yang dapat dilempar, ditangkap, dan ditangani oleh program.

## Throwable

`Throwable` adalah kelas dasar dalam hierarki pengecualian Java. Objek dari kelas ini menyimpan informasi tentang suatu kejadian tertentu dan memungkinkan informasi tersebut diteruskan dari tempat pengecualian terjadi ke kode yang bertanggung jawab menanganinya.

Hanya objek yang termasuk dalam `Throwable` atau salah satu subkelasnya yang dapat dilempar oleh JVM atau oleh programmer menggunakan `throw`. Demikian pula, klausa `catch` hanya dapat menangkap objek yang termasuk dalam hierarki ini.

Metode utama dalam `Throwable` antara lain `getMessage()`, yang digunakan untuk memperoleh pesan yang terkait dengan pengecualian, dan `printStackTrace()`, yang menampilkan jejak tumpukan eksekusi hingga titik terjadinya pengecualian.

Kelas `Throwable` memiliki dua subkelas langsung: `Exception` dan `Error`.

<img src="/images/descendentesThrowable.png"
     alt="Hierarki Throwable"
     style="max-width: 250px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Error

Kelas `Error` merepresentasikan kondisi serius yang pada umumnya tidak dapat dipulihkan oleh aplikasi. Ini adalah situasi tidak normal yang biasanya tidak seharusnya terjadi selama eksekusi program.

Beberapa subkelas penting dari `Error` adalah `AssertionError`, `IOError`, dan `VirtualMachineError`. Yang terakhir memiliki, antara lain, subkelas `InternalError`, `OutOfMemoryError`, `StackOverflowError`, dan `UnknownError`.

Error dapat dilempar oleh JVM itu sendiri, sering kali sebagai akibat dari kondisi yang terdeteksi oleh sistem operasi atau lingkungan runtime. Error juga dapat dihasilkan secara eksplisit oleh programmer, misalnya melalui `assert` atau `throw`.

<img src="/images/exceptionsError.png"
     alt="Error dan subkelasnya"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Exception

Kelas `Exception` merepresentasikan pengecualian yang, dalam kondisi tertentu, dapat ditangani dan memungkinkan aplikasi untuk pulih.

Subkelasnya mencakup `IOException`, `SQLException`, `ReflectiveOperationException`, `ClassNotFoundException`, dan `RuntimeException`.

Subkelas `Exception` yang bukan merupakan subkelas `RuntimeException` disebut **pengecualian terperiksa** (*checked exceptions*). Kompiler mengharuskan program memperhitungkannya secara eksplisit. Hal ini dapat dilakukan dengan menangkap pengecualian menggunakan klausa `catch` atau dengan mendeklarasikan menggunakan `throws` bahwa metode tersebut dapat melemparkannya.

<img src="/images/descendentesException.png"
     alt="Exception dan subkelasnya"
     style="max-width: 600px; width: 100%; height: auto; display: block; margin: 20px auto;">

## RuntimeException

Di antara subkelas `Exception`, `RuntimeException` memiliki peran penting. Kelas ini dan subkelasnya disebut **pengecualian runtime** (*runtime exceptions*).

`RuntimeException` dan subkelasnya merupakan **pengecualian tidak terperiksa** (*unchecked exceptions*). Kompiler tidak mengharuskan pengecualian tersebut ditangani secara eksplisit dengan `try`/`catch` atau dideklarasikan dengan `throws`.

Jenis pengecualian ini biasanya merepresentasikan kesalahan logis atau penggunaan program yang tidak benar. Contoh umum meliputi:

- `ClassCastException`: terjadi ketika konversi tipe secara eksplisit tidak dapat dilakukan.
- `IllegalArgumentException`: menunjukkan bahwa sebuah metode menerima argumen yang dianggap tidak valid atau tidak sesuai.
- `IndexOutOfBoundsException`: terjadi ketika program mencoba mengakses posisi yang tidak ada dalam struktur terindeks.
- `NullPointerException`: terjadi ketika operasi dilakukan pada referensi `null`.

Metode yang dapat melempar `RuntimeException` tidak perlu mendeklarasikan kemungkinan tersebut dengan `throws`. Tentu saja, pengecualian tersebut tetap dapat ditangkap dan ditangani menggunakan `try` dan `catch`.

Dalam praktiknya, banyak instance `RuntimeException` menunjukkan masalah yang sebenarnya dapat dicegah oleh program itu sendiri. Ketika pengecualian seperti ini terjadi, biasanya penting untuk menyelidiki penyebabnya dan memperbaiki masalah tersebut, bukan sekadar menangkap pengecualiannya.

<img src="/images/descendentesRuntimeException.png"
     alt="RuntimeException dan subkelasnya"
     style="max-width: 800px; width: 100%; height: auto; display: block; margin: 20px auto;">

## Pengecualian terperiksa dan tidak terperiksa

Perbedaan penting dalam hierarki pengecualian Java adalah antara **pengecualian terperiksa** dan **pengecualian tidak terperiksa**.

`Throwable` dan semua subkelasnya yang bukan subkelas `RuntimeException` atau `Error` disebut **pengecualian terperiksa**. `RuntimeException` dan subkelasnya, serta `Error` dan subkelasnya, disebut **pengecualian tidak terperiksa**.

Pengecualian terperiksa harus ditangani atau dideklarasikan secara eksplisit oleh program. Artinya, ketika sebuah metode dapat melempar pengecualian terperiksa, pengecualian tersebut harus ditangani oleh klausa `catch` atau dideklarasikan dalam klausa `throws` metode tersebut.

Sebaliknya, pengecualian tidak terperiksa tidak perlu ditangani atau dideklarasikan secara eksplisit. Kompiler tidak mengharuskan `RuntimeException`, `Error`, atau subkelasnya ditangkap atau dideklarasikan.

Secara sederhana, hierarki tersebut dapat digambarkan sebagai berikut:

```text
Throwable
├── Error
└── Exception
    └── RuntimeException
```

Struktur ini memungkinkan penanganan dilakukan pada berbagai tingkat hierarki. Misalnya, sebuah klausa `catch` dapat menangkap pengecualian tertentu atau salah satu superclass-nya, bergantung pada perilaku yang diinginkan.

Memahami hierarki ini merupakan dasar untuk memahami mekanisme penanganan pengecualian Java dan untuk menentukan pengecualian mana yang harus ditangani, mana yang harus diteruskan, dan mana yang merepresentasikan error yang perlu diperbaiki dalam program itu sendiri.

Artikel ini diadaptasi dari materi dalam buku <a href="https://www.amazon.com.br/dp/B0FWZ6HYVP">Orientação a Objetos com Java</a>, oleh <a href="http://www-usr.inf.ufsm.br/~piveta/">Eduardo Kessler Piveta</a>.
