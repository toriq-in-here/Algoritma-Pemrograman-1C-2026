GAJI_POKOK_PER_HARI = 100000
BONUS_SHIFT_MALAM = 50000
JAM_LEMBUR_VALID = [0, 1, 2, 3, 4, 6, 8]

total_gaji = 0

for hari in range(1, 3):
    print(f"Hari {hari}")
    gaji_hari = GAJI_POKOK_PER_HARI

    while True:
        jam_lembur = int(input("Masukkan jam lembur: "))
        if jam_lembur > 8:
            print("Jumlah lembur melebihi batas (maksimal 8 jam). Upah lembur tidak dihitung.")
        elif jam_lembur in JAM_LEMBUR_VALID:
            break
        else:
            print("Jam lembur tidak sesuai ketentuan. Masukkan ulang.")

    if jam_lembur == 0:
        upah_lembur = 0
    elif jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("Shift malam? (y/t): ")
    while shift not in ("y", "t"):
        shift = input("Masukkan y atau t: ")

    if shift == "y":
        gaji_hari += BONUS_SHIFT_MALAM

    total_gaji += gaji_hari + upah_lembur
    print(f"Gaji hari {hari}: Rp{gaji_hari + upah_lembur:,}")

print(f"\nTotal gaji mingguan: Rp{total_gaji:,}")

