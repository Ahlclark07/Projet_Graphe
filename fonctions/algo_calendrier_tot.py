
# J'affiche juste notre jeu de données
# algo du calendrier au plus tôt

from fonctions.affichage_valeurs import afficher_valeur


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
  