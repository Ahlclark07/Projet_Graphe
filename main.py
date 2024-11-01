import numpy as np
import sys
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
        if i > 0 and line_intermidiaire[i] < 0 :
            print("Un arc de coût négatif a été trouvé.. Le programme s'arrête")
            raise SystemExit
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

# Ici pour afficher la matrice, (on revient dessus car ce n'est actuellement pas optimale)
def afficher_matrice():
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



def algo_de_rang() :
    # On récupère les noms des sommets encore une fois pour garder le compte.
    sommets_pour_rang = []
    for ligne in sommets :
        sommets_pour_rang.append(ligne[0])
    # on initialise le rang à 0
    rang = 0
    # on se sert de numpy car c'est beaucoup plus facile pour parcourir les colonnes
    matrice_rang = np.array(matrice)

    # Une boucle pour chaque ligne du tableau même si c'est inutile d'en faire autant dans certains cas
    for i in range(0, len(matrice)):
        # On utilise une fonction utile de numpy qui permet de récupérer les colonnes qui ne contiennent que des
        # des * puis de récupérer leur index
        cols = np.all(matrice_rang == "*", axis=0)
        cols_indices = np.where(cols)[0]

        # Ne vous inquiétez pas pour la variable saut_de_pas. Elle est là au cas où on doit retirer plus d'un sommet. Il 
        # faut qu'on garde le bon index car quand on en retire 1 il faut faire -1 sur le reste
        saut_de_pas = 0
        # Ensuite c'est simple, vu qu'on a l'index des colonnes qui n'ont que des * on les retire dans notre matrice 
        # ainsi que leur ligne et on cherche les sommets qui correspondent à ces index dans notre tableau sommets_pour_rang pour les retirer
        # On les rajoute ensuite dans notre tableau de sommets de base qui aura maintenant la forme suivant pour chaque sommets :
        # [nom_du_sommet, cout, liste_des_contraintes, rang]

        for col in cols_indices:
            index_reel = col - saut_de_pas
            print("Le sommet " + str(sommets_pour_rang[index_reel]) + " a pour rang : " + str(rang)) 
            for sommet in sommets:
                if sommet[0] == sommets_pour_rang[index_reel] :
                    sommet.append(rang)   
            matrice_rang = np.delete(matrice_rang, index_reel, axis=0)
            matrice_rang = np.delete(matrice_rang, index_reel, axis=1)
            del sommets_pour_rang[index_reel]
            saut_de_pas += 1
        rang +=1
        

afficher_matrice()
algo_de_rang()
print(sommets)