import pandas as pd
data = {
    'Artist':['Artist 1','Artist 2','Artist 3'],
    'Released':[2001,2005,2008],
    'test':['test 1','test 2','test 3']
}
df = pd.DataFrame(data)
print(df)

print('-------------------------------------------------------------------')

# Slicing DataFrames
# With iloc (row, column by index)
print(df.iloc[0:2]) # rows 0-1, all columns
print('-------------------------------------------------------------------')
print(df.iloc[0:1,0:1]) # first row, first column
print('-------------------------------------------------------------------')
# with loc (row, column by name)
# Note that loc includes the last term
print(df.loc[0:1]) # rows 0-1, All columns
print('-------------------------------------------------------------------')
print(df.loc[0:0, 'Artist':'Artist']) # row 0 and 'Artist' column
