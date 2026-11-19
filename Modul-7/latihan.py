###Dictionary###
# data = {
#     "nama": "Thoriq", 
#     "Prodi": "Sistem Informasi", 
#     "NIM": "26-110"
#     }
# data['Prodi'] = "Teknik Informatika"
# data['umur'] = 20
# # del data['NIM']
# # data.clear()

# print(data)

###
# data = {
#     "nama": "Thoriq", 
#     "Prodi": "Sistem Informasi", 
#     "NIM": "26-110"
#     }
# data['Prodi'] = "Teknik Informatika"
# data['umur'] = 20

# print(data['nama'])
# print(len(data))
###Dictionary###

###SET###
# A = {"banana", "apple", "orange"}

# print(A)

##
# A = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(A)
# print(b)

# c = A.union(b)
# print(c)

# D = A.intersection(b)
# print(D)

# E = A.difference(b)
# print(E)

# F = A.symmetric_difference(b)
# print(F)

# G = A.issubset(b)
# print(G)
###TRY EXCEPT###

# angka = int(input("Masukkan angka: "))
# print("Angka yang kamu masukkan adalah: ", angka)
# print("Program selesai")

# try:
#     angka = int(input("Masukkan angka: "))
#     print("Angka yang kamu masukkan adalah: ", angka)
# except ValueError:
#     print("Input yang dimasukkan bukan angka yang valid.")

mahasiwa = {"andi": 85, "budi": 89}

try:
    print(mahasiwa["toriq"])
except KeyError:
    print("Nama tidak ditemukan")
