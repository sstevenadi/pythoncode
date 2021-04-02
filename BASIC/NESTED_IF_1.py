print ("============================INPUT============================")
nama    = input("Masukan Nama        : ")
nim     = input("Masukan NIM         : ")
alamat  = input("Masukan Alamat      : ")
ipk     = float(input("Masukan IPK         : "))
semester= int(input("Masukan Semester    : "))
nortu   = input("Masukan Nama Ortu   : ")
pekerj  = input("Masukan Pekerja     : ")
pekerj2 = input("Masukan Pekerja Ibu : ")
gaji    = int(input("Masukan Gaji Ortu   : "))

print ("============================OUTPUT===========================")

if 3.00 < ipk <= 4.00 :
    if semester >= 5 and gaji < 3000000 :
        print ("Selamat, Anda Berhak Menerima Beasiswa")
    else :
        print ("Maaf Anda Belum Diterima")
elif 0 < ipk <= 3.00 :
    print ("Maaf Anda Belum Diterima")
else :
    print ("============================ERROR============================")
