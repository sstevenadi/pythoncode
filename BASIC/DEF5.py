def kotak(n):
    print ("="*30)

    for a in range (n):
        for b in range (n,a+1,-1):
            print (" ",end="")
        for b in range (a):
            print ("*",end="")
        for b in range (a+1):
            print ("*",end="")
        print ()

    for c in range (n-1):
        for d in range (c+1):
            print (" ",end="")
        for d in range (n-1,c,-1):
            print ("*",end="")
        for d in range (n-1,c+1,-1):
            print ("*",end="")
        print ()

    print ("="*30)

a = int(input("mo brapa ? "))

kotak(a)


