class orang():
    def __init__ (self, nama, alamat, telp):
        self.nama = nama
        self.alamat = alamat
        self.telp = telp

    def __str__ (self):
        s = ''
        for telepon in sorted(self.telp):
            s = s + self.nama + "\t Alamat: "+ self.alamat +"\t Telp: " + telepon + '\n'
        return s

class buku():
    def __init__(self):
        self.kontak = {}

    def tambah (self, nama, alamat, telp):
        p = orang(nama, alamat, telp)
        self.kontak[nama] = p

    def hapus (self,nama):
        del self.kontak[nama]

    def __str__ (self):
        s = ''
        for a in self.kontak:
            s = s + str(self.kontak[a]) + '\n'
        return s
    
    def __call__(self, nama):
        return self.kontak[nama]
        
