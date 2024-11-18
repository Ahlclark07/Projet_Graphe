import numpy as np
# Création de la table qui contient les sommets et leurs données et de la table qui contient la matrice adjacente 
sommets = []
matrice = []
sommets_classe = []
# ajout de alpha de cout 0 et sans contraintes
sommets.append([0, 0])
liste_tous_les_sommets = []
liste_sommets_sans_successeurs = []

# Fonction qui permet de lire le fichier et d'en ressortir le tableau de données sous le format
# [ [sommet_0, cout, contraines_1, ..., contraintes_n ], ..., [sommet_n, cout, contraines_1, ..., contraintes_n ] ]
def lire_fichier(nom_fichier):
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
            liste_sommets_sans_successeurs.append(nom_sommet)
    # Ajouter oméga au tableau des sommets avec ses contraintes oméga fera le nombre de sommets + 1 du coup len(sommets) ici
    sommets.append([len(sommets), 0] + liste_sommets_sans_successeurs)

# Parcourir les sommets afin de remplir la matrice adjacente.
# Pour chaque sommet, on parcours l'ensemble des sommets (donc 2 boucles)
# Et on vérifie si le sommet actuel (1ere boucle) apparait en tant que contraintes pour les autres
# Si oui on affecte la longueur de la tâche si non on affecte *
def definir_matrice_adjacente(): 
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
     print("{:>11}".format(val), end=" ")
    # print(val, end=" ")

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
                    sommets_classe.append(sommet)
            matrice_rang = np.delete(matrice_rang, index_reel, axis=0)
            matrice_rang = np.delete(matrice_rang, index_reel, axis=1)
            del sommets_pour_rang[index_reel]
            # Encore une fois, ne vous inquiétez pour le saut de pas.
            saut_de_pas += 1
        # On incrémente le rang à chaque itération de l'algo
        rang +=1
    if (len(matrice_rang) != 0):
        print(matrice_rang)
        print("Circuit détecté. Le programme s'arrête.")
        raise SystemExit



# J'affiche juste notre jeu de données

# Déjà fait :
# Lire le fichier
# Détecter les coûts négatifs et arrêter le programme
# Rajouter alpha (0) et oméga (nombre de sommets + 1)
# Construit la matrice d'adjacence et l'afficher
# Fait l'algo de rang
# Modifier l'algo de rang pour gérer la détection de circuit et arrêter le programme 
# Rajouter l'algo pour calculer les dates au plus tot et au plus tard 😬
# Todo :
# Utiliser le résultat précédent pour le chemin critique
# Optimiser le code pour rendre plus facile le déroulement de l'algo sur plusieurs fichiers à la suite

# algo du calendrier au plus tôt
dapt = [] 

def algo_calendrier_tot():
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

dapd = []     
def algo_calendrier_tard():
    successeurs = []
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
    
def algo_de_marge():
    dapd_reversed = list(reversed(dapd))
    print()
    afficher_valeur("Marge")
    chemin_critique = ""
    for i in range(0, len(dapd_reversed)):
        marge = dapd_reversed[i] - dapt[i]
        afficher_valeur(marge)
        if (marge == 0):
            chemin_critique += str(sommets_classe[i][0])
            if(i < len(sommets_classe) - 1):
                chemin_critique += "->"
    print()
    afficher_valeur("Chemin critique : " +chemin_critique)
    



# Déroulement du programme
lire_fichier("tableau.txt")
definir_matrice_adjacente()
afficher_matrice()
algo_de_rang()
algo_calendrier_tot()
algo_calendrier_tard()
algo_de_marge()

