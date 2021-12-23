try:
    arquivos_contatos = open('dados/nao-existe.csv', encoding='latin_1', mode='w+')

    for linha in arquivos_contatos:
        print(linha, end='')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')

finally:
    arquivos_contatos.close()
