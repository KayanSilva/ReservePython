arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a')

print(type(arquivo))

texto_em_bytes = bytes('Esse é um texto em bytes', 'latin_1')

contato_veronica = b'15,Veronica, veronica@veronica.com.br'
arquivo.buffer.write(contato_veronica)


arquivo.close()