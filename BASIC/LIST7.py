print ('--------------------------------------------------------')

a = int(input("Input number of data : "))

b = []
e = []

for x in range (a):
    c = int(input("Input the number : "))
    b.append(c)

for y in b:
    if y%2==1:
        e.append(y)
    else :
        continue

print ('The last odd number is',e[-1])

print ('--------------------------------------------------------')