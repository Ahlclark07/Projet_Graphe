# Création de la table qui garde les sommets 
sommets = []
# ouverture du fichier (on modifiera plus tard pour le choix des fichiers)
fichier = open("tableau.txt", "r")
# Lecture des lignes des fichiers : chaque ligne représente une case du tableau
tab = fichier.readlines()
# ajout de alpha de cout 0 et sans contraintes
sommets.append([0, 0])
liste_tous_les_sommets = []
liste_sommets_sans_contraintes = []
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
            if(i == 0):
                liste_tous_les_sommets.append(line_intermidiaire[i])
        except:
            line_intermidiaire.pop(i)
    # Si la longueur du tableau est 2, il n'y pas de contraintes. On rajoute alpha comme contrainte
        if(len(line_intermidiaire) == 2):
            line_intermidiaire.append(0)
    # Ajouter la ligne à notre tableau de sommets 
    sommets.append(line_intermidiaire)

# On parcours la liste des sommets, pour chaque sommet de cette liste, on parcourt le tableau récupéré du fichier
# pour vérifier s'ils ont des successeurs. Le but est d'établir une liste pour leur affecter oméga si jamais
for nom_sommet in liste_tous_les_sommets:
    a_un_successeur = False
    for sommet in sommets:
        if(nom_sommet in sommet[2:]):
            a_un_successeur = True
            break
    if(a_un_successeur == False):
        liste_sommets_sans_contraintes.append(nom_sommet)
   

# Ajouter oméga au tableau des sommets avec ses contraintes
sommets.append([len(sommets), 0] + liste_sommets_sans_contraintes)

matrice = []

# Parcourir les sommets afin de remplir la matrice adjacente.
# Pour chaque sommet, on parcours l'ensemble des sommets (donc 2 boucles)
# Et on vérifie si le sommet actuel (1ere boucle) apparait en tant que contraintes pour les autres
# Si oui on affecte la longueur de la tâche si non on affecte *

for i in range(0, len(sommets)):
    ligne = []
    for sommet in sommets:
        if sommets[i][0] in sommet[2:]:
            ligne.append(sommets[i][1])
        else:
            ligne.append("*")
    matrice.append(ligne)

# Une fonction rapide pour afficher les valeurs sur 3 cases (à voir si il y a pas mieux à faire)
def afficher_valeur(val):
     print("{:>3}".format(val), end=" ")

# Ici pour afficher la matrice, (on revient dessus)
for i in range(-1, len(sommets)):
    for j in range (-1, len(sommets)):
        if (i == - 1) :
            if(j == - 1):
             afficher_valeur(" ")
            else :
             afficher_valeur(sommets[j][0])
        elif (i > -1 and j == -1) :
            afficher_valeur(sommets[i][0])
        else :
           afficher_valeur(matrice[i][j])
    print("\n", end="")

