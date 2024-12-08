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

