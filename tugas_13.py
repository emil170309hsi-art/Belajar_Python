#tugas 1
# nama_file = input("Masukan nama file!")

# try:
#     with open(nama_file, "r") as file:
#         for baris in file:
#             print(baris.upper(), end="")

# except FileNotFoundError:
#     print("FILE TIDAK DI TEMUKAN")


#tugas 2

# nama_file = input("Masukkan nama file: ")

# total = 0
# jumlah = 0

# try:
#     with open(nama_file, "r") as file:
#         for baris in file:
#             if baris.startswith("X-DSPAM-Confidence:"):
#                 angka = float(baris[20:].strip())
#                 total += angka
#                 jumlah += 1

#     rata_rata = total / jumlah
#     print("Average spam confidence:", rata_rata)

# except FileNotFoundError:
#     print("FILE TIDAK DITEMUKAN")
    


#tugas 3

nama_file = input("Masukkan nama file: ")

if nama_file == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                print(baris.strip())

    except FileNotFoundError:
        print("File tidak ditemukan")