def afficher_arcs(sommets):
    nbr_arcs = 0
    donnee_graphe = []
    for sommet_a in sommets:
        for sommet_b in sommets:
            if(sommet_a[0] in sommet_b[2:]):
                print(str(sommet_a[0]) + " -> " + str(sommet_b[0]) + " = " + str(sommet_a[1]))
                donnee_graphe.append([sommet_a[0], sommet_b[0], sommet_a[1]])
                nbr_arcs += 1
    print(str(nbr_arcs) + " arcs")