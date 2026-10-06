import pandas as pd
import numpy as np
# data = pd.read_csv(r"c:\Users\ztech.pk\Downloads\countries of the world.csv")
# print(data.index)

# df = pd.Series([22.5, 23.0, np.nan, 24.3,24.3],index=['Mon', 'Tue', 'Wed', 'Thu',"Thu"])
# # print(int(df.mean() +1))
# df =df.dropna().drop_duplicates()
# print(df)


# data = pd.DataFrame({
#     "Name":["john","bob","charlie"],
#     "age" : [10,20,25],
#     "city" : ["NYC","Paris","London"]
# })

# print(data)

# df = pd.read_excel(r"c:\Users\ztech.pk\Downloads\world_population_excel_workbook.xlsx")
df = pd.read_json(r"c:\Users\ztech.pk\Downloads\json_sample.json")
print(df)