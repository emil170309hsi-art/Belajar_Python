# # tugas 1

# try:
#     angka1 = float(input("Masukkan angka pertama: "))
#     angka2 = float(input("Masukkan angka kedua: "))
#     operasi = input("Masukkan operasi (+, -, *, /): ")

#     if operasi == "+":
#         hasil = angka1 + angka2
#     elif operasi == "-":
#         hasil = angka1 - angka2
#     elif operasi == "*":
#         hasil = angka1 * angka2
#     elif operasi == "/":
#         hasil = angka1 / angka2
#     else:
#         print("Operasi tidak valid!")
#         hasil = None

#     if hasil is not None:
#         print("Hasil:", hasil)

# except ValueError:
#     print("Error: Input angka harus berupa angka!")

# except ZeroDivisionError:
#     print("Error: Tidak bisa membagi dengan nol!")


# # tugas 2

# try: 
#     angka_1 = int(input("Masukan angka: "))
#     angka_2 = int(input("Masukan angka: "))
#     angka_3 = int(input("Masukan angka: "))

#     total = angka_1 + angka_2 + angka_3
#     rata = total / 3
#     print(f"hasil: {rata}")
# except ValueError:
#     print("Error: Kamu harus memasukkan ANGKA, bukan teks!")




# #tugas 3

# try:
#     nilai = int(input("Masukan suhunya: "))

# except ValueError:
#     print("Error: Input harus berupa angka!")

# else:
#     fahr = (nilai * 9/5) + 32
#     print(f"Hasilnya adalah: {fahr}")

# finally:
#     print("=== Konversi selesai ===")



# # tugas 4

# nama = input("Nama produk: ").strip()
# if not nama:
#     print("Error: Produk tidak boleh kosong!")
# else:
#     # Langkah 2: Validasi umur
#     try:
#         harga = float(input("Harga: "))
#         stok = int(input("Stok: "))
#         if harga <= 0 or stok <= 0:
#             print(f"Error: Harga atau Stok tidak boleh 0")
#         else:
#                 print("--- Hasil ---")
#                 print(f"Nama: {nama}")
#                 print(f"Harga: {harga}")
#                 print(f"Stok: {stok}")

#     except ValueError as d:
#                     print(f"Error !!!: {d}")
    


#tugas 5

try:
    harga = int(input("Masukan harga produk: "))
    diskon = int(input("Masukan diskonnya: "))
    if harga <= 0 or diskon < 1 or diskon > 100:
        print("Masukkan harga lebih dari 0 dan diskon 1 sampai 100!!")
    else:
        hasil =  harga - (harga * diskon / 100)
        print(f"harga asli: {harga:.2f}")
        print(f"Diskon: {diskon:.2f}")
        print(f"Harga setelah diskon: {hasil:.2f}")

except ValueError:
    print("Masukan angka mas")

finally:
    print("Selesai")


