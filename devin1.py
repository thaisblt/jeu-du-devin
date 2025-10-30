from random import randint

def devin1() :
    """     La machine fait deviner un nombre entre 1 et 999        """

    # Choisir un nombre entre 1 et 999
    nb_a_trouver = randint(1, 999)
    print("J'ai choisi un nombre compris entre 1 et 999. ")

    # Analyser le nombre proposé par l'utilisateur
    nb_essais = 0 
    nb_propose = 0 
    while nb_propose != nb_a_trouver :
        nb_essais += 1
        nb_propose = int(input(f"Proposition {nb_essais} : "))
        
        # Situer le nombre proposé par rapport au nombre choisi
        if nb_propose < nb_a_trouver :
            print("Trop petit ! ")
        else :
            print("Trop grand !")

    # Afficher quand le nombre est correcte et le nombre d'essais
    print(f"Bravo ! Vous avez trouvé en {nb_essais} essais. ")
    print()

if __name__ == "__main__" :
    devin1()