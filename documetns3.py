file = open("erdem.txt", "r") #read r okuma olarak dosyayı açar

#her satırda işlem yapacaksak for kullanılır
for satir in file:
    print(satir)

file.close()