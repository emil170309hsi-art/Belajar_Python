#tugas 1

jadwal_senin = ["English", "MTK","Olahraga", "IT", "Tahfidz"]

# print(f"List Lengkap: {jadwal_senin}")
# print(f"Awal: {jadwal_senin[0]}")
# print(f"Akhir: {jadwal_senin[-1]}")



# tugas 2

jadwal_senin[2] = "Kimia"
print(f"Setelah di ubah: {jadwal_senin}")



#tugas 3

nilai_mentah = [55, 63, 72, 81, 90]

for i in range(len(nilai_mentah)):
    nilai_mentah[i] = nilai_mentah[i] + 5

print("List setelah di tambah 5:", nilai_mentah)



#tugas 4

awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]

seminggu = awal_minggu + akhir_minggu
hari_kerja = seminggu[:5]

print(f"Hasil: {hari_kerja}")

