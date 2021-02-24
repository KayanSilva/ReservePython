minhaIdade = 28
sobreMim = "Meu nome é Kayan e minha idade é 28"
meuNome = "Kayan"
print(meuNome)
print(type(meuNome))
print(type(minhaIdade))

#....
substring = sobreMim[33:]
print(substring)

#....
url = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
argumento = "moedaorigem=real"
substring = argumento[5:11]
print(substring)
index = argumento.find("=")
substring = argumento[index+1:]
print(substring)
listaargumentos = argumento.split("=")
print(listaargumentos)