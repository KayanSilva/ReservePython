from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extrairArgumentos()
valor = argumentosUrl.extrairValor()
print(moedaDestino, moedaOrigem, valor)