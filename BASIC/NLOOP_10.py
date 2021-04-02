print ('-----------------------------------------')

for a in range (1,6): #Untuk baris bintang tidak perlu diisi (berfungsi buat nurunin)
    for b in range (5,a,-1): #Untuk kolom yang berfungsi sebagai spasi agar bintang dapat berada di tengah dengan dimulai dari angka terbanyak ke 'a'
        print (' ',end="") 
    for c in range (a): #Untuk kolom bintang diisi dengan range 'a' agar bintang terbuat dengan banyak jumlah a yang berurutan
        print ('*',end="") #'end' Untuk membuat spasi ke samping
    print () #Untuk menambah spasi ke bawah

print ('-----------------------------------------')