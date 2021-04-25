import pandas as pd

dados = pd.read_csv('aluguel.csv', sep=';')
dados.head(10)

tiposImoveis = dados['Tipo']
tiposImoveis.drop_duplicates(inplace = True)

tiposImoveis = pd.DataFrame(tiposImoveis)
tiposImoveis.index = range(tiposImoveis.shape[0])
tiposImoveis.columns.name = 'Id'

## Extra
data = [1,2,3,4,5]
s = pd.Series(data)
index = ['Linha ' + str(i) for i in range(5)]
s = pd.Series(data = data, index = index)
data =  {'Linha' + str(i) : i + 1 for i in range(5) }
s = pd.Series(data)
s1 = s + 2
s2 = s + s1
data = [[1,2,3], [4,5,6], [7,8,9]]
df1 = pd.DataFrame(data)
index = ['Linha ' + str(i) for i in range(3)]
columns = ['Coluna ' + str(i) for i in range(3)]
df1 = pd.DataFrame(data=data, index=index, columns=columns)
data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}
df2 = pd.DataFrame(data=data, index=index, columns=columns)
data = [(1,2,3), (4,5,6), (7,8,9)]
df3 = pd.DataFrame(data=data, index=index, columns=columns)
df1[df1> 0] = 'A'
df2[df2> 0] = 'B'
df3[df3> 0] = 'C'
df4 = pd.concat([df1,df2,df3])
df4 = pd.concat([df1,df2,df3], axis=1)