class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url invalida!!!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extrairArgumentos()
        representacaoString = "Valor: {}\n Moeda Origem: {}\n Moeda Destino {}\n".format(
            self.extrairValor(), moedaOrigem, moedaDestino)
        return representacaoString

    def __eq__(self, outraIntancia):
        return self.url == outraIntancia.url

    @staticmethod
    def urlEhValida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def extrairArgumentos(self):
        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        indiceInicialMoedaOrigem = self.encontrarIndiceInicial(
            buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if(moedaOrigem == "moedadestino"):
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontrarIndiceInicial(
                buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        indiceInicialMoedaDestino = self.encontrarIndiceInicial(
            buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontrarIndiceInicial(self, moedaBuscada) -> str:
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extrairValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontrarIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor
