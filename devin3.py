from devin1 import devin1
from devin2 import devin2

def devin3() : 
    """
    Jeu du devin programme complet : Permettre à l'utilisateur de choisir comment il souhaite jouer ou s'il veut quitter
    """
    choix = "" # pour rentrer dans la boucle
    while choix != "0" :

        # Afficher les différents choix 
        choix = ""  # réinitialise le choix à chaque partie
        while choix != "1" and choix != "2" and choix != "0" :
            print("1- L'ordinateur choisit un nombre et vous le devinez")
            print("2- Vous choisissez un nombre et l'ordinateur le devine")
            print("0- Quitter le programme")

            # Demander le choix de l'utilisateur
            choix = input("Votre choix : ")
            print()

        # Jouer de la façon dont le joueur souhaite jouer 
        if choix == "1" :
            devin1()
        elif choix == "2" :
            devin2()
        else :
            print("Au revoir")

if __name__ == "__main__" :
    devin3()