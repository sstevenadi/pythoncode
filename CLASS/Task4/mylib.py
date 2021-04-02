class segi3 (object):
    def __init__ (self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas (self):
        return self.alas*self.tinggi*0.5
    def tot (self,other):
        tot3 = self.luas() + other.luas()
        return tot3