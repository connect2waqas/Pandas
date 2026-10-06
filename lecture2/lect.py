import pandas as pd

# # Method 1: Dictionary
# data = {'Product': ['Laptop', 'Phone', 'Tablet'], 'Price': [999, 699, 299]}
# df1 = pd.DataFrame(data)
# print(df1)

# # Method 2: List of Lists
# data = [['Laptop', 999], ['Phone', 699], ['Tablet', 299]]
# df2 = pd.DataFrame(data, columns=['Product', 'Price'])
# print(df2)

# # Method 3: List of Dictionaries
# data = [
#     {'Product': 'Laptop', 'Price': 999},
#     {'Product': 'Phone', 'Price': 699},
#     {'Product': 'Tablet', 'Price': 299}
# ]
# df3 = pd.DataFrame(data)
# print(df3)

# Read CSV with no header, custom column names, and set index
# df = pd.read_csv(
#     'data.csv',header=None,names=['ID', 'Name', 'Age'],index_col='ID',na_values=['Unknown']
# )



df = pd.read_csv(r"c:\Users\ztech.pk\Downloads\stock_data.csv",header=None)
print(df)