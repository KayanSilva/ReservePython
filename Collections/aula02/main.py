# Objetos proprios

class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "Codigo {}\n Saldo {}\n".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
print(conta_do_gui)
conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47478)
conta_da_dani.deposita(1000)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]
for conta in contas:
    print(conta)

# mesmo objeto, referencia diferente
contas[2].deposita(200)
print(conta_do_gui)

# Tuplas, objetos e anemia


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


def deposita(conta):  # variação funcional - separando o comportamento dos dados
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)


contas = [conta_do_gui, conta_da_dani]
deposita_para_todas(contas)
print(contas[0], contas[1])
contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)
paulo = (39, 'Paulo', 1979)  # ruim, quebra o padrão proposto

conta_do_gui = (15, 1000)
print(conta_do_gui)
print(deposita(conta_do_gui))

#Tuplas de objetos e lista de tuplas
usuarios = [guilherme, daniela]
print(usuarios)
usuarios.append(('Paulo', 39, 1979))
print(usuarios)

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(47478)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)
for conta in contas:
        print(conta)