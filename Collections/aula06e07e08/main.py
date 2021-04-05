from operator import attrgetter
from functools import total_ordering

idades = [15, 87, 32, 65, 56, 32, 49, 37]
print(sorted(idades))  # ordenando do menor para o maior
print(list(reversed(idades)))  # ordenando ao contrario
print(sorted(idades, reverse=True))  # utilizando o proprio sorted
idades.sort()
print(idades)  # ordenando no mesmo lugar, pela lista ser mutavel

nomes = ["Guilherme", "Daniela", "Paulo"]
print(sorted(nomes))


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo

        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Codigo {}\n Saldo {}\n".format(self._codigo, self._saldo)


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(183)
conta_do_paulo.deposita(510)

conta_do_kayan = ContaSalario(200)
conta_do_kayan.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo, conta_do_kayan]


def extrai_saldo(conta):
    return conta._saldo  # utilizando acesso a uma propriedade privada não é recomendado


for conta in sorted(contas, key=extrai_saldo):
    print(conta)

# puxando direto da propriedade da classe
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

# utilizando criterio de desempate
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

for conta in sorted(contas):
    print(conta)

print("O saldo do Guilherme é menor do que da Daniela:",
      conta_do_guilherme < conta_da_daniela, "\n")

# utilizando functools para ordenações
print("O saldo do Guilherme é menor ou igual do que da Daniela:",
      conta_do_guilherme <= conta_da_daniela, "\n")
print("O saldo do Guilherme é menor ou igual do que do Kayan:",
      conta_do_guilherme <= conta_do_kayan, "\n")
print("O saldo do Guilherme é igual a do Guilherme:",
      conta_do_guilherme == conta_do_guilherme, "\n")
