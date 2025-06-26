# Importing Pandas 
import pandas as pd

# Working with csv Files : CSV (Comma-Separated Values) is a common file format used to store data in a tabular format
# Reading a CSV File 
df = pd.read_csv('financial-year-provisional.csv')
# read_scv() is a function in pandas that loads a CSV file
# df : DataFrame, the core data structure in pandas 

# DataFrame Basics
# A DataFrame is like a table with rows and columns

# Viewing Data
print(df.head()) # Shows the first 5 rows of the DataFrame

print('====================================================================================================================')

# Reading Excel Files
df2 = pd.read_excel('DATA.xlsx')
print(df2.head())

print('====================================================================================================================')

# Creating a DataFrame from a Dictionary
data = {
    "Artist": ["Artist 1", "Artist 2"],
    "Released": [2001, 2005]
}

df3= pd.DataFrame(data) 
# in this structure : keys => column headers | values => rows

# Selecting Columns
# Selecting One Column
new_df1 = df3[["Artist"]]
print(new_df1)
print()
# Selecting Multiple Columns
new_df2 = df3[['Artist','Released']]
print(new_df2)