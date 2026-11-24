---
layout: post
title: "Penghapusan tipe dan raw type di Java"
date: 2026-11-20
lang: id
translation_id: apagamento-tipos-crus-java
permalink: /id/type-erasure-and-raw-types-in-java/
share_text: >-
  Penghapusan tipe menjaga kompatibilitas; raw type kehilangan pemeriksaan elemen.
---

Java 5 memperkenalkan generik sambil menjaga kompatibilitas dengan kode lama. Melalui **penghapusan tipe** (*type erasure*), kompiler memeriksa parameter generik lalu menghapusnya dari representasi yang dijalankan JVM. Parameter diganti dengan batasnya, biasanya `Object` atau batas pertama yang dideklarasikan.

Sesudah penghapusan, `Adapter<T>` kira-kira menyerupai kelas yang memakai `Object`:

```java
public class Adapter{
    Object object;
    public Object get(){
        return object;
    }
    public void set(Object value){
        object = value;
    }
    public Adapter(Object initial){
        object = initial;
    }
}
```

Klien tanpa parameter tipe akan terlihat seperti berikut:

```java
void main(){
    Adapter a = new Adapter("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

Potongan ini **mengilustrasikan** proses, bukan salinan harfiah bytecode. Argumen tipe tidak tersedia saat runtime dengan cara yang sama seperti saat kompilasi, sehingga beberapa operasi refleksi menjadi terbatas.

## Raw type

Daftar berparameter memeriksa tipe elemennya:

```java
void main(){
    List<String> names = new ArrayList<>();
}
```

*Raw type* menghilangkan argumen tipe pada deklarasi dan konstruksi:

```java
void main(){
    List names = new ArrayList();
}
```

Pemeriksaan dari `List<String>` pun hilang; daftar ini dapat menampung string sekaligus bilangan bulat:

```java
void main(){
    List names = new ArrayList();
    names.add("Mary");
    names.add(35); // allowed
}
```

`List<?>` berarti daftar bertipe **tidak diketahui**: elemen sembarang tidak dapat ditambahkan, kecuali `null`. `List` mentah menerima elemen tanpa pemeriksaan tersebut. Dalam kode baru, gunakan argumen tipe atau wildcard; raw type terutama diperlukan untuk berinteraksi dengan kode lama.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
