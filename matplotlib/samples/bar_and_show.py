from datascience_monty_hall import play
from datascience_monty_hall import Strategie

import matplotlib.pyplot as plt


'''
scatter is like plot but don't link the points to each other
'''
def main():
    parties = 10000
    changeResult = sum(play(Strategie.CHANGER, parties))
    print("En changeant de porte, le joueur a gagné {} sur {} parties."
          .format(changeResult, parties))
    garderResult = sum(play(Strategie.GARDER, parties))
    print("En gardant son choix initial, le joueur a gagné {} sur 10000 parties."
          .format(garderResult, parties))
    plt.bar(["Garder", "Changer"], [garderResult, changeResult])
    plt.show()


if __name__ == "__main__":
    main()