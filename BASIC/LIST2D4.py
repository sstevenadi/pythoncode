print ('+'*50)

nama = []
nim = []
smt = []
ipk = []

x = int(input("Hauw meni data du yu wan tu input : "))

while 0 < x <= 10:
    a = input("Input nama lu : ")
    b = input("Nim juga dong : ")
    c = input("Semester jangan lupa : ")
    d = float(input("Kepintaran lu seberapa : "))
    nama.append(a)
    nim.append(b)
    smt.append(c)
    ipk.append(d)
    x -= 1

print ('+'*50)

pil = int(input("Automatic Sort Machine                                                      v2.0.1.3a BETA\n\nSort :\n1.Name\n2.NIM\n3.Semester\n4.GPA\n\n>>> "))

if pil == 1:
    for a1 in range (len(nama)):
        nama.sort()
        print (a1+1,".",nama[a1])

elif pil == 2:
    for a1 in range (len(nim)):
        nim.sort()
        print (a1+1,".",nim[a1])

elif pil == 3:
    for a1 in range (len(smt)):
        smt.sort()
        print (a1+1,".",smt[a1])

elif pil == 4:
    for a1 in range (len(ipk)):
        ipk.sort()
        print (a1+1,".",ipk[a1])

print ('+'*50)