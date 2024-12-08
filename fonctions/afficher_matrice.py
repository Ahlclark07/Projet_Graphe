
# Ici pour afficher la matrice, (on revient dessus car ce n'est actuellement pas optimale)
from fonctions.affichage_valeurs import afficher_valeur_matrice


def afficher_matrice(sommets, matrice):
    print("------------------------------------------------Matrice des valeurs------------------------------------------------")
    for i in range(-1, len(sommets)):
        for j in range (-1, len(sommets)):
            if (i == - 1) :
                if(j == - 1):
                    afficher_valeur_matrice(" ")
                else :
                 afficher_valeur_matrice(sommets[j][0])
            elif (i > -1 and j == -1) :
                afficher_valeur_matrice(sommets[i][0])
            else :
             afficher_valeur_matrice(matrice[i][j])
        print("\n", end="")

