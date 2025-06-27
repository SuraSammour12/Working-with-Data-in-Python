# What is a Series? 
# A Series is one-dimensional labeled array in Pandas
# A Series can create from various data sources, such as lists, NumPy arrays, or dictionaries
import pandas as pd
# Create a Series from a list
data = [10,20,30,40,50]
s = pd.Series(data)
print(s)
"""
0    10
1    20
2    30
3    40
4    50
dtype: int64
"""
# created a Series named s with numeric data, Pandas automatically assigned numerical indices (0-4) to each element
# Accessing Elements in a series
# 1. by label
print(s[2])
# 2. by position
print(s.iloc[3]) 
# 3. Accessing multiple elements
print(s[1:4]) # indices 1-3

print('-----------------------------------------------------------------------------------')
# Series Attributes
# values : returns the series data as NumPy array
print(s.values)
print('-----------------------------------------------------------------------------------')
# index : returns the index of the series
print(s.index) # RangeIndex(start=0, stop=5, step=1)
print('-----------------------------------------------------------------------------------')
# shape : return a tuple representing the dimensions of the Series
print(s.shape)
print('-----------------------------------------------------------------------------------')
# size 
print(s.size)
print('-----------------------------------------------------------------------------------')
# mean(), sum(), min(), max() : calculate summary statistics of the data
print(s.sum())
print('-----------------------------------------------------------------------------------')
# unique(), nunique() : get unique values or the number of unique values
print(s.unique())
print(s.nunique())
print('-----------------------------------------------------------------------------------')
# sort_values(), sort_index() : sort the series by values or index labels
print(s.sort_index())
print(s.sort_values())
print('-----------------------------------------------------------------------------------')
# isnull(), notnull()
print(s.isnull())
print('-----------------------------------------------------------------------------------')
print(s.notnull())
print('-----------------------------------------------------------------------------------')
# apply() : apply a custom function to each element of the series
def add_10(num):
    return num+10

new_s = s.apply(add_10)
print(f'new s is \n{new_s}')
    
print('-----------------------------------------------------------------------------------')
# lambda function 
new_s2 = s.apply(lambda x:x+100)
print(new_s2)