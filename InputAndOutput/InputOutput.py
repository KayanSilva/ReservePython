#%%
import pandas as pd
import numpy as np
import html5lib
import seaborn as sns

names_f = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=f")
names_m = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=m")

frames = [names_f, names_m]

names = pd.concat(frames)['nome'].to_frame()
names.sample(5)
np.random.seed(123)

names["id_student"] = np.random.permutation(len(names)) + 1
domains = ["@emaildomain.com.br", "@emailservice.com"]
names["domain"] = np.random.choice(domains, len(names))
names["email"] = names.nome.str.cat(names.domain).str.lower()
names.sample(5)

url = "http://tabela-cursos.herokuapp.com/index.html"
courses = pd.read_html(url)
courses = courses[0]
courses = courses.rename(columns={"Nome do curso" : "course_name"})
courses["id"] = courses.index + 1
courses = courses.set_index("id")

names["matriculas"] = np.ceil(np.random.exponential(size=len(names)) * 1.5).astype(int)
names.sample(3)
names.matriculas.describe()
sns.distplot(names.matriculas)
names.matriculas.value_counts()

todas_matriculas = []
x = np.random.rand(20)
prob = x / sum(x)
for index, row in names.iterrows():
    id = row.id_student
    matriculas = row.matriculas
    for i in range(matriculas):
        mat = [id, np.random.choice(courses.index, p = prob)]
        todas_matriculas.append(mat)
matriculas = pd.DataFrame(todas_matriculas, columns= ["id_student", "id_course"])
matriculas.head()
matricula_course = matriculas.groupby("id_course").count().join(courses["course_name"]).rename(columns={'id_student':'quantity_students'})
