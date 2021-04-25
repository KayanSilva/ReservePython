#%%
import pandas as pd
import IPython
%matplotlib inline
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20, 10))

dados = pd.read_csv('aluguel_resid.csv', sep = ';')
dados.head(10)
dados['Valor'].mean()
bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]
dados['Bairro'].drop_duplicates()
grupo_bairro = dados.groupby('Bairro')
grupo_bairro.groups
for bairro, data in grupo_bairro:
    print('{} -> {}'.format(bairro, data.Valor.mean()))
grupo_bairro['Valor'].mean().round(2)

grupo_bairro['Valor'].describe().round(2)
grupo_bairro['Valor'].aggregate(['min', 'max']).rename(columns = {'min': 'Mínimo', 'max': 'Maximo'})
fig = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})

##Extra
dados = pd.read_csv('aluguel.csv', sep = ';')
dados.head(10)
classes = [0, 2, 4, 6, 100]
quartos = pd.cut(dados.Quartos, classes)
labels = ['0 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 quartos ou mais']
quartos = pd.cut(dados.Quartos, classes, labels=labels, include_lowest=True)
pd.value_counts(quartos)
