"""
A agregação é em parte parecida com a associação

Neste caso, a agregação é quando é possível que duas classes existam individualmente, porém uma das classes só irá funcionar plenamente caso use-se de outra classe. Ao passo que, a segunda classe poderá existir de forma plena sem a outra

"""

class Biblioteca:
    def __init__(self):
        self.livros = []

    
    # Receberei uma instância da classe Livro
    def adicionar_livro(self, livro):
        self.livros.append(livro)


    def listar_livros(self):
        for livro in self.livros:
            # Como eu recebi uma instância, caso eu imprimisse puramente a instância o que apareceria seria o local da memória em que ela está armazenada
            # Para ter acesso aos atributos da instância, eu preciso fazer o seguinte:
            print(livro.titulo, livro.valor)


    def patrimonio_biblioteca(self):
        total = 0
        for livro in self.livros:
            total += livro.valor
        return total


class Livro:
    def __init__(self, titulo, valor):
        self.titulo = titulo
        self.valor = valor


biblioteca = Biblioteca()

biblioteca.listar_livros()  # ''
print(biblioteca.patrimonio_biblioteca())  # 0

l1 = Livro('Livro 1', 100)
l2 = Livro('Livro 2', 200)
l3 = Livro('Livro 3', 50)
l4 = Livro('Livro 4', 150)

biblioteca.listar_livros()  # ''

biblioteca.adicionar_livro(l1)
biblioteca.adicionar_livro(l2)
biblioteca.adicionar_livro(l3)

biblioteca.listar_livros()  # Livro 1 100, Livro 2 200, Livro 3 50

biblioteca.adicionar_livro(l4)
biblioteca.listar_livros()  #  Livro 1 100, Livro 2 200, Livro 3 50, Livro 4 150

print(biblioteca.patrimonio_biblioteca())  # 500
