# Dicionarios

aparicoes = {
    "Kayan": 1,
    "cachorro": 2,
    "nome": 1,
    "vindo": 1
}

aparicoes = dict(Kayan=2, cachorro=1)

aparicoes["Carlos"] = 1
aparicoes["Kayan"] = 3
print(aparicoes)
del aparicoes["Carlos"] # Excluindo uma chave
print(aparicoes)

print(type(aparicoes))
print(aparicoes['Kayan'])
print(aparicoes.get("xpto", 0))  # Prevenindo erro
print("cachorro" in aparicoes) #Procurando nas chaves

for elemento in aparicoes:
    print(elemento) # mostra as chaves

for chave, valor in aparicoes.items():
    print(chave, "=", valor)

