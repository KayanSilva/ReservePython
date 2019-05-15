#%%
import IPython
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15,8))

dados = pd.read_csv('aluguel_resid.csv', sep = ';')
dados.boxplot(['Valor'])
dados[dados['Valor'] >= 500000]
valor = dados['Valor']
Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
selecao = (valor >=limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]
dados_new.boxplot(['Valor'])
dados.hist(['Valor'])
dados_new.hist(['Valor'])

dados.boxplot(['Valor'], by = ['Tipo'])
grupo_tipo = dados.groupby('Tipo')['Valor']
grupo_tipo.groups
Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
limite_superior['Casa']
dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])
dados_new.boxplot(['Valor'], by = ['Tipo'])
dados_new.to_csv('aluguel_residencial_sem_outliers.csv', sep = ';', index = False)

##Extra
area =plt.figure()
g1 = area.add_subplot(2,2,1)
g2 = area.add_subplot(2,2,2)
g3 = area.add_subplot(2,2,3)
g4 = area.add_subplot(2,2,4)

dados = pd.read_csv('aluguel.csv', sep = ';')

g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor X Area')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100)
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra valor')

grupo = dados.groupby('Tipo')['Valor']
g4.bar(grupo.mean().index, grupo.mean().values)
g4.set_title('Media por tipo')

area.savefig('grafico.png', dpi = 300, bbox_inches = 'tight')