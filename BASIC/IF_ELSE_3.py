print("----------------------MENU-----------------------")
print("1. Ice Tea                  @ Rp 6000")
print("2. Caramel Machiato         @ Rp 30000")
print("3. Green Tea Latte          @ Rp 25000")
print("4. Milkshake                @ Rp 15000")
print("5. Chocolate Hazelnut       @ Rp 25000\n")

nama    = input("Masukan nama    : ")
tanggal = input("Masukan tanggal : ")
menu    = int(input("Pilih menu      : "))
jumlah  = int(input("Jumlah benda    : "))

if menu == 1:
    benda = "Ice Tea"
    harga = 6000
elif menu == 2:
    benda = "Caramel Machiato"
    harga = 30000
elif menu == 3:
    benda = "Green Tea Latte"
    harga = 25000
elif menu == 4:
    benda = "Milkshake"
    harga = 15000
elif menu == 5:
    benda = "Chocolate Hazelnut"
    harga = 25000
else :
    print("GAK ADA BEGO")

tot = jumlah*harga

print("----------------------OUTPUT---------------------")
print("Nama pembeli     : {}".format(nama))
print("Tanggal pembeli  : {}".format(tanggal))
print("Nama benda       : {}".format(benda))
print("Total harga      : {}".format(tot))