import os
from fonctions.traiter_un_graphe import traiterUnGraphe 
def afficher_menu():
    print("\n=== Menu ===")
    print("1. Lister les fichiers du dossier courant")
    print("2. Quitter")
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