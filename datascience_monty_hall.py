# Pour afficher les graphiques dans la continuité du code,
# et non pas dans une fenêtre à part:
# Pour pouvoir afficher des graphiques:
import matplotlib.pyplot as plt

# Pour utiliser la fonction randint, qui génère des nombres
# entiers de façon aléatoire:
from random import randint, seed

# Un Enum est une structure de données qui consiste en un
# ensemble d'éléments nommés. Une variable de ce type peut
# avoir comme valeur un de ces éléments.
from enum import Enum

# Ici nous définissons une sous-classe de Enum, qui contiendra
# les stratégies possibles.
class Strategie(Enum):
    CHANGER = 1
    GARDER = 2


# Utilise l'horloge système pour initialiser le générateur de
# nombres pseudo-aléatoires.
seed()


def play_game(strategie):
    '''Simule une partie du jeu Monty Hall.

    Cette fonction simule le choix de la porte par le participant,
    l'élimination d'une mauvaise porte par le présentateur, et le
    choix final. Elle ne retourne que le résultat de la partie, parce
    que nous n'aurons besoin que du résultat pour effectuer nos calculs.

    Args:
        strategie (Strategie): La stratégie du joueur

    Returns:
        bool: Le joueur a-t-il gagné?
    '''

    portes = [0, 1, 2]

    bonne_porte = randint(0, 2)

    # Choix du joueur
    premier_choix = randint(0, 2)

    # Il nous reste deux portes
    portes.remove(premier_choix)

    # Le présentateur élimine une porte
    if premier_choix == bonne_porte:
        portes.remove(portes[randint(0, 1)])
    else:
        portes = [bonne_porte]

    deuxieme_choix = 0
    # Le deuxieme choix depend de la strategie
    if strategie == Strategie.CHANGER:
        deuxieme_choix = portes[0]
    elif strategie == Strategie.GARDER:
        deuxieme_choix = premier_choix
    else:
        raise ValueError("Stratégie non reconnue!")

    return deuxieme_choix == bonne_porte


def play(strategie, nb_tours):
    '''Simule une suite de tours du jeu.

    Cette fonction renvoie les résultats de plusieurs parties
    du jeu Monty Hall sous forme d'une liste de gains par le
    joueur.

    Args:
        strategie (Strategie): La strategie du joueur
        nb_tours (int): Nombre de tours

    Returns:
        list: Liste des gains du joueurs à chaque partie
    '''

    # Ceci est une liste en compréhension. Pour en savoir plus, consulter
    # le cours "Apprenez à programmer en Python" sur OpenClassrooms
    return [1 if play_game(strategie) else 0 for i in range(nb_tours)]

def main():
    print("En changeant de porte, le joueur a gagné {} sur 10000 parties."
          .format(sum(play(Strategie.CHANGER, 10000))))
    print("En gardant son choix initial, le joueur a gagné {} sur 10000 parties."
          .format(sum(play(Strategie.GARDER, 10000))))
    plt.plot(play(Strategie.GARDER, 10))
    plt.show()


if __name__ == "__main__":
    main()
