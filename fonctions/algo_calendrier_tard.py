
 
from fonctions.affichage_valeurs import afficher_valeur


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
