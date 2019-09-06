import pandas as pd
import numpy as np
import seaborn as sns

def pandas_unique():
    titanic = sns.load_dataset('titanic')
    print(titanic.age.unique())

def pandas_describe():
    titanic = sns.load_dataset('titanic')
    print(titanic.describe(include="all"))


def pandas_fill_nan_values():
    titanic = sns.load_dataset('titanic')
    print(titanic.fillna(value={"age":0}).age.head(10))

def pandas_fill_nan_values_2():
    titanic = sns.load_dataset('titanic')
    print(titanic.fillna(method="pad").age.head(10))

def pandas_drop_nan_values():
    titanic = sns.load_dataset('titanic')
    print(titanic.dropna().age.head(10))

def csv_to_pandas():
    pandas_family = [[100, 80, 60, 90],
    [50, 40, 50, 100],
    [70, 45, 30, 110]]

    pandas_family_df = pd.DataFrame(pandas_family, index = ['mother', 'bebe', 'father'],
                                    columns= ['legs','hair','queue', 'ventre'])
    return pandas_family_df


if __name__ == '__main__':
    pandas_describe()
    print("==================")
    pandas_fill_nan_values()
    print("==================")
    pandas_fill_nan_values_2()
    print("==================")
    pandas_drop_nan_values()