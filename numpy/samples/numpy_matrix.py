from typing import Any, Callable

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, exp

from numpy.core._multiarray_umath import ndarray

'''
    Réalisation d'une variable aléatoire uniformément distribuée
    '''


def main():
    matrice_aleatoire = np.random.rand(2, 3)
    print(matrice_aleatoire)
    sommes = np.sum(matrice_aleatoire, 0)
    print(sommes)
    # la taille de somme
    print(sommes.shape)
    # plt.figure()
    # plt.scatter(range(30), matrice_aleatoire[0, :])
    # plt.scatter(range(30), matrice_aleatoire[1, :])
    # plt.show()


if __name__ == "__main__":
    main()
