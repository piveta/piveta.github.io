---
layout: post
title: "Kelas dan metode generik di Java"
date: 2026-11-24
lang: id
translation_id: classes-metodos-genericos-java
permalink: /id/generic-classes-and-methods-in-java/
share_text: >-
  Tipe generik membuat kelas dan metode dapat digunakan kembali dengan pemeriksaan tipe; contoh Adapter<T>.
---

**Polimorfisme parametrik** memungkinkan kelas, antarmuka, record, atau metode menyesuaikan diri dengan tipe yang ditentukan saat digunakan. Generik di Java mendukung penggunaan ulang kode dan mengurangi konversi tipe yang tidak perlu. `List<String>` dan `List<Integer>` memakai antarmuka yang sama, tetapi kompiler memeriksa tipe elemen masing-masing.

Tanpa parameter tipe, `Adapter` memakai `Object` untuk field, konstruktor, dan metodenya:

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

Kelas ini dapat menyimpan objek apa pun, tetapi tidak membatasi sebuah adapter pada satu tipe tertentu. Dengan mendeklarasikan `T`, implementasi yang sama memakai tipe pilihan pemanggil:

```java
public class Adapter<T>{
    T object;
    public T get(){
        return object;
    }
    public void set(T value){
        object = value;
    }
    public Adapter(T initial){
        object = initial;
    }
}
```

Klien berikut membuat `Adapter<String>`. Konstruktor dan `set` menerima string, sedangkan `get` mengembalikan string. Program mencetak `Test` lalu `New Value`:

```java
void main(){
    var a = new Adapter<String>("Test");
    IO.println(a.get());
    a.set("New Value");
    IO.println(a.get());
}
```

## Metode generik

Metode juga dapat mendeklarasikan parameter tipe sebelum tipe hasilnya. `print` menerima daftar dengan tipe berbeda sambil mempertahankan pemeriksaan oleh kompiler:

```java
public static <T> void print(List<T> list){
    for (T element : list)
        IO.println(element);
}
void main(){
    List<Integer> integers = List.of(1, 2, 3, 4);
    List<String> names = List.of("Mary", "John", "Carol");
    print(integers);
    print(names);
}
```

Parameter tersebut juga dapat menentukan tipe hasil. `first` menerima `List<T>` dan mengembalikan `T`: `Integer` untuk daftar bilangan bulat dan `String` untuk daftar nama.

```java
public static <T> T first(List<T> list) {
    return list.isEmpty() ? null : list.get(0);
}
void main(){
    List<Integer> integers = List.of(1, 2, 3, 4);
    List<String> names = List.of("Mary", "John", "Carol");
    Integer integer = first(integers);
    String name = first(names);
    IO.println(integer);
    IO.println(name);
}
```

Variabel perantara memperjelas tipe; ekspresi juga dapat dipakai secara langsung:

```java
// Implementation of "first" omitted here
void main(){
    IO.println(first(List.of(1, 2, 3, 4)));
    IO.println(first(List.of("Mary", "John", "Carol")));
}
```

## Parameter tipe dengan batas

`multiply` menerima daftar `Number` atau subtipenya. Batas `<T extends Number>` memungkinkan pemanggilan `doubleValue()` pada tiap elemen:

```java
public static <T extends Number> Double multiply(List<T> list){
    Double product = 1.0;
    for (T number : list)
        product *= number.doubleValue();
    return product;
}
```

Daftar `Integer` maupun `Double` dapat digunakan:

```java
void main(){
    IO.println(multiply(List.of(1, 2, 3, 4)));
    IO.println(multiply(List.of(1.1, 2.2, 3.5)));
}
```

Kompiler memeriksa parameter pada setiap pemanggilan, sementara metodenya tetap satu implementasi.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
