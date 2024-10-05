# Création de la table qui garde les sommets 
sommets = []
# ouverture du fichier (on modifiera plus tard pour le choix des fichiers)
fichier = open("tableau.txt", "r")
# Lecture des lignes des fichiers : chaque ligne représente une case du tableau
tab = fichier.readlines()
# ajout de alpha de cout 0 et sans contraintes
sommets.append([0, 0])
# Parcourir chaque ligne 
for line in tab :
    # Pour chaque ligne: retirer le caractère "\n" puis splitter chaque ligne en case en coupant à partir du caractère espace
    # "1 2 3 \n" devient ['1', '2', '3', ' ']
    line_intermidiaire = line.replace("\n", "").split(" ")
   # Convertir chaque case en numérique et retirer les valeurs impossible à convertir
   # ['1', '2', '3', ' '] devient [1, 2, 3]
    for i in range(0, len(line_intermidiaire)):
        try:
            line_intermidiaire[i] = int(line_intermidiaire[i])
        except:
            line_intermidiaire.pop(i)
    # Si la longueur du tableau est 2, il n'y pas de contraintes. On rajoute alpha comme contrainte
        if(len(line_intermidiaire) == 2):
            line_intermidiaire.append(0)
    # Ajouter la ligne à notre tableau de sommets 
    sommets.append(line_intermidiaire)
# Ajouter oméga au tableau des sommets 
sommets.append([len(sommets), 0])
print(sommets)
# for i in range(-1, len(sommets) + 2):
#     for j in range (-1, len(sommets) + 2):
#         if (i == - 1 and j == -1) :
#             print(" ", end="")
#         elif (i == - 1 and j != -1) :
#             print("")
#         else :
#             print("*", end="")
#     print("\n", end="")


