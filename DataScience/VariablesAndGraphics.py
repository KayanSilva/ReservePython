#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

movies = pd.read_csv("tmdb_5000_movies.csv")
movies.head()

movies["original_language"].unique()
movies["original_language"].value_counts().index
movies["original_language"].value_counts().values
movies["original_language"].value_counts().to_frame()
movies["original_language"].value_counts().to_frame().reset_index()

languages = movies.original_language.value_counts().to_frame().reset_index()
languages.columns = ["original_language", "total"]
languages.head()

sns.barplot(x="original_language", y="total", data = languages)
sns.catplot(x="original_language", kind="count", data = movies)
sns.__version__

plt.pie(languages["total"], labels= languages["original_language"])

total_languagues = movies.original_language.value_counts()
total_lan = total_languagues.sum()
total_en = total_languagues.loc["en"]
total_res = total_lan - total_en

datas = {
    'language' : ['english', 'other'],
    'total' : [total_en, total_res]
}
data = pd.DataFrame(datas)

sns.barplot(x="language", y="total", data = datas)
plt.pie(datas["total"], labels= datas["language"])

lang_other = movies.query("original_language != 'en'").original_language.value_counts()
lang_notisen = movies.query("original_language != 'en'")

sns.catplot(x="original_language", kind="count", data = lang_notisen,
aspect=2, order= lang_other.index, palette="GnBu_d")