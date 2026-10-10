# #tugas 1

# # 1. Inisialisasi
# counter = 10

# # 2. Kondisi
# while counter > 0:
#     print(counter)
#     # 3. Pembaruan (Update)
#     counter -= 1  

# print("BlastOff")

#tugas 2

# angka_rahasia = 7

# while True: 
#     data_input = int(input("Masukan angka: "))

#     if data_input == angka_rahasia:
#         print("benar")
#         break 

#     else:
#         print("Salah")
     

# print("Terima kasih sudah bermain!")


#tugas 3

total = 0
jumlah = 0

while True:
    input_angka = input("Masukkan angka (atau 'done' untuk selesai): ")

    if input_angka == "done":
        break

    try:
        angka = int(input_angka)
        total += angka
        jumlah += 1
    except:
        print("Input tidak valid")
        continue

print("Total penjumlahan angka:", total)
print("Banyaknya angka yang valid:", jumlah)

if jumlah > 0:
    rata_rata = total / jumlah
    print("Rata-rata nilai:", rata_rata)