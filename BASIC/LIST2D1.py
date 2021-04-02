print ('+'*50)

mat1 = [[1,2,3,4,5],
        [5,4,3,2,1],
        [6,7,8,9,1],
        [1,9,8,7,6],
        [1,3,5,7,9]]

mat2 = [[5,4,3,2,1],
        [1,2,3,4,5],
        [1,9,8,7,6],
        [9,8,7,6,1],
        [9,7,5,3,1]]

mat3 = [[1,2,3,4,5],
        [5,4,3,2,1],
        [6,7,8,9,1],
        [1,9,8,7,6],
        [1,3,5,7,9]]

pil = int(input("Masukan Matrix yang akan dibandingnkan (Matrix liat kode) : "))

if pil == 1:
    x = mat2
else :
    x = mat3


if y == x :
    print ("Matriks A sama dengan matriks B")
else :
    print ("“Matriks A tidak sama dengan matriks B")
    
