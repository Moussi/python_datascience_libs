from datascience_monty_hall import play
from datascience_monty_hall import Strategie

import matplotlib.pyplot as plt

'''
display points and link them to each other
'''
def main():
    print("En changeant de porte, le joueur a gagné {} sur 10000 parties."
          .format(sum(play(Strategie.CHANGER, 10000))))
    print("En gardant son choix initial, le joueur a gagné {} sur 10000 parties."
          .format(sum(play(Strategie.GARDER, 10000))))
    plt.plot(play(Strategie.GARDER, 10))
    plt.show()


if __name__ == "__main__":
    main()