print("=============================INPUT=============================")
jam = float(input("Masukan Jam : "))

if 0 <= jam <= 10 :
    print ("Good Morning Baby ")
elif 10 < jam <= 15 :
    print ("Good Afternoon Dear")
elif 15 < jam <= 18 :
    print ("Good Evening Sweetheart")
elif 18 < jam <= 24 :
    print ("Good Night Babe")
else :
    print ("Rak Mutu")

if 14 <= jam <= 16 :
    print ("Jam Kuliah")