print ('+'*50)

a = [[2,4,7,7,1],
     [8,9,1,8,2],
     [5,3,6,3,1],
     [7,8,1,0,5],
     [2,1,3,4,9]]

b = []

for x in range(len(a)):
    col = []
    for y in range (len(a[x])):
        z = a[y][x]
        col.append(z)
    b.append(col)   
    
for g in range(len(a)):
    print ("Jumlah baris pertama {} - {}".format(g+1,sum(a[g])))

for c in range(len(b)):
    print (("Jumlah kolom pertama {} - {}".format(c+1,sum(b[c]))))

print ('+'*50)
