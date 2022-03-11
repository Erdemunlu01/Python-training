#def karsilama(adsoyad = "anonim"): print("merhaba", adsoyad) default değer atama

#def karsilama(adsoyad , yas , sehir): print("merhaba hoşgeldiniz", adsoyad , yas , sehir)
#default değeri sona al fonk yazarken

def karsilama(yas , sehir, adsoyad="anonim"):
    print("merhaba", adsoyad, yas, sehir)

karsilama( "14", "istanbul")

def topla():
    a = int(input("sayı giriniz : "))
    b = int(input("sayı giriniz : "))
    return a + b
sonuc = topla()

print("sonuç", sonuc)

if topla() > 7:
    print("koşul sağlandı")
else:
    print("olmadı aga")


