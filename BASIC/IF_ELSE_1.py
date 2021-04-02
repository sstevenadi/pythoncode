print("----------------------INPUT----------------------")
nama = input("Masukan nama          : ")
tgl = input("Masukan tanggal       : ")
kaleng = int(input("Masukan jumlah kaleng : "))

if kaleng < 1:
    harga = 0
elif kaleng <= 10:
    harga = 25000
elif kaleng <= 25:
    harga = 24500
elif kaleng <= 50:
    harga = 23000
elif kaleng > 50:
    harga = 22000

tot = kaleng*harga


print("----------------------OUTPUT---------------------")
print("Nama                 : {}".format(nama))
print("Tanggal Pembelian    : {}".format(tgl))
print("Total Kaleng         : {}".format(kaleng))
print("Total Harga          : Rp {}".format(tot))