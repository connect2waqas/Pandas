# Here we to work with selecting and filtering the rows and columns:

import pandas as pd

info = {
    "Names" : ["Ilyas","Abbas","Waqas","Roman","Shahid","Ihtisham","Salman","Siraj","Bashir","Bilal"],
    "Age" : [17,13,20,22,27,20,25,25,20,25],
    "Salary" : [50000,45000,100000,60000,110000,70000,80000,120000,70000,110000],
    "Performance" : [90,70,85,55,43,58,85,49,86,75]
}

data = pd.DataFrame(info)
# print("Display the first Rows: ")
# print(data.head(1))
# print("Display The last Rows: ")
# print(data.tail(1))

# print(f"{data["Name"]} \nAnd the length of the data is: {len(data["Name"])}")

# operation_data = data[data["Salary"] > 60000]
# print(operation_data)

# filter_rows = data[(data["Salary"] >60000) & (data["Salary"] < 90000)]
# print(filter_rows)

# row_filtering = data[(data["Age"] > 20) & (data["Performance"] > 60) & (data["Salary"] > 85000)]
# print(row_filtering)

# Selecting single and multple columns
# print("Selecting Single column from data: \nSeries: ")
# single_columns = data["Names"]
# print(single_columns)
# print("Selecting Multiple columns from the data: \nDataFrame: ")
# multiple_columns = data[["Names","Salary"]]
# print(multiple_columns)

# Selecting the rows and columns based on conditions:

# operation_based = data[(data["Performance"] > 55) & (data["Salary"] > 70000) & (data["Salary"] < 90000)]
# print("Selection Based on Conditions: \nDataFrame:")
# print(operation_based)
# Filter rows where Age > 20 OR (Performance > 60 AND Salary > 85000)  
filtered = data[(data["Age"] > 20) | ((data["Performance"] > 60) & (data["Salary"] > 85000))]
print(filtered)