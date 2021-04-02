# Buat Piramid :3

print ('-----------------------------------------')

for a in range (4): #Untuk baris bintang tidak perlu diisi (berfungsi buat nurunin)
    for b in range (3,a,-1): #Untuk kolom yang berfungsi sebagai spasi agar bintang dapat berada di tengah dengan dimulai dari angka terbanyak ke 'a'
        print (' ',end="") 
    for c in range (a): #Untuk kolom bintang diisi dengan range 'a' agar bintang terbuat dengan banyak jumlah a yang berurutan
        print ('*',end="") #'end' Untuk membuat spasi ke samping
    for d in range (a+1):
        print ('*',end='')
    print () #Untuk menambah spasi ke bawah
   
print ('-----------------------------------------')
