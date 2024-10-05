sommets = []
fichier = open("tableau.txt", "r")

tab = fichier.readlines()
for line in tab :
    line = line.replace("\n", "").split(" ")
    sommets.append(line.replace("\n", "").split(" "))
    
print(sommets)