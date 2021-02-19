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

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano}: {self._likes} Like(s)'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.duracao} min: {self._likes} Like(s)'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.temporadas} temporadas: {self._likes} Like(s)'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)
vingadores.darLike()
vingadores.darLike()
tmep.darLike()
tmep.darLike()
tmep.darLike()
tmep.darLike()
demolidor.darLike()
demolidor.darLike()
atlanta.darLike()
atlanta.darLike()
atlanta.darLike()

filmes_e_serie = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_serie)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programas in playlist_fim_de_semana:
    print(programas)
