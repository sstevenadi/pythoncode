from mylib import *

def main():
    b = buku()
    b.tambah('Nia','Batang1',['081900909123','08119009010'])
    b.tambah('Nia2','Batang2',['08112300123'])
    b.tambah('Nia3','Batang3',['08342526789'])
    print ('Data Awal')
    print (b)
    print ('Data Nia')
    print (b('Nia'))
    b.hapus ("Nia")
    print ("Nia Ilang")
    print (b)

if __name__ == "__main__":
    main ()
