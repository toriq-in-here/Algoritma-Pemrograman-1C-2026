<!-- # Algoritma-Pemrograman-1D-2026 -->

mahasiswa = {"Andi": 80,"Budi": 90,"Citra": 85}

nama = input("Masukkan nama yang dicari: ")

try:
    print("Nilai mahasiswa:", mahasiswa[nama])

except KeyError:
    print("Nama mahasiswa tidak ditemukan")

#
mahasiswa = {
    "Andi": 80,
    "Budi": 90,
    "Citra": 85
}

for nama, nilai in mahasiswa.items():
    print(nama, ":", nilai)

#

webinar_a = {"Andi", "Budi", "Citra"}
webinar_b = {"Budi", "Doni", "Eko"}

semua_peserta = webinar_a | webinar_b

print("Semua peserta:", semua_peserta)

#
try:
    angka = int(input("Masukkan angka: "))
    print("Angka kamu:", angka)

except ValueError:
    print("Input harus berupa angka!")

#
webinar_a = set()
webinar_b = set()

try:
    jumlah_a = int(input("Jumlah peserta Webinar A: "))

    for i in range(jumlah_a):
        nama = input("Nama peserta A: ")
        webinar_a.add(nama)

    jumlah_b = int(input("Jumlah peserta Webinar B: "))

    for i in range(jumlah_b):
        nama = input("Nama peserta B: ")
        webinar_b.add(nama)

    print("\nPeserta Webinar A:", webinar_a)
    print("Peserta Webinar B:", webinar_b)

    print("Semua peserta:", webinar_a | webinar_b)
    print("Peserta kedua webinar:", webinar_a & webinar_b)
    print("Peserta Webinar A saja:", webinar_a - webinar_b)

except ValueError:
    print("Jumlah peserta harus berupa angka!")