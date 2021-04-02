listNilai = []
matkul = input("Input Nama Mata Kuliah : ")
while(matkul != "-"):
    nilai = input("Input Nilai "+matkul+" : ")
    tidakKetemu = True
    for listt in listNilai:
        if(listt['matkul']==matkul):
            if(nilai < listt['nilai']):
                listt['nilai'] = nilai
            tidakKetemu = False
    if(tidakKetemu):
        listNilai.append({"matkul":matkul, "nilai":nilai})
    print("------------")
    matkul = input("Input Nama Mata Kuliah : ")
print("\n\n")
print("Transkrip Nilai :")
print("--------------------")
count = 1
for listt in listNilai:
    print(str(count)+". "+listt['matkul']+" [Nilai: "+listt['nilai']+"]")
    count+=1