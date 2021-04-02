a = int(input("Masukan Baris : "))
b = int(input("Masukan Kolom : "))

c = []
tc = []
maks = 0
mins = 20
tot = 0
asd = 0

for d in range (a):
    e = []
    for f in range (b):
        e.append(int(input("Masukan Angka [{}][{}] : ".format(d+1,f+1))))
    c.append(e)

print ()

for d in range (a):
    for f in range (b):
        print (c[d][f],end=" ")
    print ()

for d in range (b):
    td = []
    for f in range (a):
        td1 = c[f][d]
        td.append(td1)
    tc.append(td)

print ()

for x in range (0,b,2):
    minstc = min(tc[x])
    makstc = max(tc[x])
    if maks < makstc:
        maks = makstc
    if mins > minstc:
        mins = minstc
    tot = tot + sum(tc[x])
    asd = asd + len(tc[x])


print ("angka max",maks)
print ("angka min",mins)
print ("rata-ratanya adalha",tot/asd)





