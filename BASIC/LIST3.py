print ('--------------------------------------------------------')

a ='Y'
b = []

while a == 'Y':
    c = int(input("Jumlah perulangan : "))
    for d in range (c):
        e = input("Masukan data : ")
        b.append(e)
    a = input("Ingin input lagi ? (Y/N)\n")
    print ()
    if a == 'N':
        f = input("Masukan data yang dicari : ")
        if f in b:
            print ('Data ditemukan')
        else :
            print ("Data tidak ditemukan\n")
            a = input('Mau coba lagi ? (Y/N)\n')
            print ()

print ('--------------------------------------------------------')
