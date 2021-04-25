import pandas as pd

dados = pd.read_csv('aluguel.csv', sep = ";")
selecao = dados['Tipo'] == 'Apartamento'
n1 = dados[selecao].shape(0)
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape(0)
selecao = (dados['Area'] > 59) & (dados['Area'] < 101 )
n3 = dados[selecao].shape(0)
selecao = (dados['Quartos'] > 3) & (dados['Tipo'] < 2000)
n4 = dados[selecao].shape(0)

print("Nº de imóveis  imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'-> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))

##Extra
data = [[1,2,3], [4,5,6], [7,8,9]]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
df[['c1', 'c3']]
df[:]
df[1:3]
df[1:][['c1', 'c3']]
df.loc['l3']
df.loc[['l3', 'l1']]
df.loc[['l1', 'c3']]
df.iloc[0, 1]
df.loc[['l1', 'l3'], ['c1', 'c2']]
df.iloc[[2, 0], [3, 0]]