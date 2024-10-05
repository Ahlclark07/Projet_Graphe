sommets = []
fichier = open("tableau.txt", "r")

tab = fichier.readlines()
for line in tab :
    line_intermidiaire = line.replace("\n", "").split(" ")
    for i in range(0, len(line_intermidiaire)):
        try:
            line_intermidiaire[i] = int(line_intermidiaire[i])
        except:
            line_intermidiaire.pop(i)

    sommets.append(line_intermidiaire)


# print(sommets)
