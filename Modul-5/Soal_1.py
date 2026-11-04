def pelanggan(n):
    if n == 1 or n == 2:
        return 1
    return pelanggan(n - 1) + pelanggan(n - 2)

print("Pelanggan Bu Lastri ")
n = int(input("Masukkan hari ke-N: "))
if n > 0:
    print(f"Jumlah pelanggan pada hari ke-{n} adalah {pelanggan(n)} orang")
else:
    print("N harus bilangan bulat positif!")
