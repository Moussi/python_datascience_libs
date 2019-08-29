from typing import Any, Callable

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, exp


def main():
    domaine = range(-100, 100)
    mu = 50
    sigma = 5
    ''' Gaussienne '''
    f = lambda x : 1/(sqrt(2*pi*pow(sigma,2))) * exp(-pow((x-mu),2)/(2*pow(sigma,2)))
    y = [f(x) for x in domaine]
    print(y)
    plt.plot(domaine, y)
    plt.show()


if __name__ == "__main__":
    main()
