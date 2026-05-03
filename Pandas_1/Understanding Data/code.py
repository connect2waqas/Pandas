import pandas as pd

# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# df = pd.read_json("sample_Data.json") 
# print(df)

# data = {
#     "name" : ["waqas","ilyas","abbas"],
#     "age" : [20,17,13],
#     "city" : ["Giro tangai","Shamshi khan","Talash"],

# }

# df = pd.DataFrame(data)

# df.to_csv("output.csv",index=False)
# df.to_excel("output.xlsx",index=False)

df = pd.read_json("sample_Data.json")
print("Display the first rows: ")
print(df.head())

print("Display the last rows: ")
print(df.tail())
