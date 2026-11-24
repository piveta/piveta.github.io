---
layout: post
title: "Pewarisan dan subtipe pada generik Java"
date: 2026-11-24
lang: id
translation_id: heranca-subtipos-genericos-java
permalink: /id/inheritance-and-subtypes-with-java-generics/
share_text: >-
  List<Car> bukan List<Vehicle>; pahami invariansi, pembacaan dengan extends, dan penulisan dengan super.
---

Tipe generik Java bersifat **invarian** secara bawaan. Walaupun `Car` mewarisi `Vehicle`, `List<Car>` bukan subtipe `List<Vehicle>`. Wildcard `extends` dan `super` menyatakan hubungan lain pada saat tipe digunakan.

## Invariansi

Dalam contoh ini, `Car` dan `Motorcycle` mewarisi `Vehicle`:

```java
public class Vehicle {
    public void move() {
        IO.println("Vehicle moving");
    }
}

public class Car extends Vehicle {
    public void honk() {
        IO.println("Horn sounded");
    }
}

public class Motorcycle extends Vehicle {
    public void doWheelie() {
        IO.println("Motorcycle doing a wheelie");
    }
}
```

Daftar mobil tidak dapat diberikan kepada variabel `List<Vehicle>`. Penugasan ini menghasilkan **kesalahan kompilasi**:

```java
void main() {
    List<Car> cars = new ArrayList<>();
    cars.add(new Car());
    // ERROR: List<Car> is not a subtype of List<Vehicle>
    List<Vehicle> vehicles = cars; // Compile-time error!
}
```

Aturan ini menjaga keamanan tipe. Jika diizinkan, `vehicles` dapat dipakai menambahkan sepeda motor ke daftar yang sebenarnya berisi mobil. Potongan berikut **hipotetis**, bukan program yang valid:

```java
    // If it compiled, this would be possible...
    vehicles.add(new Motorcycle());
    // But it would cause errors at runtime
    Car c = cars.get(0);
    // Causes a ClassCastException
```

## Penggunaan kovarian: `extends`

Untuk **membaca** kendaraan atau subtipenya, metode dapat menerima `List<? extends Vehicle>`. Setiap elemen yang dibaca setidaknya merupakan `Vehicle`:

```java
public static void print(List<? extends Vehicle> list) {
   for (Vehicle v : list)
      v.move(); // OK
   // list.add(new Car()); // Not allowed!
}
```

Metode menerima `List<Vehicle>`, `List<Car>`, dan `List<Motorcycle>`, tetapi tidak dapat menambahkan `Car` karena tipe konkret daftar tidak diketahui.

## Penggunaan kontravarian: `super`

Untuk **menambahkan** mobil, metode dapat menerima daftar `Car` atau salah satu supertipenya:

```java
public void add(List<? super Car> list) {
    list.add(new Car()); // allowed
}
```

`List<Car>`, `List<Vehicle>`, dan `List<Object>` dapat dipakai. Saat membaca, hanya `Object` yang dijamin. Kovariansi dan kontravariansi di sini berlaku untuk **penggunaan wildcard**; deklarasi `List<T>` tetap invarian.

---

*Artikel ini mengadaptasi isi buku [Orientação a Objetos com Java](https://www.amazon.com.br/dp/B0FWZ6HYVP), karya Eduardo Kessler Piveta.*
