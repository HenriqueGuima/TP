import pandas as pd
import numpy
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit

def data_split(df_copy):

    # new column with the sum of the columns
    # split the data into training and testing

    df_copy['total_consummed'] = df_copy.sum(axis=1)
    df_train, df_test = train_test_split(df_copy, test_size=0.2, random_state=42)

    df_copy['total_consummed'] = pd.cut(df_copy['total_consummed'], bins=5, labels=False)
    df_train, df_test = train_test_split(df_copy, test_size=0.2, random_state=42)
    
    # check the proportions of the data
    df_train_tc = df_train['total_consummed'].value_counts() / len(df_train)
    df_test_tc = df_test['total_consummed'].value_counts() / len(df_test)

    print('========== BEFORE ===========')
    print(df_train_tc)
    print(df_test_tc)
    print('=============================')

    #     total_consummed
    # 1    0.40625
    # 0    0.30875
    # 2    0.24125
    # 4    0.02625
    # 3    0.01750
    # Name: count, dtype: float64
    # total_consummed
    # 1    0.455
    # 2    0.275
    # 0    0.230
    # 4    0.025
    # 3    0.015
    # Name: count, dtype: float64

    # stratified split
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)
    for train_index, test_index in split.split(df_copy, df_copy['total_consummed']):
        df_train_tc = df_copy.loc[train_index]['total_consummed'].value_counts() / len(train_index)
        df_test_tc = df_copy.loc[test_index]['total_consummed'].value_counts() / len(test_index)

    #     total_consummed
    # 1    0.41625
    # 0    0.29250
    # 2    0.24750
    # 4    0.02625
    # 3    0.01750
    # Name: count, dtype: float64
    # total_consummed
    # 1    0.415
    # 0    0.295
    # 2    0.250
    # 4    0.025
    # 3    0.015
    # Name: count, dtype: float64
    
    print('========== AFTER ===========')
    print(df_train_tc)
    print(df_test_tc)
    print('=============================')


    return df_train, df_test