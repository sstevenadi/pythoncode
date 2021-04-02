print ('+'*50)

a = [[2,4,7,7,1],
     [8,9,1,8,2],
     [5,3,6,3,1],
     [7,8,1,0,5],
     [2,1,3,4,9]]

b = []

for c in range(5):
    for d in range (5):
        print (a[c][d],end=" ")
    print ()

print ()

for x in range (len(a)):
    b.append(a[x][x])

print ("Outputnya ",sum(b))

print ('+'*50)
