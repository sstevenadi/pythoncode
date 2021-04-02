print ('+'*50)

print ("\nFor Odd\n")

print (*([a for a in range(100) if a%2==0]),sep="\n")

print ("\nFor Even\n")

print (*([a for a in range(100) if a%2==1]),sep="\n")

print ('+'*50)