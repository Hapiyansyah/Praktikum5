List_buah= ["apel","jeruk","pisang","anggur","melon"]

#Akses list
print(List_buah[2])
print(List_buah[1:4])
print(List_buah[-1])

#Ubah elemen list
List_buah[3] = "jambu"
print(List_buah[3])
List_buah[3:] = "durian", "nangka"
print(List_buah[3:])

#Tambah elemen list
List_Buah = []
List_Buah.append(List_buah[0:2])
print(List_Buah)
List_Buah.append("nanas")
print(List_Buah)
List_Buah.append([1,2,3])
print(List_Buah)
List_Buah.append(List_buah)
print(List_Buah)