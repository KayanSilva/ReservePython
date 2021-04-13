# Dicionarios

from collections import defaultdict, Counter

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
del aparicoes["Carlos"]  # Excluindo uma chave
print(aparicoes)

print(type(aparicoes))
print(aparicoes['Kayan'])
print(aparicoes.get("xpto", 0))  # Prevenindo erro
print("cachorro" in aparicoes)  # Procurando nas chaves

for elemento in aparicoes:
    print(elemento)  # mostra as chaves

for chave, valor in aparicoes.items():
    print(chave, "=", valor)


meu_texto = "Bem vindo meu nome é Kayan eu gosto muito de animais e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

aparicoes = Counter(meu_texto.split())
print(aparicoes)


class Conta:
    def __init__(self):
        print("Criando uma conta")


contas = defaultdict(Conta)
print(contas[15])
