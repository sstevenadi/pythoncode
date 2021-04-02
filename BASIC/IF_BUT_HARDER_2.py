print ("====================INPUT====================")

num = int(input("Input ASCII Number : "))

print ("====================OUTPUT===================")

if num >= 0 and num <= 31 :
    print ("It's a Control Character")
elif num >= 32 and num <=47 or num >= 58 and num <= 64 or num >= 91 and num <= 96 or num >= 123 and num <=127 :
    print ("It's a Special Character")
elif num >= 48 and num <=57 :
    print ("It's a Number")
    if num % 2 == 0:
        print ("And it's an even number")
    else :
        print ("And it's an odd number")
elif num >= 65 and num <=90 :
    print ("It's a Capital letters")
    if num in [65, 69, 73, 79, 85] :
        print ("And it's a vocal alphabet")
    else :
        print ("And it's a consonant alphabet")
elif num >= 97 and num <= 122 :
    print ("It's a 	Lowercase letters")
    if num in [97, 101, 105, 111, 117] :
         print ("And it's a vocal alphabet")
    else :
        print ("And it's a consonant alphabet")
elif num < 0 or num > 127 :
    print ("Your input is not valid, please enter more than 0 or less than 128")
