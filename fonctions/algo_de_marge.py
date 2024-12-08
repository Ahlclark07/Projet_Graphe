
from fonctions.affichage_valeurs import afficher_valeur

def algo_de_marge(dapt, dapd):
    dapd_reversed = list(reversed(dapd))
    marges = [0]
    print()
    afficher_valeur("Marge")
    afficher_valeur("0")
    for i in range(1, len(dapd_reversed)):
        marge = dapd_reversed[i] - dapt[i]
        afficher_valeur(marge)
        marges.append(marge)
    return marges

