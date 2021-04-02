a = int(input("Masukan Jam   : "))
b = int(input("Masukan Menit : "))
c = b-45

if c < 0 and a <= 24:
    l = a-1
    d = c+60
    print("Alarm diset pada waktu : %d.%d"%(l,d))
elif c > 0:
    print("Alarm diset pada waktu : %d.%d"%(a,c))
else :
    print ("Jam Salah !")
