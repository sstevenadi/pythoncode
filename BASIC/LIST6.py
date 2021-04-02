print ('--------------------------------------------------------')

a = int(input("Input number of data : "))

b = []
e = []

for x in range (a):
    c = int(input("Input the number : "))
    b.append(c)

for y in b:
    if y%2==0:
        e.append(y)
    else :
        continue

print ('The second even number is',e[1])

print ('--------------------------------------------------------')