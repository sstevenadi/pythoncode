def kalk(a,b,c):
    if c == "+":
        d = a+b
    if c == "-":
        d = a-b
    if c == "/":
        d = a/b
    if c == "x":
        d = a*b
    return d

print ("="*30)

print("Pertambahan")
print(kalk(9,2,'+'),"\n")

print("Pengurangan")
print(kalk(11,4,'-'),"\n")

print("Pembagian")
print(kalk(9,3,'/'),"\n")

print("Perkalian")
print(kalk(4,3,'x'))

print ("="*30)
