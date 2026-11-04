def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol"
    return a / b
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua  : "))

print("Hasil tambah :", tambah(angka1, angka2))
print("Hasil kurang :", kurang(angka1, angka2))
print("Hasil kali   :", kali(angka1, angka2))
print("Hasil bagi   :", bagi(angka1, angka2))