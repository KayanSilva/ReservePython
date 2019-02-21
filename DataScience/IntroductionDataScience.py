#%%
import pandas as pd
import seaborn as sns

name = "Kayan"
print(name)
age = 25

grades = pd.read_csv("ratings.csv")

print(grades.head())
print(grades.shape)

grades.columns = ["cdUser", "cdMovie", "cdRatings", "Time"]
grades['cdRatings'].unique()
grades['cdRatings'].value_counts()
grades['cdRatings'].mean()

grades.cdRatings.plot()
grades.cdRatings.plot(kind='hist')
print("Average",grades['cdRatings'].mean())
print("Medium",grades['cdRatings'].median())

grades.cdRatings.describe()

sns.boxplot(grades.cdRatings)