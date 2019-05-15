#%%
import pandas as pd

dados = pd.read_csv('aluguel_resid.csv', sep=';')
dados.head(10)
dados.isnull()
dados.notnull()
dados.info()
dados[dados['Valor'].isnull()]
dados.dropna(subset= ['Valor'], inplace=True)

dados[dados['Condominio'].isnull()].shape[0]
selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())
dados = dados[~selecao]
dados.fillna(0, inplace=True)
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})
dados.to_csv('aluguel_resid.csv', sep=';', index=False)

##Extra
data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
s.fillna(0)
s.fillna(method= 'ffill')
s.fillna(method= 'bfill')
s.fillna(s.mean())
s1 = s.fillna(method= 'ffill', limit=1)
s1.fillna(method= 'bfill', limit=1)