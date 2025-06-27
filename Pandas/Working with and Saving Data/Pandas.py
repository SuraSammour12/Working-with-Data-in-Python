# Working with and saving Data
import pandas as pd

data = {
    "Artist": [
        "Michael Jackson", "AC/DC", "Pink Floyd", "Whitney Houston",
        "Meat Loaf", "Eagles", "Bee Gees", "Fleetwood Mac"
    ],
    "Album": [
        "Thriller", "Back in Black", "The Dark Side of the Moon", "The Bodyguard",
        "Bat Out of Hell", "Their Greatest Hits (1971-1975)", "Saturday Night Fever", "Rumours"
    ],
    "Released": [1982, 1980, 1973, 1992, 1977, 1976, 1977, 1977],
    "Length": ["0:42:19", "0:42:11", "0:42:49", "0:57:44", "0:46:33", "0:43:08", "1:15:54", "0:40:01"],
    "Genre": [
        "pop, rock, R&B", "hard rock", "progressive rock", "R&B, soul, pop",
        "hard rock, progressive rock", "rock, soft rock, folk rock", "disco", "soft rock"
    ],
    "Music Recording Sales (millions)": [46.0, 26.1, 24.2, 27.4, 20.6, 32.2, 20.6, 27.9],
    "Claimed Sales (millions)": [65, 50, 45, 44, 43, 42, 40, 40],
    "Released.1": [
        "30-Nov-82", "25-Jul-80", "01-Mar-73", "17-Nov-92",
        "21-Oct-77", "17-Feb-76", "15-Nov-77", "04-Feb-77"
    ],
    "Soundtrack": [None, None, None, "Y", None, None, None, None],
    "Rating": [10.0, 9.5, 9.0, 8.5, 8.0, 7.5, 7.0, 6.5]
}

df = pd.DataFrame(data)
print(df)
print('------------------------------------------------------------------------------------------')
# Finding Unique values in a column => Use the .unique Method
print(df['Released'].unique()) 
print(type(df['Released'].unique())) # numpy.ndarray
print('------------------------------------------------------------------------------------------')
# Filtering Data Based on Conditions
# Example : Suppose i  want to filter DataFrame to include only albums released in 1980 or later
print(df['Released']>1979) # this return a series of Boolean values
print('---------------------------------------------------------')
df_1980 = df[df['Released']>1979] # new DataFrame with only albums released after 1979
print(df_1980) 
print('---------------------------------------------------------')
# Saving a Filtered DataFrame
# Saving df_1980 as a CSV file (using to_csv())
df_1980.to_csv('filtered_albums.csc') # .csv file

# use to_excel() for Excel files | to_json() for JSON format