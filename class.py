class Derslik:
    #__init__(self) ön tanımlı metod. Constracter, bir sınıfta obje oluşturulduğunda ilk çalışan yer inittir
    #self derslik isimli class ın kendisi obje, çağrırken self kullanılmıyor
    def __init__(self, derslikadi):
        self.ogrenciler = []
        self.derslikadi = derslikadi

    def ogrenciekle(self, ogrenci):
        self.ogrenciler.append(ogrenci) #yukarıda açılan ogrenciler listesine değer ekler

    def ogrencicikar(self, ogrencindex):
        self.ogrenciler.pop(ogrencindex) #yukarıda açılan ogrenciler listesinden değer çıkartır

    def ogrenciliste(self):
        return self.ogrenciler

derslik = Derslik("1A")
print( derslik.derslikadi)

derslik.ogrenciekle("erdem ünlü")
derslik.ogrenciekle("serap büber")
derslik.ogrenciekle("refiye büber")

print(derslik.ogrenciliste())

derslik.ogrencicikar(1) #liste 0 dan başladığından 2. elemanı almak için 1
print(derslik.ogrenciliste())

