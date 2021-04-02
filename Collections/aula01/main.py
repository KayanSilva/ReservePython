# declarando idades
idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

# imprimindo dados
print(idade1)
print(idade2)
print(idade3)
print(idade4)

# criando lista númerica, tipando e obtendo tamanho
idades = [39, 30, 27, 18]
print(type(idades))
print(len(idades))
print(idades)
print(idades[0])
print(idades[1])
print(idades[2])

# adicionando na lista
idades.append(15)
print(idades)
print(idades[4])

# passando por todos os itens da lista
for idade in idades:
    print(idade)

# removendo um item, se não for encontrado dá erro.
idades.remove(30)
print(idades)

# adicionando um item semelhante na lista, se caso solicitado para remoção, ele exclui o primeiro encontrado.
idades.append(27)
print(idades)
idades.remove(27)
print(idades)

# descobrindo se há o item dentro da lista
print(28 in idades)
print(15 in idades)

if(15 in idades):
    idades.remove(15)

print(idades)

# adicionando item em posição especifica com insert
idades.append(19)
idades.insert(0, 20)
print(idades)

# adicionando varios itens na lista
idades = [20, 39, 18]
idades.extend([27, 19])
print(idades)

# Saber a idade que terá no proximo ano
for idade in idades:
    print(idade + 1)

idades_no_ano_que_vem = []

for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)

print(idades_no_ano_que_vem)


def proximosdoisanos(idade):
    return idade+2


idades_no_ano_que_vem = [proximosdoisanos(idade) for idade in idades]
print(idades_no_ano_que_vem)

# filtrar valores de uma lista
idades_acima_de_vinteum = [idade for idade in idades if idade > 21]
print(idades_acima_de_vinteum)

# mutabilidade da lista


def faz_processamento_de_visualizacao(lista=None):
    if lista == None:
        lista = list()

    print(len(lista))


idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)
print(idades)

# removendo todos os itens da lista
idades.clear()
