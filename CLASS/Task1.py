a = int(input("Masukan Koordinat X : "))
b = int(input("Masukan Koordinat Y : "))

if a > 0 and b > 0:
    c = "Kuadran 1"
elif a < 0 and b > 0:
    c = "Kuadran 2"
elif a < 0 and b < 0:
    c = "Kuadran 3"
elif a > 0 and b < 0:
    c = "Kuadran 4"

print ("Titik dengan lokasi (%d,%d) berada pada"%(a,b),c)