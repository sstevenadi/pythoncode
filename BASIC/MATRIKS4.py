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

mat3 = []

for a in range(0, len(mat1)):
    b = []
    for c in range(0, len(mat1[0])):
        d = 0
        for e in range(0, len(mat1)):
            d = d + (mat1[a][e] * mat2[e][c])
        b.append(d)
    mat3.append(b)

for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):
        print (mat3[x][y], end=' ')
    print ()

print ('+'*50)