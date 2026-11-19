undangan = set()
webinar_a = set()
webinar_b = set()

n = int(input("Jumlah undangan: "))
for i in range(n):
    undangan.add(input(f"Nama undangan {i+1}: "))

n = int(input("Jumlah peserta Webinar A: "))
for i in range(n):
    webinar_a.add(input(f"Nama peserta A {i+1}: "))

n = int(input("Jumlah peserta Webinar B: "))
for i in range(n):
    webinar_b.add(input(f"Nama peserta B {i+1}: "))

print("\nSemua peserta (A atau B):", webinar_a | webinar_b)
print("Hadir di keduanya:", webinar_a & webinar_b)
print("Hanya di salah satu:", webinar_a ^ webinar_b)
print("Undangan tidak hadir di mana pun:", undangan - (webinar_a | webinar_b))