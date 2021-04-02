from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=500"
argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url2)
moedaOrigem, moedaDestino = argumentosUrl.extrairArgumentos()
valor = argumentosUrl.extrairValor()
print(moedaDestino, moedaOrigem, valor)

print(len(argumentosUrl))

print(argumentosUrl)

print(argumentosUrl == argumentosUrl2)
