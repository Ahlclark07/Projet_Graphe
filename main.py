sommets = []
fichier = open("tableau.txt", "r")

tab = fichier.readlines()
for line in tab :
    sommets.append(line.replace("\n", "").split(" "))
    
print(sommets)