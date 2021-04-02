def taunaneh(a):
    if a%4==0:
        if a%100==0:
            if a%400==0:
                print ("true")
            else :
                print ("false")
        else:
            print ("true")
    else :
        print ("false")

print ("="*30)
taunaneh(2000)
taunaneh(2020)
taunaneh(2100)
taunaneh(2013)
print ("="*30)