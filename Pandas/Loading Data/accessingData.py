import pandas as pd
data = {
    "Artist": ["Artist 1", "Artist 2"],
    "Released": [2001, 2005],
    'test':['test1','test2']
}

df = pd.DataFrame(data)
print(df)

print('=============================================================================')
# Accessing Data by Index

# Using .iloc (Position-based indexing)
print(df.iloc[0, 0]) # First row, first column
print(df.iloc[1, 0]) # Second row, first column
print(df.iloc[0, 2]) # First row, third column
print(df.iloc[1, 2]) # Second row, third column

print('=============================================================================')
# Using .loc (Label-based indexing)
print(df.loc[0, 'Artist'])
print(df.loc[1, 'Artist'])
print(df.loc[0, 'Released'])
print(df.loc[1, 'test'])

print('=============================================================================')
# Custom Indexes
new_df = df.copy()
new_df.index = ['a','b']
print(new_df)
# access data using the new labels
print(new_df.loc['a','Artist'])
print(new_df.loc['b','test'])
