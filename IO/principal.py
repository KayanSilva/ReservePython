arquivos_contatos = open('dados/contatos.csv', encoding='latin_1')

'''conteudo = arquivos_contatos.readlines(10)
print(conteudo)'''

for linha in arquivos_contatos:
    print(linha, end='')
