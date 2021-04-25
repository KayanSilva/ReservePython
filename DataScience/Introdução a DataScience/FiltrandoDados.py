import pandas as pd

dados = pd.read_csv('aluguel.csv', sep=';')
lista = list(dados.Tipo.drop_duplicates())
residencial = ['Quitinete','Casa','Apartamento','Casa de Condomínio','Casa de Vila']
selecao = dados['Tipo'].isin(residencial)
dados_residencial = dados[selecao]
dados_residencial.shape[0]
dados.shape[0]
dados_residencial.index = range(dados_residencial.shape[0])

dados_residencial.to_csv('aluguel_resid.csv', sep=';', index=False)
dados_residencial_2 = pd.read_csv('aluguel_resid.csv', sep=';')

##Extra
data = [[1,2,3], [4,5,6], [7,8,9]]
list(data)
df = pd.DataFrame(data, list('321'), list('ZYX'))
df.sort_index(inplace=True, axis=1)
df.sort_values(by='X', inplace=True, axis=1)
