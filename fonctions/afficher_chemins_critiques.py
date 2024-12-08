from fonctions.affichage_valeurs import afficher_valeur, afficher_vert


def recupIndexClasse(sommets_classe, nom_sommet):
    for i, sommet in enumerate(sommets_classe):
        if(sommet[0] == nom_sommet):
            return i
    return 0
def afficher_chemins_critiques(sommets_classe, successeurs, marges):
    n = len(sommets_classe)  
    chemins_critiques = [[0]]
    doit_continuer = True
    while (doit_continuer == True):
        for chemin_critique in chemins_critiques:
            changement = False
            sommet_final = chemin_critique[-1]
            nbr_branche = 0
            for successeur in successeurs[recupIndexClasse(sommets_classe, sommet_final)]:
                if marges[recupIndexClasse(sommets_classe, successeur)] == 0 and sommet_final != n - 1:
                    if nbr_branche == 0:
                        chemin_critique.append(successeur)
                    else:
                        nouveau_chemin = chemin_critique[:]
                        nouveau_chemin[-1] = successeur
                        chemins_critiques.append(nouveau_chemin)
                    nbr_branche +=1
                    changement = True
            if(changement == False) : doit_continuer = False
    maximum = len(chemins_critiques[0])
    for chemin in chemins_critiques:
        if len(chemin) > maximum : maximum = len(chemin) 
    print("Chemins critiques :")
    meilleur_chemin_attribuer = False
    for chemin in chemins_critiques:
        texte = " -> ".join(map(str, chemin))
        if(len(chemin) == maximum and meilleur_chemin_attribuer == False):
            afficher_vert(texte +" (meilleur chemin)")
            meilleur_chemin_attribuer = True
        else:
            afficher_valeur(texte)
            print()
        
        
    return chemins_critiques
