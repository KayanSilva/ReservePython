#%%
import pandas as pd

dados = pd.read_csv('aluguel.csv', sep = ";")
type(dados)
dados.info()
dados.head(10)
dados.dtypes
data_types = pd.DataFrame(dados.dtypes, columns = ['Tipos de dados'])
data_types