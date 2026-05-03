import pandas as pd

data = pd.read_excel(r'C:\Users\ztech.pk\Downloads\Customer Call List.xlsx')
# print(data)
# Here we have to remove the duplicate and then also save it to the variable also:
# print("Removing the Duplicates from the data:")
data = data.drop_duplicates()
# print(data)
# Here we have to Remove the unusefull columns from the dataset..
data = data.drop(columns="Not_Useful_Column")
# print("The New Dataset is: \n",data)

# data["Last_Name"] = data["Last_Name"].str.lstrip("...")
# data["Last_Name"] = data["Last_Name"].str.lstrip("/")
# data["Last_Name"] = data["Last_Name"].str.rstrip("_")
# But we can do all of the above with just single method and here that's:
print("Removing the False Things: ")
data["Last_Name"] = data["Last_Name"].str.strip("123./_")
# print(data)
# Correct approach: Assign the cleaned data back
# data["Phone_Number"] = data["Phone_Number"].str.replace(r'[^a-zA-Z0-9]', '', regex=True)
# data["Phone_Number"].apply(lambda x : str(x))
# print(data["Phone_Number"])