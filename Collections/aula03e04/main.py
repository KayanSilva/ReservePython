# Herança e Polimorfismo

from abc import ABCMeta, abstractmethod
import numpy as np
import array as arr


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "Codigo {}\n Saldo {}\n".format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes()
    print(conta)

# Array, evitaremos usar o default para calculos, por motivos de suas restrições

arr.array('d', [1, 3.5])

# Para se trabalhar com número, a biblioteca referencia é a Numpy.
# Se caso não tiver instalado, utilizar o comando !pip install numby // python.exe -m pip install numpy

numeros = np.array([1, 3.5])
print(numeros)
numeros = numeros + 3
print(numeros)

# Igualidade com o __eq__


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Codigo {}\n Saldo {}\n".format(self._codigo, self._saldo)


class ContaMultiploSalario(ContaSalario):
    pass


conta1 = ContaSalario(37)
print(conta1)
conta2 = ContaCorrente(37)
print(conta2)

print("Comparação explicita:", conta1 == conta2)
print("Comparação dentro de uma lista:", conta1 in [conta2])

print("Hierarquia de classes para baixo:",
      isinstance(ContaCorrente(34), Conta))
