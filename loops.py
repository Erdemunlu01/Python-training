#bir koşul sağlanana kadar döner
i = 0
while i < 10:
    if (i==4):
        i += 1
        continue # break döngüyü kırar
    print("adım :",i)
    i += 1 # i=i+1 ile aynı işlemi yapar çarpma bölme ve çıkarma için de geçerli

print("döngü sona erdi")



