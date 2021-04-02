#Prorgram Registrasi ID

op  = 'Y'
ops = 'Y'

id = []
pw = []

print ('                                WTTP V2.3.0.0 Beta')

#Pemilihan Opsi

while op == 'Y':
    print ('--------------------------------------------------------')
    print ('WELCOME TO THE PROGRAM')
    print ('1. Log in\n2. Register\n3. Quit\n')
    op1 = input('>>> ')
    if op1 in ['1','Log In','login','log in','Login']:
        print ('--------------------------------------------------------')
        op = 1
        print ('LOGIN')
        user = input('Input ID : \n\n>>> ')
        pasw = input('Input Password : \n\n>>> ')
        if user in id and pasw in pw:
            print ('--------------------------------------------------------\n')
            print ('Login Successfull !')
            print ('Welcome user number - {} ({})'.format(id.index(user),user))
        else :
            print ('--------------------------------------------------------')
            print ('Login Unsuccessfull !')
            op = input('Want to try again ? (Y/N)\n\n>>> ')
    elif op1 in ['register','2','Register']:
        print ('--------------------------------------------------------')
        op = 1
        ops = 'Y'
        while ops == 'Y':
            inputid = input("Insert ID : \n\n>>> ")
            id.append(inputid)
            inputpw = input("Insert Password : \n\n>>> ")
            pw.append(inputpw)
            print ('\nInput Successfull !')
            print ('--------------------------------------------------------')
            ops = input("Want to insert again ? (Y/N)\n\n>>> ")
            op = 'Y'
    elif op1 in ['3','q','Quit','quit']:
        print ('--------------------------------------------------------')
        exit()
    else :
        print ('--------------------------------------------------------')
        print ('\n! Input Error !')
        print ('Wanna try again ? (Y/N) \n')
        op = input('>>> ')
        print ('--------------------------------------------------------')
