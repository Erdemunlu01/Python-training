#a koyunca yanına ekler var olan dosyanın
file = open("erdem.txt", "a")

file.write("\n") #\n alt satıra geçirir
file.write("erdem\n")
file.write("unlu\n")
file.write("python\n")

file.close()