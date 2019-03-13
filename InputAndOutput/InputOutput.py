#%%
import pandas as pd
import numpy as np
import html5lib

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
courses = courses.rename(columns={"Nomes do curso" : "course_names"})
courses["id"] = courses.index + 1
courses = courses.set_index("id")