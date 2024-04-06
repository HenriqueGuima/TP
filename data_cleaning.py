import pandas 

def data_cleaning(df):
    
    # cleaning the data
    df_copy =  df.copy()

    # drop the first and second one columns
    # drop the columns with 100% of NaN
    # replace NaN with the mean of the column

    df_copy = df_copy.drop(columns=['dataid', 'localminute'])
    df_copy = df_copy.dropna(axis=1, how='all')
    df_copy = df_copy.apply(lambda x: x.fillna(x.mean()),axis=0)

    return df_copy