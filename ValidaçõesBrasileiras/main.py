from acesso_cep import BuscaEndereco
from cpf_cnpj import DocCpf
from telefonesBr import TelefonesBr
from datas_br import DatasBr
import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)

print(resposta)


telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)


cadastro = DatasBr()
print(cadastro.dia_semana())
print(cadastro)


cep = "25800320"
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)
