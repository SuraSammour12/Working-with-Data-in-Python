# DataFrames : two-dimensional labeled data structure with columns of potentially different data types 
# DataFrames are suitable for a wide range of data, including structured data from CSV files, Excel spreadsheets, SQL databases, and more 
# Creating a DataFrames from Dictionaries
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Sarah'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
print('--------------------------------------------------------------------------')
# Column Selection
print(df['Name']) # Access the 'Name' column
print(type(df['Name'])) # <class 'pandas.core.series.Series'>
print('--------------------------------------------------------------------------')
# Accessing Rows using .iloc (index), .loc (label)
print(df.iloc[2]) # access the 3rd row by position
print('--------------------------------------------------------------------------')
print(df.loc[1]) # access the 2nd row by label
print('--------------------------------------------------------------------------')
# Slicing 
# select specific rows and columns
print(df[['Name','Age']]) # select specific columns
# type : <class 'pandas.core.frame.DataFrame'>
print('--------------------------------------------------------------------------')
print(df[1:3]) # select specific rows
print('--------------------------------------------------------------------------')
# Finding Unique Elements
unique_dates = df['Age'].unique()
print(unique_dates)
print('--------------------------------------------------------------------------')
# Conditional Filtering
age_above_25 = df[df['Age']>25]
print(age_above_25)
print('--------------------------------------------------------------------------')
# Saving DataFrames
df.to_csv('trading_data.csv',index=False)