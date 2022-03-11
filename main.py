print("hello")
print(5)
print("erdem","ünlü", 1,2,3,4)
print("erdem\nünlü") #alt alta yazar
print("01", "01", "2020", sep="-") #sep araya keler
print("{} + {} = {}".format(1,2,3)) #formatlar süslü parantez içine yazar; toplama sembolü toplama yapmaz
x = 1
y = 1.5
z = "erdem"
z2 = "1" #sayı string

#list

a = [1,2,3,4,5, "erdem"]
print(a)

#tupple

b = (1,2,3,4,5,6)

#dict veri tipi (jayson veri tipi)

c = {"elma":"apple", "kitap":"book"}

print(c)
print(b)

d = False
e = True

print(d)
print(e)

print(type(x), type(z2))

print(1+x)
print("1"+z2)
print(1+ int(z2)) #int integer a çevirir

#MAT OPERATÖRLERİ

print( 4 + 2 )
print( 4 - 2 )
print(4*2)
print(4/2)
print(4//2)#// bölme işleminin sonucunu int yapar
print(4/3)
print(4//3)#en yakın sayıya yucarlar
print(10%4)#mod işlemi bir sayıya bölümünden kalan

a = 2
b = 4
c = 5
print(a-b*c) #işlem önceliğine bakar
print((a-b)*c)#parantez önceliği

print("* ")
print("** ")
print("*** ")
print("**** ")
print("***** ")

#string çarpımı
print("* "*1)
print("* "*2)
print("* "*3)
print("* "*4)
print("* "*5)

a = "erdem python dersi"
b =["erdem", "python", "ders", 1,2,3]

print(a[0])#ilk harf
print(b[0])#ilk liste değeri

print(len(a)) #harfi saydı
print(len(b)) #liste eleman sayısı

print(a[len(a) - 1])#uzun iş 0 dan başladığından bir çıkardık tercih etme
print(a[0:5]) #sıfırdan başla 5 adım ilerle
print(a[::2]) #ikişer atlayarak al
print(a[-2]) #en sondan 2. olanı al 0 dan başlamaz sondan
print(a[-18])
print(b[0:3]) #tek tek eleman alıyor
print(b[:3])

#dic ve list farklıdır. dic de karşılık verir
c = {"elma":"apple", "kitap":"book", "test":"test"}
print(c["elma"])



