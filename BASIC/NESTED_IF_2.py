print ("============================MENU=============================")
print ("1. Dulux        (DUL)")
print ("2. Catylac      (CAT)")
print ("3. Nippon Paint (NIP)")
print ("4. Avitex       (AVI)")
print ("5. Mowillex     (MOW)")
print ("\n============================INPUT============================")
nama   = input("Masukan Nama        : ")
tanggal= input("Masukan Tanggal     : ")
urutan = input("Masukan Urutan beli : ")
merk   = str(input("Masukan Merek Cat   : "))
jumlah = int(input("Jumlah Kaleng Cat   : "))

if merk == "DUL" :
    if 0 < jumlah <= 25 :
        harga = 24500
    elif 26 <= jumlah <= 50 :
        harga = 23000
    elif jumlah > 50 :
        harga = 22000
    else :
        harga = 0
elif merk == "CAT" :
    if 0 < jumlah <= 25 :
        harga = 23500
    elif 26 <= jumlah <= 50 :
        harga = 22500
    elif jumlah > 50 :
        harga = 21000
    else :
        harga = 0
elif merk == "NIP" :
    if 0 < jumlah <= 25 :
        harga = 23500
    elif 26 <= jumlah <= 50 :
        harga = 22500
    elif jumlah > 50 :
        harga = 20500
    else :
        harga = 0
elif merk == "AVI" :
    if 0 < jumlah <= 25 :
        harga = 20000
    elif 26 <= jumlah <= 50 :
        harga = 19000
    elif jumlah > 50 :
        harga = 17500
    else :
        harga = 0
elif merk == "MOW" :
    if 0 < jumlah <= 25 :
        harga = 18500
    elif 26 <= jumlah <= 50 :
        harga = 17000
    elif jumlah > 50 :
        harga = 16000
    else :
        harga = 0
else :
    print ("Merek Gak Ada")

tot = harga*jumlah

print ("\n============================OUTPUT===========================")

print ("Nama    : {}".format(nama))
print ("Tanggal : {}".format(tanggal))
print ("Urutan  : {}".format(urutan))
print ("Merk    : {}".format(merk))
print ("Jumlah  : {}".format(jumlah))
print ("Total   : {}".format(tot))