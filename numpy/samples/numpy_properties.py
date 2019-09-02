from typing import Any, Callable

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, exp

from numpy.core._multiarray_umath import ndarray

'''
    Réalisation d'une variable aléatoire uniformément distribuée
    '''


def generate_distributed_random_variables():
    vecteur_aleatoire = np.random.rand(30)
    print(vecteur_aleatoire)
    plt.scatter(range(30), vecteur_aleatoire)
    plt.show()

def generate_distributed_random_variables_matrix():
    matrice_aleatoire = np.random.rand(1000, 100000)
    print(matrice_aleatoire)

    sommes = np.sum(matrice_aleatoire, 0)
    print("La moyenne empirique de notre distribution est {}."
          .format(np.mean(sommes)))
    print("La moyenne empirique de la variable généré par la fonction rand est {}."
          .format(np.mean(np.random.rand(100000))))
    print("La variance empirique de notre distribution est {}."
          .format(np.var(sommes)))
    print("La variance empirique de la variable généré par la fonction rand est {}."
          .format(np.var(np.random.rand(100000))))



if __name__ == "__main__":
    generate_distributed_random_variables_matrix()
