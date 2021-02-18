class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def darLike(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.darLike()
print(
    f'Nome: {vingadores.nome} - {vingadores.ano}: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.darLike()
atlanta.darLike()
print(
    f'Nome: {atlanta.nome} - {atlanta.ano}: {atlanta.likes}')
