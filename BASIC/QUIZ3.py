a = int(input("batas awal: "))
b = int(input("batas akhir: "))

x = 0
l = []

for c in range (a,b):
    x = x+1
    d = c + x
    print (d)
    l.append(d)
    if d == b:
        break

print ()
print (sum(l))
print (sum(l)/len(l))
    
