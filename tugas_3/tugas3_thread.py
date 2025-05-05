# Krisna Bimantoro
# 202210370311254

import threading
import math


def luas_segitiga(alas, tinggi):
    print(f"Luas Segitiga: {0.5 * alas * tinggi}")


def luas_persegi_panjang(panjang, lebar):
    print(f"Luas Persegi Panjang: {panjang * lebar}")


def luas_lingkaran(jari_jari):
    print(f"Luas Lingkaran: {math.pi * jari_jari ** 2}")


def volume_tabung(jari_jari, tinggi):
    print(f"Volume Tabung: {math.pi * jari_jari ** 2 * tinggi}")


def main():
    for i in range(5):
        print(f"\nIterasi {i+1}:")
        alas = float(input("Masukkan alas segitiga: "))
        tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        tinggi_tabung = float(input("Masukkan tinggi tabung: "))

        threads = [
            threading.Thread(target=luas_segitiga,
                             args=(alas, tinggi_segitiga)),
            threading.Thread(target=luas_persegi_panjang,
                             args=(panjang, lebar)),
            threading.Thread(target=luas_lingkaran, args=(jari_jari,)),
            threading.Thread(target=volume_tabung,
                             args=(jari_jari, tinggi_tabung))
        ]

        for t in threads:
            t.start()

        for t in threads:
            t.join()


if __name__ == "__main__":
    main()
