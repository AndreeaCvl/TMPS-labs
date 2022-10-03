from Df import Df
import pandas as pd
import numpy as np


if __name__ == '__main__':
    # initializing a random dataframe with column names A, B, C and D
    df = pd.DataFrame(np.random.randint(0, 100, size=(15, 4)), columns=list('ABCD'))

    # initializing the class and calling the method
    p = Df(df)
    p.scatter('A', 'B')

