print ('+'*50)

c = [d**2 for d in range (1,6)]

print (*([[a for a in range (1,6)]for b in range (1,6)]),sep="\n")

print ()

print (*([[e for e in c]for f in c]),sep="\n")

print ('+'*50)
