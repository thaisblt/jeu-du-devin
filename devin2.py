def devin2() :
    """ 
            Jouer au jeu du devin : L'utilisateur choisit un nombre entre 1 et 999 et la machine le trouve en un minimum d'essais
    """

    # Attendre que l'utilisateur ai choisi un nombre entre 1 et 999
    a_choisi = input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ? ")
    while a_choisi != "o" :
        print("J'attends ...")
        a_choisi = input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ? ")

    # Trouver le nombre en un minimum d'essais avec la méthode de la dichotomie
    nb_essais = 0
    a = 1 
    b = 999
    saisie = "x"  #pour rentrer dans la boucle
    while saisie != "t" : 
        nb_essais += 1

        # Proposer le nombre médian des nombres restants
        nb_propose = (a + b) // 2
        print(f"Proposition {nb_essais} : {nb_propose}")

        # Enregistrer la saisie correcte de l’utilisateur
        saisie = input("Trop (g)rand, trop (p)etit ou (t)rouvé ? ")
        while saisie != "g" and saisie != "p" and saisie != "t" :
            print("Je n'ai pas compris la réponse. Merci de répondre :")
            print("    g si ma proposition est trop grande")
            print("    p si ma proposition est trop petite")
            print("    t si j'ai trouvé le nombre")
            saisie = input("Trop (g)rand, trop (p)etit ou (t)rouvé ? ")

        # Modifier l'encadrement a et b en fonction de la saisie utilisateur
        if saisie == 'g' :
            b = nb_propose - 1 
        elif saisie == 'p' :
            a = nb_propose + 1


    # Afficher le nombre d'essais pour trouver le bon nombre
    print(f"J'ai trouvé en {nb_essais} essais")
    print()

if __name__ == "__main__" :
    devin2()