"""
shivank patel
407
tp3:combat monstre
"""

import random

choix = 0
force_monstr = 0
nbr_victoire = 0
nbr_defaite = 0
niveau_adv = 0
niveau_vie = 20
nbr_combat = 0
nbr_victoir_consecutive = 0
play_game = True
combat_boss = False
showed_rules = False


while play_game:

    if nbr_victoir_consecutive % 3 != 0 or nbr_victoir_consecutive == 0:
        if showed_rules is False:

            force_monstr = random.randint(1, 7)
            niveau_adv += 1
            nbr_combat += 1
        print(f"combat", nbr_combat, ": vous avez", nbr_victoire, "victoire et", nbr_defaite, "defaite\n")
        print(f"vous rencontrer le monstre", niveau_adv, "de force", force_monstr, "\n")
        print(f"vous avez", niveau_vie, "vie \n")

        choix = int(input("Que voulez vous faire?\n 1:comabtre\n 2:contourner et aller a une autre porte\n 3:afficher regle\n 4:quitter\n \nentrez votre choix: "))

    elif nbr_victoir_consecutive % 3 == 0:
        if showed_rules is False:

            combat_boss = True
            force_monstr = random.randint(7, 12)
            niveau_adv += 1
            nbr_combat += 1
        print(f"combat", nbr_combat, ": vous avez", nbr_victoire, "victoire et", nbr_defaite, "defaite\n")
        print(f"VOUS RENCONTREZ LE BOSS DE FORCE ", force_monstr, "\n")
        print(f"vous avez", niveau_vie, "vie \n")

        choix = int(input("Que voulez vous faire?\n 1:comabtre\n 2:contourner et aller a une autre porte\n 3:afficher regle\n "
                          "4:quitter \nentrez votre choix: "))
    showed_rules = False

    if choix == 1:
        dee_six_face1 = random.randint(1, 6)
        dee_six_face2 = random.randint(1, 6)
        score_total = dee_six_face1 + dee_six_face2
        print("\nvous avez choisit de combatre le monstre\n")
        print(f"\nvous avez rouler un", score_total, "\n ")

        if force_monstr >= score_total:
            print("vous avez perdu!")
            nbr_victoir_consecutive = 0
            niveau_vie -= force_monstr
            nbr_defaite += 1
            print(f"vous perdez", force_monstr, "vie")
            print(f"il vous rest", niveau_vie, "vie\n\n")
            print("vous avez", nbr_victoir_consecutive, "victoire consecutive")

        elif force_monstr < score_total:
            print("gangnant!\n")
            niveau_vie += force_monstr
            nbr_victoir_consecutive += 1
            nbr_victoire += 1
            print(f"vous gagner", force_monstr, "vie\n")
            print(f"il vous rest", niveau_vie, "vie\n\n")
            print("vous avez", nbr_victoir_consecutive, "victoire consecutive")

    elif choix == 2:
        niveau_vie -= 1
        nbr_victoir_consecutive = 0
        print("\nvous contournez le mostre,mais vous perdez une vie\n")
        print(f"vous avez", niveau_vie, "vie\n")

    elif choix == 3:
        showed_rules = True
        print("\n                      REGLE               \n ")
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n"
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire.\n "
              "Dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n"
              "\n")

    elif choix == 4:
        print("merci et au revoir")
        play_game = False
