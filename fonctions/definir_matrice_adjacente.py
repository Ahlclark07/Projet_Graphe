# Parcourir les sommets afin de remplir la matrice adjacente.
# Pour chaque sommet, on parcours l'ensemble des sommets (donc 2 boucles)
# Et on vérifie si le sommet actuel (1ere boucle) apparait en tant que contraintes pour les autres
# Si oui on affecte la longueur de la tâche si non on affecte *
def definir_matrice_adjacente(sommets): 
    matrice = []
    for i in range(0, len(sommets)):
        ligne = []
        for sommet in sommets:
            if sommets[i][0] in sommet[2:]:
                ligne.append(sommets[i][1])
            else:
                ligne.append("*")
        matrice.append(ligne)
    return matrice
