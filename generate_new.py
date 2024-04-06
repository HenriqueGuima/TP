#generate new dataset

import numpy as np
import pandas as pd
import random
import string

def generate_new_dataset(df_copy):
    filePath='C:\\Users\\Guima\\Desktop\\MIAA\\MLA\\TP\\'
    f=df_copy.to_csv(filePath+'complete_domestic_consume.csv', sep=';', index=False)
    print('New dataset generated')
    print('File path: '+filePath+'complete_domestic_consume.csv')
