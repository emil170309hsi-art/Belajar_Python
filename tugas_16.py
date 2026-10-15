#tugas 1
belanjaan = []
belanjaan.append("Telur")
belanjaan.append("Susu")
belanjaan.append("Roti")
belanjaan.insert(0,"Apel")
belanjaan.remove("Susu")

print(belanjaan)


#tugas 2
nilai = [98, 76, 88, 100, 54]
nilai_urut=sorted(nilai)

print(nilai)
print(nilai_urut)



#tugas 3

kata = input("Masukan kata-kata: ")
daftar_kata = kata.split()

print(f"Jumlah elemen: {len(kata)}")
daftar_kata.sort()

print(f"Hasilnya: {daftar_kata}")


#tugas 5

nilai_ujian = [45, 67, 88, 52, 91, 76, 60]

nilai_lulus = [nilai for nilai in nilai_ujian if nilai >= 65]

predikat = ["Lulus" if nilai >= 65 else "Remedial" for nilai in nilai_ujian]

print(f"nilai_lulus = {nilai_lulus}")
print(f"predikat = {predikat}")