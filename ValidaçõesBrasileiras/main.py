from telefonesBr import TelefonesBr
import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)

print(resposta)


telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
