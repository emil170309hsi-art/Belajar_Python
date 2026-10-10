# # tugas 1

# def salam_pembuka():
#     print(" ========================= \n Selamat datang di program saya!! \n =========================")

# salam_pembuka()


# #tugas 2

# def info_cuaca(kota,cuaca):
#     print(f"Cuaca di {kota} hari ini {cuaca}")

# info_cuaca("Lampung","Berawan")
# info_cuaca("Sukabumi","Panas")


# #tugas 3

# def kubik(angka):
#     return angka ** 3

# hasil_kubik = kubik(4)
# print(f"Hasil adalah: {hasil_kubik}")


# #tugas 4

# def hitung_harga_akhir(harga_barang,persen_pajak):
#     jumlah_pajak = harga_barang *  (persen_pajak / 100)
#     harga_akhir = harga_barang + jumlah_pajak
#     return harga_akhir

# harga = int(input("Masukan harganya: "))
# pajak = int(input("Masukan pajak: "))

# harganya = hitung_harga_akhir(harga, pajak)

# print(f"Total harga adalah: {harganya:.2f}")


#tugas 5

def fahrenheit_ke_celcius(temp_f):
    celcius = (temp_f - 32) * 5/9
    return celcius

hasil = fahrenheit_ke_celcius(98.6)
print(f"Hasil adalah: {hasil}")
