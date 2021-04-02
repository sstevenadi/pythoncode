print ('----------------------------------------------------------')

print ('1. For\n2. While\n3. Do-While')

a = int(input('\nPilih perulangan yang akan digunakan : '))
b = 0

print ('----------------------------------------------------------')

if a == 1 :
    for x in range (0,128):
        print ('The ASCII Code for',chr(x))
elif a == 2 :
    while b < 127:
        b += 1
        print ('The ASCII Code for',chr(b))
elif a == 3 :
    print ('There is no Do-While loop in Python, only in C')
else :
    print ('Wrong Input')

print ('----------------------------------------------------------')