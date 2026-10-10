
#tugas 1

jam= int(input("Berapa jam:"))
tarif=int(input("Tarifnya berapa:"))

if jam > 40 :
    jam_lembur= jam - 40
    total= (40 * tarif) + (jam_lembur * tarif * 1.5)
    print(f"pay: {total}")

else:
    print(f"pay: {jam * tarif}")



#tugas 2

try:
    jam= int(input("Berapa jam:"))
    tarif=int(input("Tarifnya berapa:"))

    if jam > 40 :
        jam_lembur= jam - 40
        total= (40 * tarif) + (jam_lembur * tarif * 1.5)
        print(f"pay: {total}")

    else:
        print(f"pay: {jam * tarif}")

except:
    print("masukan angka mas!!!")


#tugas 3

try:
    berat = int(input("Masukan berat anda: "))
    tinggi_cm = int(input("Masukan tinggi anda: "))

    tinggi_m = tinggi_cm / 100
    bmi = berat / (tinggi_m ** 2)
    skor = float(bmi)

    if skor < 18.5:
        hasil = "Kurus"

    elif skor >= 18.5 and skor < 25.0:
        hasil = "Normal"

    elif skor >= 25.0 and skor < 30.0:
        hasil = "Kelebihan"

    elif skor >= 30.0:
        hasil = "Obesitas"

    else:
        hasil = "Kurang gizi"

    print(f"BMI kamu adalah: {skor:.2f} ({hasil})")
except:
    print("Masukan angka mas!!")


# #tugas 4
try:
    tinggi = float(input("masukan tinggi anda: "))
    usia = float(input("masukan umur anda: "))
    didampingi = True

    if tinggi >= 150 and (usia > 12 or didampingi):
        print("Boleh Masuk")
    else:
        print("Tidak Boleh Masuk")
except:
    print("masukan angka mas!!")