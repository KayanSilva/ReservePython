arquivo = open('dados/contatos.csv', encoding='latin_1')

print(type(arquivo))

conteudo_em_bytes = arquivo.buffer.read()

texto_em_bytes = bytes('Esse é um texto em bytes', 'latin_1')
print(texto_em_bytes)

arquivo.close()