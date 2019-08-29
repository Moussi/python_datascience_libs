from datascience_monty_hall import play
from datascience_monty_hall import Strategie

import matplotlib.pyplot as plt


'''
scatter is like plot but don't link the points to each other
'''
def main():

    gains_changer = []
    gains_garder = []

    samples = [1000, 10000, 20000, 50000, 80000, 100000]

    for tours in samples:
        print("En changeant de porte, le joueur a gagné {} sur 10000 parties."
              .format(sum(play(Strategie.CHANGER, tours))))
        print("En gardant son choix initial, le joueur a gagné {} sur 10000 parties."
              .format(sum(play(Strategie.GARDER, tours))))
        gains_garder.append(sum(play(Strategie.GARDER, tours)))
        gains_changer.append(sum(play(Strategie.CHANGER, tours)))

    plt.scatter(samples, gains_changer)
    plt.scatter(samples, gains_garder)
    plt.show()


if __name__ == "__main__":
    main()