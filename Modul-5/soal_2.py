def cek_palindrom(kata):
    kata = kata.lower()
    return kata == kata[::-1]

print("Cek Palindrom ")
kata = input("Masukkan kata: ")
hasil = cek_palindrom(kata)
print("Hasil fungsi:", hasil)
if hasil:
    print(f"Kata '{kata}' adalah palindrom")
else:
    print(f"Kata '{kata}' bukan palindrom")
