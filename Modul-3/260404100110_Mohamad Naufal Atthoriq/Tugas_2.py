n = int(input("Masukkan tinggi setengah menara (2-15): "))
while n < 2 or n > 15:
    print("Tidak valid, ulangi!")
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

for i in range(1, n + 1): #yang membuat menara makin ke bawah makin lebar
    baris = ""
    for j in range(1, i + 1): #angka naik
        baris += str(j % 10)
    for j in range(i - 1, 0, -1): #angka turun
        baris += str(j % 10)
    print(" " * (n - i) + baris)
    
for i in range(n - 1, 0, -1): #yang membuat menara makin ke bawah makin sempit
    baris = ""
    for j in range(1, i + 1):
        baris += str(j % 10)
    for j in range(i - 1, 0, -1):
        baris += str(j % 10)
    print(" " * (n - i) + baris)