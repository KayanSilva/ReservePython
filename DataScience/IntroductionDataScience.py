#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

name = "Kayan"
print(name)
age = 25
print(age)

grades = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")
movies.head()

print(grades.head())
print(grades.shape)

print(grades['rating'].unique())
print(grades['rating'].value_counts())
print(grades['rating'].mean())

print(grades.rating.plot())
print(grades.rating.plot(kind='hist'))
print("Average",grades.rating.mean())
print("Medium",grades.rating.median())

grades.rating.describe()

sns.boxplot(grades.rating)

grades.query("movieId==1").rating.mean()

grades.groupby("movieId").mean()

media_grades = grades.groupby("movieId").mean()["rating"]
media_grades.head()

media_grades.plot(kind='hist')

sns.boxplot(media_grades)
sns.distplot(media_grades, bins=10)
plt.hist(media_grades)
plt.title("Histograma")
plt.figure(figsize=(5,8))
sns.boxplot(y=media_grades)

sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})