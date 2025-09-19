import random


niveau_vie = 20

fantome = random.randint(1,5)

dee_six_face = random.randint(1,6)



print("vous rencontrez un fantome de niveau", (fantome))

choix = int(input("voulez vous le combatre?\n 1:comabtre\n 2:contourner et aller a une autre porte\n 3:afficher regle\n 4:quitter\n entrez votre choix:\n "))

while True:
        if choix == "1":
            print("vous avez choisit de combatre le fantome avc", (fantome), "vie")
            print("vous avez rouler un", (dee_six_face), "\n " )

            if fantome > dee_six_face:
                print("vous avez perdu")
                niveau_vie -= fantome
                print("il vous rest", (niveau_vie), "vie")

            elif fantome == dee_six_face:
                print("gangnat")
                niveau_vie += fantome
                print("il vous rest", (niveau_vie), "vie")

            else:
                print("gagnant")
                niveau_vie += fantome
                print("il vous rest", (niveau_vie), "vie")


        elif choix == "2":
