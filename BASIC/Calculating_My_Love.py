print ("============================PILIHAN============================")
print ("1. +\n2. -\n3. x\n4. :\n5. ^\n6. v")

print ("=============================INPUT=============================")
pil = str(input("Pilih Fungsi : "))

if pil == "tambah" :
    print("=============================INPUT=============================")
    a1 = float(input("Masukan Angka 1 : "))
    a2 = float(input("Masukan Angka 2 : "))
    a3 = a1 + a2
    print("=============================OUTPUT============================")
    print ("Hasilnya adalah {}".format(a3))
elif pil == "kurang" :
    print("=============================INPUT=============================")
    a1 = float(input("Masukan Angka 1 : "))
    a2 = float(input("Masukan Angka 2 : "))
    a3 = a1 - a2
    print("=============================OUTPUT============================")
    print ("Hasilnya adalah {}".format(a3))
elif pil == "kali" :
    print("=============================INPUT=============================")
    a1 = float(input("Masukan Angka 1 : "))
    a2 = float(input("Masukan Angka 2 : "))
    a3 = a1 * a2
    print("=============================OUTPUT============================")
    print ("Hasilnya adalah {}".format(a3))
elif pil == "bagi" :
    print("=============================INPUT=============================")
    a1 = float(input("Masukan Angka 1 : "))
    a2 = float(input("Masukan Angka 2 : "))
    a3 = a1 / a2
    print("=============================OUTPUT============================")
    print ("Hasilnya adalah {}".format(a3))
elif pil == "pangkat" :
    print("=============================INPUT=============================")
    a1 = float(input("Masukan Angka 1 : "))
    a2 = float(input("Masukan Angka 2 : "))
    a3 = a1 ** a2
    print("=============================OUTPUT============================")
    print ("Hasilnya adalah {}".format(a3))
elif pil == "akar" :
    print("=============================INPUT=============================")
    a1 = float(input("Masukan Angka 1 : "))
    a2 = float(input("Masukan Angka 2 : "))
    a3 = a1 // a2
    print("=============================OUTPUT============================")
    print ("Hasilnya adalah {}".format(a3))
else :
    print("*****************************ERROR*****************************")

