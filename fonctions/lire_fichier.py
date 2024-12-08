import os
# Fonction qui permet de lire le fichier et d'en ressortir le tableau de données sous le format
# [ [sommet_0, cout, contraines_1, ..., contraintes_n ], ..., [sommet_n, cout, contraines_1, ..., contraintes_n ] ]
def lire_fichier(nom_fichier, sommets):
    liste_tous_les_sommets = []
    liste_sommets_sans_successeurs = []
    arreteProgramme = False
    # ouverture du fichier (on modifiera plus tard pour le choix des fichiers)
    fichier = open(nom_fichier, "r")
    # Lecture des lignes des fichiers : chaque ligne représente une case du tableau
    tab = fichier.readlines()
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
                if i > 0 and line_intermidiaire[i] < 0 :
                    arreteProgramme = True
            except:
                line_intermidiaire.pop(i)
            if arreteProgramme == True:
                return arreteProgramme
    
            
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
            liste_sommets_sans_successeurs.append(nom_sommet)
    # Ajouter oméga au tableau des sommets avec ses contraintes oméga fera le nombre de sommets + 1 du coup len(sommets) ici
    sommets.append([len(sommets), 0] + liste_sommets_sans_successeurs)
    return arreteProgramme

