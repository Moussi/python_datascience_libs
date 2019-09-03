from datascience_monty_hall import Strategie

import numpy as np
import matplotlib.pyplot as plt


def monty_hall(strategie, nb_tour):
    '''Simule une partie du jeu Monty Hall.

    Cette fonction simule le choix de la porte par le participant,
    l'élimination d'une mauvaise porte par le présentateur, et le
    choix final.

    Args:
        strategie (Strategie): La stratégie du joueur, 0 pour GARDER et 1 pour CHANGER
        nb_tours (int): Nombre de tours

    Returns:
        gain (tableau numpy): tableau Numpy des gains du joueur
    '''

    # nombre de porte dans le jeu
    nb_porte = 3

    # Construction de la matrice aléatoire des choix par tour.
    # 1 ligne = 1 tour
    premier_choix = np.random.randint(0, nb_porte, nb_tour)
    print(premier_choix)

    # tableau des bonnes portes
    bonnes_portes = np.random.randint(0, nb_porte, nb_tour)
    print(bonnes_portes)

    # On compare le premier_choix du joueur et le tableau des bonnes portes et selon la stratégie :
    # 0-GARDER =  si la porte choisie est égale à la bonne porte, le joueur a gagné
    # 1-CHANGER = si la porte choisie est égale à la bonne porte, le joueur a perdu puisqu'il a décidé de
    #             changer son choix. En revanche, si la porte choisie n'était pas la bonne porte, il gagne puisque
    #             en changeant il va tomber sur la bonne porte (le présentateur retirant systématiquement une
    #             mauvaise porte)

    gains = []
    if strategie == Strategie.GARDER:
        gains = premier_choix == bonnes_portes
    elif strategie == Strategie.CHANGER:
        # Quand je change je prend la bonne porte  si mon premier choix était faux
        gains = premier_choix != bonnes_portes
    else:
        raise ValueError("Stratégie non reconnue!")
    print(gains)
    total_gains = sum(gains)
    print(total_gains)
    return total_gains



if __name__ == "__main__":
    a = monty_hall(Strategie.CHANGER, 100)
    b = monty_hall(Strategie.GARDER, 100)
    print(a)
    print(b)
    plt.bar(["CHANGER", "GARDER"],[a,b])
    plt.show()