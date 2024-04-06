import pandas
import numpy
from sklearn.model_selection import train_test_split
import data_split, data_cleaning, generate_new

# switching between the two datasets for better cleanup like removing columns with more than 100% of NaN
# df = pandas.read_csv("consumos.csv")
df = pandas.read_csv("consumos_short.csv")

df_copy = data_cleaning.data_cleaning(df)

# split the data into training and testing
df_train, df_test = data_split.data_split(df_copy)

generate_new.generate_new_dataset(df_copy)

# print(df_test.shape)
# print(df_train)