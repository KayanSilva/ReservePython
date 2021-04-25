#%%
import pandas as pd

dados = pd.read_csv('aluguel_resid.csv', sep=';')
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
dados.head(10)
dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)
dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)
casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
dados.head(10)

dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])
del dados_aux['Valor Bruto']
dados_aux.pop('Valor Bruto m2')
dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis=1, inplace=True)
dados.head(5)
dados_aux.head(5)
dados.to_csv('aluguel_resid.csv', sep=';', index=False)

##Extra
s = pd.Series(list('asdadeadesdasesda'))
s.unique()
s.value_counts()
dados = pd.read_csv('aluguel.csv', sep=';')
dados.Tipo.unique()
dados.Tipo.value_counts()