import pandas as pd

df = pd.read_csv(r"c:\Users\ztech.pk\Downloads\weather_data.csv")

# print(df.head(2))
# print(df.tail(2))

# rows , columns = df.shape

# print(rows,"\n",columns,)

# print(df.info())

# print(df.describe())
# print(df.columns)

# print(df[["day","temperature"]])

# print(df[["temperature"]].describe())

# print(df[df.temperature >=32])  

# print(df[df.temperature == df.temperature.max()])
# print(df.temperature.max())

# print(df[["temperature","day"]].max())
 
# print(df.index)

# df.set_index("day",inplace=True)
# print(df)
# print(df.loc["1/2/2017"])

# print(df.loc[0])


