# here we have to find the informative summary about the data:
import pandas as pd

data = pd.read_csv("sales_data_sample.csv",encoding="latin1")
print("Display The infomation about the data: ")

print(data.info())