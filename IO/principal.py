try:
    with open('dados/contatos.csv', encoding='latin_1') as arquivos_contatos:
        for linha in arquivos_contatos:
            print(linha, end='')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
