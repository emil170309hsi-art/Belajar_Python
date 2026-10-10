# #tugas 1

# s = "Belajar Python itu Menyenangkan"

# print(s[0])
# print(s[-1])
# print(s[7])


# #tugas2 
# s = "Belajar Python itu Menyenangkan"
# print(s[8:14])
# print(s[0:7])
# print(s[19:31])


# #tugas 3

# kata=input("Masukan kata! ")
# kata2=kata[::-1]

# print(kata2[::])

# if kata == kata2:
#     print("Itu kalimat Palindrom")

# else:
#     print("_________")


# #tugas 4
# kode="BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

# print(kode[::3])


#tugas 5
nama_salah = "mUHAMMAD fAHRI"

nama1=nama_salah[0:8]
nama2=nama_salah[9:14]

nama1_baru=nama1[0].upper() + nama1[1:].lower()
nama2_baru=nama2[0].upper() + nama2[1:].lower()

hasil=nama1_baru + " " + nama2_baru

print(hasil)