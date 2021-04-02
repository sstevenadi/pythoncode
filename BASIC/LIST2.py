print ('--------------------------------------------------------')

inp = 'Y'
a = []

while inp == 'Y':
    b = int(input('Masukan jumlah perulangan : '))
    for c in range (b):
        d = float(input("Masukan angka desimal : "))
        a.append(d)
    inp = input('Ingin lanjut atau tidak ? (Y/N)\n')
    print ()

print ('--------------------------------------------------------')

for e in range (len(a)):
    print ("Index ke-{} = {}".format(e,a[e]))

print ('--------------------------------------------------------')
