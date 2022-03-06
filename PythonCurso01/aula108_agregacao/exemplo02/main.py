class Locadora:
    def __init__(self):
        self.filmes = []


    def adicionar_filme(self, filme):
        self.filmes.append(filme)


    def listar_filmes(self):
        for filme in self.filmes:
            print(filme.nome)


class Filme:
    def __init__(self, nome):
        self.nome = nome


locadora = Locadora()
f1 = Filme('Um filme qualquer')
f2 = Filme('Outro filmezin')
f3 = Filme('Mais um filme')

locadora.adicionar_filme(f1)
locadora.listar_filmes()  # Um filme qualquer

print()
print('--------------------------------')
print()

locadora.adicionar_filme(f2)
locadora.adicionar_filme(f3)
locadora.listar_filmes()  # Um filme qualquer, Outro filmezin, Mais um filme
