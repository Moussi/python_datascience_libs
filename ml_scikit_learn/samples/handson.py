import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def readDatatSetAndDraw():
    house_data = pd.read_csv('../house.csv')
    print(house_data.head(5))
    plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize=4)
    plt.show()


def readDatatSetPart():
    house_data = pd.read_csv('../house.csv')
    house_data = house_data[house_data['loyer'] < 1000]
    print(house_data.head(5))
    plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize=4)
    plt.show()


if __name__ == '__main__':
    readDatatSetAndDraw()
