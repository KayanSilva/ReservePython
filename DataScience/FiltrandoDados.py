import pandas as pd

dados = pd.read_csv('aluguel.csv', sep=';')
lista = list(dados.Tipo.drop_duplicates())
residencial = ['Quitinete','Casa','Apartamento','Casa de Condomínio','Casa de Vila']
selecao = dados['Tipo'].isin(residencial)
dados_residencial = dados[selecao]
dados_residencial.shape[0]
dados.shape[0]
dados_residencial.index = range(dados_residencial.shape[0])