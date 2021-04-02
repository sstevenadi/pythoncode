print ("====================INPUT====================")

num = int(input("Input Number : "))

print ("====================OUTPUT===================")

if num > 0 and num < 10 :
    print ("Your input is a number in the units")
elif num >= 10 and num < 100 :
    print ("Your input is a number in the tens")
elif num >= 100 and num < 1000 :
    print ("Your input is a number in the hundreds")
else :
    print ("Your input is not valid, please enter more than 0 or below 1000")