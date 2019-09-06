import pandas as pd
import numpy as np

def numpy_to_pandas():
    pandas_family = [[100, 80, 60, 90],
    [50, 40, 50, 100],
    [70, 45, 30, 110]]

    pandas_family_df = pd.DataFrame(pandas_family, index = ['mother', 'bebe', 'father'],
                                    columns= ['legs','hair','queue', 'ventre'])
    return pandas_family_df

def csv_to_pandas():
    pandas_family = [[100, 80, 60, 90],
    [50, 40, 50, 100],
    [70, 45, 30, 110]]

    pandas_family_df = pd.DataFrame(pandas_family, index = ['mother', 'bebe', 'father'],
                                    columns= ['legs','hair','queue', 'ventre'])
    return pandas_family_df


if __name__ == '__main__':
    ndf = numpy_to_pandas()
    print(ndf['ventre'].values)
