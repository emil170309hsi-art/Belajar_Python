#tugas 1

# nama_file = "catatan_belanja.txt"

# with open(nama_file, "a") as file:
#     print(f"\nMenambahkan item baru ke '{nama_file}'...")

#     tugas_baru = input("Masukkan tugas anda: ")

#     file.write(tugas_baru + "\n")

#     print("Berhasil menambahkan 1 item baru.")

# print(f"File '{nama_file}' telah ditutup.")



#tugas 2

# with open("sumber.txt", "r") as file_sumber:
#     isi_file = file_sumber.read()

# with open("salinan.txt", "w") as file_salinan:
#     file_salinan.write(isi_file)

# print("File berhasil disalin!")


#tugas 3

# import os

# nama_file = input("Masukan Nama Filenya: ")
# if os.path.exists(nama_file):
#     filen= input(f"Anda Yakin Utk Menghapus {nama_file}? (y/n)")

#     if filen == "y":
#         os.remove(nama_file)
#         print("Selesai!!")

#     else :
#         print("Tidak Jadi!!")
# else:
#     print(f"File '{nama_file}' tidak ada.")