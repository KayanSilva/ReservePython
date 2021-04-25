#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

grades = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")
tmb = pd.read_csv("tmdb_5000_movies.csv")

grades_ToyStory = grades.query("movieId == 1")
grades_Jumanji = grades.query("movieId == 2")

print("Average notes the Toy Story %.2f" % grades_ToyStory.rating.mean())
print("Middle notes the Toy Story %.2f" % grades_ToyStory.rating.median())
print("Average notes the Jumanji %.2f" % grades_Jumanji.rating.mean())
print("Middle notes the Jumanji %.2f" % grades_Jumanji.rating.median())

movie1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
movie2 = np.append(np.array([5] * 10), np.array([1] * 10))
sns.distplot(movie1)
sns.distplot(movie2)
plt.hist(movie1)
plt.hist(movie2)
plt.boxplot([movie1, movie2])
plt.boxplot([grades_ToyStory.rating, grades_Jumanji.rating])

sns.boxplot(x="movieId", y="rating", data= grades.query("movieId in [1,2]"))