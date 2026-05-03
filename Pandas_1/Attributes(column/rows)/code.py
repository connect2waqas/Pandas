import pandas as pd

data = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print("Display the shape of data: ")
print(data.shape)
# print("Display the columns Names: ")
print("Display the columns Names: \n",data.columns)
