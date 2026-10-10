#tugas 1
# judul = input("Masukan judul: ")
# judul_baru = judul.strip().title()

# print(f"{judul_baru}")

# tugas 2
# email= input("Masukan Email Anda: ")

# if "@" in email and email.endswith((".com",".co.id")):
#     print("Email Valid")
# else:
#     print("Email Tidak Valid!!")

#tugas 3
# kata = "harga tiket sangat mahal"
# kata_sensor = kata.replace("mahal","***")
# print(f"{kata_sensor}")

# tugas 4
# nama = input("Masukkan nama organisasi: ")

# kata = nama.split()

# akronim = ""

# for k in kata:
#     akronim += k[0]

# print(akronim.upper())

#tugas 5
judul = input("Masukkan judul artikel: ")

judul = judul.lower()

slug = ""

for karakter in judul:
    if karakter.isalnum() or karakter == " ":
        if karakter == " ":
            slug += "-"
        else:
            slug += karakter

print(slug)
