nilai_mahasiswa =[80, 75, 90, 85, 70]

print("daftar mahasiswa", nilai_mahasiswa)

tertinggi = max(nilai_mahasiswa)
terendah = min(nilai_mahasiswa)

print ("nilai tertinggi:", tertinggi)
print ("nilai terendah:", terendah)

rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)
print("rata-rata: 80")

nilai_mahasiswa.append(99)
print("nilai setelah ditambahkan:", nilai_mahasiswa)

nilai_mahasiswa.remove(85)
print("nilai setelah di hapus:", nilai_mahasiswa)



