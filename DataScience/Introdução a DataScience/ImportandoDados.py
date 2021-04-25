#%%
import pandas as pd

dados = pd.read_csv('aluguel.csv', sep = ";")
type(dados)
dados.info()
dados.head(10)
dados.dtypes
data_types = pd.DataFrame(dados.dtypes, columns = ['Tipos de dados'])
data_types.columns.name = 'Variaveis'
dados.shape
print('A base de dados possui {} registros e {} variaveis'.format(dados.shape[0], dados.shape[1]))

## Extra
json = open('aluguel.json')
print(json.read())
dsjson = pd.read_json('aluguel.json')
dstxt = pd.read_table('aluguel.txt')
dsxlsx = pd.read_excel('aluguel.xlsx')
dshtml = pd.read_html('https://unafiscosaude.org.br/site/tabelas-de-precos-dos-planos-ativos-para-comercializacao/')
dshtml[0]
df_html = pd.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')
len(df_html)
df_html[0]