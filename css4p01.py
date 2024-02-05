# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:28:43 2024

@author: Prudence
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Cleaning data
df = pd.read_csv("C:/Users/Prudence/css2024_Project01/movie_dataset.csv")

print(df.info())
print(df.describe())
len(df)-len(df.drop_duplicates())

# Replace space from column names with another character
df.columns = df.columns.str.replace(' ', '_')

# Removing space between column values
df['Title'] = df['Title'].apply(lambda x: x.replace(' ', ''))
df['Director'] = df['Director'].apply(lambda x: x.replace(' ', ''))
df['Actors'] = df['Actors'].apply(lambda x: x.replace(' ', ''))
df['Description'] = df['Description'].apply(lambda x: x.replace(' ', ''))

# Dealing with NaNs using fillna
avg_rev = df["Revenue_(Millions)"].mean()

df["Revenue_(Millions)"].fillna(avg_rev, inplace = True)
"""
Answer is 82.95637614678898
"""

avg_meta = df["Metascore"].mean()

df["Metascore"].fillna(avg_meta, inplace = True)
"""
Answer is 58.98504273504273
"""

print(df.info())
print(df.describe())

# Determining the movie ratings
df_avg = df['Rating'].mean()
print(df_avg)

film_ranking = df.sort_values('Rating', ascending=False)

plt.barh(film_ranking['Title'].head(10),film_ranking['Rating'].head(10), align='center', color='skyblue')

plt.ylabel('Frequency')
plt.xlabel("Ratings")
plt.title("Highest-rated Movies")
plt.show()

rating_sorted_data =df.sort_values(by= 'Rating', ascending=False)
print(rating_sorted_data)
"""
Answer is The Dark Knight
"""

# Average revenue from 2015 to 2017
average_revenue_2015_to_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]['Revenue_(Millions)'].mean()
"""
Answer is 68.064
"""


# Movies directed by Christopher Nolan
movies_by_Nolan = df.query("Director=='ChristopherNolan'")
print(movies_by_Nolan)
"""
Answer is 5
"""
# number of movies per year (which will include 2016)
years = df['Year'].value_counts()
"""
Answer is 297
"""

# average movie  with highest ratings
years2 = years[years >=10]
year_avg_rating = df.loc[df['Year'].isin(years2.index)].groupby('Year')['Rating'].mean()
""""
Answer is 2007( which has a rating of 7.13396, this is the highest rating)
"""
# dataset with a rating of at least 8.0
movies_with_rating_at_least_8 = df[df['Rating'] >= 8.0].shape[0]
"""
Answer is 78
"""

# The median rating of movies directed by Christopher Nolan
median_rating_christopher_movies = df[df['Director'] == 'ChristopherNolan']['Rating'].median()
"""
Answer is 8.6
"""

# % increase in the number of movies made between 2006 and 2016
movies_in_2006 = df[df['Year'] == 2006].shape[0]
movies_in_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase_2006_to_2016 = ((movies_in_2016 - movies_in_2006) / movies_in_2006) * 100
"""
Answer is 575.0
"""

# Most common actor in the movie dataset
from collections import Counter
list = ['Actors']
conts = Counter(list)
all_actors = df['Actors'].str.split(',').sum()
most_common_actor = Counter(all_actors).most_common(1)[0][0].strip()
"""
Answer is Mark Wahlberg
"""

# number of unique genres
all_genres = df['Genre'].str.split(',').sum()
unique_genres = len(set(all_genres))

"""
Answer is 20
"""
# A correlation of the numerical feautures
correlation_matrix = df[['Runtime_(Minutes)', 'Year', 'Rating', 'Votes', 'Revenue_(Millions)', 'Metascore']].corr()




