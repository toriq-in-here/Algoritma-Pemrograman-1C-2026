
n = int(input("Masukkan bilangan bulat positif n: "))

for i in range(1, n + 1):
    # Piramida kiri: angka 1 sampai i
    for angka in range(1, i + 1):
        print(angka, end="")
    for spasi in range(n - i):
        print(" ", end="")

    # Jarak antar piramida
    print("   ", end="")

    # Piramida kanan (cermin): angka i sampai 1
    for spasi in range(n - i):
        print(" ", end="")
    for angka in range(i, 0, -1):
        print(angka, end="")

    print()
