def hitung_nilai(nama, tugas, uts, uas):
    akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)
    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"
    if grade in ["A", "B", "C"]:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print("Hasil Perhitungan")
    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", round(akhir, 2))
    print("Grade          :", grade)
    print("Status         :", status)

print("Nilai Akhir Mahasiswa")
nama = input("Nama mahasiswa : ")
tugas = float(input("Nilai tugas    : "))
uts = float(input("Nilai UTS      : "))
uas = float(input("Nilai UAS      : "))
hitung_nilai(nama, tugas, uts, uas)