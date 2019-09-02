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
    plt.figure()
    plt.hist(sommes, bins = 100)
    plt.show()

def main():
    domaine = range(-100, 100)
    mu = 50
    sigma = 5
    ''' Gaussienne '''
    f = lambda x: 1 / (sqrt(2 * pi * pow(sigma, 2))) * exp(-pow((x - mu), 2) / (2 * pow(sigma, 2)))
    y = [f(x) for x in domaine]
    print(y)
    plt.plot(domaine, y)
    plt.show()


if __name__ == "__main__":
    generate_distributed_random_variables_matrix()
