import pandas as pd

info = {
    "Names" : ["Ilyas","Abbas","Waqas","Roman","Shahid","Ihtisham","Salman","Siraj","Bashir","Bilal"],
    "Age" : [17,13,20,22,27,20,25,25,20,25],
    "Salary" : [50000,45000,100000,60000,110000,70000,80000,120000,70000,110000],
    "Performance" : [90,70,85,55,43,58,85,49,86,75]
}

df = pd.DataFrame(info)

# print(df)

# As we have to add a column to the dataframe so for that we should use method to do that:
# first assigning the values to new data:

# df["Bonus"] = df["Salary"] * 0.1

# print(df)
