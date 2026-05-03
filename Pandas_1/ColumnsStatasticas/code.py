# Here we have to find the descriptive statistics of a dataframe:

import pandas as pd

data = pd.read_csv("sales_data_sample.csv" , encoding="latin1")

print(data.describe())
data[data["QUANTITYORDERED"].max() and data[data["PRICEEACH"].max()]]