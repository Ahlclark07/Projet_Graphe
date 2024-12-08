import numpy as np
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

# Une fonction rapide pour afficher les valeurs sur 3 cases (à voir si il y a pas mieux à faire)
def afficher_valeur_matrice(val):
     print("{:>3}".format(val), end=" ")
# Une fonction rapide pour afficher les valeurs sur 11 cases (à voir si il y a pas mieux à faire)
def afficher_valeur(val):
     print("{:>11}".format(val), end=" ")

# Une fonction pour afficher les valeurs en rouge
def afficher_erreur(message):
    print(f"\033[31m{message}\033[0m")

# Une fonction pour afficher les valeurs en vert
def afficher_vert(message):
    print(f"\033[32m{message}\033[0m")



# Ici pour afficher la matrice, (on revient dessus car ce n'est actuellement pas optimale)
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

# J'affiche juste notre jeu de données
# algo du calendrier au plus tôt

def algo_calendrier_tot(sommets_classe, sommets):
  dapt = []
  afficher_valeur("Rang")
  for sommet in sommets_classe:
      afficher_valeur(sommet[-1])
  print()  
  afficher_valeur("Tache")
  for sommet in sommets_classe:
      afficher_valeur(str(sommet[0]) +"("+str(sommet[1]) + ")")
  print()
  afficher_valeur("PDCS")
  dpprs = []
  indice = 0
  for sommet in sommets_classe:  
      if(sommet[0] == 0):
          afficher_valeur("-")
          dapt.append(0)
          dpprs.append([0])
      else: 
          dpprs.append([])        
          liste_predecesseurs = ""
          if(len(sommet) > 2):
            for i in range(2, len(sommet) - 1):
                valeur_date = 0
                liste_predecesseurs += str(sommet[i])
                y = 0
                for prd in sommets_classe:
                    if prd[0] == sommet[i]:
                     valeur_date += prd[1]
                    if sommets_classe[y][0] == sommet[i]:
                        valeur_date += dapt[y]                 
                    y +=1
               
                    
                dpprs[indice].append(valeur_date) 
                if i != len(sommet)-2 :
                    liste_predecesseurs += ","
            meilleur_valeur = dpprs[indice][0]
            for valeur in dpprs[indice]:
                if valeur > meilleur_valeur :
                    meilleur_valeur = valeur
            dapt.append(meilleur_valeur)          
            afficher_valeur(liste_predecesseurs)
      indice += 1
  print()
  afficher_valeur("DPPR")
  for dppr in dpprs :
      dates = ""
      for i in range(0, len(dppr)):
        dates += str(dppr[i])
        if(i < len(dppr) - 1):
            dates += ","
      afficher_valeur(dates)
  print()
  afficher_valeur("DAPT")
  for valeur in dapt :
      afficher_valeur(valeur)
  return dapt
   
def algo_calendrier_tard(sommets_classe, sommets, dapt):
    successeurs = []
    dapd = []
    for sommet in reversed(sommets_classe):
        tab = []
        for sommet_ in sommets:
            if(sommet[0] in sommet_[2:len(sommet_) -1]):    
                 tab.append(sommet_[0])
        successeurs.append(tab)
    dpsc = []
    dapt_reversed = list(reversed(dapt))
    sc_reversed = list(reversed(sommets_classe))
    indice = 0
    for element in successeurs:
        if(len(element) == 0):
            dpsc.append([dapt_reversed[0]])
            dapd.append(dapt_reversed[0])
        else :
            dpsc.append([])
            for successeur in element:
                valeur = 0
                for i in range(0, len(sommets_classe)):
                    if sc_reversed[i][0] == successeur:
                        valeur = dapd[i]
                    if i == indice:
                        valeur -= sc_reversed[i][1]
                dpsc[indice].append(valeur)
            valeur_min = dpsc[indice][0] 
            for valeur in dpsc[indice]:
                if valeur_min > valeur:
                    valeur_min = valeur
            dapd.append(valeur_min)
        indice += 1
    print()
    afficher_valeur("SCCS")
    for tab in reversed(successeurs):
        i = 0
        texte = ""
        for valeur in tab:
            texte +=str(valeur)
            if(i < len(tab) - 1):
                texte += ","
            i +=1
        if texte == "":
            afficher_valeur("-")
        else:
            afficher_valeur(texte)
    print()
    afficher_valeur("DPSC")
    for tab in reversed(dpsc):
        texte = ""
        i = 0
        for valeur in tab:
            texte += str(valeur)
            if(i != len(tab)-1):
                texte += ","
            i += 1
        afficher_valeur(texte)
    print()
    afficher_valeur("DAPD")
    for valeur in reversed(dapd):
        afficher_valeur(valeur)
    return successeurs, dapd

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
    for chemin in chemins_critiques:
        texte = " -> ".join(map(str, chemin))
        if(len(chemin) == maximum):
            afficher_vert(texte)
        else:
            afficher_valeur(texte)
            print()
        
        
    return chemins_critiques

def afficher_menu():
    print("\n=== Menu ===")
    print("1. Lister les fichiers du dossier courant")
    print("2. Quitter")

def traiterUnGraphe(fichier):
    sommets = []
    matrice = []
    sommets_classe = []
    nbr_arcs = 0
        # ajout de alpha de cout 0 et sans contraintes
    sommets.append([0, 0]) 
    cout_negatif = lire_fichier("./tableaux/" + fichier, sommets)
    print("\n--------------------------------------Création du graphe d’ordonnancement :----------------------------------------------")
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


       
    
def recupIndexClasse(sommets_classe, nom_sommet):
    for i, sommet in enumerate(sommets_classe):
        if(sommet[0] == nom_sommet):
            return i
    return 0
### Programme

def main():
    continuer = True
    print("Bienvenue dans le programme ! Faites un choix")
    fichiers = os.listdir('./tableaux')
    print( " | ".join(map(str, fichiers)))
    while(continuer):
        choix = input("Entrez le numéro du fichier que vous souhaitez traiter parmi la liste ci dessous. Si vous souhaitez arrêter le programme inscrivez un autre numéro : ")
        fichier = "table " + choix +".txt"
        if(fichier in fichiers):
            traiterUnGraphe(fichier)
        else:
            print("Arrêt du programme ! Au revoir ! :)")
            continuer = False

main()