# import sys

# def cetak_dasar(objek):
#     teks = str(objek) + "\n"
#     sys.stdout.write(teks)

# cetak_dasar("allo_dunia")
# cetak_dasar(123)
###
# def menampilkan_luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas

# menampilkan_luas_persegi_panjang(10,5)
# print(menampilkan_luas_persegi_panjang(10,5))
###
# def luas(sisi):
#     return sisi*sisi

# print(luas(10))
###
# def hitung_nilai(nilai):
#     if nilai >= 90:
#         return "A"
#     elif nilai >= 80:
#         return "B"
#     elif nilai >= 70:
#         return "C"
#     else:
#         return "D"

# print(hitung_nilai(80))
###
# kali = lambda a , b : a * b
# print(kali(5,5))
###
# luas = lambda sisi: sisi * sisi
# print(luas(10))
# nama_kampus = "UTM"

# def tampilkan_info()
#     prodi = "Sistem Informasi"
#     print("kampus:", nama_kampus)
#     print("prodi:", prodi)

# tampilkan_info()


def perkenalan(nama, hobi):
    print("Halo, nama saya", nama)
    print("Hobi saya adalah", hobi)

nama_saya = input("Masukkan nama Anda: ")
hobi_saya = input("Masukkan hobi Anda: ")

perkenalan(nama_saya, hobi_saya)