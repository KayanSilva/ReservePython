idades = [15, 87, 32, 65, 56, 32, 49, 37]
for i in range(len(idades)):  # lazy
    print(i, idades[i])

print(enumerate(idades))  # lazy
print(list(range(len(idades))))  # forçando a geração

for indice, idade in enumerate(idades):  # unpacking da tupla
    print(indice, "x", idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979),
]

for nome, idade, nascimento in usuarios:  # desempacotando
    print(nome)

for nome, _, _ in usuarios:  # desempacotando, ignorando valores não utilizados
    print(nome)
