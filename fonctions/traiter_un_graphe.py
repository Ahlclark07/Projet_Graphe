from fonctions.afficher_chemins_critiques import afficher_chemins_critiques
from fonctions.afficher_matrice import afficher_matrice
from fonctions.algo_calendrier_tard import algo_calendrier_tard
from fonctions.algo_calendrier_tot import algo_calendrier_tot
from fonctions.algo_de_marge import algo_de_marge
from fonctions.algo_de_rang import algo_de_rang
from fonctions.definir_matrice_adjacente import definir_matrice_adjacente
from fonctions.lire_fichier import lire_fichier

from fonctions.affichage_valeurs import afficher_erreur, afficher_vert


def traiterUnGraphe(fichier):
    sommets = []
    matrice = []
    sommets_classe = []
    nbr_arcs = 0
        # ajout de alpha de cout 0 et sans contraintes
    sommets.append([0, 0]) 
    cout_negatif = lire_fichier("./tableaux/" + fichier, sommets)
    print(f"\n--------------------------------------Création du graphe d’ordonnancement de {fichier} :----------------------------------------------")
    print(str(len(sommets)) + " sommets")
    donnee_graphe = []
    for sommet_a in sommets:
        for sommet_b in sommets:
            if(sommet_a[0] in sommet_b[2:]):
                print(str(sommet_a[0]) + " -> " + str(sommet_b[0]) + " = " + str(sommet_a[1]))
                donnee_graphe.append([sommet_a[0], sommet_b[0], sommet_a[1]])
                nbr_arcs += 1
    print(str(nbr_arcs) + " arcs")
    if(cout_negatif):
        afficher_erreur("Cout négatif retrouvé dans le programme")
    else:
        matrice = definir_matrice_adjacente(sommets)
        afficher_matrice(sommets, matrice)
        print("\n--------------------------------------Détection de circuit et détermination des rangs :----------------------------------------------")
        circuit = algo_de_rang(sommets, matrice, sommets_classe)
        if(circuit):
            afficher_erreur("Circuit détecté le programme s'arrête \n")
        else:
            afficher_vert("-> Il n’y a pas de circuit \n Il n’y a pas d’arcs négatifs \n-> C’est un graphe d’ordonnancement")
            print("\n------------------------------------------------------------------------Calendrier des dates :----------------------------------------------")
            dapt = algo_calendrier_tot(sommets_classe, sommets)
            successeurs, dapd = algo_calendrier_tard(sommets_classe, sommets, dapt)
            marges = algo_de_marge(dapt, dapd)
            print()
            afficher_chemins_critiques(sommets_classe, list(reversed(successeurs)), marges)
           
            # afficher_chemins_critiques(marges, list(reversed(successeurs)), sommets_classe)


       
    
