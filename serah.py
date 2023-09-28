jumlah = int(input("Masukkan jumlah peserta = "))
kapasitas = int(input("Masukkan jumlah kapasitas = "))

jumlah_bis = int(jumlah/kapasitas)
if jumlah > kapasitas :
    print("jumlah bis = 2")
else:
    print("jumlah bis = ", jumlah_bis)