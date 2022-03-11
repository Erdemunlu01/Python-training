a = 10
b = 4
c = "volkan"


if 1 == 1 :
    print("bu gerçekten 1")
    print("buradayım")
    if 1 > 0 :
        print("evet büyük")

# == != < > <= >=

if a != b:
    print("a b den farklı")
    if b > a:
        print("evet b büyüktür")


if (a != b and b > a):
    print("a b den farklıdır ")
    print("b a dan büyüktür")

if a != b or b > a:
    print("a b den farklıdır ")
    print("b a dan büyüktür")


if (a != b and b > a) or c=="volkan":
    print("koşul sağlandı")

if not(b>a):
    print("koşul sağlandı")
elif b==4:
    print("2.koşul sağlandı")

else:
    print("hiç bir koşul sağlanmadı")


if a==5:
    print("koşul sağlandı")
elif b==4:
    print("2.koşul sağlandı")

else:
    print("hiç bir koşul sağlanmadı")


