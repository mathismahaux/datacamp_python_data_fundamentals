# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]

movies_1990s = subset[(subset["release_year"] < 2000)]

plt.hist(movies_1990s["duration"])
plt.title('Distribution of the durations of the movies released in the 1990s')
plt.xlabel('Duration (in minutes)')
plt.ylabel('Amount of movies')
plt.show()

duration = 100

action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

short_movie_count = 0

for label, row in action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)