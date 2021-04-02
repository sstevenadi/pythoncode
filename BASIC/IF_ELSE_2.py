print("----------------------INPUT----------------------")
tinggi = float(input("Masukan tinggi : "))
berat = float(input("Masukan berat  : "))

bmi = berat/(tinggi*tinggi)
bmi2 = round(bmi,3)

print("BMI = {}".format(bmi2))

if bmi < 18:
    print("----------------------OUTPUT---------------------")
    print("Under Weight")
elif bmi <= 25:
    print("----------------------OUTPUT---------------------")
    print("Normal Weight")
elif bmi <= 27:
    print("----------------------OUTPUT---------------------")
    print("Over Weight")
elif bmi > 27:
    print("----------------------OUTPUT---------------------")
    print("Obesitas")