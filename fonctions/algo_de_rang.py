import numpy as np

def algo_de_rang(sommets, matrice, sommets_classe) :
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
        changements = []
        for col in cols_indices:
            index_reel = col - saut_de_pas
            for sommet in sommets:
                if sommet[0] == sommets_pour_rang[index_reel] :
                    sommet.append(rang)   
                    sommets_classe.append(sommet)
            matrice_rang = np.delete(matrice_rang, index_reel, axis=0)
            matrice_rang = np.delete(matrice_rang, index_reel, axis=1)
            changements.append(sommets_pour_rang[index_reel])
            del sommets_pour_rang[index_reel]
            # Encore une fois, ne vous inquiétez pour le saut de pas.
            saut_de_pas += 1
        # On incrémente le rang à chaque itération de l'algo
        if(len(changements) > 0):
            print("Points d'entrée : " + " ".join(map(str, changements)))
            print("Suspression des points d'entrés")
            print("Le rang attribué est : " + str((rang)))
            print("Points restants : " + " - ".join(map(str, sommets_pour_rang)))
        rang +=1
    return len(matrice_rang) != 0
