file = open("erdem.txt", "r")
file.seek(8) #ilk 8 karakteri atla
data = file.read(6) #içine girilen sayı kadar karakteri alır(seek komutu kullanılınca atlanan üzerinden sayar)
print(data)

file.close()